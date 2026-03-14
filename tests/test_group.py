import uuid
from src.models.group import Group


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
