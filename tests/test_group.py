import uuid
from src.models.group import Group
from src.models.person import Person


def test_group_name_is_set():
    group = Group(name="Trip to Paris")
    assert group.name == "Trip to Paris"


def test_group_id_is_auto_generated_uuid():
    group = Group(name="Roommates")
    assert isinstance(group.id, str)
    uuid.UUID(group.id)  # raises ValueError if not a valid UUID


def test_group_members_defaults_to_empty_list():
    group = Group(name="Roommates")
    assert group.members == []


def test_group_expenses_defaults_to_empty_list():
    group = Group(name="Roommates")
    assert group.expenses == []


def test_add_member_appends_to_members():
    group = Group(name="Roommates")
    alice = Person(name="Alice")
    group.add_member(alice)
    assert alice in group.members
    assert len(group.members) == 1


def test_add_expense_appends_to_expenses():
    group = Group(name="Roommates")
    alice = Person(name="Alice")
    bob = Person(name="Bob")
    group.add_member(alice)
    group.add_member(bob)
    group.add_expense(description="Dinner", amount=40.0, paid_by=alice, split_among=[alice, bob])
    assert len(group.expenses) == 1
    expense = group.expenses[0]
    assert expense.description == "Dinner"
    assert expense.amount == 40.0
    assert expense.paid_by is alice
    assert expense.split_among == [alice, bob]


def test_calculate_balances_three_person_split():
    group = Group(name="Trip")
    alice = Person(name="Alice")
    bob = Person(name="Bob")
    carol = Person(name="Carol")
    group.add_member(alice)
    group.add_member(bob)
    group.add_member(carol)
    # Alice pays 30.0 split equally among all three — each owes 10.0
    # Alice is owed 20.0 (paid 30, owes 10), Bob owes 10.0, Carol owes 10.0
    group.add_expense(description="Groceries", amount=30.0, paid_by=alice, split_among=[alice, bob, carol])
    balances = group.calculate_balances()
    assert balances[alice] == 20.0
    assert balances[bob] == -10.0
    assert balances[carol] == -10.0
