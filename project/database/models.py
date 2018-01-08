from sqlalchemy import Column, Text, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from configparser import ConfigParser, ExtendedInterpolation

config = ConfigParser(interpolation=ExtendedInterpolation())
config.read('../../config.ini')
PROJECT_DB_PATH = config['DATABASES']['PROJECT_DB_PATH']


# inherit the functionality to create a database
Base = declarative_base()

# provide a class name for the database table
class Documents(Base):
    # provide a name used in SQL to query the table
    __tablename__ = 'DOCUMENTS'

    # provide column names and data types
    # for each field in the database
    # additional paramater are available for the columns
    # and data types
    document_id = Column(Integer(), primary_key=True)
    path = Column(Text())
    filename = Column(Text())
    document_text = Column(Text())
    table_text = Column(Text())
    last_modified_by = Column(Text())
    author = Column(Text())
    created = Column(Text())
    last_printed = Column(Text())
    revision = Column(Text())
    num_tables = Column(Text())

class Sections(Base):
    __tablename__ = 'SECTIONS'

    section_id = Column(Integer(), primary_key=True)
    filename = Column(Text())
    section_name = Column(Text())
    section_text = Column(Text())


if __name__ == "__main__":
    # instantiate the database connection
    engine = create_engine(PROJECT_DB_PATH)

    # create the tables in the database
    Base.metadata.create_all(engine)