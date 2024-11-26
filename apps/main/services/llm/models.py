from pydantic import BaseModel
from datetime import date


class ExperienceModel(BaseModel):
    starting: date | None
    ending: date | None
    title: str
    location: str
    url: str | None
    description: str


class CVModel(BaseModel):
    skills: list[str]
    hobbies: list[str]
    interests: list[str]
    languages: list[str]
    carriers: list[ExperienceModel]
    projects: list[ExperienceModel]
    educations: list[ExperienceModel]


class PositionModel(BaseModel):
    title: str
    description: str


class CVGeneratorModel(CVModel):
    comment: str
    fitness: int
