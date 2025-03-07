import json
from dataclasses import asdict, dataclass, field
from typing import List


@dataclass
class Card:
    # CollectionState
    boosters_lifetime: int = 0
    boosters: int = 0
    infinity_split_count: int = 0
    token_card: bool = False
    unlocked_borders: List[str] = field(default_factory=list)

    def __str__(self):
        return json.dumps(asdict(self), indent=4)
