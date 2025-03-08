import json
from dataclasses import asdict, dataclass, field
from typing import List


@dataclass
class Card:
    # CollectionState
    in_deck: bool = False
    owned: bool = False
    token_card: bool = False

    boosters_lifetime: int = 0
    boosters: int = 0
    infinity_split_count: int = 0
    variant_count: int = 0

    time_created: str = field(default_factory=str)
    unlocked_borders: List[str] = field(default_factory=list)
    unlocked_effects: List[str] = field(default_factory=list)

    # MasteryState
    mastery_level: int = 0
    total_mastery_experience: int = 0

    # RewardState
    in_token_shop: bool = False

    def __str__(self):
        return json.dumps(asdict(self), indent=4)
