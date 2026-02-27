# SQLALCHEMY
## What is SQLAlchemy:
SQLAlchemy is a powerful Python SQL toolkit and Object Relational Mapper (ORM) that gives developers full control and flexibility over database operations.
It provides two major ways to interact with databases:
SQLAlchemy ORM                  SQLAlchemy Core                             
Uses Python classes as tables   Uses SQL expression language                
More Pythonic                   Closer to raw SQL                           
Suitable for large applications Suitable for lightweight or complex queries
Works with sessions             Works with connections  
## Project Description
This project demonstrates how to use SQLAlchemy in Python using two different approaches:
ORM (Object Relational Mapping)
Core (SQL Expression Language)
The project performs basic CRUD operations (Create, Read, Update, Delete) using an SQLite database.
It is a beginner-friendly example to understand how SQLAlchemy works internally.
## Technologies Used
Python 3
SQLAlchemy
SQLite Database
## ORM_EXAMPLE.py
Reference: 
ORM_EXAMPLE
This file demonstrates SQLAlchemy ORM approach.
## What it does:
Creates SQLite database: practice.db
Defines a table using a Python class (User)
Creates table automatically
Inserts single record
Inserts multiple records
Retrieves all records
Filters records using conditions
Updates records
Deletes records
## Key Concepts Used:
create_engine()
declarative_base()
sessionmaker()
session.add()
session.query()
session.commit()
In ORM, tables are represented as Python classes, and rows are treated as objects.

## core_example.py
Reference: 
core_example
This file demonstrates SQLAlchemy Core approach.
## What it does:
Creates SQLite database: core_db.db
Defines table using Table() and MetaData
Inserts single and multiple records
Selects records
Applies conditional queries
Updates records
Deletes records
## Key Concepts Used:
Table()
MetaData()
insert()
select()
update()
delete()
engine.connect()
In Core, we write database operations using SQL expressions, which is closer to raw SQL.

## Difference Between ORM and Core
Feature	ORM	Core
Table Definition	Python Class	Table() object
Data Handling	Objects	SQL Expressions
Transactions	Session	Connection
Best For	Large Applications	Lightweight / Direct SQL control
## How to Run This Project
Step 1: Install SQLAlchemy
pip install sqlalchemy
Step 2: Run ORM Example
python ORM_EXAMPLE.py
Step 3: Run Core Example
python core_example.py
## After running:
practice.db will be created (ORM)
core_db.db will be created (Core)
## Learning Objectives
By completing this project, you will understand:
How to connect Python to a database
How SQLAlchemy works
Difference between ORM and Core
How CRUD operations are implemented in both approaches
How transactions and commits work
## Who Can Use This?
Beginners learning SQLAlchemy
Students learning Database Systems
Anyone practicing Python database integration
Developers comparing ORM vs Core
