import uuid
from dataclasses import dataclass, field
from datetime import datetime, timezone

from src.models.person import Person


@dataclass
class Expense:
    description: str
    amount: float
    paid_by: Person
    split_among: list[Person]
    id: str = field(default_factory=lambda: str(uuid.uuid4()))
    created_at: datetime = field(default_factory=lambda: datetime.now(timezone.utc))
