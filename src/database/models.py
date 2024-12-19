from sqlalchemy import Column, Integer, String, Text
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class UserInput(Base):
    __tablename__ = 'user_inputs'

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(String, index=True)
    input_text = Column(Text, nullable=False)

class KeywordAnalysis(Base):
    __tablename__ = 'keyword_analysis'

    id = Column(Integer, primary_key=True, index=True)
    user_input_id = Column(Integer, nullable=False)
    keywords = Column(Text, nullable=False)