#1.Importing requried libraries
from sqlalchemy import create_engine,Column,Integer,String,Table,MetaData,insert,select, text,update,delete

#2.Database creation
engine=create_engine("sqlite:///core_db.db",echo=True)
print("Database created successfully")

#.3.Creating a table using Core
m=MetaData()

#4.Creating a table model
users=Table(
    "users",m,Column("id",Integer,primary_key=True),
    Column("name",String),
    Column("age",Integer)

)

#5.Create table in database
m.create_all(engine)
print("Table created successfully")

#6.Inserting data into table
with engine.connect() as conn:
    ins=insert(users).values(id=101,name="Nandhini",age=22)
    conn.execute(ins)
    conn.commit()
print("Data inserted successfully")

#7.Inserting multiple data
with engine.connect() as conn:
    insrt=insert(users).values([{"id":102,"name":"Sathya","age":25},
    {"id":103,"name":"Karthik","age":30},])
    conn.execute(insrt)
    conn.commit()
print("Multiple data inserted successfully")

#8.Querying the data
with engine.connect() as conn:
    sel = select(users)
    r = conn.execute(sel)
    for row in r:
        print(row)
    conn.commit()
print("Data retrieved successfully")

#9.Retrieving on specific condition
with engine.connect() as conn:
    s=select(users).where(users.c.age>=20)
    r=conn.execute(s)
    for i in r:
        print(i.name)

#10.Updating the data
with engine.connect() as conn:
    u=update(users).where(users.c.id==101).values(name="NandhiniKanike")
    r=conn.execute(u)
    conn.commit()
print("Data updated successfully")

with engine.connect() as conn:
    u=update(users).where(users.c.age>=24).values(age=users.c.age+1)
    r=conn.execute(u)
    conn.commit()
print("Data updated successfully")

#11.Deleting the data
with engine.connect() as conn:
    d=delete(users).where(users.c.age==31)
    r=conn.execute(d)
    if r:
        print("Data deleted successfully")
        conn.commit()
    else:
        print("No data found with age 31")

with engine.connect() as conn:
    d=delete(users).where(users.c.age>=20)
    r=conn.execute(d)
    if r:
        print("Data deleted successfully")
        conn.commit()
    else:
        print("No data found with age >= 20")








