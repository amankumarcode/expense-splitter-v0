import uuid
from datetime import datetime
from src.models.person import Person
from src.models.expense import Expense


def test_expense_fields_are_set_correctly():
    alice = Person(name="Alice")
    bob = Person(name="Bob")
    expense = Expense(
        description="Dinner",
        amount=60.0,
        paid_by=alice,
        split_among=[alice, bob],
    )
    assert expense.description == "Dinner"
    assert expense.amount == 60.0
    assert expense.paid_by is alice
    assert expense.split_among == [alice, bob]


def test_expense_id_is_auto_generated_uuid():
    alice = Person(name="Alice")
    expense = Expense(description="Lunch", amount=20.0, paid_by=alice, split_among=[alice])
    assert isinstance(expense.id, str)
    uuid.UUID(expense.id)  # raises ValueError if not a valid UUID


def test_expense_created_at_is_auto_generated_datetime():
    alice = Person(name="Alice")
    expense = Expense(description="Coffee", amount=5.0, paid_by=alice, split_among=[alice])
    assert isinstance(expense.created_at, datetime)
