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
    settlements: list[tuple[Person, Person, float]] = field(default_factory=list)

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
        for debtor, creditor, amount in self.settlements:
            balances[debtor] = balances.get(debtor, 0.0) + amount
            balances[creditor] = balances.get(creditor, 0.0) - amount
        return balances

    def settle_debt(self, debtor: Person, creditor: Person) -> None:
        balances = self.calculate_balances()
        amount = -balances.get(debtor, 0.0)
        if amount > 0:
            self.settlements.append((debtor, creditor, amount))

    def simplify_debts(self) -> list[tuple[Person, Person, float]]:
        balances = self.calculate_balances()
        creditors = sorted([(p, b) for p, b in balances.items() if b > 0], key=lambda x: x[1], reverse=True)
        debtors = sorted([(p, -b) for p, b in balances.items() if b < 0], key=lambda x: x[1], reverse=True)
        transactions: list[tuple[Person, Person, float]] = []
        i, j = 0, 0
        while i < len(debtors) and j < len(creditors):
            debtor, debt = debtors[i]
            creditor, credit = creditors[j]
            amount = min(debt, credit)
            transactions.append((debtor, creditor, amount))
            debt -= amount
            credit -= amount
            debtors[i] = (debtor, debt)
            creditors[j] = (creditor, credit)
            if abs(debt) < 1e-9:
                i += 1
            if abs(credit) < 1e-9:
                j += 1
        return transactions
