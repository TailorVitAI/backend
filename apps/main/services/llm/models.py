from pydantic import BaseModel
from datetime import date


class ExperienceModel(BaseModel):
    starting: date | None
    ending: date | None
    title: str
    role: str
    location: str | None
    url: str | None
    description: str


class CVModel(BaseModel):
    summary: str
    title: str
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


class CVGeneratorModel(BaseModel):
    comment: str
    fitness: int
    cv: CVModel
