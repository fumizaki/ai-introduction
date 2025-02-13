from enum import Enum

class MemberRole(str, Enum):
    DIRECTOR = 'director'
    MANAGER = 'manager'
    STAFF = 'staff'

    @classmethod
    def keys(cls) -> list[str]:
        return [i.name for i in cls]

    @classmethod
    def values(cls) -> list[str]:
        return [i.value for i in cls]
