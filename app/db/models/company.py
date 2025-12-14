from db.base import Base
from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship


class Company(Base):
    __tablename__ = "companies"

    name: Mapped[str] = mapped_column(String(255), unique=True, index=True)
    avatar: Mapped[str | None]

    owner_id: Mapped[int] = mapped_column(ForeignKey("users.id"))

    owner = relationship("User", back_populates="company")
    contacts = relationship(
        "CompanyContact", back_populates="company", cascade="all, delete-orphan"
    )


class CompanyContact(Base):
    __tablename__ = "company_contacts"

    city: Mapped[str]
    address: Mapped[str]
    phone: Mapped[str]
    email: Mapped[str]

    company_id: Mapped[int] = mapped_column(ForeignKey("companies.id"))
    company = relationship("Company", back_populates="contacts")
