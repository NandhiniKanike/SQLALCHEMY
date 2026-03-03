#1. Import the requried libraries
from sqlalchemy import create_engine,Column,Integer,String
from sqlalchemy.orm import declarative_base,sessionmaker

#2.DataBase Creation
engine=create_engine("sqlite:///student.db",echo=True)
print("Database Created")

#3.Creating Base Class
Base=declarative_base()

#4.Define the model
class Student(Base):
    __tablename__="students"
    id=Column(Integer,primary_key=True)
    name=Column(String)
    marks=Column(Integer)
    status=Column(String)

#5.Create the table in databse
Base.metadata.create_all(engine)
print("Table created ")

#6.Creating session
Session=sessionmaker(bind=engine)
s=Session()

def add_students():
    try:
        id=int(input("Enter student id no:"))
        name=input("Enter student name:")
        marks=int(input("Enter student marks:"))
        if marks >=35:
            status="Pass"
        else:
            status="Fail"
        student=Student(id=id,name=name,marks=marks,status=status)
        s.add(student)
        s.commit()
        print("Student added successfully")
    except Exception as e:
        s.rollback()
        print("Error:",e)

def view_students():
    students=s.query(Student).all()
    print("\n----------Student Details ----------")
    for i in students:
        print(f"ID:{i.id},Name:{i.name},Marks={i.marks},Status:{i.status}")
    print("-----------------------------------")

def update_student():
    id=int(input("Enter student id no:"))
    students=s.query(Student).filter_by(id=id).first()
    if students:
        marks=int(input("Enter student marks:"))
        if marks>=35:
            students.status="Pass"
        else:
            students.status="Fail"
        s.commit()
        print(f"Student details updated sucessfully for id:{id}")
    else:
        print("Student details does not exists")

def delete_student():
    sid=int(input("Enter student id no:"))
    student=s.query(Student).filter_by(id=sid).first()
    if student:
        s.delete(student)
        s.commit()
        print("Student details deleted sucessfully")
    else:
        print("Student details does not exists")
def search_student():
    name=input("Enter the student name:")
    students=s.query(Student).filter(Student.name.ilike(f"%{name}%")).all()
    if students:
        for i in students:
            print(f"ID:{i.id},Name:{i.name},Marks={i.marks},Status:{i.status}")
    else:
        print("Student not found")
def bulk_insert():
    students=[
        {"id":111,"name":"Ravi","marks":45,"status":"Pass"},
        {"id":112,"name":"Raju","marks":25,"status":"Fail"},
        {"id":113,"name":"Ramesh","marks":55,"status":"Pass"},
        {"id":114,"name":"Suresh","marks":15,"status":"Fail"},
        {"id":115,"name":"Mahesh","marks":65,"status":"Pass"}
    ]
    s.bulk_insert_mappings(Student,students)
    s.commit()
    print("Bulk insert completed successfully")

while True:
    print("\n1.Add Student \n2.View Student \n3.Update Student \n4.Delete Student \n5.Search Student \n6.Bulk Insert \n7.Exists")
    choice=int(input("Enter your choice:"))
    if choice==1:
        add_students()
    elif choice==2:
        view_students()
    elif choice==3:
        update_student()
    elif choice==4:
        delete_student()
    elif choice==5:
        search_student()
    elif choice==6:
        bulk_insert()
    elif choice==7:
        print("Exit the programm")
        break
    else:
        print("Enter the valid choice")
s.close()
