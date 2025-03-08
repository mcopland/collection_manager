import json
from typing import Dict

from ..common.constants import CARD_TYPE_PATTERNS, FILE_PATHS, TOKEN_CARDS
from .card import Card


class CardCollection:

    def __init__(self):
        self.cards: Dict[str, Card] = {}
        self.load()

    def load(self) -> None:
        """Load and parse collection data from game state files."""
        collection_state = self.__load_json(FILE_PATHS["collection"])["ServerState"]
        mastery_state = self.__load_json(FILE_PATHS["mastery"])["ServerState"]
        reward_state = self.__load_json(FILE_PATHS["reward"])["ServerState"]

        self.__load_cards(collection_state)
        self.__set_deck_status(collection_state)
        self.__set_ownership(collection_state)
        self.__set_time_created(collection_state)
        self.__set_unlocked_effects(collection_state)
        self.__set_card_mastery(mastery_state)
        self.__set_shop_rotation(reward_state)

    def get_card(self, card_id: str):
        """Retrieve a card by ID."""
        return self.cards.get(card_id, None)

    def __load_json(self, file_path) -> dict:
        """Load data from JSON file."""
        with open(file_path, encoding="utf-8-sig") as file:
            return json.load(file)

    def __get_or_create_card(self, card_id: str) -> Card:
        return self.cards.setdefault(card_id, Card())

    def __load_cards(self, collection_state: dict) -> None:
        for card_id, card_data in collection_state["CardDefStats"]["Stats"].items():
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

    def __set_deck_status(self, collection_state: dict) -> None:
        for deck_data in collection_state["Decks"]:
            for card_data in deck_data["Cards"]:
                current_card = self.__get_or_create_card(card_data["CardDefId"])
                current_card.in_deck = True

    def __set_ownership(self, collection_state: dict) -> None:
        for card_data in collection_state["CardOwnership"]["Dao"]["S"]:
            current_card = self.__get_or_create_card(card_data["C"])
            current_card.owned = True
            current_card.variant_count = len(card_data.get("V", []))

    def __set_time_created(self, collection_state: dict) -> None:
        for card_data in collection_state["Cards"]:
            current_card = self.__get_or_create_card(card_data["CardDefId"])
            if "TimeCreated" in card_data:
                time_created = card_data["TimeCreated"].split(".")[0].rstrip("Z")
                if not current_card.time_created or time_created < current_card.time_created:
                    current_card.time_created = time_created

    def __set_unlocked_effects(self, collection_state: dict) -> None:
        for card_id, card_data in collection_state["CardFinishAndFlareStats"].items():
            if card_id == "$type":
                continue
            current_card = self.__get_or_create_card(card_id)
            unlocked_effects = card_data["UnlockedEffects"]
            current_card.unlocked_effects = [key for key in unlocked_effects.keys() if key not in ["$type", "None"]]

    def __set_card_mastery(self, mastery_state: dict) -> None:
        for card_id, card_data in mastery_state["CharacterMasteryProgress"]["CharacterProgressData"].items():
            if card_id == "$type":
                continue
            current_card = self.__get_or_create_card(card_id)
            current_card.mastery_level = int(card_data["LastClaimedLevel"])
            current_card.total_mastery_experience = card_data.get("Experience", 0)

    def __set_shop_rotation(self, reward_state: dict) -> None:
        for card_id in reward_state["PickedVariableRewards"]["Rewards"]["TokenShopCardsSeries4Box"]:
            current_card = self.__get_or_create_card(card_id[4:])
            current_card.in_token_shop = not current_card.owned
