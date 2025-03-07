import json
from typing import Dict

from ..common.constants import CARD_TYPE_PATTERNS, FILE_PATHS, TOKEN_CARDS
from .card import Card


class CardCollection:

    def __init__(self):
        self.cards: Dict[str, Card] = {}

    def load(self) -> None:
        """Load and parse collection data from game state files."""
        collection_state = self.__load_json(FILE_PATHS["collection"])["ServerState"]

        self.__load_cards(collection_state)

    def get_card(self, card_id: str):
        """Retrieve a card by ID."""
        return self.cards.get(card_id, None)

    def __load_json(self, file_path) -> dict:
        """Load data from JSON file."""
        with open(file_path, encoding="utf-8-sig") as file:
            return json.load(file)

    def __get_or_create_card(self, card_id: str) -> Card:
        return self.cards.setdefault(card_id, Card())

    def __load_cards(self, server_state: dict) -> None:
        for card_id, card_data in server_state["CardDefStats"]["Stats"].items():
            if card_id == "$type":
                continue
            current_card = self.__get_or_create_card(card_id)
            if self.__is_token(card_id):
                current_card.token_card = True
                continue
            current_card.boosters = card_data.get("Boosters", 0)
            current_card.boosters_lifetime = card_data.get("BoostersLifetime", 0)
            current_card.infinity_split_count = card_data.get("InfinitySplitCount", 0)
            current_card.unlocked_borders = card_data.get("UnlockedBorders", [])

    def __is_token(self, card_id: str) -> bool:
        """Determine the type of a card based on its ID."""
        return (
            card_id in TOKEN_CARDS
            or any(card_id.startswith(prefix) and len(card_id) > len(prefix) for prefix in CARD_TYPE_PATTERNS["prefix"])
            or any(card_id.endswith(suffix) and len(card_id) > len(suffix) for suffix in CARD_TYPE_PATTERNS["suffix"])
        )
