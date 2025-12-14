from sqlalchemy import Enum as SQLEnum
from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.api.core.enums import UserRole
from app.db.base import Base


class User(Base):

    email: Mapped[str] = mapped_column(String(255), unique=True, index=True)
    hashed_password: Mapped[str]

    role: Mapped[UserRole] = mapped_column(
        SQLEnum(UserRole), default=UserRole.COMPANY, nullable=False
    )

    company = relationship("Company", back_populates="owner", uselist=False)
