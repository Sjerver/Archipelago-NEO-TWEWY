from __future__ import annotations

from enum import Enum
from typing import NamedTuple

from BaseClasses import ItemClassification


class NEOTwewyItemData(NamedTuple):
    """Special data container to contain the metadata of each item to make filtering work."""

    id: int
    item_type: NEOTwewyItemType
    item_classification: ItemClassification
    item_groups: list[NEOTwewyItemGroup]
    brand: str = "Unbranded"
    drop_increase: int = 0
    element: str = "None"


class NEOTwewyItemType(Enum):
    Invalid = -1  # Needed?
    Badge = 0
    Costume = 1  # Threads
    Food = 2  # Needed?
    Valuable = 3  # FP
    ItemMaterial = 4  # Needed?
    Book = 5
    Music = 6  # Needed?
    # Add PIN Buttons mostly because of MinamimotoPIN Check can't at base be Y/X


class NEOTwewyItemGroup(Enum):
    COMBAT_PIN = "Combat Pin"
    SECRET_REPORT = "Secret Report"
    MONEY = "Money Pin"
    RARE_METAL = "Rare Metal Pin"
    FP_ITEM = "FP_ITEM"
    # HEADGEAR = "Headgear"
    # TOPS = "Tops"
    # BOTTOMS = "Bottoms"
    # FOOTWEAR = "Footwear"
    # TWO_PIECE = "Two-Piece"
    # ACCESSORY = "Accessory"


ITEM_DATA: dict[str, NEOTwewyItemData] = {
    "Shockwave": NEOTwewyItemData(
        1000, NEOTwewyItemType.Badge, ItemClassification.filler, [NEOTwewyItemGroup.COMBAT_PIN], "Unbranded", 0, "None"
    ),
    "Azamaru": NEOTwewyItemData(
        1001,
        NEOTwewyItemType.Badge,
        ItemClassification.filler,
        [NEOTwewyItemGroup.COMBAT_PIN],
        "Jupiter of the Monkey",
        0,
        "Fire",
    ),
    "Shishio": NEOTwewyItemData(
        1002,
        NEOTwewyItemType.Badge,
        ItemClassification.filler,
        [NEOTwewyItemGroup.COMBAT_PIN],
        "Jupiter of the Monkey",
        0,
        "Fire",
    ),
    "Midaregami": NEOTwewyItemData(
        1003,
        NEOTwewyItemType.Badge,
        ItemClassification.filler,
        [NEOTwewyItemGroup.COMBAT_PIN],
        "Jupiter of the Monkey",
        0,
        "None",
    ),
    "Namikuguri": NEOTwewyItemData(
        1004,
        NEOTwewyItemType.Badge,
        ItemClassification.filler,
        [NEOTwewyItemGroup.COMBAT_PIN],
        "Jupiter of the Monkey",
        0,
        "Water",
    ),
    "Fuchin": NEOTwewyItemData(
        1005,
        NEOTwewyItemType.Badge,
        ItemClassification.filler,
        [NEOTwewyItemGroup.COMBAT_PIN],
        "Jupiter of the Monkey",
        0,
        "Wind",
    ),
    "Kurorushi": NEOTwewyItemData(
        1006,
        NEOTwewyItemType.Badge,
        ItemClassification.filler,
        [NEOTwewyItemGroup.COMBAT_PIN],
        "Jupiter of the Monkey",
        0,
        "Darkness",
    ),
    "Honebami": NEOTwewyItemData(
        1007,
        NEOTwewyItemType.Badge,
        ItemClassification.filler,
        [NEOTwewyItemGroup.COMBAT_PIN],
        "Jupiter of the Monkey",
        0,
        "Darkness",
    ),
    "Grizzly": NEOTwewyItemData(
        1008, NEOTwewyItemType.Badge, ItemClassification.filler, [NEOTwewyItemGroup.COMBAT_PIN], "Unbranded", 0, "None"
    ),
    "Onimaru": NEOTwewyItemData(
        1009,
        NEOTwewyItemType.Badge,
        ItemClassification.filler,
        [NEOTwewyItemGroup.COMBAT_PIN],
        "Jupiter of the Monkey",
        0,
        "None",
    ),
    "Kitsunegasaki": NEOTwewyItemData(
        1010,
        NEOTwewyItemType.Badge,
        ItemClassification.filler,
        [NEOTwewyItemGroup.COMBAT_PIN],
        "Jupiter of the Monkey",
        0,
        "Fire",
    ),
    "Yukimitsu": NEOTwewyItemData(
        1011,
        NEOTwewyItemType.Badge,
        ItemClassification.filler,
        [NEOTwewyItemGroup.COMBAT_PIN],
        "Jupiter of the Monkey",
        0,
        "Fire",
    ),
    "Sayosamonji": NEOTwewyItemData(
        1012,
        NEOTwewyItemType.Badge,
        ItemClassification.filler,
        [NEOTwewyItemGroup.COMBAT_PIN],
        "Jupiter of the Monkey",
        0,
        "None",
    ),
    "Aizen": NEOTwewyItemData(
        1013,
        NEOTwewyItemType.Badge,
        ItemClassification.filler,
        [NEOTwewyItemGroup.COMBAT_PIN],
        "Jupiter of the Monkey",
        0,
        "None",
    ),
    "Spin Twinz": NEOTwewyItemData(
        1014,
        NEOTwewyItemType.Badge,
        ItemClassification.filler,
        [NEOTwewyItemGroup.COMBAT_PIN],
        "croaky panic",
        0,
        "Water",
    ),
    "Tsurumaru": NEOTwewyItemData(
        1015,
        NEOTwewyItemType.Badge,
        ItemClassification.filler,
        [NEOTwewyItemGroup.COMBAT_PIN],
        "Jupiter of the Monkey",
        0,
        "Wind",
    ),
    "Reigetsu": NEOTwewyItemData(
        1016,
        NEOTwewyItemType.Badge,
        ItemClassification.filler,
        [NEOTwewyItemGroup.COMBAT_PIN],
        "Jupiter of the Monkey",
        0,
        "Wind",
    ),
    "Jupiter of the Monkey II": NEOTwewyItemData(
        1017,
        NEOTwewyItemType.Badge,
        ItemClassification.filler,
        [NEOTwewyItemGroup.COMBAT_PIN],
        "Jupiter of the Monkey",
        0,
        "Light",
    ),
    "Hotaru": NEOTwewyItemData(
        1018,
        NEOTwewyItemType.Badge,
        ItemClassification.filler,
        [NEOTwewyItemGroup.COMBAT_PIN],
        "Jupiter of the Monkey",
        0,
        "Light",
    ),
    "Grin Reaper": NEOTwewyItemData(
        1019,
        NEOTwewyItemType.Badge,
        ItemClassification.filler,
        [NEOTwewyItemGroup.COMBAT_PIN],
        "Tigre PUNKS",
        0,
        "None",
    ),
    "Grunge Punch": NEOTwewyItemData(
        1020,
        NEOTwewyItemType.Badge,
        ItemClassification.filler,
        [NEOTwewyItemGroup.COMBAT_PIN],
        "Tigre PUNKS",
        0,
        "None",
    ),
    "Jungle King": NEOTwewyItemData(
        1021,
        NEOTwewyItemType.Badge,
        ItemClassification.filler,
        [NEOTwewyItemGroup.COMBAT_PIN],
        "Tigre PUNKS",
        0,
        "Fire",
    ),
    "Primal Roar": NEOTwewyItemData(
        1022,
        NEOTwewyItemType.Badge,
        ItemClassification.filler,
        [NEOTwewyItemGroup.COMBAT_PIN],
        "Tigre PUNKS",
        0,
        "Fire",
    ),
    "Mosh 'n' Mash": NEOTwewyItemData(
        1023,
        NEOTwewyItemType.Badge,
        ItemClassification.filler,
        [NEOTwewyItemGroup.COMBAT_PIN],
        "Tigre PUNKS",
        0,
        "Fire",
    ),
    "Fangs of Ice": NEOTwewyItemData(
        1024, NEOTwewyItemType.Badge, ItemClassification.filler, [NEOTwewyItemGroup.COMBAT_PIN], "Tigre PUNKS", 0, "Ice"
    ),
    "Slashcicle": NEOTwewyItemData(
        1025, NEOTwewyItemType.Badge, ItemClassification.filler, [NEOTwewyItemGroup.COMBAT_PIN], "Tigre PUNKS", 0, "Ice"
    ),
    "Right Claw": NEOTwewyItemData(
        1026,
        NEOTwewyItemType.Badge,
        ItemClassification.filler,
        [NEOTwewyItemGroup.COMBAT_PIN],
        "Tigre PUNKS",
        0,
        "Sound",
    ),
    "Wicked Howl": NEOTwewyItemData(
        1027,
        NEOTwewyItemType.Badge,
        ItemClassification.filler,
        [NEOTwewyItemGroup.COMBAT_PIN],
        "Tigre PUNKS",
        0,
        "Sound",
    ),
    "Tigres Assemble!": NEOTwewyItemData(
        1028,
        NEOTwewyItemType.Badge,
        ItemClassification.filler,
        [NEOTwewyItemGroup.COMBAT_PIN],
        "Tigre PUNKS",
        0,
        "None",
    ),
    "Rock 'n' Rock": NEOTwewyItemData(
        1029,
        NEOTwewyItemType.Badge,
        ItemClassification.filler,
        [NEOTwewyItemGroup.COMBAT_PIN],
        "Tigre PUNKS",
        0,
        "Stone",
    ),
    "Crusher Rush": NEOTwewyItemData(
        1030,
        NEOTwewyItemType.Badge,
        ItemClassification.filler,
        [NEOTwewyItemGroup.COMBAT_PIN],
        "Tigre PUNKS",
        0,
        "Stone",
    ),
    "Beringei": NEOTwewyItemData(
        1031, NEOTwewyItemType.Badge, ItemClassification.filler, [NEOTwewyItemGroup.COMBAT_PIN], "Unbranded", 0, "Stone"
    ),
    "Just Up Ahead": NEOTwewyItemData(
        1032, NEOTwewyItemType.Badge, ItemClassification.filler, [NEOTwewyItemGroup.COMBAT_PIN], "MONOCROW", 0, "None"
    ),
    "Honor and Sacrifice": NEOTwewyItemData(
        1033, NEOTwewyItemType.Badge, ItemClassification.filler, [NEOTwewyItemGroup.COMBAT_PIN], "MONOCROW", 0, "None"
    ),
    "All or Nothing": NEOTwewyItemData(
        1034, NEOTwewyItemType.Badge, ItemClassification.filler, [NEOTwewyItemGroup.COMBAT_PIN], "MONOCROW", 0, "None"
    ),
    "One Day Closer": NEOTwewyItemData(
        1035, NEOTwewyItemType.Badge, ItemClassification.filler, [NEOTwewyItemGroup.COMBAT_PIN], "MONOCROW", 0, "Time"
    ),
    "Time Is Relative": NEOTwewyItemData(
        1036, NEOTwewyItemType.Badge, ItemClassification.filler, [NEOTwewyItemGroup.COMBAT_PIN], "MONOCROW", 0, "Time"
    ),
    "Got Your Back": NEOTwewyItemData(
        1037,
        NEOTwewyItemType.Badge,
        ItemClassification.filler,
        [NEOTwewyItemGroup.COMBAT_PIN],
        "MONOCROW",
        0,
        "Darkness",
    ),
    "Take a Chance": NEOTwewyItemData(
        1038,
        NEOTwewyItemType.Badge,
        ItemClassification.filler,
        [NEOTwewyItemGroup.COMBAT_PIN],
        "MONOCROW",
        0,
        "Darkness",
    ),
    "No Turning Back": NEOTwewyItemData(
        1039, NEOTwewyItemType.Badge, ItemClassification.filler, [NEOTwewyItemGroup.COMBAT_PIN], "MONOCROW", 0, "Poison"
    ),
    "Trial Without Error": NEOTwewyItemData(
        1040, NEOTwewyItemType.Badge, ItemClassification.filler, [NEOTwewyItemGroup.COMBAT_PIN], "MONOCROW", 0, "Poison"
    ),
    "Stinger": NEOTwewyItemData(
        1041,
        NEOTwewyItemType.Badge,
        ItemClassification.filler,
        [NEOTwewyItemGroup.COMBAT_PIN],
        "Unbranded",
        0,
        "Poison",
    ),
    "No Plan Required": NEOTwewyItemData(
        1042,
        NEOTwewyItemType.Badge,
        ItemClassification.filler,
        [NEOTwewyItemGroup.COMBAT_PIN],
        "MONOCROW",
        0,
        "Electric",
    ),
    "Don't Be Shocked": NEOTwewyItemData(
        1043,
        NEOTwewyItemType.Badge,
        ItemClassification.filler,
        [NEOTwewyItemGroup.COMBAT_PIN],
        "MONOCROW",
        0,
        "Electric",
    ),
    "Cut Me Down": NEOTwewyItemData(
        1044,
        NEOTwewyItemType.Badge,
        ItemClassification.filler,
        [NEOTwewyItemGroup.COMBAT_PIN],
        "MONOCROW",
        0,
        "Electric",
    ),
    "Quench Your Thirst": NEOTwewyItemData(
        1045, NEOTwewyItemType.Badge, ItemClassification.filler, [NEOTwewyItemGroup.COMBAT_PIN], "MONOCROW", 0, "Poison"
    ),
    "Try It Again": NEOTwewyItemData(
        1046, NEOTwewyItemType.Badge, ItemClassification.filler, [NEOTwewyItemGroup.COMBAT_PIN], "MONOCROW", 0, "Poison"
    ),
    "Force Rounds": NEOTwewyItemData(
        1047, NEOTwewyItemType.Badge, ItemClassification.filler, [NEOTwewyItemGroup.COMBAT_PIN], "Unbranded", 0, "None"
    ),
    "Sugar Beam": NEOTwewyItemData(
        1048,
        NEOTwewyItemType.Badge,
        ItemClassification.filler,
        [NEOTwewyItemGroup.COMBAT_PIN],
        "NATURAL PUPPY",
        0,
        "None",
    ),
    "Nighty-Night Beam": NEOTwewyItemData(
        1049,
        NEOTwewyItemType.Badge,
        ItemClassification.filler,
        [NEOTwewyItemGroup.COMBAT_PIN],
        "NATURAL PUPPY",
        0,
        "None",
    ),
    "Glitter Beam": NEOTwewyItemData(
        1050,
        NEOTwewyItemType.Badge,
        ItemClassification.filler,
        [NEOTwewyItemGroup.COMBAT_PIN],
        "NATURAL PUPPY",
        0,
        "Electric",
    ),
    "Zip-Zap Beam": NEOTwewyItemData(
        1051,
        NEOTwewyItemType.Badge,
        ItemClassification.filler,
        [NEOTwewyItemGroup.COMBAT_PIN],
        "NATURAL PUPPY",
        0,
        "Electric",
    ),
    "Stylish Beam": NEOTwewyItemData(
        1052,
        NEOTwewyItemType.Badge,
        ItemClassification.filler,
        [NEOTwewyItemGroup.COMBAT_PIN],
        "NATURAL PUPPY",
        0,
        "Ice",
    ),
    "Lovebird Magnum": NEOTwewyItemData(
        1053,
        NEOTwewyItemType.Badge,
        ItemClassification.filler,
        [NEOTwewyItemGroup.COMBAT_PIN],
        "NATURAL PUPPY",
        0,
        "Ice",
    ),
    "Garbage Gatling": NEOTwewyItemData(
        1054,
        NEOTwewyItemType.Badge,
        ItemClassification.filler,
        [NEOTwewyItemGroup.COMBAT_PIN],
        "NATURAL PUPPY",
        0,
        "Kinesis",
    ),
    "Top Dog Gatling": NEOTwewyItemData(
        1055,
        NEOTwewyItemType.Badge,
        ItemClassification.filler,
        [NEOTwewyItemGroup.COMBAT_PIN],
        "NATURAL PUPPY",
        0,
        "Kinesis",
    ),
    "Icky Beam": NEOTwewyItemData(
        1056,
        NEOTwewyItemType.Badge,
        ItemClassification.filler,
        [NEOTwewyItemGroup.COMBAT_PIN],
        "NATURAL PUPPY",
        0,
        "Poison",
    ),
    "Frog": NEOTwewyItemData(
        1057, NEOTwewyItemType.Badge, ItemClassification.filler, [NEOTwewyItemGroup.COMBAT_PIN], "Unbranded", 0, "Water"
    ),
    "Freestyle Launcher": NEOTwewyItemData(
        1058,
        NEOTwewyItemType.Badge,
        ItemClassification.filler,
        [NEOTwewyItemGroup.COMBAT_PIN],
        "NATURAL PUPPY",
        0,
        "Ice",
    ),
    "Lovely Launcher": NEOTwewyItemData(
        1059,
        NEOTwewyItemType.Badge,
        ItemClassification.filler,
        [NEOTwewyItemGroup.COMBAT_PIN],
        "NATURAL PUPPY",
        0,
        "Sound",
    ),
    "Cupid Launcher": NEOTwewyItemData(
        1060,
        NEOTwewyItemType.Badge,
        ItemClassification.filler,
        [NEOTwewyItemGroup.COMBAT_PIN],
        "NATURAL PUPPY",
        0,
        "Sound",
    ),
    "Cuddly Launcher": NEOTwewyItemData(
        1061,
        NEOTwewyItemType.Badge,
        ItemClassification.filler,
        [NEOTwewyItemGroup.COMBAT_PIN],
        "NATURAL PUPPY",
        0,
        "Light",
    ),
    "Heartthrob Launcher": NEOTwewyItemData(
        1062,
        NEOTwewyItemType.Badge,
        ItemClassification.filler,
        [NEOTwewyItemGroup.COMBAT_PIN],
        "NATURAL PUPPY",
        0,
        "Light",
    ),
    "Hobblin' Hippo": NEOTwewyItemData(
        1063,
        NEOTwewyItemType.Badge,
        ItemClassification.filler,
        [NEOTwewyItemGroup.COMBAT_PIN],
        "croaky panic",
        0,
        "Kinesis",
    ),
    "croaky panic": NEOTwewyItemData(
        1064,
        NEOTwewyItemType.Badge,
        ItemClassification.filler,
        [NEOTwewyItemGroup.COMBAT_PIN],
        "croaky panic",
        0,
        "Kinesis",
    ),
    "MONOCROW": NEOTwewyItemData(
        1065, NEOTwewyItemType.Badge, ItemClassification.filler, [NEOTwewyItemGroup.COMBAT_PIN], "MONOCROW", 0, "None"
    ),
    "The Idol Within": NEOTwewyItemData(
        1066, NEOTwewyItemType.Badge, ItemClassification.filler, [NEOTwewyItemGroup.COMBAT_PIN], "MONOCROW", 0, "None"
    ),
    "Be My Last": NEOTwewyItemData(
        1067, NEOTwewyItemType.Badge, ItemClassification.filler, [NEOTwewyItemGroup.COMBAT_PIN], "MONOCROW", 0, "Fire"
    ),
    "All Burned Out": NEOTwewyItemData(
        1068, NEOTwewyItemType.Badge, ItemClassification.filler, [NEOTwewyItemGroup.COMBAT_PIN], "MONOCROW", 0, "Fire"
    ),
    "Aspect of Truth": NEOTwewyItemData(
        1069,
        NEOTwewyItemType.Badge,
        ItemClassification.filler,
        [NEOTwewyItemGroup.COMBAT_PIN],
        "MONOCROW",
        0,
        "Darkness",
    ),
    "Live Your Truth": NEOTwewyItemData(
        1070,
        NEOTwewyItemType.Badge,
        ItemClassification.filler,
        [NEOTwewyItemGroup.COMBAT_PIN],
        "MONOCROW",
        0,
        "Darkness",
    ),
    "Grus": NEOTwewyItemData(
        1071,
        NEOTwewyItemType.Badge,
        ItemClassification.filler,
        [NEOTwewyItemGroup.COMBAT_PIN],
        "Unbranded",
        0,
        "Darkness",
    ),
    "Rapturous Rabbits": NEOTwewyItemData(
        1072, NEOTwewyItemType.Badge, ItemClassification.filler, [NEOTwewyItemGroup.COMBAT_PIN], "Cony×Cony", 0, "Burst"
    ),
    "Classical Cacophany": NEOTwewyItemData(
        1073, NEOTwewyItemType.Badge, ItemClassification.filler, [NEOTwewyItemGroup.COMBAT_PIN], "Cony×Cony", 0, "Burst"
    ),
    "Magical Metamorphosis": NEOTwewyItemData(
        1074, NEOTwewyItemType.Badge, ItemClassification.filler, [NEOTwewyItemGroup.COMBAT_PIN], "Cony×Cony", 0, "Burst"
    ),
    "Blizzard Bunny": NEOTwewyItemData(
        1075, NEOTwewyItemType.Badge, ItemClassification.filler, [NEOTwewyItemGroup.COMBAT_PIN], "Cony×Cony", 0, "Ice"
    ),
    "Frosty Friendship": NEOTwewyItemData(
        1076, NEOTwewyItemType.Badge, ItemClassification.filler, [NEOTwewyItemGroup.COMBAT_PIN], "Cony×Cony", 0, "Ice"
    ),
    "Stellar Self-Portrait": NEOTwewyItemData(
        1077, NEOTwewyItemType.Badge, ItemClassification.filler, [NEOTwewyItemGroup.COMBAT_PIN], "Cony×Cony", 0, "Stone"
    ),
    "Gorgeous Gemstone": NEOTwewyItemData(
        1078, NEOTwewyItemType.Badge, ItemClassification.filler, [NEOTwewyItemGroup.COMBAT_PIN], "Cony×Cony", 0, "Stone"
    ),
    "Black Hole Bunny": NEOTwewyItemData(
        1079,
        NEOTwewyItemType.Badge,
        ItemClassification.filler,
        [NEOTwewyItemGroup.COMBAT_PIN],
        "Cony×Cony",
        0,
        "Gravity",
    ),
    "The Great Magma Escape": NEOTwewyItemData(
        1080,
        NEOTwewyItemType.Badge,
        ItemClassification.filler,
        [NEOTwewyItemGroup.COMBAT_PIN],
        "Shepherd House",
        0,
        "Burst",
    ),
    "The Great Balloon Voyage": NEOTwewyItemData(
        1081,
        NEOTwewyItemType.Badge,
        ItemClassification.filler,
        [NEOTwewyItemGroup.COMBAT_PIN],
        "Shepherd House",
        0,
        "Wind",
    ),
    "The Fluffy Ovine Cloud": NEOTwewyItemData(
        1082,
        NEOTwewyItemType.Badge,
        ItemClassification.filler,
        [NEOTwewyItemGroup.COMBAT_PIN],
        "Shepherd House",
        0,
        "Wind",
    ),
    "The Lonely Space Warrior": NEOTwewyItemData(
        1083,
        NEOTwewyItemType.Badge,
        ItemClassification.filler,
        [NEOTwewyItemGroup.COMBAT_PIN],
        "Shepherd House",
        0,
        "Kinesis",
    ),
    "The Great Lunar View": NEOTwewyItemData(
        1084,
        NEOTwewyItemType.Badge,
        ItemClassification.filler,
        [NEOTwewyItemGroup.COMBAT_PIN],
        "Shepherd House",
        0,
        "Kinesis",
    ),
    "The Pyramids' Old Secret": NEOTwewyItemData(
        1085,
        NEOTwewyItemType.Badge,
        ItemClassification.filler,
        [NEOTwewyItemGroup.COMBAT_PIN],
        "Shepherd House",
        0,
        "Kinesis",
    ),
    "The Ever-Moving Machine": NEOTwewyItemData(
        1086,
        NEOTwewyItemType.Badge,
        ItemClassification.filler,
        [NEOTwewyItemGroup.COMBAT_PIN],
        "Shepherd House",
        0,
        "Electric",
    ),
    "Puffer": NEOTwewyItemData(
        1087,
        NEOTwewyItemType.Badge,
        ItemClassification.filler,
        [NEOTwewyItemGroup.COMBAT_PIN],
        "Unbranded",
        0,
        "Poison",
    ),
    "Out of Your Mine": NEOTwewyItemData(
        1088, NEOTwewyItemType.Badge, ItemClassification.filler, [NEOTwewyItemGroup.COMBAT_PIN], "garagara", 0, "Burst"
    ),
    "Be of Two Mines": NEOTwewyItemData(
        1089, NEOTwewyItemType.Badge, ItemClassification.filler, [NEOTwewyItemGroup.COMBAT_PIN], "garagara", 0, "Burst"
    ),
    "Boom in the Night": NEOTwewyItemData(
        1090, NEOTwewyItemType.Badge, ItemClassification.filler, [NEOTwewyItemGroup.COMBAT_PIN], "garagara", 0, "Burst"
    ),
    "Chain Is Gonna Come": NEOTwewyItemData(
        1091, NEOTwewyItemType.Badge, ItemClassification.filler, [NEOTwewyItemGroup.COMBAT_PIN], "garagara", 0, "None"
    ),
    "Back on the Chain Bang": NEOTwewyItemData(
        1092, NEOTwewyItemType.Badge, ItemClassification.filler, [NEOTwewyItemGroup.COMBAT_PIN], "garagara", 0, "None"
    ),
    "Bad to the Bomb": NEOTwewyItemData(
        1093, NEOTwewyItemType.Badge, ItemClassification.filler, [NEOTwewyItemGroup.COMBAT_PIN], "garagara", 0, "Poison"
    ),
    "Snake in the Blast": NEOTwewyItemData(
        1094, NEOTwewyItemType.Badge, ItemClassification.filler, [NEOTwewyItemGroup.COMBAT_PIN], "garagara", 0, "Poison"
    ),
    "Bee in Your Bomb-et": NEOTwewyItemData(
        1095,
        NEOTwewyItemType.Badge,
        ItemClassification.filler,
        [NEOTwewyItemGroup.COMBAT_PIN],
        "garagara",
        0,
        "Darkness",
    ),
    "I Scream, U Scream!": NEOTwewyItemData(
        1096,
        NEOTwewyItemType.Badge,
        ItemClassification.filler,
        [NEOTwewyItemGroup.COMBAT_PIN],
        "croaky panic",
        0,
        "Water",
    ),
    "Bloom 4 U": NEOTwewyItemData(
        1097,
        NEOTwewyItemType.Badge,
        ItemClassification.filler,
        [NEOTwewyItemGroup.COMBAT_PIN],
        "croaky panic",
        0,
        "Water",
    ),
    "Takanosu": NEOTwewyItemData(
        1098,
        NEOTwewyItemType.Badge,
        ItemClassification.filler,
        [NEOTwewyItemGroup.COMBAT_PIN],
        "Jupiter of the Monkey",
        0,
        "None",
    ),
    "Kumokiri": NEOTwewyItemData(
        1099,
        NEOTwewyItemType.Badge,
        ItemClassification.filler,
        [NEOTwewyItemGroup.COMBAT_PIN],
        "Jupiter of the Monkey",
        0,
        "None",
    ),
    "Taikokane": NEOTwewyItemData(
        1100,
        NEOTwewyItemType.Badge,
        ItemClassification.filler,
        [NEOTwewyItemGroup.COMBAT_PIN],
        "Jupiter of the Monkey",
        0,
        "Sound",
    ),
    "Kasen Kanesada": NEOTwewyItemData(
        1101,
        NEOTwewyItemType.Badge,
        ItemClassification.filler,
        [NEOTwewyItemGroup.COMBAT_PIN],
        "Jupiter of the Monkey",
        0,
        "Sound",
    ),
    "Iwatoshi": NEOTwewyItemData(
        1102,
        NEOTwewyItemType.Badge,
        ItemClassification.filler,
        [NEOTwewyItemGroup.COMBAT_PIN],
        "Jupiter of the Monkey",
        0,
        "Stone",
    ),
    "Omokage": NEOTwewyItemData(
        1103,
        NEOTwewyItemType.Badge,
        ItemClassification.filler,
        [NEOTwewyItemGroup.COMBAT_PIN],
        "Jupiter of the Monkey",
        0,
        "Stone",
    ),
    "Wolf": NEOTwewyItemData(
        1104, NEOTwewyItemType.Badge, ItemClassification.filler, [NEOTwewyItemGroup.COMBAT_PIN], "Unbranded", 0, "Light"
    ),
    "Thunder and Lightning": NEOTwewyItemData(
        1105,
        NEOTwewyItemType.Badge,
        ItemClassification.filler,
        [NEOTwewyItemGroup.COMBAT_PIN],
        "IL CAVALLO DEL RE",
        0,
        "Electric",
    ),
    "Iris": NEOTwewyItemData(
        1106,
        NEOTwewyItemType.Badge,
        ItemClassification.filler,
        [NEOTwewyItemGroup.COMBAT_PIN],
        "Unbranded",
        0,
        "Poison",
    ),
    "Caught in the Undertow": NEOTwewyItemData(
        1107,
        NEOTwewyItemType.Badge,
        ItemClassification.filler,
        [NEOTwewyItemGroup.COMBAT_PIN],
        "IL CAVALLO DEL RE",
        0,
        "Water",
    ),
    "Let the Rain Fall Down": NEOTwewyItemData(
        1108,
        NEOTwewyItemType.Badge,
        ItemClassification.filler,
        [NEOTwewyItemGroup.COMBAT_PIN],
        "IL CAVALLO DEL RE",
        0,
        "Water",
    ),
    "Taste of Poison Paradise": NEOTwewyItemData(
        1109,
        NEOTwewyItemType.Badge,
        ItemClassification.filler,
        [NEOTwewyItemGroup.COMBAT_PIN],
        "IL CAVALLO DEL RE",
        0,
        "Poison",
    ),
    "Diamonds in the Sky": NEOTwewyItemData(
        1110,
        NEOTwewyItemType.Badge,
        ItemClassification.filler,
        [NEOTwewyItemGroup.COMBAT_PIN],
        "IL CAVALLO DEL RE",
        0,
        "Kinesis",
    ),
    "All Comes Crashing Down": NEOTwewyItemData(
        1111,
        NEOTwewyItemType.Badge,
        ItemClassification.filler,
        [NEOTwewyItemGroup.COMBAT_PIN],
        "IL CAVALLO DEL RE",
        0,
        "Kinesis",
    ),
    "What a Wicked Game": NEOTwewyItemData(
        1112,
        NEOTwewyItemType.Badge,
        ItemClassification.filler,
        [NEOTwewyItemGroup.COMBAT_PIN],
        "IL CAVALLO DEL RE",
        0,
        "Electric",
    ),
    "Where I Break Free": NEOTwewyItemData(
        1113,
        NEOTwewyItemType.Badge,
        ItemClassification.filler,
        [NEOTwewyItemGroup.COMBAT_PIN],
        "IL CAVALLO DEL RE",
        0,
        "None",
    ),
    "Born of Stormy Skies": NEOTwewyItemData(
        1114,
        NEOTwewyItemType.Badge,
        ItemClassification.filler,
        [NEOTwewyItemGroup.COMBAT_PIN],
        "IL CAVALLO DEL RE",
        0,
        "Electric",
    ),
    "Lightning in My Hands": NEOTwewyItemData(
        1115,
        NEOTwewyItemType.Badge,
        ItemClassification.filler,
        [NEOTwewyItemGroup.COMBAT_PIN],
        "IL CAVALLO DEL RE",
        0,
        "Electric",
    ),
    "In the Stars Tonight": NEOTwewyItemData(
        1116,
        NEOTwewyItemType.Badge,
        ItemClassification.filler,
        [NEOTwewyItemGroup.COMBAT_PIN],
        "IL CAVALLO DEL RE",
        0,
        "Light",
    ),
    "Blinded by the Light": NEOTwewyItemData(
        1117,
        NEOTwewyItemType.Badge,
        ItemClassification.filler,
        [NEOTwewyItemGroup.COMBAT_PIN],
        "IL CAVALLO DEL RE",
        0,
        "Light",
    ),
    "In My Misery": NEOTwewyItemData(
        1118,
        NEOTwewyItemType.Badge,
        ItemClassification.filler,
        [NEOTwewyItemGroup.COMBAT_PIN],
        "IL CAVALLO DEL RE",
        0,
        "Darkness",
    ),
    "Phoenix": NEOTwewyItemData(
        1119, NEOTwewyItemType.Badge, ItemClassification.filler, [NEOTwewyItemGroup.COMBAT_PIN], "Unbranded", 0, "None"
    ),
    "Joli bécot": NEOTwewyItemData(
        1120, NEOTwewyItemType.Badge, ItemClassification.filler, [NEOTwewyItemGroup.COMBAT_PIN], "Joli bécot", 0, "None"
    ),
    "Angelic Kick": NEOTwewyItemData(
        1121, NEOTwewyItemType.Badge, ItemClassification.filler, [NEOTwewyItemGroup.COMBAT_PIN], "Joli bécot", 0, "None"
    ),
    "Gust of Gorgeous": NEOTwewyItemData(
        1122, NEOTwewyItemType.Badge, ItemClassification.filler, [NEOTwewyItemGroup.COMBAT_PIN], "Joli bécot", 0, "Wind"
    ),
    "Wicked Wind": NEOTwewyItemData(
        1123, NEOTwewyItemType.Badge, ItemClassification.filler, [NEOTwewyItemGroup.COMBAT_PIN], "Joli bécot", 0, "Wind"
    ),
    "Sistah Subwoofer": NEOTwewyItemData(
        1124,
        NEOTwewyItemType.Badge,
        ItemClassification.filler,
        [NEOTwewyItemGroup.COMBAT_PIN],
        "Joli bécot",
        0,
        "Sound",
    ),
    "Disco Divekick": NEOTwewyItemData(
        1125,
        NEOTwewyItemType.Badge,
        ItemClassification.filler,
        [NEOTwewyItemGroup.COMBAT_PIN],
        "Joli bécot",
        0,
        "Sound",
    ),
    "Soul Ablaze": NEOTwewyItemData(
        1126, NEOTwewyItemType.Badge, ItemClassification.filler, [NEOTwewyItemGroup.COMBAT_PIN], "Joli bécot", 0, "Fire"
    ),
    "Killer Princess": NEOTwewyItemData(
        1127, NEOTwewyItemType.Badge, ItemClassification.filler, [NEOTwewyItemGroup.COMBAT_PIN], "Joli bécot", 0, "Fire"
    ),
    "Leo Armo": NEOTwewyItemData(
        1128, NEOTwewyItemType.Badge, ItemClassification.filler, [NEOTwewyItemGroup.COMBAT_PIN], "Unbranded", 0, "Fire"
    ),
    "Marvelous Crash": NEOTwewyItemData(
        1129,
        NEOTwewyItemType.Badge,
        ItemClassification.filler,
        [NEOTwewyItemGroup.COMBAT_PIN],
        "Joli bécot",
        0,
        "Stone",
    ),
    "Crater's Kiss": NEOTwewyItemData(
        1130,
        NEOTwewyItemType.Badge,
        ItemClassification.filler,
        [NEOTwewyItemGroup.COMBAT_PIN],
        "Joli bécot",
        0,
        "Stone",
    ),
    "Cranberry Crystal": NEOTwewyItemData(
        1131,
        NEOTwewyItemType.Badge,
        ItemClassification.filler,
        [NEOTwewyItemGroup.COMBAT_PIN],
        "Joli bécot",
        0,
        "Stone",
    ),
    "Pink Matador": NEOTwewyItemData(
        1132,
        NEOTwewyItemType.Badge,
        ItemClassification.filler,
        [NEOTwewyItemGroup.COMBAT_PIN],
        "Joli bécot",
        0,
        "Electric",
    ),
    "Electric Manicure": NEOTwewyItemData(
        1133,
        NEOTwewyItemType.Badge,
        ItemClassification.filler,
        [NEOTwewyItemGroup.COMBAT_PIN],
        "Joli bécot",
        0,
        "Electric",
    ),
    "Bolt of Beauty": NEOTwewyItemData(
        1134,
        NEOTwewyItemType.Badge,
        ItemClassification.filler,
        [NEOTwewyItemGroup.COMBAT_PIN],
        "Joli bécot",
        0,
        "Electric",
    ),
    "Rex": NEOTwewyItemData(
        1135, NEOTwewyItemType.Badge, ItemClassification.filler, [NEOTwewyItemGroup.COMBAT_PIN], "Unbranded", 0, "Stone"
    ),
    "Cherry Bomb": NEOTwewyItemData(
        1136,
        NEOTwewyItemType.Badge,
        ItemClassification.filler,
        [NEOTwewyItemGroup.COMBAT_PIN],
        "Joli bécot",
        0,
        "Kinesis",
    ),
    "Jealous Rage": NEOTwewyItemData(
        1137,
        NEOTwewyItemType.Badge,
        ItemClassification.filler,
        [NEOTwewyItemGroup.COMBAT_PIN],
        "Joli bécot",
        0,
        "Kinesis",
    ),
    "Bad Romance": NEOTwewyItemData(
        1138,
        NEOTwewyItemType.Badge,
        ItemClassification.filler,
        [NEOTwewyItemGroup.COMBAT_PIN],
        "Joli bécot",
        0,
        "Kinesis",
    ),
    "Cold Cony×Cony": NEOTwewyItemData(
        1139, NEOTwewyItemType.Badge, ItemClassification.filler, [NEOTwewyItemGroup.COMBAT_PIN], "Cony×Cony", 0, "Ice"
    ),
    "Glacial Getaway": NEOTwewyItemData(
        1140, NEOTwewyItemType.Badge, ItemClassification.filler, [NEOTwewyItemGroup.COMBAT_PIN], "Cony×Cony", 0, "Ice"
    ),
    "Polar Princess": NEOTwewyItemData(
        1141, NEOTwewyItemType.Badge, ItemClassification.filler, [NEOTwewyItemGroup.COMBAT_PIN], "Cony×Cony", 0, "Ice"
    ),
    "Creepy Crystal": NEOTwewyItemData(
        1142, NEOTwewyItemType.Badge, ItemClassification.filler, [NEOTwewyItemGroup.COMBAT_PIN], "Cony×Cony", 0, "Stone"
    ),
    "Velvet Vampire": NEOTwewyItemData(
        1143, NEOTwewyItemType.Badge, ItemClassification.filler, [NEOTwewyItemGroup.COMBAT_PIN], "Cony×Cony", 0, "Stone"
    ),
    "Calamitous Candle": NEOTwewyItemData(
        1144, NEOTwewyItemType.Badge, ItemClassification.filler, [NEOTwewyItemGroup.COMBAT_PIN], "Cony×Cony", 0, "Fire"
    ),
    "Bérangère Lapin": NEOTwewyItemData(
        1145, NEOTwewyItemType.Badge, ItemClassification.filler, [NEOTwewyItemGroup.COMBAT_PIN], "Cony×Cony", 0, "Light"
    ),
    "Grégoire Lapin": NEOTwewyItemData(
        1146, NEOTwewyItemType.Badge, ItemClassification.filler, [NEOTwewyItemGroup.COMBAT_PIN], "Cony×Cony", 0, "Light"
    ),
    "Popguin": NEOTwewyItemData(
        1147, NEOTwewyItemType.Badge, ItemClassification.filler, [NEOTwewyItemGroup.COMBAT_PIN], "Unbranded", 0, "Ice"
    ),
    "Topo the Generous": NEOTwewyItemData(
        1148,
        NEOTwewyItemType.Badge,
        ItemClassification.filler,
        [NEOTwewyItemGroup.COMBAT_PIN],
        "Top o' Topo",
        0,
        "Burst",
    ),
    "Once Upon a Dream": NEOTwewyItemData(
        1149,
        NEOTwewyItemType.Badge,
        ItemClassification.filler,
        [NEOTwewyItemGroup.COMBAT_PIN],
        "Top o' Topo",
        0,
        "Burst",
    ),
    "Music of the Woods": NEOTwewyItemData(
        1150,
        NEOTwewyItemType.Badge,
        ItemClassification.filler,
        [NEOTwewyItemGroup.COMBAT_PIN],
        "Top o' Topo",
        0,
        "Sound",
    ),
    "Mom's Secret Ingredient": NEOTwewyItemData(
        1151,
        NEOTwewyItemType.Badge,
        ItemClassification.filler,
        [NEOTwewyItemGroup.COMBAT_PIN],
        "Top o' Topo",
        0,
        "Poison",
    ),
    "A Mysterious Gift": NEOTwewyItemData(
        1152,
        NEOTwewyItemType.Badge,
        ItemClassification.filler,
        [NEOTwewyItemGroup.COMBAT_PIN],
        "Top o' Topo",
        0,
        "Poison",
    ),
    "The World Within": NEOTwewyItemData(
        1153,
        NEOTwewyItemType.Badge,
        ItemClassification.filler,
        [NEOTwewyItemGroup.COMBAT_PIN],
        "Top o' Topo",
        0,
        "Light",
    ),
    "Topo the Ingenious": NEOTwewyItemData(
        1154,
        NEOTwewyItemType.Badge,
        ItemClassification.filler,
        [NEOTwewyItemGroup.COMBAT_PIN],
        "Top o' Topo",
        0,
        "Light",
    ),
    "My Precious Moments": NEOTwewyItemData(
        1155,
        NEOTwewyItemType.Badge,
        ItemClassification.filler,
        [NEOTwewyItemGroup.COMBAT_PIN],
        "Top o' Topo",
        0,
        "Time",
    ),
    "Topo the Beloved": NEOTwewyItemData(
        1156,
        NEOTwewyItemType.Badge,
        ItemClassification.filler,
        [NEOTwewyItemGroup.COMBAT_PIN],
        "Top o' Topo",
        0,
        "Time",
    ),
    "ShoGun・Void": NEOTwewyItemData(
        1157, NEOTwewyItemType.Badge, ItemClassification.filler, [NEOTwewyItemGroup.COMBAT_PIN], "RyuGu", 0, "None"
    ),
    "ManjuSage・Void": NEOTwewyItemData(
        1158, NEOTwewyItemType.Badge, ItemClassification.filler, [NEOTwewyItemGroup.COMBAT_PIN], "RyuGu", 0, "None"
    ),
    "EnJo・Blaze": NEOTwewyItemData(
        1159, NEOTwewyItemType.Badge, ItemClassification.filler, [NEOTwewyItemGroup.COMBAT_PIN], "RyuGu", 0, "Fire"
    ),
    "KoYo・Blaze": NEOTwewyItemData(
        1160, NEOTwewyItemType.Badge, ItemClassification.filler, [NEOTwewyItemGroup.COMBAT_PIN], "RyuGu", 0, "Fire"
    ),
    "Tsubaki・Frost": NEOTwewyItemData(
        1161, NEOTwewyItemType.Badge, ItemClassification.filler, [NEOTwewyItemGroup.COMBAT_PIN], "RyuGu", 0, "Ice"
    ),
    "HiGan・Frost": NEOTwewyItemData(
        1162, NEOTwewyItemType.Badge, ItemClassification.filler, [NEOTwewyItemGroup.COMBAT_PIN], "RyuGu", 0, "Ice"
    ),
    "InaZuma・Surge": NEOTwewyItemData(
        1163, NEOTwewyItemType.Badge, ItemClassification.filler, [NEOTwewyItemGroup.COMBAT_PIN], "RyuGu", 0, "Electric"
    ),
    "RaiJin・Surge": NEOTwewyItemData(
        1164, NEOTwewyItemType.Badge, ItemClassification.filler, [NEOTwewyItemGroup.COMBAT_PIN], "RyuGu", 0, "Electric"
    ),
    "Doku Doku Panic": NEOTwewyItemData(
        1165,
        NEOTwewyItemType.Badge,
        ItemClassification.filler,
        [NEOTwewyItemGroup.COMBAT_PIN],
        "croaky panic",
        0,
        "Poison",
    ),
    "KeiRyu・Epoch": NEOTwewyItemData(
        1166, NEOTwewyItemType.Badge, ItemClassification.filler, [NEOTwewyItemGroup.COMBAT_PIN], "RyuGu", 0, "Time"
    ),
    "RyuGu・Void": NEOTwewyItemData(
        1167, NEOTwewyItemType.Badge, ItemClassification.filler, [NEOTwewyItemGroup.COMBAT_PIN], "RyuGu", 0, "None"
    ),
    "HanaDoki・Void": NEOTwewyItemData(
        1168, NEOTwewyItemType.Badge, ItemClassification.filler, [NEOTwewyItemGroup.COMBAT_PIN], "RyuGu", 0, "None"
    ),
    "Slitherin' Snake": NEOTwewyItemData(
        1169,
        NEOTwewyItemType.Badge,
        ItemClassification.filler,
        [NEOTwewyItemGroup.COMBAT_PIN],
        "croaky panic",
        0,
        "Poison",
    ),
    "HoGyoku・Gleam": NEOTwewyItemData(
        1170, NEOTwewyItemType.Badge, ItemClassification.filler, [NEOTwewyItemGroup.COMBAT_PIN], "RyuGu", 0, "Light"
    ),
    "Jelly": NEOTwewyItemData(
        1171,
        NEOTwewyItemType.Badge,
        ItemClassification.filler,
        [NEOTwewyItemGroup.COMBAT_PIN],
        "Unbranded",
        0,
        "Electric",
    ),
    "Righteous Rabbit": NEOTwewyItemData(
        1172, NEOTwewyItemType.Badge, ItemClassification.filler, [NEOTwewyItemGroup.COMBAT_PIN], "Cony×Cony", 0, "None"
    ),
    "Brooding Bunny": NEOTwewyItemData(
        1173, NEOTwewyItemType.Badge, ItemClassification.filler, [NEOTwewyItemGroup.COMBAT_PIN], "Cony×Cony", 0, "None"
    ),
    "Ring-a-Ling": NEOTwewyItemData(
        1174,
        NEOTwewyItemType.Badge,
        ItemClassification.filler,
        [NEOTwewyItemGroup.COMBAT_PIN],
        "croaky panic",
        0,
        "Kinesis",
    ),
    "Flyin' High": NEOTwewyItemData(
        1175,
        NEOTwewyItemType.Badge,
        ItemClassification.filler,
        [NEOTwewyItemGroup.COMBAT_PIN],
        "croaky panic",
        0,
        "Kinesis",
    ),
    "Melancony×Melancony": NEOTwewyItemData(
        1176,
        NEOTwewyItemType.Badge,
        ItemClassification.filler,
        [NEOTwewyItemGroup.COMBAT_PIN],
        "Cony×Cony",
        0,
        "Gravity",
    ),
    "ConyｘCony": NEOTwewyItemData(
        1177,
        NEOTwewyItemType.Badge,
        ItemClassification.filler,
        [NEOTwewyItemGroup.COMBAT_PIN],
        "Cony×Cony",
        0,
        "Gravity",
    ),
    "Seraphic Snow": NEOTwewyItemData(
        1178, NEOTwewyItemType.Badge, ItemClassification.filler, [NEOTwewyItemGroup.COMBAT_PIN], "Cony×Cony", 0, "Ice"
    ),
    "Raven": NEOTwewyItemData(
        1179, NEOTwewyItemType.Badge, ItemClassification.filler, [NEOTwewyItemGroup.COMBAT_PIN], "Unbranded", 0, "Wind"
    ),
    "Balloon Trip": NEOTwewyItemData(
        1180,
        NEOTwewyItemType.Badge,
        ItemClassification.filler,
        [NEOTwewyItemGroup.COMBAT_PIN],
        "Top o' Topo",
        0,
        "Burst",
    ),
    "Riled-Up Ribbon": NEOTwewyItemData(
        1181,
        NEOTwewyItemType.Badge,
        ItemClassification.filler,
        [NEOTwewyItemGroup.COMBAT_PIN],
        "Top o' Topo",
        0,
        "Burst",
    ),
    "Topo the Talented": NEOTwewyItemData(
        1182,
        NEOTwewyItemType.Badge,
        ItemClassification.filler,
        [NEOTwewyItemGroup.COMBAT_PIN],
        "Top o' Topo",
        0,
        "Sound",
    ),
    "Catch a Wave": NEOTwewyItemData(
        1183,
        NEOTwewyItemType.Badge,
        ItemClassification.filler,
        [NEOTwewyItemGroup.COMBAT_PIN],
        "croaky panic",
        0,
        "Water",
    ),
    "Kappa Panic": NEOTwewyItemData(
        1184,
        NEOTwewyItemType.Badge,
        ItemClassification.filler,
        [NEOTwewyItemGroup.COMBAT_PIN],
        "croaky panic",
        0,
        "Water",
    ),
    "A Forlorn Treasure": NEOTwewyItemData(
        1185,
        NEOTwewyItemType.Badge,
        ItemClassification.filler,
        [NEOTwewyItemGroup.COMBAT_PIN],
        "Top o' Topo",
        0,
        "Darkness",
    ),
    "Cave of Secrets": NEOTwewyItemData(
        1186,
        NEOTwewyItemType.Badge,
        ItemClassification.filler,
        [NEOTwewyItemGroup.COMBAT_PIN],
        "Top o' Topo",
        0,
        "Darkness",
    ),
    "In the Snipeline": NEOTwewyItemData(
        1187, NEOTwewyItemType.Badge, ItemClassification.filler, [NEOTwewyItemGroup.COMBAT_PIN], "garagara", 0, "None"
    ),
    "Don't Miss Your Shot": NEOTwewyItemData(
        1188, NEOTwewyItemType.Badge, ItemClassification.filler, [NEOTwewyItemGroup.COMBAT_PIN], "garagara", 0, "None"
    ),
    "Any Way You Snipe It": NEOTwewyItemData(
        1189, NEOTwewyItemType.Badge, ItemClassification.filler, [NEOTwewyItemGroup.COMBAT_PIN], "garagara", 0, "None"
    ),
    "garagara": NEOTwewyItemData(
        1190, NEOTwewyItemType.Badge, ItemClassification.filler, [NEOTwewyItemGroup.COMBAT_PIN], "garagara", 0, "None"
    ),
    "Shot in the Dank": NEOTwewyItemData(
        1191, NEOTwewyItemType.Badge, ItemClassification.filler, [NEOTwewyItemGroup.COMBAT_PIN], "garagara", 0, "Poison"
    ),
    "What Can Never Be": NEOTwewyItemData(
        1192,
        NEOTwewyItemType.Badge,
        ItemClassification.filler,
        [NEOTwewyItemGroup.COMBAT_PIN],
        "IL CAVALLO DEL RE",
        0,
        "None",
    ),
    "Stuck in the Middle": NEOTwewyItemData(
        1193,
        NEOTwewyItemType.Badge,
        ItemClassification.filler,
        [NEOTwewyItemGroup.COMBAT_PIN],
        "IL CAVALLO DEL RE",
        0,
        "Gravity",
    ),
    "Time in a Bottle": NEOTwewyItemData(
        1194,
        NEOTwewyItemType.Badge,
        ItemClassification.filler,
        [NEOTwewyItemGroup.COMBAT_PIN],
        "IL CAVALLO DEL RE",
        0,
        "Time",
    ),
    "Stay Gold": NEOTwewyItemData(
        1195,
        NEOTwewyItemType.Badge,
        ItemClassification.filler,
        [NEOTwewyItemGroup.COMBAT_PIN],
        "IL CAVALLO DEL RE",
        0,
        "Light",
    ),
    "Stay Beautiful": NEOTwewyItemData(
        1196,
        NEOTwewyItemType.Badge,
        ItemClassification.filler,
        [NEOTwewyItemGroup.COMBAT_PIN],
        "IL CAVALLO DEL RE",
        0,
        "Darkness",
    ),
    "Let the Storm Rage On": NEOTwewyItemData(
        1197,
        NEOTwewyItemType.Badge,
        ItemClassification.filler,
        [NEOTwewyItemGroup.COMBAT_PIN],
        "IL CAVALLO DEL RE",
        0,
        "Electric",
    ),
    "SuiGen・Void": NEOTwewyItemData(
        1198, NEOTwewyItemType.Badge, ItemClassification.filler, [NEOTwewyItemGroup.COMBAT_PIN], "RyuGu", 0, "None"
    ),
    "KoCho・Void": NEOTwewyItemData(
        1199, NEOTwewyItemType.Badge, ItemClassification.filler, [NEOTwewyItemGroup.COMBAT_PIN], "RyuGu", 0, "None"
    ),
    "ShiDare・Shade": NEOTwewyItemData(
        1200, NEOTwewyItemType.Badge, ItemClassification.filler, [NEOTwewyItemGroup.COMBAT_PIN], "RyuGu", 0, "Darkness"
    ),
    "Tsuzumi・Echo": NEOTwewyItemData(
        1201, NEOTwewyItemType.Badge, ItemClassification.filler, [NEOTwewyItemGroup.COMBAT_PIN], "RyuGu", 0, "Sound"
    ),
    "Shiba": NEOTwewyItemData(
        1202, NEOTwewyItemType.Badge, ItemClassification.filler, [NEOTwewyItemGroup.COMBAT_PIN], "Unbranded", 0, "None"
    ),
    "Let's Have Fungis!": NEOTwewyItemData(
        1203, NEOTwewyItemType.Badge, ItemClassification.filler, [NEOTwewyItemGroup.COMBAT_PIN], "Unbranded", 0, "Water"
    ),
    "Fuel to the Fire": NEOTwewyItemData(
        1204, NEOTwewyItemType.Badge, ItemClassification.filler, [NEOTwewyItemGroup.COMBAT_PIN], "garagara", 0, "Fire"
    ),
    "Fire in the Belly": NEOTwewyItemData(
        1205, NEOTwewyItemType.Badge, ItemClassification.filler, [NEOTwewyItemGroup.COMBAT_PIN], "garagara", 0, "Fire"
    ),
    "Ifs, Ands, or Bolts": NEOTwewyItemData(
        1206,
        NEOTwewyItemType.Badge,
        ItemClassification.filler,
        [NEOTwewyItemGroup.COMBAT_PIN],
        "garagara",
        0,
        "Electric",
    ),
    "Sparks Will Fly": NEOTwewyItemData(
        1207,
        NEOTwewyItemType.Badge,
        ItemClassification.filler,
        [NEOTwewyItemGroup.COMBAT_PIN],
        "garagara",
        0,
        "Electric",
    ),
    "AraUmi・Gale": NEOTwewyItemData(
        1208, NEOTwewyItemType.Badge, ItemClassification.filler, [NEOTwewyItemGroup.COMBAT_PIN], "RyuGu", 0, "Wind"
    ),
    "FuJin・Gale": NEOTwewyItemData(
        1209, NEOTwewyItemType.Badge, ItemClassification.filler, [NEOTwewyItemGroup.COMBAT_PIN], "RyuGu", 0, "Wind"
    ),
    "IroGoi・Shift": NEOTwewyItemData(
        1210, NEOTwewyItemType.Badge, ItemClassification.filler, [NEOTwewyItemGroup.COMBAT_PIN], "RyuGu", 0, "Kinesis"
    ),
    "ShoRyu・Gleam": NEOTwewyItemData(
        1211, NEOTwewyItemType.Badge, ItemClassification.filler, [NEOTwewyItemGroup.COMBAT_PIN], "RyuGu", 0, "Light"
    ),
    "The Prismatic Princess": NEOTwewyItemData(
        1212,
        NEOTwewyItemType.Badge,
        ItemClassification.filler,
        [NEOTwewyItemGroup.COMBAT_PIN],
        "Top o' Topo",
        0,
        "Light",
    ),
    "The Benevolent King": NEOTwewyItemData(
        1213,
        NEOTwewyItemType.Badge,
        ItemClassification.filler,
        [NEOTwewyItemGroup.COMBAT_PIN],
        "Top o' Topo",
        0,
        "Light",
    ),
    "Top o' Topo": NEOTwewyItemData(
        1214,
        NEOTwewyItemType.Badge,
        ItemClassification.filler,
        [NEOTwewyItemGroup.COMBAT_PIN],
        "Top o' Topo",
        0,
        "Electric",
    ),
    "Petals of Love": NEOTwewyItemData(
        1215,
        NEOTwewyItemType.Badge,
        ItemClassification.filler,
        [NEOTwewyItemGroup.COMBAT_PIN],
        "Top o' Topo",
        0,
        "Fire",
    ),
    "Topo the Adventurous": NEOTwewyItemData(
        1216,
        NEOTwewyItemType.Badge,
        ItemClassification.filler,
        [NEOTwewyItemGroup.COMBAT_PIN],
        "Top o' Topo",
        0,
        "Fire",
    ),
    "Fairytale Memories": NEOTwewyItemData(
        1217, NEOTwewyItemType.Badge, ItemClassification.filler, [NEOTwewyItemGroup.COMBAT_PIN], "Top o' Topo", 0, "Ice"
    ),
    "Topo the Famished": NEOTwewyItemData(
        1218, NEOTwewyItemType.Badge, ItemClassification.filler, [NEOTwewyItemGroup.COMBAT_PIN], "Top o' Topo", 0, "Ice"
    ),
    "The Enchanted Baker": NEOTwewyItemData(
        1219, NEOTwewyItemType.Badge, ItemClassification.filler, [NEOTwewyItemGroup.COMBAT_PIN], "Top o' Topo", 0, "Ice"
    ),
    "An Inseparable Pair": NEOTwewyItemData(
        1220,
        NEOTwewyItemType.Badge,
        ItemClassification.filler,
        [NEOTwewyItemGroup.COMBAT_PIN],
        "Top o' Topo",
        0,
        "Gravity",
    ),
    "Hammond's New Home": NEOTwewyItemData(
        1221,
        NEOTwewyItemType.Badge,
        ItemClassification.filler,
        [NEOTwewyItemGroup.COMBAT_PIN],
        "Top o' Topo",
        0,
        "Darkness",
    ),
    "Mr. Mew": NEOTwewyItemData(
        1222, NEOTwewyItemType.Badge, ItemClassification.filler, [NEOTwewyItemGroup.COMBAT_PIN], "Unbranded", 0, "Light"
    ),
    "KaChu・Blaze": NEOTwewyItemData(
        1223, NEOTwewyItemType.Badge, ItemClassification.filler, [NEOTwewyItemGroup.COMBAT_PIN], "RyuGu", 0, "Fire"
    ),
    "AkaFuji・Blaze": NEOTwewyItemData(
        1224, NEOTwewyItemType.Badge, ItemClassification.filler, [NEOTwewyItemGroup.COMBAT_PIN], "RyuGu", 0, "Fire"
    ),
    "Firestorm": NEOTwewyItemData(
        1225, NEOTwewyItemType.Badge, ItemClassification.filler, [NEOTwewyItemGroup.COMBAT_PIN], "Unbranded", 0, "Fire"
    ),
    "GoKa・Blaze": NEOTwewyItemData(
        1226, NEOTwewyItemType.Badge, ItemClassification.filler, [NEOTwewyItemGroup.COMBAT_PIN], "RyuGu", 0, "Fire"
    ),
    "Notice Me Lightning": NEOTwewyItemData(
        1227,
        NEOTwewyItemType.Badge,
        ItemClassification.filler,
        [NEOTwewyItemGroup.COMBAT_PIN],
        "NATURAL PUPPY",
        0,
        "Electric",
    ),
    "Oh Em Gee Lightning": NEOTwewyItemData(
        1228,
        NEOTwewyItemType.Badge,
        ItemClassification.filler,
        [NEOTwewyItemGroup.COMBAT_PIN],
        "NATURAL PUPPY",
        0,
        "Electric",
    ),
    "Trendy Tornado": NEOTwewyItemData(
        1229,
        NEOTwewyItemType.Badge,
        ItemClassification.filler,
        [NEOTwewyItemGroup.COMBAT_PIN],
        "NATURAL PUPPY",
        0,
        "Stone",
    ),
    "Giddy Graviton": NEOTwewyItemData(
        1230,
        NEOTwewyItemType.Badge,
        ItemClassification.filler,
        [NEOTwewyItemGroup.COMBAT_PIN],
        "NATURAL PUPPY",
        0,
        "Gravity",
    ),
    "Good Mood Graviton": NEOTwewyItemData(
        1231,
        NEOTwewyItemType.Badge,
        ItemClassification.filler,
        [NEOTwewyItemGroup.COMBAT_PIN],
        "NATURAL PUPPY",
        0,
        "Gravity",
    ),
    "Relative Absoluteness": NEOTwewyItemData(
        1232,
        NEOTwewyItemType.Badge,
        ItemClassification.filler,
        [NEOTwewyItemGroup.COMBAT_PIN],
        "MONOCROW",
        0,
        "Gravity",
    ),
    "Pachy": NEOTwewyItemData(
        1233, NEOTwewyItemType.Badge, ItemClassification.filler, [NEOTwewyItemGroup.COMBAT_PIN], "Unbranded", 0, "Stone"
    ),
    "A Day Off Outside": NEOTwewyItemData(
        1234,
        NEOTwewyItemType.Badge,
        ItemClassification.filler,
        [NEOTwewyItemGroup.COMBAT_PIN],
        "Shepherd House",
        0,
        "Wind",
    ),
    "The Cozy Hilltop Windmill": NEOTwewyItemData(
        1235,
        NEOTwewyItemType.Badge,
        ItemClassification.filler,
        [NEOTwewyItemGroup.COMBAT_PIN],
        "Shepherd House",
        0,
        "Wind",
    ),
    "The Breezy Ovine Wind": NEOTwewyItemData(
        1236,
        NEOTwewyItemType.Badge,
        ItemClassification.filler,
        [NEOTwewyItemGroup.COMBAT_PIN],
        "Shepherd House",
        0,
        "Wind",
    ),
    "The Ever-Arctic Treasure": NEOTwewyItemData(
        1237,
        NEOTwewyItemType.Badge,
        ItemClassification.filler,
        [NEOTwewyItemGroup.COMBAT_PIN],
        "Shepherd House",
        0,
        "Ice",
    ),
    "A Moonlit Night Inside": NEOTwewyItemData(
        1238,
        NEOTwewyItemType.Badge,
        ItemClassification.filler,
        [NEOTwewyItemGroup.COMBAT_PIN],
        "Shepherd House",
        0,
        "Ice",
    ),
    "The Woolly Triple Axel": NEOTwewyItemData(
        1239,
        NEOTwewyItemType.Badge,
        ItemClassification.filler,
        [NEOTwewyItemGroup.COMBAT_PIN],
        "Shepherd House",
        0,
        "Ice",
    ),
    "Cursed Croaker": NEOTwewyItemData(
        1240,
        NEOTwewyItemType.Badge,
        ItemClassification.filler,
        [NEOTwewyItemGroup.COMBAT_PIN],
        "croaky panic",
        0,
        "Darkness",
    ),
    "Roly Poly Cricket": NEOTwewyItemData(
        1241,
        NEOTwewyItemType.Badge,
        ItemClassification.filler,
        [NEOTwewyItemGroup.COMBAT_PIN],
        "croaky panic",
        0,
        "Darkness",
    ),
    "Thirsty Frog": NEOTwewyItemData(
        1242,
        NEOTwewyItemType.Badge,
        ItemClassification.filler,
        [NEOTwewyItemGroup.COMBAT_PIN],
        "croaky panic",
        0,
        "Light",
    ),
    "Golden Kappa Panic": NEOTwewyItemData(
        1243,
        NEOTwewyItemType.Badge,
        ItemClassification.filler,
        [NEOTwewyItemGroup.COMBAT_PIN],
        "croaky panic",
        0,
        "Light",
    ),
    "Snap Crackle Popcorn": NEOTwewyItemData(
        1244,
        NEOTwewyItemType.Badge,
        ItemClassification.filler,
        [NEOTwewyItemGroup.COMBAT_PIN],
        "croaky panic",
        0,
        "Water",
    ),
    "Sunny Side Skillet": NEOTwewyItemData(
        1245,
        NEOTwewyItemType.Badge,
        ItemClassification.filler,
        [NEOTwewyItemGroup.COMBAT_PIN],
        "croaky panic",
        0,
        "Water",
    ),
    "A Tasty Ovine Snack": NEOTwewyItemData(
        1246,
        NEOTwewyItemType.Badge,
        ItemClassification.filler,
        [NEOTwewyItemGroup.COMBAT_PIN],
        "Shepherd House",
        0,
        "Wind",
    ),
    "The Gentle Airplane Pilot": NEOTwewyItemData(
        1247,
        NEOTwewyItemType.Badge,
        ItemClassification.filler,
        [NEOTwewyItemGroup.COMBAT_PIN],
        "Shepherd House",
        0,
        "Wind",
    ),
    "The Song of Friendship": NEOTwewyItemData(
        1248,
        NEOTwewyItemType.Badge,
        ItemClassification.filler,
        [NEOTwewyItemGroup.COMBAT_PIN],
        "Shepherd House",
        0,
        "Sound",
    ),
    "The Woolly Jazz Player": NEOTwewyItemData(
        1249,
        NEOTwewyItemType.Badge,
        ItemClassification.filler,
        [NEOTwewyItemGroup.COMBAT_PIN],
        "Shepherd House",
        0,
        "Sound",
    ),
    "Back to the Ewe-ture": NEOTwewyItemData(
        1250,
        NEOTwewyItemType.Badge,
        ItemClassification.filler,
        [NEOTwewyItemGroup.COMBAT_PIN],
        "Shepherd House",
        0,
        "Time",
    ),
    "Shark": NEOTwewyItemData(
        1251, NEOTwewyItemType.Badge, ItemClassification.filler, [NEOTwewyItemGroup.COMBAT_PIN], "Unbranded", 0, "Water"
    ),
    "Chef Amphibie": NEOTwewyItemData(
        1252,
        NEOTwewyItemType.Badge,
        ItemClassification.filler,
        [NEOTwewyItemGroup.COMBAT_PIN],
        "croaky panic",
        0,
        "Poison",
    ),
    "Star Quarterback": NEOTwewyItemData(
        1253, NEOTwewyItemType.Badge, ItemClassification.filler, [NEOTwewyItemGroup.COMBAT_PIN], "HOG FANG", 0, "None"
    ),
    "Dine 'n' Dash": NEOTwewyItemData(
        1254, NEOTwewyItemType.Badge, ItemClassification.filler, [NEOTwewyItemGroup.COMBAT_PIN], "HOG FANG", 0, "None"
    ),
    "Bolt Boar": NEOTwewyItemData(
        1255,
        NEOTwewyItemType.Badge,
        ItemClassification.filler,
        [NEOTwewyItemGroup.COMBAT_PIN],
        "HOG FANG",
        0,
        "Electric",
    ),
    "Mr. Fangman": NEOTwewyItemData(
        1256,
        NEOTwewyItemType.Badge,
        ItemClassification.filler,
        [NEOTwewyItemGroup.COMBAT_PIN],
        "HOG FANG",
        0,
        "Electric",
    ),
    "Burnin' Boar": NEOTwewyItemData(
        1257, NEOTwewyItemType.Badge, ItemClassification.filler, [NEOTwewyItemGroup.COMBAT_PIN], "HOG FANG", 0, "Fire"
    ),
    "HOG FANG": NEOTwewyItemData(
        1258, NEOTwewyItemType.Badge, ItemClassification.filler, [NEOTwewyItemGroup.COMBAT_PIN], "HOG FANG", 0, "Fire"
    ),
    "Big Bang Boar": NEOTwewyItemData(
        1259, NEOTwewyItemType.Badge, ItemClassification.filler, [NEOTwewyItemGroup.COMBAT_PIN], "HOG FANG", 0, "Burst"
    ),
    "Cervus": NEOTwewyItemData(
        1260,
        NEOTwewyItemType.Badge,
        ItemClassification.filler,
        [NEOTwewyItemGroup.COMBAT_PIN],
        "Unbranded",
        0,
        "Electric",
    ),
    "UFO Rescue": NEOTwewyItemData(
        1261, NEOTwewyItemType.Badge, ItemClassification.filler, [NEOTwewyItemGroup.COMBAT_PIN], "HOG FANG", 0, "Light"
    ),
    "Tigre PUNKS": NEOTwewyItemData(
        1262,
        NEOTwewyItemType.Badge,
        ItemClassification.filler,
        [NEOTwewyItemGroup.COMBAT_PIN],
        "Tigre PUNKS",
        0,
        "Light",
    ),
    "Bright Chord": NEOTwewyItemData(
        1263,
        NEOTwewyItemType.Badge,
        ItemClassification.filler,
        [NEOTwewyItemGroup.COMBAT_PIN],
        "Tigre PUNKS",
        0,
        "Light",
    ),
    "Bootleg Tune": NEOTwewyItemData(
        1264,
        NEOTwewyItemType.Badge,
        ItemClassification.filler,
        [NEOTwewyItemGroup.COMBAT_PIN],
        "Tigre PUNKS",
        0,
        "Sound",
    ),
    "Discordance": NEOTwewyItemData(
        1265,
        NEOTwewyItemType.Badge,
        ItemClassification.filler,
        [NEOTwewyItemGroup.COMBAT_PIN],
        "Tigre PUNKS",
        0,
        "Sound",
    ),
    "Maiden Beat": NEOTwewyItemData(
        1266,
        NEOTwewyItemType.Badge,
        ItemClassification.filler,
        [NEOTwewyItemGroup.COMBAT_PIN],
        "Tigre PUNKS",
        0,
        "Sound",
    ),
    "Aw, That Shucks!": NEOTwewyItemData(
        1267, NEOTwewyItemType.Badge, ItemClassification.filler, [NEOTwewyItemGroup.COMBAT_PIN], "Unbranded", 0, "Time"
    ),
    "Headliner": NEOTwewyItemData(
        1268,
        NEOTwewyItemType.Badge,
        ItemClassification.filler,
        [NEOTwewyItemGroup.COMBAT_PIN],
        "Tigre PUNKS",
        0,
        "Sound",
    ),
    "Runaway Rocket": NEOTwewyItemData(
        1269, NEOTwewyItemType.Badge, ItemClassification.filler, [NEOTwewyItemGroup.COMBAT_PIN], "HOG FANG", 0, "Light"
    ),
    "Clawed Guardian": NEOTwewyItemData(
        1270,
        NEOTwewyItemType.Badge,
        ItemClassification.filler,
        [NEOTwewyItemGroup.COMBAT_PIN],
        "Tigre PUNKS",
        0,
        "Light",
    ),
    "HOG Healer": NEOTwewyItemData(
        1271, NEOTwewyItemType.Badge, ItemClassification.filler, [NEOTwewyItemGroup.COMBAT_PIN], "HOG FANG", 0, "Light"
    ),
    "Rip-Roarin' Red": NEOTwewyItemData(
        1272, NEOTwewyItemType.Badge, ItemClassification.filler, [NEOTwewyItemGroup.COMBAT_PIN], "HOG FANG", 0, "None"
    ),
    "Never Too Young": NEOTwewyItemData(
        1273, NEOTwewyItemType.Badge, ItemClassification.filler, [NEOTwewyItemGroup.COMBAT_PIN], "HOG FANG", 0, "None"
    ),
    "Lost in Space": NEOTwewyItemData(
        1274, NEOTwewyItemType.Badge, ItemClassification.filler, [NEOTwewyItemGroup.COMBAT_PIN], "HOG FANG", 0, "None"
    ),
    "Rainbow Route 66": NEOTwewyItemData(
        1275, NEOTwewyItemType.Badge, ItemClassification.filler, [NEOTwewyItemGroup.COMBAT_PIN], "HOG FANG", 0, "Wind"
    ),
    "Hogway to Heaven": NEOTwewyItemData(
        1276, NEOTwewyItemType.Badge, ItemClassification.filler, [NEOTwewyItemGroup.COMBAT_PIN], "HOG FANG", 0, "Wind"
    ),
    "Heartful Hot Dog": NEOTwewyItemData(
        1277, NEOTwewyItemType.Badge, ItemClassification.filler, [NEOTwewyItemGroup.COMBAT_PIN], "HOG FANG", 0, "Stone"
    ),
    "Rhino": NEOTwewyItemData(
        1278, NEOTwewyItemType.Badge, ItemClassification.filler, [NEOTwewyItemGroup.COMBAT_PIN], "Unbranded", 0, "Stone"
    ),
    "FANG Defender": NEOTwewyItemData(
        1279, NEOTwewyItemType.Badge, ItemClassification.filler, [NEOTwewyItemGroup.COMBAT_PIN], "HOG FANG", 0, "Light"
    ),
    "Watch Your Step": NEOTwewyItemData(
        1280,
        NEOTwewyItemType.Badge,
        ItemClassification.filler,
        [NEOTwewyItemGroup.COMBAT_PIN],
        "MONOCROW",
        0,
        "Kinesis",
    ),
    "You Can Overcome": NEOTwewyItemData(
        1281,
        NEOTwewyItemType.Badge,
        ItemClassification.filler,
        [NEOTwewyItemGroup.COMBAT_PIN],
        "MONOCROW",
        0,
        "Kinesis",
    ),
    "Look Out Below": NEOTwewyItemData(
        1282,
        NEOTwewyItemType.Badge,
        ItemClassification.filler,
        [NEOTwewyItemGroup.COMBAT_PIN],
        "MONOCROW",
        0,
        "Kinesis",
    ),
    "Absolute Relativity": NEOTwewyItemData(
        1283,
        NEOTwewyItemType.Badge,
        ItemClassification.filler,
        [NEOTwewyItemGroup.COMBAT_PIN],
        "MONOCROW",
        0,
        "Kinesis",
    ),
    "Pig": NEOTwewyItemData(
        1284,
        NEOTwewyItemType.Badge,
        ItemClassification.filler,
        [NEOTwewyItemGroup.COMBAT_PIN],
        "Unbranded",
        0,
        "Kinesis",
    ),
    "Seductive Snare": NEOTwewyItemData(
        1285,
        NEOTwewyItemType.Badge,
        ItemClassification.filler,
        [NEOTwewyItemGroup.COMBAT_PIN],
        "Joli bécot",
        0,
        "Gravity",
    ),
    "Deadly Fragrance": NEOTwewyItemData(
        1286,
        NEOTwewyItemType.Badge,
        ItemClassification.filler,
        [NEOTwewyItemGroup.COMBAT_PIN],
        "Joli bécot",
        0,
        "Gravity",
    ),
    "A Drawn Conclusion": NEOTwewyItemData(
        1287,
        NEOTwewyItemType.Badge,
        ItemClassification.filler,
        [NEOTwewyItemGroup.COMBAT_PIN],
        "garagara",
        0,
        "Gravity",
    ),
    "Gravving at Straws": NEOTwewyItemData(
        1288,
        NEOTwewyItemType.Badge,
        ItemClassification.filler,
        [NEOTwewyItemGroup.COMBAT_PIN],
        "garagara",
        0,
        "Gravity",
    ),
    "Leon": NEOTwewyItemData(
        1289,
        NEOTwewyItemType.Badge,
        ItemClassification.filler,
        [NEOTwewyItemGroup.COMBAT_PIN],
        "Unbranded",
        0,
        "Gravity",
    ),
    "Tenka Juzumaru": NEOTwewyItemData(
        1290,
        NEOTwewyItemType.Badge,
        ItemClassification.filler,
        [NEOTwewyItemGroup.COMBAT_PIN],
        "Jupiter of the Monkey",
        0,
        "Sound",
    ),
    "Tenka Mikazuki": NEOTwewyItemData(
        1291,
        NEOTwewyItemType.Badge,
        ItemClassification.filler,
        [NEOTwewyItemGroup.COMBAT_PIN],
        "Jupiter of the Monkey",
        0,
        "Sound",
    ),
    "Coochy-Coochy-Coo": NEOTwewyItemData(
        1292,
        NEOTwewyItemType.Badge,
        ItemClassification.filler,
        [NEOTwewyItemGroup.COMBAT_PIN],
        "Unbranded",
        0,
        "Poison",
    ),
    "Black Cat Crush": NEOTwewyItemData(
        1293,
        NEOTwewyItemType.Badge,
        ItemClassification.filler,
        [NEOTwewyItemGroup.COMBAT_PIN],
        "Gatto Nero",
        0,
        "Light",
    ),
    "Black Cat Cards": NEOTwewyItemData(
        1294,
        NEOTwewyItemType.Badge,
        ItemClassification.filler,
        [NEOTwewyItemGroup.COMBAT_PIN],
        "Gatto Nero",
        0,
        "Electric",
    ),
    "Black Cat Comet": NEOTwewyItemData(
        1295, NEOTwewyItemType.Badge, ItemClassification.filler, [NEOTwewyItemGroup.COMBAT_PIN], "Gatto Nero", 0, "Fire"
    ),
    "Black Cat Burst": NEOTwewyItemData(
        1296,
        NEOTwewyItemType.Badge,
        ItemClassification.filler,
        [NEOTwewyItemGroup.COMBAT_PIN],
        "Gatto Nero",
        0,
        "Kinesis",
    ),
    "Black Cat Blades": NEOTwewyItemData(
        1297, NEOTwewyItemType.Badge, ItemClassification.filler, [NEOTwewyItemGroup.COMBAT_PIN], "Gatto Nero", 0, "Ice"
    ),
    "Black Cat Burn": NEOTwewyItemData(
        1298,
        NEOTwewyItemType.Badge,
        ItemClassification.filler,
        [NEOTwewyItemGroup.COMBAT_PIN],
        "Gatto Nero",
        0,
        "Darkness",
    ),
    "St. Ver's Uppercut": NEOTwewyItemData(
        1299,
        NEOTwewyItemType.Badge,
        ItemClassification.filler,
        [NEOTwewyItemGroup.COMBAT_PIN],
        "Gatto Nero",
        0,
        "Light",
    ),
    "St. Aestas' Shrapnel": NEOTwewyItemData(
        1300,
        NEOTwewyItemType.Badge,
        ItemClassification.filler,
        [NEOTwewyItemGroup.COMBAT_PIN],
        "Gatto Nero",
        0,
        "Light",
    ),
    "St. Autumnus' Strike": NEOTwewyItemData(
        1301,
        NEOTwewyItemType.Badge,
        ItemClassification.filler,
        [NEOTwewyItemGroup.COMBAT_PIN],
        "Gatto Nero",
        0,
        "Light",
    ),
    "St. Hiems' Shotgun": NEOTwewyItemData(
        1302,
        NEOTwewyItemType.Badge,
        ItemClassification.filler,
        [NEOTwewyItemGroup.COMBAT_PIN],
        "Gatto Nero",
        0,
        "Light",
    ),
    "Charge Punch E": NEOTwewyItemData(
        1303, NEOTwewyItemType.Badge, ItemClassification.filler, [NEOTwewyItemGroup.COMBAT_PIN], "Gatto Nero", 0, "Time"
    ),
    "Snare Trap E": NEOTwewyItemData(
        1304,
        NEOTwewyItemType.Badge,
        ItemClassification.filler,
        [NEOTwewyItemGroup.COMBAT_PIN],
        "Gatto Nero",
        0,
        "Gravity",
    ),
    "Just Keep Swimmin'!": NEOTwewyItemData(
        1305, NEOTwewyItemType.Badge, ItemClassification.filler, [NEOTwewyItemGroup.COMBAT_PIN], "Unbranded", 0, "Water"
    ),
    "What a Shock!": NEOTwewyItemData(
        1306,
        NEOTwewyItemType.Badge,
        ItemClassification.filler,
        [NEOTwewyItemGroup.COMBAT_PIN],
        "Unbranded",
        0,
        "Electric",
    ),
    "Stop the Music!": NEOTwewyItemData(
        1307, NEOTwewyItemType.Badge, ItemClassification.filler, [NEOTwewyItemGroup.COMBAT_PIN], "Unbranded", 0, "Burst"
    ),
    "Thanks Very Mochi!": NEOTwewyItemData(
        1308,
        NEOTwewyItemType.Badge,
        ItemClassification.filler,
        [NEOTwewyItemGroup.COMBAT_PIN],
        "Unbranded",
        0,
        "Gravity",
    ),
    "Holy Guacamole!": NEOTwewyItemData(
        1309, NEOTwewyItemType.Badge, ItemClassification.filler, [NEOTwewyItemGroup.COMBAT_PIN], "Unbranded", 0, "Fire"
    ),
    "Exercisin' Gator": NEOTwewyItemData(
        1310,
        NEOTwewyItemType.Badge,
        ItemClassification.filler,
        [NEOTwewyItemGroup.COMBAT_PIN],
        "Unbranded",
        0,
        "Gravity",
    ),
    "Handstandin' Panda": NEOTwewyItemData(
        1311,
        NEOTwewyItemType.Badge,
        ItemClassification.filler,
        [NEOTwewyItemGroup.COMBAT_PIN],
        "Unbranded",
        0,
        "Kinesis",
    ),
    "Archipelago": NEOTwewyItemData(
        5000, NEOTwewyItemType.Badge, ItemClassification.filler, [], "Unbranded", 0, "None"
    ),
    "5 Yen": NEOTwewyItemData(
        5001,
        NEOTwewyItemType.Badge,
        ItemClassification.skip_balancing,
        [NEOTwewyItemGroup.MONEY],
        "Unbranded",
        0,
        "None",
    ),
    "10 Yen": NEOTwewyItemData(
        5002,
        NEOTwewyItemType.Badge,
        ItemClassification.skip_balancing,
        [NEOTwewyItemGroup.MONEY],
        "Unbranded",
        0,
        "None",
    ),
    "50 Yen": NEOTwewyItemData(
        5003,
        NEOTwewyItemType.Badge,
        ItemClassification.skip_balancing,
        [NEOTwewyItemGroup.MONEY],
        "Unbranded",
        0,
        "None",
    ),
    "100 Yen": NEOTwewyItemData(
        5004,
        NEOTwewyItemType.Badge,
        ItemClassification.skip_balancing,
        [NEOTwewyItemGroup.MONEY],
        "Unbranded",
        0,
        "None",
    ),
    "500 Yen": NEOTwewyItemData(
        5005,
        NEOTwewyItemType.Badge,
        ItemClassification.skip_balancing,
        [NEOTwewyItemGroup.MONEY],
        "Unbranded",
        0,
        "None",
    ),
    "1000 Yen": NEOTwewyItemData(
        5006,
        NEOTwewyItemType.Badge,
        ItemClassification.skip_balancing,
        [NEOTwewyItemGroup.MONEY],
        "Unbranded",
        0,
        "None",
    ),
    "5000 Yen": NEOTwewyItemData(
        5007,
        NEOTwewyItemType.Badge,
        ItemClassification.skip_balancing,
        [NEOTwewyItemGroup.MONEY],
        "Unbranded",
        0,
        "None",
    ),
    "10000 Yen": NEOTwewyItemData(
        5008,
        NEOTwewyItemType.Badge,
        ItemClassification.skip_balancing,
        [NEOTwewyItemGroup.MONEY],
        "Unbranded",
        0,
        "None",
    ),
    "100000 Yen": NEOTwewyItemData(
        5009,
        NEOTwewyItemType.Badge,
        ItemClassification.skip_balancing,
        [NEOTwewyItemGroup.MONEY],
        "Unbranded",
        0,
        "None",
    ),
    "Scarletite": NEOTwewyItemData(
        5100, NEOTwewyItemType.Badge, ItemClassification.filler, [NEOTwewyItemGroup.RARE_METAL], "Unbranded", 0, "None"
    ),
    "Rare Metal": NEOTwewyItemData(
        5101, NEOTwewyItemType.Badge, ItemClassification.filler, [NEOTwewyItemGroup.RARE_METAL], "Unbranded", 0, "None"
    ),
    "Tektite": NEOTwewyItemData(
        5102, NEOTwewyItemType.Badge, ItemClassification.filler, [NEOTwewyItemGroup.RARE_METAL], "Unbranded", 0, "None"
    ),
    "Adamantite": NEOTwewyItemData(
        5103, NEOTwewyItemType.Badge, ItemClassification.filler, [NEOTwewyItemGroup.RARE_METAL], "Unbranded", 0, "None"
    ),
    "Orichalcum": NEOTwewyItemData(
        5104, NEOTwewyItemType.Badge, ItemClassification.filler, [NEOTwewyItemGroup.RARE_METAL], "Unbranded", 0, "None"
    ),
    "Shadow Matter": NEOTwewyItemData(
        5105, NEOTwewyItemType.Badge, ItemClassification.filler, [NEOTwewyItemGroup.RARE_METAL], "Unbranded", 0, "None"
    ),
    "Dark Matter": NEOTwewyItemData(
        5106, NEOTwewyItemType.Badge, ItemClassification.filler, [NEOTwewyItemGroup.RARE_METAL], "Unbranded", 0, "None"
    ),
    "Axion": NEOTwewyItemData(
        5107, NEOTwewyItemType.Badge, ItemClassification.filler, [NEOTwewyItemGroup.RARE_METAL], "Unbranded", 0, "None"
    ),
    "Dilaton": NEOTwewyItemData(
        5108, NEOTwewyItemType.Badge, ItemClassification.filler, [NEOTwewyItemGroup.RARE_METAL], "Unbranded", 0, "None"
    ),
    "Dibaryon": NEOTwewyItemData(
        5109, NEOTwewyItemType.Badge, ItemClassification.filler, [NEOTwewyItemGroup.RARE_METAL], "Unbranded", 0, "None"
    ),
    "Sfermion": NEOTwewyItemData(
        5110, NEOTwewyItemType.Badge, ItemClassification.filler, [NEOTwewyItemGroup.RARE_METAL], "Unbranded", 0, "None"
    ),
    "Legendary Headphones": NEOTwewyItemData(
        10000, NEOTwewyItemType.Costume, ItemClassification.filler, [], "Jupiter of the Monkey", 5, "None"
    ),
    "Legendary Tank Top": NEOTwewyItemData(
        10001, NEOTwewyItemType.Costume, ItemClassification.filler, [], "Jupiter of the Monkey", 0, "None"
    ),
    "Legendary Shorts": NEOTwewyItemData(
        10002, NEOTwewyItemType.Costume, ItemClassification.filler, [], "Jupiter of the Monkey", 0, "None"
    ),
    "Legendary Sneakers": NEOTwewyItemData(
        10003, NEOTwewyItemType.Costume, ItemClassification.filler, [], "Jupiter of the Monkey", 0, "None"
    ),
    "Legendary Music Player": NEOTwewyItemData(
        10004, NEOTwewyItemType.Costume, ItemClassification.filler, [], "Jupiter of the Monkey", 0, "None"
    ),
    "Flower Headband": NEOTwewyItemData(
        10100, NEOTwewyItemType.Costume, ItemClassification.filler, [], "Top o' Topo", 0, "None"
    ),
    "Ribbon Headband": NEOTwewyItemData(
        10101, NEOTwewyItemType.Costume, ItemClassification.filler, [], "Top o' Topo", 0, "None"
    ),
    "Topo Hat": NEOTwewyItemData(
        10102, NEOTwewyItemType.Costume, ItemClassification.filler, [], "Top o' Topo", 0, "None"
    ),
    "Romantic Blouse": NEOTwewyItemData(
        10103, NEOTwewyItemType.Costume, ItemClassification.filler, [], "Top o' Topo", 0, "None"
    ),
    "Fluffy Sweater": NEOTwewyItemData(
        10104, NEOTwewyItemType.Costume, ItemClassification.filler, [], "Top o' Topo", 0, "None"
    ),
    "Top o' Topo T-Shirt": NEOTwewyItemData(
        10105, NEOTwewyItemType.Costume, ItemClassification.filler, [], "Top o' Topo", 0, "None"
    ),
    "Flowy Tulle Skirt": NEOTwewyItemData(
        10106, NEOTwewyItemType.Costume, ItemClassification.filler, [], "Top o' Topo", 0, "None"
    ),
    "Cropped Pants": NEOTwewyItemData(
        10107, NEOTwewyItemType.Costume, ItemClassification.filler, [], "Top o' Topo", 0, "None"
    ),
    "Tasteful Dress": NEOTwewyItemData(
        10108, NEOTwewyItemType.Costume, ItemClassification.filler, [], "Top o' Topo", 0, "None"
    ),
    "Marine Dress": NEOTwewyItemData(
        10109, NEOTwewyItemType.Costume, ItemClassification.filler, [], "Top o' Topo", 0, "None"
    ),
    "Ribbon Pumps": NEOTwewyItemData(
        10110, NEOTwewyItemType.Costume, ItemClassification.filler, [], "Top o' Topo", 0, "None"
    ),
    "Frilly Sandals": NEOTwewyItemData(
        10111, NEOTwewyItemType.Costume, ItemClassification.filler, [], "Top o' Topo", 0, "None"
    ),
    "Comfy Loafers": NEOTwewyItemData(
        10112, NEOTwewyItemType.Costume, ItemClassification.filler, [], "Top o' Topo", 0, "None"
    ),
    "Ribbon Bag": NEOTwewyItemData(
        10113, NEOTwewyItemType.Costume, ItemClassification.filler, [], "Top o' Topo", 0, "None"
    ),
    "Modest Tote Bag": NEOTwewyItemData(
        10114, NEOTwewyItemType.Costume, ItemClassification.filler, [], "Top o' Topo", 0, "None"
    ),
    "Cozy Cardigan": NEOTwewyItemData(
        10115, NEOTwewyItemType.Costume, ItemClassification.filler, [], "Top o' Topo", 0, "None"
    ),
    "Airy Skirt": NEOTwewyItemData(
        10116, NEOTwewyItemType.Costume, ItemClassification.filler, [], "Top o' Topo", 0, "None"
    ),
    "Flower Scrunchie": NEOTwewyItemData(
        10117, NEOTwewyItemType.Costume, ItemClassification.filler, [], "Top o' Topo", 0, "None"
    ),
    "Dazzling Denim Cap": NEOTwewyItemData(
        10200, NEOTwewyItemType.Costume, ItemClassification.filler, [], "Joli bécot", 0, "None"
    ),
    "Cattle Print Hat": NEOTwewyItemData(
        10201, NEOTwewyItemType.Costume, ItemClassification.filler, [], "Joli bécot", 0, "None"
    ),
    "Cattle Print-Belted Cap": NEOTwewyItemData(
        10202, NEOTwewyItemType.Costume, ItemClassification.filler, [], "Joli bécot", 0, "None"
    ),
    "Denim Jacket": NEOTwewyItemData(
        10203, NEOTwewyItemType.Costume, ItemClassification.filler, [], "Joli bécot", 0, "None"
    ),
    "Grim Cardigan": NEOTwewyItemData(
        10204, NEOTwewyItemType.Costume, ItemClassification.filler, [], "Joli bécot", 0, "None"
    ),
    "Open-Shoulder Top": NEOTwewyItemData(
        10205, NEOTwewyItemType.Costume, ItemClassification.filler, [], "Joli bécot", 0, "None"
    ),
    "Lacy Bustier": NEOTwewyItemData(
        10206, NEOTwewyItemType.Costume, ItemClassification.filler, [], "Joli bécot", 0, "None"
    ),
    "Shredded Jeans": NEOTwewyItemData(
        10207, NEOTwewyItemType.Costume, ItemClassification.filler, [], "Joli bécot", 0, "None"
    ),
    "Marble Jeans": NEOTwewyItemData(
        10208, NEOTwewyItemType.Costume, ItemClassification.filler, [], "Joli bécot", 0, "None"
    ),
    "Leather Miniskirt": NEOTwewyItemData(
        10209, NEOTwewyItemType.Costume, ItemClassification.filler, [], "Joli bécot", 0, "None"
    ),
    "Pink Frilled Skort": NEOTwewyItemData(
        10210, NEOTwewyItemType.Costume, ItemClassification.filler, [], "Joli bécot", 0, "None"
    ),
    "Trendy Two-Piece": NEOTwewyItemData(
        10211, NEOTwewyItemType.Costume, ItemClassification.filler, [], "Joli bécot", 0, "None"
    ),
    "Sparkling Sandals": NEOTwewyItemData(
        10212, NEOTwewyItemType.Costume, ItemClassification.filler, [], "Joli bécot", 0, "None"
    ),
    "Lace-up Knee-High Boots": NEOTwewyItemData(
        10213, NEOTwewyItemType.Costume, ItemClassification.filler, [], "Joli bécot", 0, "None"
    ),
    "Rouge Ruched Boots": NEOTwewyItemData(
        10214, NEOTwewyItemType.Costume, ItemClassification.filler, [], "Joli bécot", 0, "None"
    ),
    "Leather Shoes": NEOTwewyItemData(
        10215, NEOTwewyItemType.Costume, ItemClassification.filler, [], "Joli bécot", 0, "None"
    ),
    "Shimmering Phone Case": NEOTwewyItemData(
        10216, NEOTwewyItemType.Costume, ItemClassification.filler, [], "Joli bécot", 0, "None"
    ),
    "Pink Press-On Nails": NEOTwewyItemData(
        10217, NEOTwewyItemType.Costume, ItemClassification.filler, [], "Joli bécot", 0, "None"
    ),
    "Golden Lighter": NEOTwewyItemData(
        10218, NEOTwewyItemType.Costume, ItemClassification.filler, [], "Joli bécot", 0, "None"
    ),
    "Pink Sunglasses": NEOTwewyItemData(
        10219, NEOTwewyItemType.Costume, ItemClassification.filler, [], "Joli bécot", 0, "None"
    ),
    "Red Mohawk Set": NEOTwewyItemData(
        10300, NEOTwewyItemType.Costume, ItemClassification.filler, [], "Tigre PUNKS", 0, "None"
    ),
    "Studded Tiger Cap": NEOTwewyItemData(
        10301, NEOTwewyItemType.Costume, ItemClassification.filler, [], "Tigre PUNKS", 0, "None"
    ),
    "Studded Leather Cap": NEOTwewyItemData(
        10302, NEOTwewyItemType.Costume, ItemClassification.filler, [], "Tigre PUNKS", 0, "None"
    ),
    "Tiger Mohawk Set": NEOTwewyItemData(
        10303, NEOTwewyItemType.Costume, ItemClassification.filler, [], "Tigre PUNKS", 0, "None"
    ),
    "Biker Jacket": NEOTwewyItemData(
        10304, NEOTwewyItemType.Costume, ItemClassification.filler, [], "Tigre PUNKS", 0, "None"
    ),
    "Patched Biker Jacket": NEOTwewyItemData(
        10305, NEOTwewyItemType.Costume, ItemClassification.filler, [], "Tigre PUNKS", 0, "None"
    ),
    "Red Biker Vest": NEOTwewyItemData(
        10306, NEOTwewyItemType.Costume, ItemClassification.filler, [], "Tigre PUNKS", 0, "None"
    ),
    "Tiger Biker Vest": NEOTwewyItemData(
        10307, NEOTwewyItemType.Costume, ItemClassification.filler, [], "Tigre PUNKS", 0, "None"
    ),
    "Red Plaid Coat": NEOTwewyItemData(
        10308, NEOTwewyItemType.Costume, ItemClassification.filler, [], "Tigre PUNKS", 0, "None"
    ),
    "White Linen Shirt": NEOTwewyItemData(
        10309, NEOTwewyItemType.Costume, ItemClassification.filler, [], "Tigre PUNKS", 0, "None"
    ),
    "Bondage Pants": NEOTwewyItemData(
        10310, NEOTwewyItemType.Costume, ItemClassification.filler, [], "Tigre PUNKS", 0, "None"
    ),
    "Skirted Bondage Pants": NEOTwewyItemData(
        10311, NEOTwewyItemType.Costume, ItemClassification.filler, [], "Tigre PUNKS", 0, "None"
    ),
    "Bondage Shorts": NEOTwewyItemData(
        10312, NEOTwewyItemType.Costume, ItemClassification.filler, [], "Tigre PUNKS", 0, "None"
    ),
    "Plaid Pants": NEOTwewyItemData(
        10313, NEOTwewyItemType.Costume, ItemClassification.filler, [], "Tigre PUNKS", 0, "None"
    ),
    "Studded Boots": NEOTwewyItemData(
        10314, NEOTwewyItemType.Costume, ItemClassification.filler, [], "Tigre PUNKS", 0, "None"
    ),
    "White Creepers": NEOTwewyItemData(
        10315, NEOTwewyItemType.Costume, ItemClassification.filler, [], "Tigre PUNKS", 0, "None"
    ),
    "Tiger Creepers": NEOTwewyItemData(
        10316, NEOTwewyItemType.Costume, ItemClassification.filler, [], "Tigre PUNKS", 0, "None"
    ),
    "Belted Boots": NEOTwewyItemData(
        10317, NEOTwewyItemType.Costume, ItemClassification.filler, [], "Tigre PUNKS", 0, "None"
    ),
    "Spiked Wristband": NEOTwewyItemData(
        10318, NEOTwewyItemType.Costume, ItemClassification.filler, [], "Tigre PUNKS", 0, "None"
    ),
    "Spiked Choker": NEOTwewyItemData(
        10319, NEOTwewyItemType.Costume, ItemClassification.filler, [], "Tigre PUNKS", 0, "None"
    ),
    "Mini Shoulder Bag": NEOTwewyItemData(
        10320, NEOTwewyItemType.Costume, ItemClassification.filler, [], "Tigre PUNKS", 0, "None"
    ),
    "Tiger Backpack": NEOTwewyItemData(
        10321, NEOTwewyItemType.Costume, ItemClassification.filler, [], "Tigre PUNKS", 0, "None"
    ),
    "Peach Blossom": NEOTwewyItemData(
        10400, NEOTwewyItemType.Costume, ItemClassification.filler, [], "Cony×Cony", 0, "None"
    ),
    "Iberis": NEOTwewyItemData(10401, NEOTwewyItemType.Costume, ItemClassification.filler, [], "Cony×Cony", 0, "None"),
    "Scarlet Sage": NEOTwewyItemData(
        10402, NEOTwewyItemType.Costume, ItemClassification.filler, [], "Cony×Cony", 0, "None"
    ),
    "Viola": NEOTwewyItemData(10403, NEOTwewyItemType.Costume, ItemClassification.filler, [], "Cony×Cony", 1, "None"),
    "Black Lily": NEOTwewyItemData(
        10404, NEOTwewyItemType.Costume, ItemClassification.filler, [], "Cony×Cony", 0, "None"
    ),
    "Baby's Breath": NEOTwewyItemData(
        10405, NEOTwewyItemType.Costume, ItemClassification.filler, [], "Cony×Cony", 0, "None"
    ),
    "Calla Lily": NEOTwewyItemData(
        10406, NEOTwewyItemType.Costume, ItemClassification.filler, [], "Cony×Cony", 0, "None"
    ),
    "Black Camellia": NEOTwewyItemData(
        10407, NEOTwewyItemType.Costume, ItemClassification.filler, [], "Cony×Cony", 0, "None"
    ),
    "Petunia": NEOTwewyItemData(10408, NEOTwewyItemType.Costume, ItemClassification.filler, [], "Cony×Cony", 0, "None"),
    "Hollyhock": NEOTwewyItemData(
        10409, NEOTwewyItemType.Costume, ItemClassification.filler, [], "Cony×Cony", 0, "None"
    ),
    "Clover": NEOTwewyItemData(10410, NEOTwewyItemType.Costume, ItemClassification.filler, [], "Cony×Cony", 0, "None"),
    "Hyacinth": NEOTwewyItemData(
        10411, NEOTwewyItemType.Costume, ItemClassification.filler, [], "Cony×Cony", 0, "None"
    ),
    "Buttercup": NEOTwewyItemData(
        10412, NEOTwewyItemType.Costume, ItemClassification.filler, [], "Cony×Cony", 0, "None"
    ),
    "Canna Lily": NEOTwewyItemData(
        10413, NEOTwewyItemType.Costume, ItemClassification.filler, [], "Cony×Cony", 0, "None"
    ),
    "Dahlia": NEOTwewyItemData(10414, NEOTwewyItemType.Costume, ItemClassification.filler, [], "Cony×Cony", 0, "None"),
    "Deadly Nightshade": NEOTwewyItemData(
        10415, NEOTwewyItemType.Costume, ItemClassification.filler, [], "Cony×Cony", 0, "None"
    ),
    "Bougainvillea": NEOTwewyItemData(
        10416, NEOTwewyItemType.Costume, ItemClassification.filler, [], "Cony×Cony", 0, "None"
    ),
    "Anthurium": NEOTwewyItemData(
        10417, NEOTwewyItemType.Costume, ItemClassification.filler, [], "Cony×Cony", 0, "None"
    ),
    "Peony": NEOTwewyItemData(10418, NEOTwewyItemType.Costume, ItemClassification.filler, [], "Cony×Cony", 0, "None"),
    "Blue Rose": NEOTwewyItemData(
        10419, NEOTwewyItemType.Costume, ItemClassification.filler, [], "Cony×Cony", 0, "None"
    ),
    "Baby Rose": NEOTwewyItemData(
        10420, NEOTwewyItemType.Costume, ItemClassification.filler, [], "Cony×Cony", 15, "None"
    ),
    "Black Rose": NEOTwewyItemData(
        10421, NEOTwewyItemType.Costume, ItemClassification.filler, [], "Cony×Cony", 20, "None"
    ),
    "Raven Blossom": NEOTwewyItemData(
        10500, NEOTwewyItemType.Costume, ItemClassification.filler, [], "RyuGu", 0, "None"
    ),
    "Hollyhock Blossom": NEOTwewyItemData(
        10501, NEOTwewyItemType.Costume, ItemClassification.filler, [], "RyuGu", 0, "None"
    ),
    "Cornflower Hemp": NEOTwewyItemData(
        10502, NEOTwewyItemType.Costume, ItemClassification.filler, [], "RyuGu", 0, "None"
    ),
    "Sakura on Straw": NEOTwewyItemData(
        10503, NEOTwewyItemType.Costume, ItemClassification.filler, [], "RyuGu", 0, "None"
    ),
    "Cobalt Bishamon": NEOTwewyItemData(
        10504, NEOTwewyItemType.Costume, ItemClassification.filler, [], "RyuGu", 0, "None"
    ),
    "Black-Scarlet Blossom": NEOTwewyItemData(
        10505, NEOTwewyItemType.Costume, ItemClassification.filler, [], "RyuGu", 0, "None"
    ),
    "Shaded Chrysanthemum": NEOTwewyItemData(
        10506, NEOTwewyItemType.Costume, ItemClassification.filler, [], "RyuGu", 0, "None"
    ),
    "Lapis Chrysanthemum": NEOTwewyItemData(
        10507, NEOTwewyItemType.Costume, ItemClassification.filler, [], "RyuGu", 0, "None"
    ),
    "Golden Sparrow": NEOTwewyItemData(
        10508, NEOTwewyItemType.Costume, ItemClassification.filler, [], "RyuGu", 0, "None"
    ),
    "Flowing Indigo": NEOTwewyItemData(
        10509, NEOTwewyItemType.Costume, ItemClassification.filler, [], "RyuGu", 0, "None"
    ),
    "Flowing Silver": NEOTwewyItemData(
        10510, NEOTwewyItemType.Costume, ItemClassification.filler, [], "RyuGu", 0, "None"
    ),
    "Porcelain Blossom": NEOTwewyItemData(
        10511, NEOTwewyItemType.Costume, ItemClassification.filler, [], "RyuGu", 0, "None"
    ),
    "Violet-Ebony Foxglove": NEOTwewyItemData(
        10512, NEOTwewyItemType.Costume, ItemClassification.filler, [], "RyuGu", 0, "None"
    ),
    "Crimson Sand Blossom": NEOTwewyItemData(
        10513, NEOTwewyItemType.Costume, ItemClassification.filler, [], "RyuGu", 0, "None"
    ),
    "Maiden Blossom": NEOTwewyItemData(
        10514, NEOTwewyItemType.Costume, ItemClassification.filler, [], "RyuGu", 0, "None"
    ),
    "Gilded Bamboo": NEOTwewyItemData(
        10515, NEOTwewyItemType.Costume, ItemClassification.filler, [], "RyuGu", 5, "None"
    ),
    "Flaming Blossom": NEOTwewyItemData(
        10516, NEOTwewyItemType.Costume, ItemClassification.filler, [], "RyuGu", 0, "None"
    ),
    "Oversized Beanie": NEOTwewyItemData(
        10600, NEOTwewyItemType.Costume, ItemClassification.filler, [], "garagara", 1, "None"
    ),
    "Cloth Headband": NEOTwewyItemData(
        10601, NEOTwewyItemType.Costume, ItemClassification.filler, [], "garagara", 0, "None"
    ),
    "Turquoise Headband": NEOTwewyItemData(
        10602, NEOTwewyItemType.Costume, ItemClassification.filler, [], "garagara", 0, "None"
    ),
    "Bohemian T-Shirt": NEOTwewyItemData(
        10603, NEOTwewyItemType.Costume, ItemClassification.filler, [], "garagara", 0, "None"
    ),
    "Bohemian Pullover": NEOTwewyItemData(
        10604, NEOTwewyItemType.Costume, ItemClassification.filler, [], "garagara", 0, "None"
    ),
    "Poncho": NEOTwewyItemData(10605, NEOTwewyItemType.Costume, ItemClassification.filler, [], "garagara", 0, "None"),
    "Cloak": NEOTwewyItemData(10606, NEOTwewyItemType.Costume, ItemClassification.filler, [], "garagara", 0, "None"),
    "Bohemian Pants": NEOTwewyItemData(
        10607, NEOTwewyItemType.Costume, ItemClassification.filler, [], "garagara", 0, "None"
    ),
    "Harem Pants": NEOTwewyItemData(
        10608, NEOTwewyItemType.Costume, ItemClassification.filler, [], "garagara", 0, "None"
    ),
    "Bohemian Skirt": NEOTwewyItemData(
        10609, NEOTwewyItemType.Costume, ItemClassification.filler, [], "garagara", 0, "None"
    ),
    "Hippie Overalls": NEOTwewyItemData(
        10610, NEOTwewyItemType.Costume, ItemClassification.filler, [], "garagara", 0, "None"
    ),
    "Hippie Dress": NEOTwewyItemData(
        10611, NEOTwewyItemType.Costume, ItemClassification.filler, [], "garagara", 0, "None"
    ),
    "Bohemian Dress": NEOTwewyItemData(
        10612, NEOTwewyItemType.Costume, ItemClassification.filler, [], "garagara", 0, "None"
    ),
    "Bohemian Sandals": NEOTwewyItemData(
        10613, NEOTwewyItemType.Costume, ItemClassification.filler, [], "garagara", 0, "None"
    ),
    "Beaded Sandals": NEOTwewyItemData(
        10614, NEOTwewyItemType.Costume, ItemClassification.filler, [], "garagara", 0, "None"
    ),
    "Bohemian Slip-ons": NEOTwewyItemData(
        10615, NEOTwewyItemType.Costume, ItemClassification.filler, [], "garagara", 0, "None"
    ),
    "Moccasin Boots": NEOTwewyItemData(
        10616, NEOTwewyItemType.Costume, ItemClassification.filler, [], "garagara", 0, "None"
    ),
    "Turquoise Necklace": NEOTwewyItemData(
        10617, NEOTwewyItemType.Costume, ItemClassification.filler, [], "garagara", 0, "None"
    ),
    "Turquoise Bracelet": NEOTwewyItemData(
        10618, NEOTwewyItemType.Costume, ItemClassification.filler, [], "garagara", 0, "None"
    ),
    "Hippie Shoulder Bag": NEOTwewyItemData(
        10619, NEOTwewyItemType.Costume, ItemClassification.filler, [], "garagara", 5, "None"
    ),
    "Compagno": NEOTwewyItemData(
        10700, NEOTwewyItemType.Costume, ItemClassification.filler, [], "IL CAVALLO DEL RE", 0, "None"
    ),
    "Galassia": NEOTwewyItemData(
        10701, NEOTwewyItemType.Costume, ItemClassification.filler, [], "IL CAVALLO DEL RE", 3, "None"
    ),
    "Bellezza suprema": NEOTwewyItemData(
        10702, NEOTwewyItemType.Costume, ItemClassification.filler, [], "IL CAVALLO DEL RE", 0, "None"
    ),
    "Onore": NEOTwewyItemData(
        10703, NEOTwewyItemType.Costume, ItemClassification.filler, [], "IL CAVALLO DEL RE", 0, "None"
    ),
    "Tradizione": NEOTwewyItemData(
        10704, NEOTwewyItemType.Costume, ItemClassification.filler, [], "IL CAVALLO DEL RE", 0, "None"
    ),
    "Rispetto": NEOTwewyItemData(
        10705, NEOTwewyItemType.Costume, ItemClassification.filler, [], "IL CAVALLO DEL RE", 0, "None"
    ),
    "Innovazione": NEOTwewyItemData(
        10706, NEOTwewyItemType.Costume, ItemClassification.filler, [], "IL CAVALLO DEL RE", 0, "None"
    ),
    "Inimitabile": NEOTwewyItemData(
        10707, NEOTwewyItemType.Costume, ItemClassification.filler, [], "IL CAVALLO DEL RE", 0, "None"
    ),
    "Notte romantica": NEOTwewyItemData(
        10708, NEOTwewyItemType.Costume, ItemClassification.filler, [], "IL CAVALLO DEL RE", 0, "None"
    ),
    "Futuro": NEOTwewyItemData(
        10709, NEOTwewyItemType.Costume, ItemClassification.filler, [], "IL CAVALLO DEL RE", 0, "None"
    ),
    "Infinito": NEOTwewyItemData(
        10710, NEOTwewyItemType.Costume, ItemClassification.filler, [], "IL CAVALLO DEL RE", 0, "None"
    ),
    "Sentiero": NEOTwewyItemData(
        10711, NEOTwewyItemType.Costume, ItemClassification.filler, [], "IL CAVALLO DEL RE", 5, "None"
    ),
    "Vacanza": NEOTwewyItemData(
        10712, NEOTwewyItemType.Costume, ItemClassification.filler, [], "IL CAVALLO DEL RE", 0, "None"
    ),
    "Denaro e potere": NEOTwewyItemData(
        10713, NEOTwewyItemType.Costume, ItemClassification.filler, [], "IL CAVALLO DEL RE", 0, "None"
    ),
    "Amore e desiderio": NEOTwewyItemData(
        10714, NEOTwewyItemType.Costume, ItemClassification.filler, [], "IL CAVALLO DEL RE", 0, "None"
    ),
    "Pigliatutto": NEOTwewyItemData(
        10715, NEOTwewyItemType.Costume, ItemClassification.filler, [], "IL CAVALLO DEL RE", 0, "None"
    ),
    "Fiore di cristallo": NEOTwewyItemData(
        10716, NEOTwewyItemType.Costume, ItemClassification.filler, [], "IL CAVALLO DEL RE", 5, "None"
    ),
    "Bucket Hat": NEOTwewyItemData(
        10800, NEOTwewyItemType.Costume, ItemClassification.filler, [], "Shepherd House", 0, "None"
    ),
    "Hair Brooch": NEOTwewyItemData(
        10801, NEOTwewyItemType.Costume, ItemClassification.filler, [], "Shepherd House", 0, "None"
    ),
    "Sheepy T-Shirt": NEOTwewyItemData(
        10802, NEOTwewyItemType.Costume, ItemClassification.filler, [], "Shepherd House", 0, "None"
    ),
    "Polo Shirt": NEOTwewyItemData(
        10803, NEOTwewyItemType.Costume, ItemClassification.filler, [], "Shepherd House", 0, "None"
    ),
    "Turtleneck Sweater": NEOTwewyItemData(
        10804, NEOTwewyItemType.Costume, ItemClassification.filler, [], "Shepherd House", 0, "None"
    ),
    "White Shirt": NEOTwewyItemData(
        10805, NEOTwewyItemType.Costume, ItemClassification.filler, [], "Shepherd House", 0, "None"
    ),
    "Down Jacket": NEOTwewyItemData(
        10806, NEOTwewyItemType.Costume, ItemClassification.filler, [], "Shepherd House", 0, "None"
    ),
    "Chinos": NEOTwewyItemData(
        10807, NEOTwewyItemType.Costume, ItemClassification.filler, [], "Shepherd House", 0, "None"
    ),
    "Corduroy Pants": NEOTwewyItemData(
        10808, NEOTwewyItemType.Costume, ItemClassification.filler, [], "Shepherd House", 0, "None"
    ),
    "Knee-Length Skirt": NEOTwewyItemData(
        10809, NEOTwewyItemType.Costume, ItemClassification.filler, [], "Shepherd House", 0, "None"
    ),
    "Wrap Skirt": NEOTwewyItemData(
        10810, NEOTwewyItemType.Costume, ItemClassification.filler, [], "Shepherd House", 0, "None"
    ),
    "Shirt Dress": NEOTwewyItemData(
        10811, NEOTwewyItemType.Costume, ItemClassification.filler, [], "Shepherd House", 0, "None"
    ),
    "Strapped Pumps": NEOTwewyItemData(
        10812, NEOTwewyItemType.Costume, ItemClassification.filler, [], "Shepherd House", 0, "None"
    ),
    "Slip-ons": NEOTwewyItemData(
        10813, NEOTwewyItemType.Costume, ItemClassification.filler, [], "Shepherd House", 0, "None"
    ),
    "Formal Bag": NEOTwewyItemData(
        10814, NEOTwewyItemType.Costume, ItemClassification.filler, [], "Shepherd House", 0, "None"
    ),
    "Wool Scarf": NEOTwewyItemData(
        10815, NEOTwewyItemType.Costume, ItemClassification.filler, [], "Shepherd House", 5, "None"
    ),
    "Waterproof Hat": NEOTwewyItemData(
        10900, NEOTwewyItemType.Costume, ItemClassification.filler, [], "Jupiter of the Monkey", 0, "None"
    ),
    "Peacock Cap": NEOTwewyItemData(
        10901, NEOTwewyItemType.Costume, ItemClassification.filler, [], "Jupiter of the Monkey", 0, "None"
    ),
    "Bodhidharma Tank Top": NEOTwewyItemData(
        10902, NEOTwewyItemType.Costume, ItemClassification.filler, [], "Jupiter of the Monkey", 0, "None"
    ),
    "Varuna T-Shirt": NEOTwewyItemData(
        10903, NEOTwewyItemType.Costume, ItemClassification.filler, [], "Jupiter of the Monkey", 0, "None"
    ),
    "Amitabha Windbreaker": NEOTwewyItemData(
        10904, NEOTwewyItemType.Costume, ItemClassification.filler, [], "Jupiter of the Monkey", 0, "None"
    ),
    "Virupaksa Hoodie": NEOTwewyItemData(
        10905, NEOTwewyItemType.Costume, ItemClassification.filler, [], "Jupiter of the Monkey", 0, "None"
    ),
    "Maitreya Jersey": NEOTwewyItemData(
        10906, NEOTwewyItemType.Costume, ItemClassification.filler, [], "Jupiter of the Monkey", 0, "None"
    ),
    "Vaisravana Jacket": NEOTwewyItemData(
        10907, NEOTwewyItemType.Costume, ItemClassification.filler, [], "Jupiter of the Monkey", 0, "None"
    ),
    "Lightning Shorts": NEOTwewyItemData(
        10908, NEOTwewyItemType.Costume, ItemClassification.filler, [], "Jupiter of the Monkey", 0, "None"
    ),
    "Skanda Sweatpants": NEOTwewyItemData(
        10909, NEOTwewyItemType.Costume, ItemClassification.filler, [], "Jupiter of the Monkey", 0, "None"
    ),
    "Kumbhira Sweatpants": NEOTwewyItemData(
        10910, NEOTwewyItemType.Costume, ItemClassification.filler, [], "Jupiter of the Monkey", 0, "None"
    ),
    "Yama Sweatpants": NEOTwewyItemData(
        10911, NEOTwewyItemType.Costume, ItemClassification.filler, [], "Jupiter of the Monkey", 0, "None"
    ),
    "Om Sneakers": NEOTwewyItemData(
        10912, NEOTwewyItemType.Costume, ItemClassification.filler, [], "Jupiter of the Monkey", 0, "None"
    ),
    "Gekirin Sneakers": NEOTwewyItemData(
        10913, NEOTwewyItemType.Costume, ItemClassification.filler, [], "Jupiter of the Monkey", 0, "None"
    ),
    "Kshana Sneakers": NEOTwewyItemData(
        10914, NEOTwewyItemType.Costume, ItemClassification.filler, [], "Jupiter of the Monkey", 0, "None"
    ),
    "Samsara Sneakers": NEOTwewyItemData(
        10915, NEOTwewyItemType.Costume, ItemClassification.filler, [], "Jupiter of the Monkey", 0, "None"
    ),
    "Karma Shoulder Bag": NEOTwewyItemData(
        10916, NEOTwewyItemType.Costume, ItemClassification.filler, [], "Jupiter of the Monkey", 0, "None"
    ),
    "Naraka Rucksack": NEOTwewyItemData(
        10917, NEOTwewyItemType.Costume, ItemClassification.filler, [], "Jupiter of the Monkey", 0, "None"
    ),
    "Monochrome Cap": NEOTwewyItemData(
        11000, NEOTwewyItemType.Costume, ItemClassification.filler, [], "MONOCROW", 0, "None"
    ),
    "Monochrome Beanie": NEOTwewyItemData(
        11001, NEOTwewyItemType.Costume, ItemClassification.filler, [], "MONOCROW", 0, "None"
    ),
    "Monochrome T-Shirt": NEOTwewyItemData(
        11002, NEOTwewyItemType.Costume, ItemClassification.filler, [], "MONOCROW", 0, "None"
    ),
    "Monochrome Jacket": NEOTwewyItemData(
        11003, NEOTwewyItemType.Costume, ItemClassification.filler, [], "MONOCROW", 0, "None"
    ),
    "Monochrome Hoodie": NEOTwewyItemData(
        11004, NEOTwewyItemType.Costume, ItemClassification.filler, [], "MONOCROW", 0, "None"
    ),
    "Criss Cross Tank Top": NEOTwewyItemData(
        11005, NEOTwewyItemType.Costume, ItemClassification.filler, [], "MONOCROW", 0, "None"
    ),
    "Sarouel Pants": NEOTwewyItemData(
        11006, NEOTwewyItemType.Costume, ItemClassification.filler, [], "MONOCROW", 0, "None"
    ),
    "Monochrome Shorts": NEOTwewyItemData(
        11007, NEOTwewyItemType.Costume, ItemClassification.filler, [], "MONOCROW", 0, "None"
    ),
    "Sporty Miniskirt": NEOTwewyItemData(
        11008, NEOTwewyItemType.Costume, ItemClassification.filler, [], "MONOCROW", 0, "None"
    ),
    "Sporty Dress": NEOTwewyItemData(
        11009, NEOTwewyItemType.Costume, ItemClassification.filler, [], "MONOCROW", 0, "None"
    ),
    "Leather Sneakers": NEOTwewyItemData(
        11010, NEOTwewyItemType.Costume, ItemClassification.filler, [], "MONOCROW", 0, "None"
    ),
    "Sneaker Sandals": NEOTwewyItemData(
        11011, NEOTwewyItemType.Costume, ItemClassification.filler, [], "MONOCROW", 0, "None"
    ),
    "Sneaker Boots": NEOTwewyItemData(
        11012, NEOTwewyItemType.Costume, ItemClassification.filler, [], "MONOCROW", 0, "None"
    ),
    "Monochrome Watch": NEOTwewyItemData(
        11013, NEOTwewyItemType.Costume, ItemClassification.filler, [], "MONOCROW", 0, "None"
    ),
    "Dog Tags": NEOTwewyItemData(11014, NEOTwewyItemType.Costume, ItemClassification.filler, [], "MONOCROW", 0, "None"),
    "Sling Bag": NEOTwewyItemData(
        11015, NEOTwewyItemType.Costume, ItemClassification.filler, [], "MONOCROW", 5, "None"
    ),
    "Mask": NEOTwewyItemData(11016, NEOTwewyItemType.Costume, ItemClassification.filler, [], "MONOCROW", 0, "None"),
    "High-Class Hat": NEOTwewyItemData(
        11100, NEOTwewyItemType.Costume, ItemClassification.filler, [], "NATURAL PUPPY", 3, "None"
    ),
    "Straw Hat": NEOTwewyItemData(
        11101, NEOTwewyItemType.Costume, ItemClassification.filler, [], "NATURAL PUPPY", 0, "None"
    ),
    "Cute Camisole": NEOTwewyItemData(
        11102, NEOTwewyItemType.Costume, ItemClassification.filler, [], "NATURAL PUPPY", 0, "None"
    ),
    "Crossover Cardigan": NEOTwewyItemData(
        11103, NEOTwewyItemType.Costume, ItemClassification.filler, [], "NATURAL PUPPY", 0, "None"
    ),
    "Chesterfield Coat": NEOTwewyItemData(
        11104, NEOTwewyItemType.Costume, ItemClassification.filler, [], "NATURAL PUPPY", 0, "None"
    ),
    "Tailored Jacket": NEOTwewyItemData(
        11105, NEOTwewyItemType.Costume, ItemClassification.filler, [], "NATURAL PUPPY", 0, "None"
    ),
    "Striped T-Shirt": NEOTwewyItemData(
        11106, NEOTwewyItemType.Costume, ItemClassification.filler, [], "NATURAL PUPPY", 0, "None"
    ),
    "Dandy Dress Shirt": NEOTwewyItemData(
        11107, NEOTwewyItemType.Costume, ItemClassification.filler, [], "NATURAL PUPPY", 0, "None"
    ),
    "White Jeans": NEOTwewyItemData(
        11108, NEOTwewyItemType.Costume, ItemClassification.filler, [], "NATURAL PUPPY", 0, "None"
    ),
    "Flared Skirt": NEOTwewyItemData(
        11109, NEOTwewyItemType.Costume, ItemClassification.filler, [], "NATURAL PUPPY", 0, "None"
    ),
    "Black Jeans": NEOTwewyItemData(
        11110, NEOTwewyItemType.Costume, ItemClassification.filler, [], "NATURAL PUPPY", 0, "None"
    ),
    "Comfy Overalls": NEOTwewyItemData(
        11111, NEOTwewyItemType.Costume, ItemClassification.filler, [], "NATURAL PUPPY", 0, "None"
    ),
    "Delightful Dress": NEOTwewyItemData(
        11112, NEOTwewyItemType.Costume, ItemClassification.filler, [], "NATURAL PUPPY", 0, "None"
    ),
    "Angelic Dress": NEOTwewyItemData(
        11113, NEOTwewyItemType.Costume, ItemClassification.filler, [], "NATURAL PUPPY", 0, "None"
    ),
    "Lovely Dress": NEOTwewyItemData(
        11114, NEOTwewyItemType.Costume, ItemClassification.filler, [], "NATURAL PUPPY", 0, "None"
    ),
    "Minimalistic Mules": NEOTwewyItemData(
        11115, NEOTwewyItemType.Costume, ItemClassification.filler, [], "NATURAL PUPPY", 0, "None"
    ),
    "PVC Pumps": NEOTwewyItemData(
        11116, NEOTwewyItemType.Costume, ItemClassification.filler, [], "NATURAL PUPPY", 0, "None"
    ),
    "Chukka Boots": NEOTwewyItemData(
        11117, NEOTwewyItemType.Costume, ItemClassification.filler, [], "NATURAL PUPPY", 0, "None"
    ),
    "Standard Tie": NEOTwewyItemData(
        11118, NEOTwewyItemType.Costume, ItemClassification.filler, [], "NATURAL PUPPY", 0, "None"
    ),
    "Knit Tie": NEOTwewyItemData(
        11119, NEOTwewyItemType.Costume, ItemClassification.filler, [], "NATURAL PUPPY", 0, "None"
    ),
    "Flat-Brim Snapback": NEOTwewyItemData(
        11200, NEOTwewyItemType.Costume, ItemClassification.filler, [], "HOG FANG", 0, "None"
    ),
    "Baseball Cap": NEOTwewyItemData(
        11201, NEOTwewyItemType.Costume, ItemClassification.filler, [], "HOG FANG", 0, "None"
    ),
    "Faux-Vintage Beanie": NEOTwewyItemData(
        11202, NEOTwewyItemType.Costume, ItemClassification.filler, [], "HOG FANG", 5, "None"
    ),
    "Wired Hairband": NEOTwewyItemData(
        11203, NEOTwewyItemType.Costume, ItemClassification.filler, [], "HOG FANG", 0, "None"
    ),
    "Down Vest": NEOTwewyItemData(
        11204, NEOTwewyItemType.Costume, ItemClassification.filler, [], "HOG FANG", 0, "None"
    ),
    "Pullover Hoodie": NEOTwewyItemData(
        11205, NEOTwewyItemType.Costume, ItemClassification.filler, [], "HOG FANG", 0, "None"
    ),
    "Printed T-Shirt": NEOTwewyItemData(
        11206, NEOTwewyItemType.Costume, ItemClassification.filler, [], "HOG FANG", 0, "None"
    ),
    "Flannel Shirt": NEOTwewyItemData(
        11207, NEOTwewyItemType.Costume, ItemClassification.filler, [], "HOG FANG", 0, "None"
    ),
    "M-1951 Field Jacket": NEOTwewyItemData(
        11208, NEOTwewyItemType.Costume, ItemClassification.filler, [], "HOG FANG", 0, "None"
    ),
    "Faux-Vintage Jacket": NEOTwewyItemData(
        11209, NEOTwewyItemType.Costume, ItemClassification.filler, [], "HOG FANG", 0, "None"
    ),
    "Cuffed Jeans": NEOTwewyItemData(
        11210, NEOTwewyItemType.Costume, ItemClassification.filler, [], "HOG FANG", 0, "None"
    ),
    "Vintage Ripped Jeans": NEOTwewyItemData(
        11211, NEOTwewyItemType.Costume, ItemClassification.filler, [], "HOG FANG", 0, "None"
    ),
    "Camo Cargo Pants": NEOTwewyItemData(
        11212, NEOTwewyItemType.Costume, ItemClassification.filler, [], "HOG FANG", 0, "None"
    ),
    "Tight Denim Skirt": NEOTwewyItemData(
        11213, NEOTwewyItemType.Costume, ItemClassification.filler, [], "HOG FANG", 0, "None"
    ),
    "Denim Shirt Dress": NEOTwewyItemData(
        11214, NEOTwewyItemType.Costume, ItemClassification.filler, [], "HOG FANG", 0, "None"
    ),
    "Work Boots": NEOTwewyItemData(
        11215, NEOTwewyItemType.Costume, ItemClassification.filler, [], "HOG FANG", 0, "None"
    ),
    "High-top Sneakers": NEOTwewyItemData(
        11216, NEOTwewyItemType.Costume, ItemClassification.filler, [], "HOG FANG", 0, "None"
    ),
    "Low-top Sneakers": NEOTwewyItemData(
        11217, NEOTwewyItemType.Costume, ItemClassification.filler, [], "HOG FANG", 0, "None"
    ),
    "Patched-up Sneakers": NEOTwewyItemData(
        11218, NEOTwewyItemType.Costume, ItemClassification.filler, [], "HOG FANG", 0, "None"
    ),
    "Chain Necklace": NEOTwewyItemData(
        11219, NEOTwewyItemType.Costume, ItemClassification.filler, [], "HOG FANG", 0, "None"
    ),
    "Wallet Chain": NEOTwewyItemData(
        11220, NEOTwewyItemType.Costume, ItemClassification.filler, [], "HOG FANG", 0, "None"
    ),
    "Sunglasses": NEOTwewyItemData(
        11221, NEOTwewyItemType.Costume, ItemClassification.filler, [], "HOG FANG", 0, "None"
    ),
    "Retroesque Boom Box": NEOTwewyItemData(
        11222, NEOTwewyItemType.Costume, ItemClassification.filler, [], "HOG FANG", 0, "None"
    ),
    "Denim Cap": NEOTwewyItemData(
        11300, NEOTwewyItemType.Costume, ItemClassification.filler, [], "Gatto Nero", 0, "None"
    ),
    "Beret": NEOTwewyItemData(11301, NEOTwewyItemType.Costume, ItemClassification.filler, [], "Gatto Nero", 0, "None"),
    "Buckle Sleeve Shirt": NEOTwewyItemData(
        11302, NEOTwewyItemType.Costume, ItemClassification.filler, [], "Gatto Nero", 0, "None"
    ),
    "Zippered Shirt": NEOTwewyItemData(
        11303, NEOTwewyItemType.Costume, ItemClassification.filler, [], "Gatto Nero", 0, "None"
    ),
    "Off-the-Shoulder Top": NEOTwewyItemData(
        11304, NEOTwewyItemType.Costume, ItemClassification.filler, [], "Gatto Nero", 0, "None"
    ),
    "Shirt Jacket": NEOTwewyItemData(
        11305, NEOTwewyItemType.Costume, ItemClassification.filler, [], "Gatto Nero", 0, "None"
    ),
    "Denim Micro-Miniskirt": NEOTwewyItemData(
        11306, NEOTwewyItemType.Costume, ItemClassification.filler, [], "Gatto Nero", 0, "None"
    ),
    "Asymmetrical Miniskirt": NEOTwewyItemData(
        11307, NEOTwewyItemType.Costume, ItemClassification.filler, [], "Gatto Nero", 0, "None"
    ),
    "Frayed Cargo Pants": NEOTwewyItemData(
        11308, NEOTwewyItemType.Costume, ItemClassification.filler, [], "Gatto Nero", 0, "None"
    ),
    "Asymmetrical Jeans": NEOTwewyItemData(
        11309, NEOTwewyItemType.Costume, ItemClassification.filler, [], "Gatto Nero", 0, "None"
    ),
    "Bell-Sleeved Two-Piece": NEOTwewyItemData(
        11310, NEOTwewyItemType.Costume, ItemClassification.filler, [], "Gatto Nero", 0, "None"
    ),
    "Jumpsuit": NEOTwewyItemData(
        11311, NEOTwewyItemType.Costume, ItemClassification.filler, [], "Gatto Nero", 0, "None"
    ),
    "Ankle Boots": NEOTwewyItemData(
        11312, NEOTwewyItemType.Costume, ItemClassification.filler, [], "Gatto Nero", 0, "None"
    ),
    "Mid-Calf Boots": NEOTwewyItemData(
        11313, NEOTwewyItemType.Costume, ItemClassification.filler, [], "Gatto Nero", 0, "None"
    ),
    "Fishnet Socks": NEOTwewyItemData(
        11314, NEOTwewyItemType.Costume, ItemClassification.filler, [], "Gatto Nero", 0, "None"
    ),
    "Hip Pack": NEOTwewyItemData(
        11315, NEOTwewyItemType.Costume, ItemClassification.filler, [], "Gatto Nero", 0, "None"
    ),
    "Mr. Mew Hoodie": NEOTwewyItemData(
        11316, NEOTwewyItemType.Costume, ItemClassification.filler, [], "Gatto Nero", 0, "None"
    ),
    "Mr. Mew Phone Case": NEOTwewyItemData(
        11317, NEOTwewyItemType.Costume, ItemClassification.filler, [], "Gatto Nero", 0, "None"
    ),
    "Mr. Mew Pouch": NEOTwewyItemData(
        11318, NEOTwewyItemType.Costume, ItemClassification.filler, [], "Gatto Nero", 0, "None"
    ),
    "Rainbow Afro Wig": NEOTwewyItemData(
        11400, NEOTwewyItemType.Costume, ItemClassification.filler, [], "croaky panic", 0, "None"
    ),
    "Samurai Wig": NEOTwewyItemData(
        11401, NEOTwewyItemType.Costume, ItemClassification.filler, [], "croaky panic", 0, "None"
    ),
    "Bunny Maid Hairband": NEOTwewyItemData(
        11402, NEOTwewyItemType.Costume, ItemClassification.filler, [], "croaky panic", 0, "None"
    ),
    "Space Kitty T-Shirt": NEOTwewyItemData(
        11403, NEOTwewyItemType.Costume, ItemClassification.filler, [], "croaky panic", 0, "None"
    ),
    "Christmassy Coat": NEOTwewyItemData(
        11404, NEOTwewyItemType.Costume, ItemClassification.filler, [], "croaky panic", 0, "None"
    ),
    "Ribbit Rubber Ring": NEOTwewyItemData(
        11405, NEOTwewyItemType.Costume, ItemClassification.filler, [], "croaky panic", 0, "None"
    ),
    "Christmassy Pants": NEOTwewyItemData(
        11406, NEOTwewyItemType.Costume, ItemClassification.filler, [], "croaky panic", 0, "None"
    ),
    "Maid Costume": NEOTwewyItemData(
        11407, NEOTwewyItemType.Costume, ItemClassification.filler, [], "croaky panic", 0, "None"
    ),
    "Ninja Costume": NEOTwewyItemData(
        11408, NEOTwewyItemType.Costume, ItemClassification.filler, [], "croaky panic", 0, "None"
    ),
    "Stilts": NEOTwewyItemData(
        11409, NEOTwewyItemType.Costume, ItemClassification.filler, [], "croaky panic", 0, "None"
    ),
    "Roller Skates": NEOTwewyItemData(
        11410, NEOTwewyItemType.Costume, ItemClassification.filler, [], "croaky panic", 0, "None"
    ),
    "Half-Hearted Summer Gift": NEOTwewyItemData(
        11411, NEOTwewyItemType.Costume, ItemClassification.filler, [], "croaky panic", 5, "None"
    ),
    "Schnoz Spectacles": NEOTwewyItemData(
        11412, NEOTwewyItemType.Costume, ItemClassification.filler, [], "croaky panic", 0, "None"
    ),
    "Tomonami's Blade": NEOTwewyItemData(
        11413, NEOTwewyItemType.Costume, ItemClassification.filler, [], "croaky panic", 0, "None"
    ),
    "B.H.C.C Panama Hat": NEOTwewyItemData(
        11500, NEOTwewyItemType.Costume, ItemClassification.filler, [], "BLACK HONEY CHILI COOKIE", 0, "None"
    ),
    "B.H.C.C Baseball Cap": NEOTwewyItemData(
        11501, NEOTwewyItemType.Costume, ItemClassification.filler, [], "BLACK HONEY CHILI COOKIE", 0, "None"
    ),
    "B.H.C.C T-Shirt": NEOTwewyItemData(
        11502, NEOTwewyItemType.Costume, ItemClassification.filler, [], "BLACK HONEY CHILI COOKIE", 0, "None"
    ),
    "B.H.C.C Biker Jacket": NEOTwewyItemData(
        11503, NEOTwewyItemType.Costume, ItemClassification.filler, [], "BLACK HONEY CHILI COOKIE", 0, "None"
    ),
    "B.H.C.C Leather Pants": NEOTwewyItemData(
        11504, NEOTwewyItemType.Costume, ItemClassification.filler, [], "BLACK HONEY CHILI COOKIE", 0, "None"
    ),
    "B.H.C.C Shorts": NEOTwewyItemData(
        11505, NEOTwewyItemType.Costume, ItemClassification.filler, [], "BLACK HONEY CHILI COOKIE", 0, "None"
    ),
    "B.H.C.C Shoes": NEOTwewyItemData(
        11506, NEOTwewyItemType.Costume, ItemClassification.filler, [], "BLACK HONEY CHILI COOKIE", 0, "None"
    ),
    "B.H.C.C Side Gore Boots": NEOTwewyItemData(
        11507, NEOTwewyItemType.Costume, ItemClassification.filler, [], "BLACK HONEY CHILI COOKIE", 0, "None"
    ),
    "B.H.C.C Tote Bag": NEOTwewyItemData(
        11508, NEOTwewyItemType.Costume, ItemClassification.filler, [], "BLACK HONEY CHILI COOKIE", 0, "None"
    ),
    "FP": NEOTwewyItemData(
        30000,
        NEOTwewyItemType.Valuable,
        ItemClassification.skip_balancing,
        [NEOTwewyItemGroup.FP_ITEM],
        "Unbranded",
        0,
        "None",
    ),
    "Secret Report No. 1": NEOTwewyItemData(
        31000,
        NEOTwewyItemType.Book,
        ItemClassification.progression,
        [NEOTwewyItemGroup.SECRET_REPORT],
        "Unbranded",
        0,
        "None",
    ),
    "Secret Report No. 2": NEOTwewyItemData(
        31001,
        NEOTwewyItemType.Book,
        ItemClassification.progression,
        [NEOTwewyItemGroup.SECRET_REPORT],
        "Unbranded",
        0,
        "None",
    ),
    "Secret Report No. 3": NEOTwewyItemData(
        31002,
        NEOTwewyItemType.Book,
        ItemClassification.progression,
        [NEOTwewyItemGroup.SECRET_REPORT],
        "Unbranded",
        0,
        "None",
    ),
    "Secret Report No. 4": NEOTwewyItemData(
        31003,
        NEOTwewyItemType.Book,
        ItemClassification.progression,
        [NEOTwewyItemGroup.SECRET_REPORT],
        "Unbranded",
        0,
        "None",
    ),
    "Secret Report No. 5": NEOTwewyItemData(
        31004,
        NEOTwewyItemType.Book,
        ItemClassification.progression,
        [NEOTwewyItemGroup.SECRET_REPORT],
        "Unbranded",
        0,
        "None",
    ),
    "Secret Report No. 6": NEOTwewyItemData(
        31005,
        NEOTwewyItemType.Book,
        ItemClassification.progression,
        [NEOTwewyItemGroup.SECRET_REPORT],
        "Unbranded",
        0,
        "None",
    ),
    "Secret Report No. 7": NEOTwewyItemData(
        31006,
        NEOTwewyItemType.Book,
        ItemClassification.progression,
        [NEOTwewyItemGroup.SECRET_REPORT],
        "Unbranded",
        0,
        "None",
    ),
    "Secret Report No. 8": NEOTwewyItemData(
        31007,
        NEOTwewyItemType.Book,
        ItemClassification.progression,
        [NEOTwewyItemGroup.SECRET_REPORT],
        "Unbranded",
        0,
        "None",
    ),
    "Secret Report No. 9": NEOTwewyItemData(
        31008,
        NEOTwewyItemType.Book,
        ItemClassification.progression,
        [NEOTwewyItemGroup.SECRET_REPORT],
        "Unbranded",
        0,
        "None",
    ),
    "Secret Report No. 10": NEOTwewyItemData(
        31009,
        NEOTwewyItemType.Book,
        ItemClassification.progression,
        [NEOTwewyItemGroup.SECRET_REPORT],
        "Unbranded",
        0,
        "None",
    ),
    "Secret Report No. 11": NEOTwewyItemData(
        31010,
        NEOTwewyItemType.Book,
        ItemClassification.progression,
        [NEOTwewyItemGroup.SECRET_REPORT],
        "Unbranded",
        0,
        "None",
    ),
    "Secret Report No. 12": NEOTwewyItemData(
        31011,
        NEOTwewyItemType.Book,
        ItemClassification.progression,
        [NEOTwewyItemGroup.SECRET_REPORT],
        "Unbranded",
        0,
        "None",
    ),
    "Secret Report No. 13": NEOTwewyItemData(
        31012,
        NEOTwewyItemType.Book,
        ItemClassification.progression,
        [NEOTwewyItemGroup.SECRET_REPORT],
        "Unbranded",
        0,
        "None",
    ),
    "Secret Report No. 14": NEOTwewyItemData(
        31013,
        NEOTwewyItemType.Book,
        ItemClassification.progression,
        [NEOTwewyItemGroup.SECRET_REPORT],
        "Unbranded",
        0,
        "None",
    ),
    "Secret Report No. 15": NEOTwewyItemData(
        31014,
        NEOTwewyItemType.Book,
        ItemClassification.progression,
        [NEOTwewyItemGroup.SECRET_REPORT],
        "Unbranded",
        0,
        "None",
    ),
    "Secret Report No. 16": NEOTwewyItemData(
        31015,
        NEOTwewyItemType.Book,
        ItemClassification.progression,
        [NEOTwewyItemGroup.SECRET_REPORT],
        "Unbranded",
        0,
        "None",
    ),
    "Secret Report No. 17": NEOTwewyItemData(
        31016,
        NEOTwewyItemType.Book,
        ItemClassification.progression,
        [NEOTwewyItemGroup.SECRET_REPORT],
        "Unbranded",
        0,
        "None",
    ),
    "Secret Report No. 18": NEOTwewyItemData(
        31017,
        NEOTwewyItemType.Book,
        ItemClassification.progression,
        [NEOTwewyItemGroup.SECRET_REPORT],
        "Unbranded",
        0,
        "None",
    ),
    "Secret Report No. 19": NEOTwewyItemData(
        31018,
        NEOTwewyItemType.Book,
        ItemClassification.progression,
        [NEOTwewyItemGroup.SECRET_REPORT],
        "Unbranded",
        0,
        "None",
    ),
    "Secret Report No. 20": NEOTwewyItemData(
        31019,
        NEOTwewyItemType.Book,
        ItemClassification.progression,
        [NEOTwewyItemGroup.SECRET_REPORT],
        "Unbranded",
        0,
        "None",
    ),
    "Secret Report No. 21": NEOTwewyItemData(
        31020,
        NEOTwewyItemType.Book,
        ItemClassification.progression,
        [NEOTwewyItemGroup.SECRET_REPORT],
        "Unbranded",
        0,
        "None",
    ),
    "Secret Report No. 22": NEOTwewyItemData(
        31021,
        NEOTwewyItemType.Book,
        ItemClassification.progression,
        [NEOTwewyItemGroup.SECRET_REPORT],
        "Unbranded",
        0,
        "None",
    ),
    "Secret Report No. 23": NEOTwewyItemData(
        31022,
        NEOTwewyItemType.Book,
        ItemClassification.progression,
        [NEOTwewyItemGroup.SECRET_REPORT],
        "Unbranded",
        0,
        "None",
    ),
    "Secret Report No. 24": NEOTwewyItemData(
        31023,
        NEOTwewyItemType.Book,
        ItemClassification.progression,
        [NEOTwewyItemGroup.SECRET_REPORT],
        "Unbranded",
        0,
        "None",
    ),
    "Tips & Tricks Vol. 1": NEOTwewyItemData(
        31100, NEOTwewyItemType.Book, ItemClassification.filler, [], "Unbranded", 0, "None"
    ),
    "Tips & Tricks Vol. 2": NEOTwewyItemData(
        31101, NEOTwewyItemType.Book, ItemClassification.filler, [], "Unbranded", 0, "None"
    ),
    "Tips & Tricks Vol. 3": NEOTwewyItemData(
        31102, NEOTwewyItemType.Book, ItemClassification.filler, [], "Unbranded", 0, "None"
    ),
    "Tips & Tricks Vol. 4": NEOTwewyItemData(
        31103, NEOTwewyItemType.Book, ItemClassification.filler, [], "Unbranded", 0, "None"
    ),
    "Tips & Tricks Vol. 5": NEOTwewyItemData(
        31104, NEOTwewyItemType.Book, ItemClassification.filler, [], "Unbranded", 0, "None"
    ),
    "Tips & Tricks Vol. 6": NEOTwewyItemData(
        31105, NEOTwewyItemType.Book, ItemClassification.filler, [], "Unbranded", 0, "None"
    ),
    "Tips & Tricks Vol. 7": NEOTwewyItemData(
        31106, NEOTwewyItemType.Book, ItemClassification.filler, [], "Unbranded", 0, "None"
    ),
    "Tips & Tricks Vol. 8": NEOTwewyItemData(
        31107, NEOTwewyItemType.Book, ItemClassification.filler, [], "Unbranded", 0, "None"
    ),
    "Tips & Tricks Vol. 9": NEOTwewyItemData(
        31108, NEOTwewyItemType.Book, ItemClassification.filler, [], "Unbranded", 0, "None"
    ),
    "Tips & Tricks Vol. 10": NEOTwewyItemData(
        31109, NEOTwewyItemType.Book, ItemClassification.filler, [], "Unbranded", 0, "None"
    ),
    "Tips & Tricks Vol. 11": NEOTwewyItemData(
        31110, NEOTwewyItemType.Book, ItemClassification.filler, [], "Unbranded", 0, "None"
    ),
    "Tips & Tricks Vol. 12": NEOTwewyItemData(
        31111, NEOTwewyItemType.Book, ItemClassification.filler, [], "Unbranded", 0, "None"
    ),
    "Tips & Tricks Vol. 13": NEOTwewyItemData(
        31112, NEOTwewyItemType.Book, ItemClassification.filler, [], "Unbranded", 0, "None"
    ),
    "Tips & Tricks Vol. 14": NEOTwewyItemData(
        31113, NEOTwewyItemType.Book, ItemClassification.filler, [], "Unbranded", 0, "None"
    ),
    "Tips & Tricks Vol. 15": NEOTwewyItemData(
        31114, NEOTwewyItemType.Book, ItemClassification.filler, [], "Unbranded", 0, "None"
    ),
    "Tips & Tricks Vol. 16": NEOTwewyItemData(
        31115, NEOTwewyItemType.Book, ItemClassification.filler, [], "Unbranded", 0, "None"
    ),
    "Tips & Tricks Vol. 17": NEOTwewyItemData(
        31116, NEOTwewyItemType.Book, ItemClassification.filler, [], "Unbranded", 0, "None"
    ),
    "Tips & Tricks Vol. 18": NEOTwewyItemData(
        31117, NEOTwewyItemType.Book, ItemClassification.filler, [], "Unbranded", 0, "None"
    ),
    "Tips & Tricks Vol. 19": NEOTwewyItemData(
        31118, NEOTwewyItemType.Book, ItemClassification.filler, [], "Unbranded", 0, "None"
    ),
    "Tips & Tricks Vol. 20": NEOTwewyItemData(
        31119, NEOTwewyItemType.Book, ItemClassification.filler, [], "Unbranded", 0, "None"
    ),
    "Tips & Tricks Vol. 21": NEOTwewyItemData(
        31120, NEOTwewyItemType.Book, ItemClassification.filler, [], "Unbranded", 0, "None"
    ),
    "Tips & Tricks Vol. 22": NEOTwewyItemData(
        31121, NEOTwewyItemType.Book, ItemClassification.filler, [], "Unbranded", 0, "None"
    ),
    "Tips & Tricks Vol. 23": NEOTwewyItemData(
        31122, NEOTwewyItemType.Book, ItemClassification.filler, [], "Unbranded", 0, "None"
    ),
    "Tips & Tricks Vol. 24": NEOTwewyItemData(
        31123, NEOTwewyItemType.Book, ItemClassification.filler, [], "Unbranded", 0, "None"
    ),
    "Tips & Tricks Vol. 25": NEOTwewyItemData(
        31124, NEOTwewyItemType.Book, ItemClassification.filler, [], "Unbranded", 0, "None"
    ),
    "Tips & Tricks Vol. 26": NEOTwewyItemData(
        31125, NEOTwewyItemType.Book, ItemClassification.filler, [], "Unbranded", 0, "None"
    ),
    "Tips & Tricks Vol. 27": NEOTwewyItemData(
        31126, NEOTwewyItemType.Book, ItemClassification.filler, [], "Unbranded", 0, "None"
    ),
    "Tips & Tricks Vol. 28": NEOTwewyItemData(
        31127, NEOTwewyItemType.Book, ItemClassification.filler, [], "Unbranded", 0, "None"
    ),
    "Tips & Tricks Vol. 29": NEOTwewyItemData(
        31128, NEOTwewyItemType.Book, ItemClassification.filler, [], "Unbranded", 0, "None"
    ),
    "Tips & Tricks Vol. 30": NEOTwewyItemData(
        31129, NEOTwewyItemType.Book, ItemClassification.filler, [], "Unbranded", 0, "None"
    ),
    "Tips & Tricks Vol. 31": NEOTwewyItemData(
        31130, NEOTwewyItemType.Book, ItemClassification.filler, [], "Unbranded", 0, "None"
    ),
    "Tips & Tricks Vol. 32": NEOTwewyItemData(
        31131, NEOTwewyItemType.Book, ItemClassification.filler, [], "Unbranded", 0, "None"
    ),
    "Tips & Tricks Vol. 33": NEOTwewyItemData(
        31132, NEOTwewyItemType.Book, ItemClassification.filler, [], "Unbranded", 0, "None"
    ),
    "Tips & Tricks Vol. 34": NEOTwewyItemData(
        31133, NEOTwewyItemType.Book, ItemClassification.filler, [], "Unbranded", 0, "None"
    ),
    "Tips & Tricks Vol. 35": NEOTwewyItemData(
        31134, NEOTwewyItemType.Book, ItemClassification.filler, [], "Unbranded", 0, "None"
    ),
    "Tips & Tricks Vol. 36": NEOTwewyItemData(
        31135, NEOTwewyItemType.Book, ItemClassification.filler, [], "Unbranded", 0, "None"
    ),
    "Tips & Tricks Vol. 37": NEOTwewyItemData(
        31136, NEOTwewyItemType.Book, ItemClassification.filler, [], "Unbranded", 0, "None"
    ),
    "Tips & Tricks Vol. 38": NEOTwewyItemData(
        31137, NEOTwewyItemType.Book, ItemClassification.filler, [], "Unbranded", 0, "None"
    ),
    "Tips & Tricks Vol. 39": NEOTwewyItemData(
        31138, NEOTwewyItemType.Book, ItemClassification.filler, [], "Unbranded", 0, "None"
    ),
    "Tips & Tricks Vol. 40": NEOTwewyItemData(
        31139, NEOTwewyItemType.Book, ItemClassification.filler, [], "Unbranded", 0, "None"
    ),
    "Fighting as a Team": NEOTwewyItemData(
        31200, NEOTwewyItemType.Book, ItemClassification.filler, [], "Unbranded", 0, "None"
    ),
    "Combos": NEOTwewyItemData(31201, NEOTwewyItemType.Book, ItemClassification.filler, [], "Unbranded", 0, "None"),
    "Dodging": NEOTwewyItemData(31202, NEOTwewyItemType.Book, ItemClassification.filler, [], "Unbranded", 0, "None"),
    "Noise Counterattacks": NEOTwewyItemData(
        31203, NEOTwewyItemType.Book, ItemClassification.filler, [], "Unbranded", 0, "None"
    ),
    "Elemental Affinities": NEOTwewyItemData(
        31204, NEOTwewyItemType.Book, ItemClassification.filler, [], "Unbranded", 0, "None"
    ),
    "Status Ailments": NEOTwewyItemData(
        31205, NEOTwewyItemType.Book, ItemClassification.filler, [], "Unbranded", 0, "None"
    ),
    "Experience Points": NEOTwewyItemData(
        31206, NEOTwewyItemType.Book, ItemClassification.filler, [], "Unbranded", 0, "None"
    ),
    "Killing It in Combat": NEOTwewyItemData(
        31207, NEOTwewyItemType.Book, ItemClassification.filler, [], "Unbranded", 0, "None"
    ),
    "Powered-Up Mashups": NEOTwewyItemData(
        31208, NEOTwewyItemType.Book, ItemClassification.filler, [], "Unbranded", 0, "None"
    ),
    "Killer Remixes": NEOTwewyItemData(
        31209, NEOTwewyItemType.Book, ItemClassification.filler, [], "Unbranded", 0, "None"
    ),
    "Picking Up Pins": NEOTwewyItemData(
        31211, NEOTwewyItemType.Book, ItemClassification.filler, [], "Unbranded", 0, "None"
    ),
    "Evolving Pins": NEOTwewyItemData(
        31212, NEOTwewyItemType.Book, ItemClassification.filler, [], "Unbranded", 0, "None"
    ),
    "Pin Ensembles": NEOTwewyItemData(
        31213, NEOTwewyItemType.Book, ItemClassification.filler, [], "Unbranded", 0, "None"
    ),
    "Uber Pins": NEOTwewyItemData(31214, NEOTwewyItemType.Book, ItemClassification.filler, [], "Unbranded", 0, "None"),
    "Collecting Pins": NEOTwewyItemData(
        31215, NEOTwewyItemType.Book, ItemClassification.filler, [], "Unbranded", 0, "None"
    ),
    "Pin Decks": NEOTwewyItemData(31216, NEOTwewyItemType.Book, ItemClassification.filler, [], "Unbranded", 0, "None"),
    "Scanning": NEOTwewyItemData(31217, NEOTwewyItemType.Book, ItemClassification.filler, [], "Unbranded", 0, "None"),
    "Noise Symbols": NEOTwewyItemData(
        31218, NEOTwewyItemType.Book, ItemClassification.filler, [], "Unbranded", 0, "None"
    ),
    "Chaining Battles": NEOTwewyItemData(
        31219, NEOTwewyItemType.Book, ItemClassification.filler, [], "Unbranded", 0, "None"
    ),
    "Red Noise Symbols": NEOTwewyItemData(
        31220, NEOTwewyItemType.Book, ItemClassification.filler, [], "Unbranded", 0, "None"
    ),
    "Blue Noise Symbols": NEOTwewyItemData(
        31221, NEOTwewyItemType.Book, ItemClassification.filler, [], "Unbranded", 0, "None"
    ),
    "Pink Noise Symbols": NEOTwewyItemData(
        31222, NEOTwewyItemType.Book, ItemClassification.filler, [], "Unbranded", 0, "None"
    ),
    "Fighting Pig Noise": NEOTwewyItemData(
        31223, NEOTwewyItemType.Book, ItemClassification.filler, [], "Unbranded", 0, "None"
    ),
    "Pale Noise Symbols": NEOTwewyItemData(
        31224, NEOTwewyItemType.Book, ItemClassification.filler, [], "Unbranded", 0, "None"
    ),
    "Orange Noise Symbols": NEOTwewyItemData(
        31225, NEOTwewyItemType.Book, ItemClassification.filler, [], "Unbranded", 0, "None"
    ),
    "Farming FP": NEOTwewyItemData(31226, NEOTwewyItemType.Book, ItemClassification.filler, [], "Unbranded", 0, "None"),
    "Emotion Noise: Enraged": NEOTwewyItemData(
        31227, NEOTwewyItemType.Book, ItemClassification.filler, [], "Unbranded", 0, "None"
    ),
    "Emotion Noise: Somber": NEOTwewyItemData(
        31228, NEOTwewyItemType.Book, ItemClassification.filler, [], "Unbranded", 0, "None"
    ),
    "Emotion Noise: Serene": NEOTwewyItemData(
        31229, NEOTwewyItemType.Book, ItemClassification.filler, [], "Unbranded", 0, "None"
    ),
    "Emotion Noise: Fearful": NEOTwewyItemData(
        31230, NEOTwewyItemType.Book, ItemClassification.filler, [], "Unbranded", 0, "None"
    ),
    "ShibuPay": NEOTwewyItemData(31231, NEOTwewyItemType.Book, ItemClassification.filler, [], "Unbranded", 0, "None"),
    "Abilities": NEOTwewyItemData(31232, NEOTwewyItemType.Book, ItemClassification.filler, [], "Unbranded", 0, "None"),
    "Style": NEOTwewyItemData(31233, NEOTwewyItemType.Book, ItemClassification.filler, [], "Unbranded", 0, "None"),
    "Shop Quests": NEOTwewyItemData(
        31234, NEOTwewyItemType.Book, ItemClassification.filler, [], "Unbranded", 0, "None"
    ),
    "Becoming a Regular": NEOTwewyItemData(
        31235, NEOTwewyItemType.Book, ItemClassification.filler, [], "Unbranded", 0, "None"
    ),
    "Dining Out": NEOTwewyItemData(31236, NEOTwewyItemType.Book, ItemClassification.filler, [], "Unbranded", 0, "None"),
    "Favorite Foods": NEOTwewyItemData(
        31237, NEOTwewyItemType.Book, ItemClassification.filler, [], "Unbranded", 0, "None"
    ),
    "Udagawa Graffiti Wall": NEOTwewyItemData(
        31238, NEOTwewyItemType.Book, ItemClassification.filler, [], "Unbranded", 0, "None"
    ),
    "Scramble Slams": NEOTwewyItemData(
        31239, NEOTwewyItemType.Book, ItemClassification.filler, [], "Unbranded", 0, "None"
    ),
    "Mental Notes": NEOTwewyItemData(
        31240, NEOTwewyItemType.Book, ItemClassification.filler, [], "Unbranded", 0, "None"
    ),
    "Social Network Skills": NEOTwewyItemData(
        31241, NEOTwewyItemType.Book, ItemClassification.filler, [], "Unbranded", 0, "None"
    ),
    "Side Quests": NEOTwewyItemData(
        31242, NEOTwewyItemType.Book, ItemClassification.filler, [], "Unbranded", 0, "None"
    ),
    "Chapter Select": NEOTwewyItemData(
        31243, NEOTwewyItemType.Book, ItemClassification.filler, [], "Unbranded", 0, "None"
    ),
    "(CD) Track 1": NEOTwewyItemData(
        32000, NEOTwewyItemType.Music, ItemClassification.filler, [], "Unbranded", 0, "None"
    ),
    "(CD) Track 11": NEOTwewyItemData(
        32001, NEOTwewyItemType.Music, ItemClassification.filler, [], "Unbranded", 0, "None"
    ),
    "(CD) Track 5": NEOTwewyItemData(
        32002, NEOTwewyItemType.Music, ItemClassification.filler, [], "Unbranded", 0, "None"
    ),
    "(CD) Track 8": NEOTwewyItemData(
        32003, NEOTwewyItemType.Music, ItemClassification.filler, [], "Unbranded", 0, "None"
    ),
    "(CD) Track 12": NEOTwewyItemData(
        32004, NEOTwewyItemType.Music, ItemClassification.filler, [], "Unbranded", 0, "None"
    ),
    "(CD) Track 9": NEOTwewyItemData(
        32005, NEOTwewyItemType.Music, ItemClassification.filler, [], "Unbranded", 0, "None"
    ),
    "(CD) Track 15": NEOTwewyItemData(
        32006, NEOTwewyItemType.Music, ItemClassification.filler, [], "Unbranded", 0, "None"
    ),
    "(CD) Track 6": NEOTwewyItemData(
        32007, NEOTwewyItemType.Music, ItemClassification.filler, [], "Unbranded", 0, "None"
    ),
    "(CD) Track 18": NEOTwewyItemData(
        32008, NEOTwewyItemType.Music, ItemClassification.filler, [], "Unbranded", 0, "None"
    ),
    "(CD) Track 10": NEOTwewyItemData(
        32009, NEOTwewyItemType.Music, ItemClassification.filler, [], "Unbranded", 0, "None"
    ),
    "(CD) Track 19": NEOTwewyItemData(
        32010, NEOTwewyItemType.Music, ItemClassification.filler, [], "Unbranded", 0, "None"
    ),
    "(CD) Track 16": NEOTwewyItemData(
        32011, NEOTwewyItemType.Music, ItemClassification.filler, [], "Unbranded", 0, "None"
    ),
    "(CD) Track 14": NEOTwewyItemData(
        32012, NEOTwewyItemType.Music, ItemClassification.filler, [], "Unbranded", 0, "None"
    ),
    "(CD) Track 17": NEOTwewyItemData(
        32013, NEOTwewyItemType.Music, ItemClassification.filler, [], "Unbranded", 0, "None"
    ),
    "(CD) Track 4": NEOTwewyItemData(
        32014, NEOTwewyItemType.Music, ItemClassification.filler, [], "Unbranded", 0, "None"
    ),
    "(CD) Track 3": NEOTwewyItemData(
        32015, NEOTwewyItemType.Music, ItemClassification.filler, [], "Unbranded", 0, "None"
    ),
    "(CD) Track 13": NEOTwewyItemData(
        32016, NEOTwewyItemType.Music, ItemClassification.filler, [], "Unbranded", 0, "None"
    ),
    "(CD) Track 7": NEOTwewyItemData(
        32017, NEOTwewyItemType.Music, ItemClassification.filler, [], "Unbranded", 0, "None"
    ),
    "(CD) Track 21": NEOTwewyItemData(
        32018, NEOTwewyItemType.Music, ItemClassification.filler, [], "Unbranded", 0, "None"
    ),
    "(CD) Track 20": NEOTwewyItemData(
        32019, NEOTwewyItemType.Music, ItemClassification.filler, [], "Unbranded", 0, "None"
    ),
    "(CD) Track 29": NEOTwewyItemData(
        32020, NEOTwewyItemType.Music, ItemClassification.filler, [], "Unbranded", 0, "None"
    ),
    "(CD) Track 2": NEOTwewyItemData(
        32021, NEOTwewyItemType.Music, ItemClassification.filler, [], "Unbranded", 0, "None"
    ),
    "(CD) Track 30": NEOTwewyItemData(
        32022, NEOTwewyItemType.Music, ItemClassification.filler, [], "Unbranded", 0, "None"
    ),
    "(CD) Track 22": NEOTwewyItemData(
        32023, NEOTwewyItemType.Music, ItemClassification.filler, [], "Unbranded", 0, "None"
    ),
    "(CD) Track 23": NEOTwewyItemData(
        32024, NEOTwewyItemType.Music, ItemClassification.filler, [], "Unbranded", 0, "None"
    ),
    "(CD) Track 24": NEOTwewyItemData(
        32025, NEOTwewyItemType.Music, ItemClassification.filler, [], "Unbranded", 0, "None"
    ),
    "(CD) Track 25": NEOTwewyItemData(
        32026, NEOTwewyItemType.Music, ItemClassification.filler, [], "Unbranded", 0, "None"
    ),
    "(CD) Track 26": NEOTwewyItemData(
        32027, NEOTwewyItemType.Music, ItemClassification.filler, [], "Unbranded", 0, "None"
    ),
    "(CD) Track 27": NEOTwewyItemData(
        32028, NEOTwewyItemType.Music, ItemClassification.filler, [], "Unbranded", 0, "None"
    ),
    "(CD) Track 28": NEOTwewyItemData(
        32029, NEOTwewyItemType.Music, ItemClassification.filler, [], "Unbranded", 0, "None"
    ),
    "(CD) Track 48": NEOTwewyItemData(
        32030, NEOTwewyItemType.Music, ItemClassification.filler, [], "Unbranded", 0, "None"
    ),
    "(CD) Track 44": NEOTwewyItemData(
        32031, NEOTwewyItemType.Music, ItemClassification.filler, [], "Unbranded", 0, "None"
    ),
    "(CD) Track 38": NEOTwewyItemData(
        32032, NEOTwewyItemType.Music, ItemClassification.filler, [], "Unbranded", 0, "None"
    ),
    "(CD) Track 47": NEOTwewyItemData(
        32033, NEOTwewyItemType.Music, ItemClassification.filler, [], "Unbranded", 0, "None"
    ),
    "(CD) Track 43": NEOTwewyItemData(
        32034, NEOTwewyItemType.Music, ItemClassification.filler, [], "Unbranded", 0, "None"
    ),
    "(CD) Track 36": NEOTwewyItemData(
        32035, NEOTwewyItemType.Music, ItemClassification.filler, [], "Unbranded", 0, "None"
    ),
    "(CD) Track 45": NEOTwewyItemData(
        32036, NEOTwewyItemType.Music, ItemClassification.filler, [], "Unbranded", 0, "None"
    ),
    "(CD) Track 34": NEOTwewyItemData(
        32037, NEOTwewyItemType.Music, ItemClassification.filler, [], "Unbranded", 0, "None"
    ),
    "(CD) Track 40": NEOTwewyItemData(
        32038, NEOTwewyItemType.Music, ItemClassification.filler, [], "Unbranded", 0, "None"
    ),
    "(CD) Track 46": NEOTwewyItemData(
        32039, NEOTwewyItemType.Music, ItemClassification.filler, [], "Unbranded", 0, "None"
    ),
    "(CD) Track 41": NEOTwewyItemData(
        32040, NEOTwewyItemType.Music, ItemClassification.filler, [], "Unbranded", 0, "None"
    ),
    "(CD) Track 49": NEOTwewyItemData(
        32041, NEOTwewyItemType.Music, ItemClassification.filler, [], "Unbranded", 0, "None"
    ),
    "(CD) Track 37": NEOTwewyItemData(
        32042, NEOTwewyItemType.Music, ItemClassification.filler, [], "Unbranded", 0, "None"
    ),
    "(CD) Track 39": NEOTwewyItemData(
        32043, NEOTwewyItemType.Music, ItemClassification.filler, [], "Unbranded", 0, "None"
    ),
    "(CD) Track 33": NEOTwewyItemData(
        32044, NEOTwewyItemType.Music, ItemClassification.filler, [], "Unbranded", 0, "None"
    ),
    "(CD) Track 32": NEOTwewyItemData(
        32045, NEOTwewyItemType.Music, ItemClassification.filler, [], "Unbranded", 0, "None"
    ),
    "(CD) Track 50": NEOTwewyItemData(
        32046, NEOTwewyItemType.Music, ItemClassification.filler, [], "Unbranded", 0, "None"
    ),
    "(CD) Track 35": NEOTwewyItemData(
        32047, NEOTwewyItemType.Music, ItemClassification.filler, [], "Unbranded", 0, "None"
    ),
    "(CD) Track 42": NEOTwewyItemData(
        32048, NEOTwewyItemType.Music, ItemClassification.filler, [], "Unbranded", 0, "None"
    ),
    "(CD) Track 51": NEOTwewyItemData(
        32049, NEOTwewyItemType.Music, ItemClassification.filler, [], "Unbranded", 0, "None"
    ),
    "(CD) Track 31": NEOTwewyItemData(
        32050, NEOTwewyItemType.Music, ItemClassification.filler, [], "Unbranded", 0, "None"
    ),
    "5 FP": NEOTwewyItemData(
        33001,
        NEOTwewyItemType.Valuable,
        ItemClassification.skip_balancing,
        [NEOTwewyItemGroup.FP_ITEM],
        "Unbranded",
        0,
        "None",
    ),
    "3x Rare Metal": NEOTwewyItemData(
        33002, NEOTwewyItemType.Badge, ItemClassification.filler, [NEOTwewyItemGroup.RARE_METAL], "Unbranded", 0, "None"
    ),
    "3x Tektite": NEOTwewyItemData(
        33003, NEOTwewyItemType.Badge, ItemClassification.filler, [NEOTwewyItemGroup.RARE_METAL], "Unbranded", 0, "None"
    ),
    "2 FP": NEOTwewyItemData(
        33004,
        NEOTwewyItemType.Valuable,
        ItemClassification.skip_balancing,
        [NEOTwewyItemGroup.FP_ITEM],
        "Unbranded",
        0,
        "None",
    ),
}

# List of all threads of the "Joli becot" brand
JOLI_BECOT_THREADS = [
    itemName
    for itemName, itemData in ITEM_DATA.items()
    if itemData.brand == "Joli bécot" and itemData.item_type == NEOTwewyItemType.Costume
]

# List of all threads that have drop rate increasing abilities
DROP_INCREASING_THREADS = [itemName for itemName, itemData in ITEM_DATA.items() if itemData.drop_increase > 0]


# Dict of all items to their id
ITEM_NAME_TO_ID = {item_name: item_data.id for item_name, item_data in ITEM_DATA.items()}

# Dict of all items to their default classification
DEFAULT_ITEM_CLASSIFICATIONS = {item_name: item_data.item_classification for item_name, item_data in ITEM_DATA.items()}

# Dict of all item groups and the items in that group
ITEM_GROUPS: dict[str, list[str]] = {group.value: [] for group in NEOTwewyItemGroup}

for item_name, item_data in ITEM_DATA.items():
    for group in item_data.item_groups:
        ITEM_GROUPS[group.value].append(item_name)
    # Element Affinity Groups
    if item_data.element in ITEM_GROUPS.keys():
        ITEM_GROUPS[item_data.element].append(item_name)
    else:
        ITEM_GROUPS[item_data.element] = []

# Dict of all items and which groups they belong to
ITEM_TO_GROUPS: dict[str, list[str]] = {}

for group, items in ITEM_GROUPS.items():
    for item in items:
        ITEM_TO_GROUPS.setdefault(item, []).append(group)