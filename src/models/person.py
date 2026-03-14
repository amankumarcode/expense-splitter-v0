import uuid
from dataclasses import dataclass, field


@dataclass(frozen=True)
class Person:
    name: str
    id: str = field(default_factory=lambda: str(uuid.uuid4()))
