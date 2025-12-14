from enum import Enum


class UserRole(str, Enum):
    ADMIN = "admin"
    COMPANY = "company"
    EMPLOYEE = "employee"
