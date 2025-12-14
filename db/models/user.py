from sqlalchemy import String
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import relationship
from sqlalchemy.orm import mapped_column
from db.base import Base
from core.enums import UserRole
from sqlalchemy import Enum as SQLEnum


class User(Base):

    email: Mapped[str] = mapped_column(String(255), unique=True, index=True)
    hashed_password: Mapped[str]

    role: Mapped[UserRole] = mapped_column(
        SQLEnum(UserRole), default=UserRole.COMPANY, nullable=False
    )

    company = relationship("Company", back_populates="owner", uselist=False)
