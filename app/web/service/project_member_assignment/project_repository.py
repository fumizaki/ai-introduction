from abc import ABC, abstractmethod
from .project_entity import Project
import pandas as pd

class ProjectRepository(ABC):

    @abstractmethod
    def get_all(self) -> list[Project]:
        raise NotImplementedError
    

class ProjectRepositoryImpl(ProjectRepository):

    def __init__(self) -> None:
        pass

    def get_all(self) -> list[Project]:
        df = pd.read_csv('dataset/project_member_assignment/project.csv', header=0, encoding='utf-8')
        return [
            Project(
                id=v['id'],
                scale=v['scale'],
                english_required=v['english_required']
            ) for _, v in df.iterrows()
        ]
    

def implement() -> ProjectRepository:
    return ProjectRepositoryImpl()