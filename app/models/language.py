from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from ..database import Base


class Language(Base):
    __tablename__ = "languages"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100))
    syntax_code = Column(String(50))
    codes = relationship("Code", back_populates="language", cascade="all, delete")
