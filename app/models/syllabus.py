from pydantic import BaseModel, Field

class Unit(BaseModel) :

    unit : int = Field(description='Unit Number')
    title : str = Field(description="Unit Title")
    topics : list[str] = Field(description='List of Topics in the unit')


class Syllabus(BaseModel) :

    subject : str = Field(description='Subject name')
    units : list[Unit] = Field(description='List of units')