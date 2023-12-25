from dataclasses import (
    dataclass
)

@dataclass
class Field:
    name:           str
    type:           str
    is_primary:     bool = False
    is_nullable:    bool = False
    doc:            str = None

    @property
    def is_required(self) -> bool:
        return not self.is_nullable
    