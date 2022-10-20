from pydantic import BaseModel


class InputPredict(BaseModel):
    type_school: str
    school_accreditation: str
    interest: str
    gender: str
    residence: str
    parent_was_in_college: bool


class ResponsePredict(BaseModel):
    will_go_to_college: str
