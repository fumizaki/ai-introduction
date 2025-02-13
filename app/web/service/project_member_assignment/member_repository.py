from abc import ABC, abstractmethod
from .member_entity import Member
import pandas as pd

class MemberRepository(ABC):

    @abstractmethod
    def get_all(self) -> list[Member]:
        raise NotImplementedError
    

class MemberRepositoryImpl(MemberRepository):
    
    def __init__(self) -> None:
        pass

    def get_all(self) -> list[Member]:
        df = pd.read_csv('dataset/project_member_assignment/member.csv', header=0, encoding='utf-8')
        return [
            Member(
                id=v['id'],
                role=v['role'],
                processing_skill=v['processing_skill'],
                english_skill=v['english_skill']
            ) for _, v in df.iterrows()
        ]
    

def implement() -> MemberRepository:
    return MemberRepositoryImpl()