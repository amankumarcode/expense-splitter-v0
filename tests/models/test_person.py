import uuid
from src.models.person import Person


def test_person_name_is_set():
    person = Person(name="Alice")
    assert person.name == "Alice"


def test_person_id_is_auto_generated_uuid():
    person = Person(name="Bob")
    assert isinstance(person.id, str)
    uuid.UUID(person.id)  # raises ValueError if not a valid UUID


def test_two_people_with_same_name_have_different_ids():
    p1 = Person(name="Charlie")
    p2 = Person(name="Charlie")
    assert p1.id != p2.id
