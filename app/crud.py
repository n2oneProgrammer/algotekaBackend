from sqlalchemy.orm import Session
from app import models, schema


def get_algorithms(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Algorithm).offset(skip).limit(limit).all()


def get_algorithms_by_id(db: Session, id: int):
    return db.query(models.Algorithm).filter(models.Algorithm.id == id).first()


def get_algorithms_by_name(db: Session, name: str):
    return db.query(models.Algorithm).filter(models.Algorithm.name == name).first()


async def create_algorithm(db: Session, data: schema.AlgorithmCreate):
    db_algorithm = models.Algorithm(
        name=data.name
    )
    db.add(db_algorithm)
    db.commit()
    db.refresh(db_algorithm)
    return db_algorithm


def get_languages(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Language).offset(skip).limit(limit).all()


def get_language_by_id(db: Session, id: int):
    return db.query(models.Language).filter(models.Language.id == id).first()


async def create_language(db: Session, language: schema.LanguageCreate):
    db_language = models.Language(
        name=language.name,
        syntax_code=language.syntax_code
    )
    db.add(db_language)
    db.commit()
    db.refresh(db_language)
    return db_language


def get_codes(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Code).offset(skip).limit(limit).all()


async def create_code(db: Session, data: schema.CodeCreate):
    if get_algorithms_by_id(db, data.algorithm_id) is None:
        return None
    if get_language_by_id(db, data.language_id) is None:
        return None
    db_code = models.Code(
        code=data.code,
        language_id=data.language_id,
        algorithm_id=data.algorithm_id
    )
    db.add(db_code)
    db.commit()
    db.refresh(db_code)
    return db_code
