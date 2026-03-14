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
