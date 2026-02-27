#1.Importing requried libraries
from sqlalchemy import create_engine,Column,Integer,String
from sqlalchemy.orm import declarative_base,sessionmaker

#2.Database Creation
engine=create_engine("sqlite:///practice.db",echo=True)
print("Database created sucessfully")

#3.Creating Base Class
Base=declarative_base()

#4.Creating table model
class User(Base):
    __tablename__="users"
    id=Column(Integer,primary_key=True)
    name=Column(String)
    age=Column(Integer)

#5.Create Table in Database
Base.metadata.create_all(engine)
print("Table created successfully")

#6.Creating a session-Session is used to:Insert data,Update data,Delete data,Commit transaction
Session=sessionmaker(bind=engine)
session=Session()

#7.Instering the data
new_user=User(id=101,name="Nandhini",age=22)
session.add(new_user)
session.commit()
print("Data inserted successfully")

#8.Inserting multiple data
users=[
    User(id=102,name="Sathya",age=25),
    User(id=103,name="Karthik",age=30),
    User(id=104,name="Priya",age=28)
]
session.add_all(users)
session.commit()
print("Multiple data inserted successfully")

#9.Querying the data
users=session.query(User).all()
for u in users:
    print(u.id,u.name,u.age)
print("Data retrived sucessfully")

#10.Retriving on specific condition
user=session.query(User).filter(User.age >= 25).all()
for u in user:
    print(u.id,u.name,u.age)

user=session.query(User).filter_by(age=22).first()
if user:
    print(user.name)
else:
    print("No user found with age 22")

#11.Updating the data
user=session.query(User).filter(User.age>=18).all()
for u in user:
    u.age += 2
session.commit()
print("Data updated successfully")

#12.Deleting the data
user=session.query(User).filter_by(name="Sathya").first()
if user:
    session.delete(user)
    session.commit()
    print("Data deleted successfully")
else:
    print("No user found with name Sathya")

user=session.query(User).filter(User.age>25).all()
for u in user:
    session.delete(u)
session.commit()
print("Data deleted successfully")


