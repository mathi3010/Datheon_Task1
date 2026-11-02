from pydantic import BaseModel, Field


class ResumeData(BaseModel):

    name: str

    job_title: str

    skills: list[str]

    experience_years: float