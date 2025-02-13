import pulp
from .project_entity import Project
from .member_entity import Member
from .member_value import MemberRole

class AssignmentOptimizer:
    """プロジェクトへの最適なメンバーアサインを行うクラス"""
    def __init__(self, projects: list[Project], members: list[Member]):
        self.projects: list[Project] = projects
        self.members: list[Member] = members
        self.problem: pulp.LpProblem = pulp.LpProblem("Assignment_Problem", pulp.LpMaximize)
        self.x = {}

    def compute_score(self, member: Member, project: Project) -> float:
        """メンバーとプロジェクトの適合度をスコア化"""
        score = member.processing_skill * (project.scale / 100.0)
        if project.english_required:
            score += member.english_skill
        return score

    def setup_variables(self) -> None:
        """アサイン変数を作成"""
        for c in self.members:
            for p in self.projects:
                var_name = f"x_{c.id}_{p.id}"
                self.x[(c.id, p.id)] = pulp.LpVariable(var_name, cat='Binary')

    def setup_constraints(self) -> None:
        """制約条件を追加"""
        for p in self.projects:
            for role in MemberRole.values():
                self.problem += pulp.lpSum(self.x[(m.id, p.id)] for m in self.members if m.role == role) >= 1, f"Project_{p.id}_Role_{role}_Requirement"
        for m in self.members:
            self.problem += pulp.lpSum(self.x[(m.id, p.id)] for p in self.projects) <= 1, f"Member_{m.id}_Single_Assignment"

    def setup_objective(self) -> None:
        """目的関数(スコアの最大化)を定義"""
        self.problem += pulp.lpSum(
            self.compute_score(m, p) * self.x[(m.id, p.id)] for m in self.members for p in self.projects
        ), "Total_Score"

    def solve(self) -> list[dict]:
        """最適化を実行"""
        self.setup_variables()
        self.setup_constraints()
        self.setup_objective()
        self.problem.solve()

        assignments = []
        for p in self.projects:
            for m in self.members:
                if pulp.value(self.x[(m.id, p.id)]) == 1:
                    assignments.append({
                        "Project": p.id,
                        "Member": m.id,
                        "Role": m.role,
                        "Score": self.compute_score(m, p)
                    })
        return assignments