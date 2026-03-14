import uuid
from dataclasses import dataclass, field

from src.models.person import Person
from src.models.expense import Expense


@dataclass
class Group:
    name: str
    id: str = field(default_factory=lambda: str(uuid.uuid4()))
    members: list[Person] = field(default_factory=list)
    expenses: list[Expense] = field(default_factory=list)

    def add_member(self, person: Person) -> None:
        self.members.append(person)

    def add_expense(self, description: str, amount: float, paid_by: Person, split_among: list[Person]) -> Expense:
        expense = Expense(description=description, amount=amount, paid_by=paid_by, split_among=split_among)
        self.expenses.append(expense)
        return expense

    def calculate_balances(self) -> dict[Person, float]:
        balances: dict[Person, float] = {}
        for expense in self.expenses:
            balances[expense.paid_by] = balances.get(expense.paid_by, 0.0) + expense.amount
            share = expense.amount / len(expense.split_among)
            for person in expense.split_among:
                balances[person] = balances.get(person, 0.0) - share
        return balances
