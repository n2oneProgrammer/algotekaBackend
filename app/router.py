from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app import crud as crud
from app.dependencies import get_db
from app.schema import LanguageResponse, LanguageCreate, CodeResponse, CodeCreate, AlgorithmResponse, AlgorithmCreate, \
    AlgorithmResponseWithCodes, CodeResponseWithAlgorithms

router_language = APIRouter(tags=["language"])
router_code = APIRouter(tags=["code"])
router_algorithm = APIRouter(tags=["algorithm"])


@router_language.get("/languages", response_model=List[LanguageResponse])
async def get_languages(
        skip: int = 0, limit: int = 100, db: Session = Depends(get_db)
):
    languages = crud.get_languages(db, skip, limit)

    return languages


@router_language.post("/languages", response_model=LanguageResponse, status_code=201)
async def create_language(
        language: LanguageCreate,
        db: Session = Depends(get_db)
):
    language = await crud.create_language(db, language)
    return language


@router_code.get("/code", response_model=List[CodeResponseWithAlgorithms])
async def get_codes(
        skip: int = 0, limit: int = 100, db: Session = Depends(get_db)
):
    codes = crud.get_codes(db, skip, limit)

    return codes


@router_code.post("/code", response_model=CodeResponseWithAlgorithms, status_code=201)
async def create_code(
        code: CodeCreate,
        db: Session = Depends(get_db)
):
    code = await crud.create_code(db, code)
    if code is None:
        raise HTTPException(status_code=404, detail="I dont find that algorithm or language")
    return code


@router_algorithm.get("/algorithm", response_model=List[AlgorithmResponse])
async def get_algorithm(
        skip: int = 0, limit: int = 100, db: Session = Depends(get_db)
):
    algorithms = crud.get_algorithms(db, skip, limit)

    return algorithms


@router_algorithm.get("/algorithm/{algorithm_id}", response_model=AlgorithmResponseWithCodes)
async def get_algorithm(algorithm_id: int, db: Session = Depends(get_db)
                        ):
    algorithm = crud.get_algorithms_by_id(db, algorithm_id)
    if algorithm is None:
        raise HTTPException(status_code=404, detail="algorithm doesnt find")
    return algorithm


@router_algorithm.post("/algorithm", response_model=AlgorithmResponseWithCodes, status_code=201)
async def create_algorithm(
        algorithm: AlgorithmCreate,
        db: Session = Depends(get_db)
):
    algorithm = await crud.create_algorithm(db, algorithm)
    return algorithm
