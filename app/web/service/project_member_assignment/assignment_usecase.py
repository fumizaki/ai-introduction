from .assignment_optimizer import AssignmentOptimizer
from .project_repository import implement as implement_project_repository
from .member_repository import implement as implement_member_repository


class AssignmentUsecase:
    def __init__(self) -> None:
        self.project_repository = implement_project_repository()
        self.member_repository = implement_member_repository()

    def exec(self) -> list[dict]:
        projects = self.project_repository.get_all()
        members = self.member_repository.get_all()
        opt = AssignmentOptimizer(projects=projects, members=members)
        return opt.solve()