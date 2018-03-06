# Python SQL toolkit and Object Relational Mapper
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine
import os 

sqlite_db_path = os.path.join('non-static','gov_awards.sqlite')

# Create engine using the `gov_awards.sqlite` database file
engine = create_engine(f'sqlite:///{sqlite_db_path}')

# Declare a Base using `automap_base()`
Base = automap_base()

# Use the Base class to reflect the database tables
Base.prepare(engine, reflect=True)

# assign awards table to variable
Awards = Base.classes.awards

# Create a session
session = Session(engine)