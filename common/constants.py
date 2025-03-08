from pathlib import Path

FILE_PATHS = {
    "collection": Path.home() / "AppData/Locallow/Second Dinner/SNAP/Standalone/States/nvprod/CollectionState.json",
    "mastery": Path.home() / "AppData/Locallow/Second Dinner/SNAP/Standalone/States/nvprod/CharacterMasteryState.json",
    "reward": Path.home() / "AppData/Locallow/Second Dinner/SNAP/Standalone/States/nvprod/RewardState.json",
}

TOKEN_CARDS = frozenset(
    {
        "Broodling",
        "CapsShield",
        "Chimichanga",
        "Demon",
        "Djinn",
        "DoomBot",
        "DoomBot2099",
        "Drone",
        "EbonyBlade",
        "IceCube",
        "Mjolnir",
        "Monster",
        "MuramasaShard",
        "MysterioUnrevealed",
        "Ninja",
        "Pig",
        "Raptor",
        "Rock",
        "ScarletSpiderClone",
        "SinisterClone",
        "SPdr",
        "Squirrel",
        "Stormbreaker",
        "Symbiote",
        "TheVoid",
        "TigerSpirit",
        "Vibranium",
        "WinterSoldier",
    }
)

CARD_TYPE_PATTERNS = {
    "prefix": ["Evolved", "Snowguard", "Widows"],
    "suffix": ["Arrow", "Stone", "Tutorial"],
}
