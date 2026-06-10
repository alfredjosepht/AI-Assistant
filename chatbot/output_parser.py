from pydantic import BaseModel
from langchain_core.output_parsers import PydanticOutputParser


class Person(BaseModel):
    name: str
    age: int


person_parser = PydanticOutputParser(
    pydantic_object=Person
)


class Event(BaseModel):
    task: str
    datetime: str


event_parser = PydanticOutputParser(
    pydantic_object=Event
)