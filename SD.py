from  fastapi import FastAPI
from pydantic import BaseModel 
import mysql.connector

connection=mysql.connector.connect(
    host='localhost',
    user='root',
    password='mysql@123$#$#',
    database='school')

cursor=connection.cursor()
app=FastAPI()

class DBModel(BaseModel):
    sid:int
    sname:str
    age:int
    address:str
    deptno:int

@app.get('/students')
def students_details():
    query='select * from students'
    cursor.execute(query)
    result=cursor.fetchall()
    return result

@app.get('/students/id/{sid}')
def student_by_id(sid:int):
    query ='select * from students where sid=%s'
    cursor.execute(query,(sid,))
    result=cursor.fetchone()
    return result

@app.get('/students/address/{address}')
def student_by_address(address:str):
    query ='select * from students where address=%s'
    cursor.execute(query,(address,))
    result=cursor.fetchall()
    return result

@app.get('/students/department/{deptno}')
def students_by_deptno(deptno:int):
    query='select s.sid,s.sname,s.age,s.address,d.deptno,d.dname from students s inner join department d on (s.deptno=d.deptno) where d.deptno=%s'
    cursor.execute(query,(deptno,))
    result=cursor.fetchall()
    return result

@app.post('/students')
def new_student_details(student:DBModel):
    query='insert into students values(%s,%s,%s,%s,%s)'
    values=(student.sid,student.sname,student.age,student.address,student.deptno)
    cursor.execute(query,values)
    connection.commit()
    return {"message": "Student added successfully"}

@app.put('/students/{sid}')
def update_student(sid:int,student:DBModel):
    query='update students set sname=%s, age=%s, address=%s, deptno=%s where sid=%s'
    values=(student.sname,student.age,student.address,student.deptno,sid)
    cursor.execute(query,values)
    connection.commit()
    return {"message": "Student updated successfully"}

@app.delete('/students/{sid}')
def delete_student(sid:int):
    query='delete from students where sid=%s'
    cursor.execute(query,(sid,))
    connection.commit()
    return {"message": "Student deleted successfully"}
