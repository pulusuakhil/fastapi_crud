from pydantic import BaseModel
from fastapi import APIRouter

router = APIRouter()
employees={1:{'ename':'siva','age':21,'salary':10000},
           2:{'ename':'raju','age':22,'salary':20000}
           }
class Employee(BaseModel):
    ename:str
    age:int
    salary:int

@router.get("/")
def get_user():
    return employees

@router.get('/employees/{empid}')
def get_employee(empid:int):
    return employees[empid]

@router.post('/employees')
def add_employee(employee:Employee):
    add_new=max(employees.keys())+1
    employees[add_new]=employee.dict()
    return employees[add_new]

@router.put('/employees/{empid}')
def update_employee(empid:int,employee:Employee):
    if empid in employees:
        employees[empid]=employee.dict()
        return employees
    

@router.delete('/employees/{empid}')
def delete_employee(empid:int):
    if empid in employees:
        del employees[empid]


