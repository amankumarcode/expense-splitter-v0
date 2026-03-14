import uuid
from dataclasses import dataclass, field


@dataclass
class Person:
    name: str
    id: str = field(default_factory=lambda: str(uuid.uuid4()))
