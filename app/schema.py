from pydantic import BaseModel
from typing import List


class LanguageResponse(BaseModel):
    name: str
    syntax_code: str

    class Config:
        orm_mode = True


class LanguageCreate(BaseModel):
    name: str
    syntax_code: str

    class Config:
        orm_mode = True


class CodeResponse(BaseModel):
    code: str
    language: LanguageResponse

    class Config:
        orm_mode = True


class CodeCreate(BaseModel):
    code: str
    language_id: int
    algorithm_id: int

    class Config:
        orm_mode = True


class AlgorithmResponse(BaseModel):
    id: int
    name: str

    class Config:
        orm_mode = True


class AlgorithmResponseWithCodes(AlgorithmResponse):
    codes: List[CodeResponse]

    class Config:
        orm_mode = True


class AlgorithmCreate(BaseModel):
    name: str

    class Config:
        orm_mode = True


class CodeResponseWithAlgorithms(CodeResponse):
    algorithm: AlgorithmResponse

    class Config:
        orm_mode = True
