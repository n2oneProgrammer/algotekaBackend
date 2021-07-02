from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from ..database import Base


class Code(Base):
    __tablename__ = "codes"

    id = Column(Integer, primary_key=True, index=True)
    code = Column(String(2000))
    language_id = Column(Integer, ForeignKey("languages.id"))
    language = relationship("Language", back_populates="codes", cascade="save-update")
    algorithm_id = Column(Integer, ForeignKey("algorithms.id"))
    algorithm = relationship("Algorithm", back_populates="codes", cascade="save-update")
