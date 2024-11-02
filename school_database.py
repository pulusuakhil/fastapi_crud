from fastapi import FastAPI
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
    id:int
    name:str
    age:int
    grade:str

@app.get('/students')
def students_details():
    query='select * from students'
    cursor.execute(query)
    result=cursor.fetchall()
    return result
    
@app.get('/students/{id}')
def student_by_id(id:int):
    query='select * from students where id=%s'
    cursor.execute(query,(id,))
    result=cursor.fetchone()
    return result

@app.post('/students')
def new_student_details(student:DBModel):
    query='insert into students values(%s,%s,%s,%s)'
    values=(student.id,student.name,student.age,student.grade)
    cursor.execute(query,values)
    connection.commit()
    return {"message": "Student added successfully"}

@app.put('/students/{id}')
def update_student(id:int,student:DBModel):
    query='update students set id=%s,name=%s,age=%s,grade=%s where id=%s'
    values=(student.id,student.name,student.age,student.grade,id)
    cursor.execute(query,values)
    connection.commit()
    return {"message": "Student updated successfully"}

@app.delete('/students/{id}')
def delete_student(id:int):
    query='delete from students where id=%s'
    cursor.execute(query,(id,))
    connection.commit()
    return {"message": "Student deleted successfully"}

