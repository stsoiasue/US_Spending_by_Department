# Python SQL toolkit and Object Relational Mapper
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.orm import Session
from sqlalchemy import create_engine
import os 

# sqlite_db_path = os.path.join('app','non-static','us_data.sqlite')
sqlite_db_path = os.path.join('non-static','data.sqlite')

# Create engine using the `us_data.sqlite` database file
engine = create_engine(f'sqlite:///{sqlite_db_path}')

# Declare a Base using `declarative_base()`
Base = declarative_base()

# establish Contracts class
class Contract(Base):
    __tablename__ = 'lat_lon'
    index = Column(Integer, primary_key=True)
    Awarding_Agency = Column(String(255))
    Subtier_Agency = Column(String(255))
    Subtier_Code = Column(String(255))
    Category = Column(String(255))
    POP_City = Column(String(255))
    POP_State = Column(String(255))
    POP_Zip = Column(String(255))
    Recipient_Name = Column(String(255))
    Total_Obligation = Column(String(255))
    Latitude = Column(Float)
    Longitude = Column(Float)
    Description = Column(String(255))
    Contract_ID = Column(String(255))

# establish Top class
class Top(Base):
    __tablename__ = 'top_ten'
    index = Column(Integer, primary_key=True)
    Awarding_Agency = Column(String(255))
    Subtier_Agency = Column(String(255))
    Subtier_Code = Column(String(255))
    Category = Column(String(255))
    POP_City = Column(String(255))
    POP_State = Column(String(255))
    POP_Zip = Column(String(255))
    Recipient_Name = Column(String(255))
    Total_Obligation = Column(String(255))
    Latitude = Column(Float)
    Longitude = Column(Float)
    Description = Column(String(255))
    Contract_ID = Column(String(255))
#     Percentage_of_Dept = Column(Integer)
#     Percentage_of_Total = Column(Integer)

# Create a Contracts table within the database
Base.metadata.create_all(engine)

# create session object
session = Session(bind=engine)

# assign table to Contracts variable
Contracts = session.query(Contract)

# assign table to Top variable
Top_Contracts = session.query(Top)