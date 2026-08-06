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
    brand: str


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
    # HEADGEAR = "Headgear"
    # TOPS = "Tops"
    # BOTTOMS = "Bottoms"
    # FOOTWEAR = "Footwear"
    # TWO_PIECE = "Two-Piece"
    # ACCESSORY = "Accessory"


ITEM_DATA: dict[str, NEOTwewyItemData] = {
    "Shockwave": NEOTwewyItemData(
        1000, NEOTwewyItemType.Badge, ItemClassification.filler, [NEOTwewyItemGroup.COMBAT_PIN], "Unbranded"
    ),
    "Azamaru": NEOTwewyItemData(
        1001, NEOTwewyItemType.Badge, ItemClassification.filler, [NEOTwewyItemGroup.COMBAT_PIN], "Jupiter of the Monkey"
    ),
    "Shishio": NEOTwewyItemData(
        1002, NEOTwewyItemType.Badge, ItemClassification.filler, [NEOTwewyItemGroup.COMBAT_PIN], "Jupiter of the Monkey"
    ),
    "Midaregami": NEOTwewyItemData(
        1003, NEOTwewyItemType.Badge, ItemClassification.filler, [NEOTwewyItemGroup.COMBAT_PIN], "Jupiter of the Monkey"
    ),
    "Namikuguri": NEOTwewyItemData(
        1004, NEOTwewyItemType.Badge, ItemClassification.filler, [NEOTwewyItemGroup.COMBAT_PIN], "Jupiter of the Monkey"
    ),
    "Fuchin": NEOTwewyItemData(
        1005, NEOTwewyItemType.Badge, ItemClassification.filler, [NEOTwewyItemGroup.COMBAT_PIN], "Jupiter of the Monkey"
    ),
    "Kurorushi": NEOTwewyItemData(
        1006, NEOTwewyItemType.Badge, ItemClassification.filler, [NEOTwewyItemGroup.COMBAT_PIN], "Jupiter of the Monkey"
    ),
    "Honebami": NEOTwewyItemData(
        1007, NEOTwewyItemType.Badge, ItemClassification.filler, [NEOTwewyItemGroup.COMBAT_PIN], "Jupiter of the Monkey"
    ),
    "Grizzly": NEOTwewyItemData(
        1008, NEOTwewyItemType.Badge, ItemClassification.filler, [NEOTwewyItemGroup.COMBAT_PIN], "Unbranded"
    ),
    "Onimaru": NEOTwewyItemData(
        1009, NEOTwewyItemType.Badge, ItemClassification.filler, [NEOTwewyItemGroup.COMBAT_PIN], "Jupiter of the Monkey"
    ),
    "Kitsunegasaki": NEOTwewyItemData(
        1010, NEOTwewyItemType.Badge, ItemClassification.filler, [NEOTwewyItemGroup.COMBAT_PIN], "Jupiter of the Monkey"
    ),
    "Yukimitsu": NEOTwewyItemData(
        1011, NEOTwewyItemType.Badge, ItemClassification.filler, [NEOTwewyItemGroup.COMBAT_PIN], "Jupiter of the Monkey"
    ),
    "Sayosamonji": NEOTwewyItemData(
        1012, NEOTwewyItemType.Badge, ItemClassification.filler, [NEOTwewyItemGroup.COMBAT_PIN], "Jupiter of the Monkey"
    ),
    "Aizen": NEOTwewyItemData(
        1013, NEOTwewyItemType.Badge, ItemClassification.filler, [NEOTwewyItemGroup.COMBAT_PIN], "Jupiter of the Monkey"
    ),
    "Spin Twinz": NEOTwewyItemData(
        1014, NEOTwewyItemType.Badge, ItemClassification.filler, [NEOTwewyItemGroup.COMBAT_PIN], "croaky panic"
    ),
    "Tsurumaru": NEOTwewyItemData(
        1015, NEOTwewyItemType.Badge, ItemClassification.filler, [NEOTwewyItemGroup.COMBAT_PIN], "Jupiter of the Monkey"
    ),
    "Reigetsu": NEOTwewyItemData(
        1016, NEOTwewyItemType.Badge, ItemClassification.filler, [NEOTwewyItemGroup.COMBAT_PIN], "Jupiter of the Monkey"
    ),
    "Jupiter of the Monkey II": NEOTwewyItemData(
        1017, NEOTwewyItemType.Badge, ItemClassification.filler, [NEOTwewyItemGroup.COMBAT_PIN], "Jupiter of the Monkey"
    ),
    "Hotaru": NEOTwewyItemData(
        1018, NEOTwewyItemType.Badge, ItemClassification.filler, [NEOTwewyItemGroup.COMBAT_PIN], "Jupiter of the Monkey"
    ),
    "Grin Reaper": NEOTwewyItemData(
        1019, NEOTwewyItemType.Badge, ItemClassification.filler, [NEOTwewyItemGroup.COMBAT_PIN], "Tigre PUNKS"
    ),
    "Grunge Punch": NEOTwewyItemData(
        1020, NEOTwewyItemType.Badge, ItemClassification.filler, [NEOTwewyItemGroup.COMBAT_PIN], "Tigre PUNKS"
    ),
    "Jungle King": NEOTwewyItemData(
        1021, NEOTwewyItemType.Badge, ItemClassification.filler, [NEOTwewyItemGroup.COMBAT_PIN], "Tigre PUNKS"
    ),
    "Primal Roar": NEOTwewyItemData(
        1022, NEOTwewyItemType.Badge, ItemClassification.filler, [NEOTwewyItemGroup.COMBAT_PIN], "Tigre PUNKS"
    ),
    "Mosh 'n' Mash": NEOTwewyItemData(
        1023, NEOTwewyItemType.Badge, ItemClassification.filler, [NEOTwewyItemGroup.COMBAT_PIN], "Tigre PUNKS"
    ),
    "Fangs of Ice": NEOTwewyItemData(
        1024, NEOTwewyItemType.Badge, ItemClassification.filler, [NEOTwewyItemGroup.COMBAT_PIN], "Tigre PUNKS"
    ),
    "Slashcicle": NEOTwewyItemData(
        1025, NEOTwewyItemType.Badge, ItemClassification.filler, [NEOTwewyItemGroup.COMBAT_PIN], "Tigre PUNKS"
    ),
    "Right Claw": NEOTwewyItemData(
        1026, NEOTwewyItemType.Badge, ItemClassification.filler, [NEOTwewyItemGroup.COMBAT_PIN], "Tigre PUNKS"
    ),
    "Wicked Howl": NEOTwewyItemData(
        1027, NEOTwewyItemType.Badge, ItemClassification.filler, [NEOTwewyItemGroup.COMBAT_PIN], "Tigre PUNKS"
    ),
    "Tigres Assemble!": NEOTwewyItemData(
        1028, NEOTwewyItemType.Badge, ItemClassification.filler, [NEOTwewyItemGroup.COMBAT_PIN], "Tigre PUNKS"
    ),
    "Rock 'n' Rock": NEOTwewyItemData(
        1029, NEOTwewyItemType.Badge, ItemClassification.filler, [NEOTwewyItemGroup.COMBAT_PIN], "Tigre PUNKS"
    ),
    "Crusher Rush": NEOTwewyItemData(
        1030, NEOTwewyItemType.Badge, ItemClassification.filler, [NEOTwewyItemGroup.COMBAT_PIN], "Tigre PUNKS"
    ),
    "Beringei": NEOTwewyItemData(
        1031, NEOTwewyItemType.Badge, ItemClassification.filler, [NEOTwewyItemGroup.COMBAT_PIN], "Unbranded"
    ),
    "Just Up Ahead": NEOTwewyItemData(
        1032, NEOTwewyItemType.Badge, ItemClassification.filler, [NEOTwewyItemGroup.COMBAT_PIN], "MONOCROW"
    ),
    "Honor and Sacrifice": NEOTwewyItemData(
        1033, NEOTwewyItemType.Badge, ItemClassification.filler, [NEOTwewyItemGroup.COMBAT_PIN], "MONOCROW"
    ),
    "All or Nothing": NEOTwewyItemData(
        1034, NEOTwewyItemType.Badge, ItemClassification.filler, [NEOTwewyItemGroup.COMBAT_PIN], "MONOCROW"
    ),
    "One Day Closer": NEOTwewyItemData(
        1035, NEOTwewyItemType.Badge, ItemClassification.filler, [NEOTwewyItemGroup.COMBAT_PIN], "MONOCROW"
    ),
    "Time Is Relative": NEOTwewyItemData(
        1036, NEOTwewyItemType.Badge, ItemClassification.filler, [NEOTwewyItemGroup.COMBAT_PIN], "MONOCROW"
    ),
    "Got Your Back": NEOTwewyItemData(
        1037, NEOTwewyItemType.Badge, ItemClassification.filler, [NEOTwewyItemGroup.COMBAT_PIN], "MONOCROW"
    ),
    "Take a Chance": NEOTwewyItemData(
        1038, NEOTwewyItemType.Badge, ItemClassification.filler, [NEOTwewyItemGroup.COMBAT_PIN], "MONOCROW"
    ),
    "No Turning Back": NEOTwewyItemData(
        1039, NEOTwewyItemType.Badge, ItemClassification.filler, [NEOTwewyItemGroup.COMBAT_PIN], "MONOCROW"
    ),
    "Trial Without Error": NEOTwewyItemData(
        1040, NEOTwewyItemType.Badge, ItemClassification.filler, [NEOTwewyItemGroup.COMBAT_PIN], "MONOCROW"
    ),
    "Stinger": NEOTwewyItemData(
        1041, NEOTwewyItemType.Badge, ItemClassification.filler, [NEOTwewyItemGroup.COMBAT_PIN], "Unbranded"
    ),
    "No Plan Required": NEOTwewyItemData(
        1042, NEOTwewyItemType.Badge, ItemClassification.filler, [NEOTwewyItemGroup.COMBAT_PIN], "MONOCROW"
    ),
    "Don't Be Shocked": NEOTwewyItemData(
        1043, NEOTwewyItemType.Badge, ItemClassification.filler, [NEOTwewyItemGroup.COMBAT_PIN], "MONOCROW"
    ),
    "Cut Me Down": NEOTwewyItemData(
        1044, NEOTwewyItemType.Badge, ItemClassification.filler, [NEOTwewyItemGroup.COMBAT_PIN], "MONOCROW"
    ),
    "Quench Your Thirst": NEOTwewyItemData(
        1045, NEOTwewyItemType.Badge, ItemClassification.filler, [NEOTwewyItemGroup.COMBAT_PIN], "MONOCROW"
    ),
    "Try It Again": NEOTwewyItemData(
        1046, NEOTwewyItemType.Badge, ItemClassification.filler, [NEOTwewyItemGroup.COMBAT_PIN], "MONOCROW"
    ),
    "Force Rounds": NEOTwewyItemData(
        1047, NEOTwewyItemType.Badge, ItemClassification.filler, [NEOTwewyItemGroup.COMBAT_PIN], "Unbranded"
    ),
    "Sugar Beam": NEOTwewyItemData(
        1048, NEOTwewyItemType.Badge, ItemClassification.filler, [NEOTwewyItemGroup.COMBAT_PIN], "NATURAL PUPPY"
    ),
    "Nighty-Night Beam": NEOTwewyItemData(
        1049, NEOTwewyItemType.Badge, ItemClassification.filler, [NEOTwewyItemGroup.COMBAT_PIN], "NATURAL PUPPY"
    ),
    "Glitter Beam": NEOTwewyItemData(
        1050, NEOTwewyItemType.Badge, ItemClassification.filler, [NEOTwewyItemGroup.COMBAT_PIN], "NATURAL PUPPY"
    ),
    "Zip-Zap Beam": NEOTwewyItemData(
        1051, NEOTwewyItemType.Badge, ItemClassification.filler, [NEOTwewyItemGroup.COMBAT_PIN], "NATURAL PUPPY"
    ),
    "Stylish Beam": NEOTwewyItemData(
        1052, NEOTwewyItemType.Badge, ItemClassification.filler, [NEOTwewyItemGroup.COMBAT_PIN], "NATURAL PUPPY"
    ),
    "Lovebird Magnum": NEOTwewyItemData(
        1053, NEOTwewyItemType.Badge, ItemClassification.filler, [NEOTwewyItemGroup.COMBAT_PIN], "NATURAL PUPPY"
    ),
    "Garbage Gatling": NEOTwewyItemData(
        1054, NEOTwewyItemType.Badge, ItemClassification.filler, [NEOTwewyItemGroup.COMBAT_PIN], "NATURAL PUPPY"
    ),
    "Top Dog Gatling": NEOTwewyItemData(
        1055, NEOTwewyItemType.Badge, ItemClassification.filler, [NEOTwewyItemGroup.COMBAT_PIN], "NATURAL PUPPY"
    ),
    "Icky Beam": NEOTwewyItemData(
        1056, NEOTwewyItemType.Badge, ItemClassification.filler, [NEOTwewyItemGroup.COMBAT_PIN], "NATURAL PUPPY"
    ),
    "Frog": NEOTwewyItemData(
        1057, NEOTwewyItemType.Badge, ItemClassification.filler, [NEOTwewyItemGroup.COMBAT_PIN], "Unbranded"
    ),
    "Freestyle Launcher": NEOTwewyItemData(
        1058, NEOTwewyItemType.Badge, ItemClassification.filler, [NEOTwewyItemGroup.COMBAT_PIN], "NATURAL PUPPY"
    ),
    "Lovely Launcher": NEOTwewyItemData(
        1059, NEOTwewyItemType.Badge, ItemClassification.filler, [NEOTwewyItemGroup.COMBAT_PIN], "NATURAL PUPPY"
    ),
    "Cupid Launcher": NEOTwewyItemData(
        1060, NEOTwewyItemType.Badge, ItemClassification.filler, [NEOTwewyItemGroup.COMBAT_PIN], "NATURAL PUPPY"
    ),
    "Cuddly Launcher": NEOTwewyItemData(
        1061, NEOTwewyItemType.Badge, ItemClassification.filler, [NEOTwewyItemGroup.COMBAT_PIN], "NATURAL PUPPY"
    ),
    "Heartthrob Launcher": NEOTwewyItemData(
        1062, NEOTwewyItemType.Badge, ItemClassification.filler, [NEOTwewyItemGroup.COMBAT_PIN], "NATURAL PUPPY"
    ),
    "Hobblin' Hippo": NEOTwewyItemData(
        1063, NEOTwewyItemType.Badge, ItemClassification.filler, [NEOTwewyItemGroup.COMBAT_PIN], "croaky panic"
    ),
    "croaky panic": NEOTwewyItemData(
        1064, NEOTwewyItemType.Badge, ItemClassification.filler, [NEOTwewyItemGroup.COMBAT_PIN], "croaky panic"
    ),
    "MONOCROW": NEOTwewyItemData(
        1065, NEOTwewyItemType.Badge, ItemClassification.filler, [NEOTwewyItemGroup.COMBAT_PIN], "MONOCROW"
    ),
    "The Idol Within": NEOTwewyItemData(
        1066, NEOTwewyItemType.Badge, ItemClassification.filler, [NEOTwewyItemGroup.COMBAT_PIN], "MONOCROW"
    ),
    "Be My Last": NEOTwewyItemData(
        1067, NEOTwewyItemType.Badge, ItemClassification.filler, [NEOTwewyItemGroup.COMBAT_PIN], "MONOCROW"
    ),
    "All Burned Out": NEOTwewyItemData(
        1068, NEOTwewyItemType.Badge, ItemClassification.filler, [NEOTwewyItemGroup.COMBAT_PIN], "MONOCROW"
    ),
    "Aspect of Truth": NEOTwewyItemData(
        1069, NEOTwewyItemType.Badge, ItemClassification.filler, [NEOTwewyItemGroup.COMBAT_PIN], "MONOCROW"
    ),
    "Live Your Truth": NEOTwewyItemData(
        1070, NEOTwewyItemType.Badge, ItemClassification.filler, [NEOTwewyItemGroup.COMBAT_PIN], "MONOCROW"
    ),
    "Grus": NEOTwewyItemData(
        1071, NEOTwewyItemType.Badge, ItemClassification.filler, [NEOTwewyItemGroup.COMBAT_PIN], "Unbranded"
    ),
    "Rapturous Rabbits": NEOTwewyItemData(
        1072, NEOTwewyItemType.Badge, ItemClassification.filler, [NEOTwewyItemGroup.COMBAT_PIN], "Cony×Cony"
    ),
    "Classical Cacophany": NEOTwewyItemData(
        1073, NEOTwewyItemType.Badge, ItemClassification.filler, [NEOTwewyItemGroup.COMBAT_PIN], "Cony×Cony"
    ),
    "Magical Metamorphosis": NEOTwewyItemData(
        1074, NEOTwewyItemType.Badge, ItemClassification.filler, [NEOTwewyItemGroup.COMBAT_PIN], "Cony×Cony"
    ),
    "Blizzard Bunny": NEOTwewyItemData(
        1075, NEOTwewyItemType.Badge, ItemClassification.filler, [NEOTwewyItemGroup.COMBAT_PIN], "Cony×Cony"
    ),
    "Frosty Friendship": NEOTwewyItemData(
        1076, NEOTwewyItemType.Badge, ItemClassification.filler, [NEOTwewyItemGroup.COMBAT_PIN], "Cony×Cony"
    ),
    "Stellar Self-Portrait": NEOTwewyItemData(
        1077, NEOTwewyItemType.Badge, ItemClassification.filler, [NEOTwewyItemGroup.COMBAT_PIN], "Cony×Cony"
    ),
    "Gorgeous Gemstone": NEOTwewyItemData(
        1078, NEOTwewyItemType.Badge, ItemClassification.filler, [NEOTwewyItemGroup.COMBAT_PIN], "Cony×Cony"
    ),
    "Black Hole Bunny": NEOTwewyItemData(
        1079, NEOTwewyItemType.Badge, ItemClassification.filler, [NEOTwewyItemGroup.COMBAT_PIN], "Cony×Cony"
    ),
    "The Great Magma Escape": NEOTwewyItemData(
        1080, NEOTwewyItemType.Badge, ItemClassification.filler, [NEOTwewyItemGroup.COMBAT_PIN], "Shepherd House"
    ),
    "The Great Balloon Voyage": NEOTwewyItemData(
        1081, NEOTwewyItemType.Badge, ItemClassification.filler, [NEOTwewyItemGroup.COMBAT_PIN], "Shepherd House"
    ),
    "The Fluffy Ovine Cloud": NEOTwewyItemData(
        1082, NEOTwewyItemType.Badge, ItemClassification.filler, [NEOTwewyItemGroup.COMBAT_PIN], "Shepherd House"
    ),
    "The Lonely Space Warrior": NEOTwewyItemData(
        1083, NEOTwewyItemType.Badge, ItemClassification.filler, [NEOTwewyItemGroup.COMBAT_PIN], "Shepherd House"
    ),
    "The Great Lunar View": NEOTwewyItemData(
        1084, NEOTwewyItemType.Badge, ItemClassification.filler, [NEOTwewyItemGroup.COMBAT_PIN], "Shepherd House"
    ),
    "The Pyramids' Old Secret": NEOTwewyItemData(
        1085, NEOTwewyItemType.Badge, ItemClassification.filler, [NEOTwewyItemGroup.COMBAT_PIN], "Shepherd House"
    ),
    "The Ever-Moving Machine": NEOTwewyItemData(
        1086, NEOTwewyItemType.Badge, ItemClassification.filler, [NEOTwewyItemGroup.COMBAT_PIN], "Shepherd House"
    ),
    "Puffer": NEOTwewyItemData(
        1087, NEOTwewyItemType.Badge, ItemClassification.filler, [NEOTwewyItemGroup.COMBAT_PIN], "Unbranded"
    ),
    "Out of Your Mine": NEOTwewyItemData(
        1088, NEOTwewyItemType.Badge, ItemClassification.filler, [NEOTwewyItemGroup.COMBAT_PIN], "garagara"
    ),
    "Be of Two Mines": NEOTwewyItemData(
        1089, NEOTwewyItemType.Badge, ItemClassification.filler, [NEOTwewyItemGroup.COMBAT_PIN], "garagara"
    ),
    "Boom in the Night": NEOTwewyItemData(
        1090, NEOTwewyItemType.Badge, ItemClassification.filler, [NEOTwewyItemGroup.COMBAT_PIN], "garagara"
    ),
    "Chain Is Gonna Come": NEOTwewyItemData(
        1091, NEOTwewyItemType.Badge, ItemClassification.filler, [NEOTwewyItemGroup.COMBAT_PIN], "garagara"
    ),
    "Back on the Chain Bang": NEOTwewyItemData(
        1092, NEOTwewyItemType.Badge, ItemClassification.filler, [NEOTwewyItemGroup.COMBAT_PIN], "garagara"
    ),
    "Bad to the Bomb": NEOTwewyItemData(
        1093, NEOTwewyItemType.Badge, ItemClassification.filler, [NEOTwewyItemGroup.COMBAT_PIN], "garagara"
    ),
    "Snake in the Blast": NEOTwewyItemData(
        1094, NEOTwewyItemType.Badge, ItemClassification.filler, [NEOTwewyItemGroup.COMBAT_PIN], "garagara"
    ),
    "Bee in Your Bomb-et": NEOTwewyItemData(
        1095, NEOTwewyItemType.Badge, ItemClassification.filler, [NEOTwewyItemGroup.COMBAT_PIN], "garagara"
    ),
    "I Scream, U Scream!": NEOTwewyItemData(
        1096, NEOTwewyItemType.Badge, ItemClassification.filler, [NEOTwewyItemGroup.COMBAT_PIN], "croaky panic"
    ),
    "Bloom 4 U": NEOTwewyItemData(
        1097, NEOTwewyItemType.Badge, ItemClassification.filler, [NEOTwewyItemGroup.COMBAT_PIN], "croaky panic"
    ),
    "Takanosu": NEOTwewyItemData(
        1098, NEOTwewyItemType.Badge, ItemClassification.filler, [NEOTwewyItemGroup.COMBAT_PIN], "Jupiter of the Monkey"
    ),
    "Kumokiri": NEOTwewyItemData(
        1099, NEOTwewyItemType.Badge, ItemClassification.filler, [NEOTwewyItemGroup.COMBAT_PIN], "Jupiter of the Monkey"
    ),
    "Taikokane": NEOTwewyItemData(
        1100, NEOTwewyItemType.Badge, ItemClassification.filler, [NEOTwewyItemGroup.COMBAT_PIN], "Jupiter of the Monkey"
    ),
    "Kasen Kanesada": NEOTwewyItemData(
        1101, NEOTwewyItemType.Badge, ItemClassification.filler, [NEOTwewyItemGroup.COMBAT_PIN], "Jupiter of the Monkey"
    ),
    "Iwatoshi": NEOTwewyItemData(
        1102, NEOTwewyItemType.Badge, ItemClassification.filler, [NEOTwewyItemGroup.COMBAT_PIN], "Jupiter of the Monkey"
    ),
    "Omokage": NEOTwewyItemData(
        1103, NEOTwewyItemType.Badge, ItemClassification.filler, [NEOTwewyItemGroup.COMBAT_PIN], "Jupiter of the Monkey"
    ),
    "Wolf": NEOTwewyItemData(
        1104, NEOTwewyItemType.Badge, ItemClassification.filler, [NEOTwewyItemGroup.COMBAT_PIN], "Unbranded"
    ),
    "Thunder and Lightning": NEOTwewyItemData(
        1105, NEOTwewyItemType.Badge, ItemClassification.filler, [NEOTwewyItemGroup.COMBAT_PIN], "IL CAVALLO DEL RE"
    ),
    "Iris": NEOTwewyItemData(
        1106, NEOTwewyItemType.Badge, ItemClassification.filler, [NEOTwewyItemGroup.COMBAT_PIN], "Unbranded"
    ),
    "Caught in the Undertow": NEOTwewyItemData(
        1107, NEOTwewyItemType.Badge, ItemClassification.filler, [NEOTwewyItemGroup.COMBAT_PIN], "IL CAVALLO DEL RE"
    ),
    "Let the Rain Fall Down": NEOTwewyItemData(
        1108, NEOTwewyItemType.Badge, ItemClassification.filler, [NEOTwewyItemGroup.COMBAT_PIN], "IL CAVALLO DEL RE"
    ),
    "Taste of Poison Paradise": NEOTwewyItemData(
        1109, NEOTwewyItemType.Badge, ItemClassification.filler, [NEOTwewyItemGroup.COMBAT_PIN], "IL CAVALLO DEL RE"
    ),
    "Diamonds in the Sky": NEOTwewyItemData(
        1110, NEOTwewyItemType.Badge, ItemClassification.filler, [NEOTwewyItemGroup.COMBAT_PIN], "IL CAVALLO DEL RE"
    ),
    "All Comes Crashing Down": NEOTwewyItemData(
        1111, NEOTwewyItemType.Badge, ItemClassification.filler, [NEOTwewyItemGroup.COMBAT_PIN], "IL CAVALLO DEL RE"
    ),
    "What a Wicked Game": NEOTwewyItemData(
        1112, NEOTwewyItemType.Badge, ItemClassification.filler, [NEOTwewyItemGroup.COMBAT_PIN], "IL CAVALLO DEL RE"
    ),
    "Where I Break Free": NEOTwewyItemData(
        1113, NEOTwewyItemType.Badge, ItemClassification.filler, [NEOTwewyItemGroup.COMBAT_PIN], "IL CAVALLO DEL RE"
    ),
    "Born of Stormy Skies": NEOTwewyItemData(
        1114, NEOTwewyItemType.Badge, ItemClassification.filler, [NEOTwewyItemGroup.COMBAT_PIN], "IL CAVALLO DEL RE"
    ),
    "Lightning in My Hands": NEOTwewyItemData(
        1115, NEOTwewyItemType.Badge, ItemClassification.filler, [NEOTwewyItemGroup.COMBAT_PIN], "IL CAVALLO DEL RE"
    ),
    "In the Stars Tonight": NEOTwewyItemData(
        1116, NEOTwewyItemType.Badge, ItemClassification.filler, [NEOTwewyItemGroup.COMBAT_PIN], "IL CAVALLO DEL RE"
    ),
    "Blinded by the Light": NEOTwewyItemData(
        1117, NEOTwewyItemType.Badge, ItemClassification.filler, [NEOTwewyItemGroup.COMBAT_PIN], "IL CAVALLO DEL RE"
    ),
    "In My Misery": NEOTwewyItemData(
        1118, NEOTwewyItemType.Badge, ItemClassification.filler, [NEOTwewyItemGroup.COMBAT_PIN], "IL CAVALLO DEL RE"
    ),
    "Phoenix": NEOTwewyItemData(
        1119, NEOTwewyItemType.Badge, ItemClassification.filler, [NEOTwewyItemGroup.COMBAT_PIN], "Unbranded"
    ),
    "Joli bécot": NEOTwewyItemData(
        1120, NEOTwewyItemType.Badge, ItemClassification.filler, [NEOTwewyItemGroup.COMBAT_PIN], "Joli bécot"
    ),
    "Angelic Kick": NEOTwewyItemData(
        1121, NEOTwewyItemType.Badge, ItemClassification.filler, [NEOTwewyItemGroup.COMBAT_PIN], "Joli bécot"
    ),
    "Gust of Gorgeous": NEOTwewyItemData(
        1122, NEOTwewyItemType.Badge, ItemClassification.filler, [NEOTwewyItemGroup.COMBAT_PIN], "Joli bécot"
    ),
    "Wicked Wind": NEOTwewyItemData(
        1123, NEOTwewyItemType.Badge, ItemClassification.filler, [NEOTwewyItemGroup.COMBAT_PIN], "Joli bécot"
    ),
    "Sistah Subwoofer": NEOTwewyItemData(
        1124, NEOTwewyItemType.Badge, ItemClassification.filler, [NEOTwewyItemGroup.COMBAT_PIN], "Joli bécot"
    ),
    "Disco Divekick": NEOTwewyItemData(
        1125, NEOTwewyItemType.Badge, ItemClassification.filler, [NEOTwewyItemGroup.COMBAT_PIN], "Joli bécot"
    ),
    "Soul Ablaze": NEOTwewyItemData(
        1126, NEOTwewyItemType.Badge, ItemClassification.filler, [NEOTwewyItemGroup.COMBAT_PIN], "Joli bécot"
    ),
    "Killer Princess": NEOTwewyItemData(
        1127, NEOTwewyItemType.Badge, ItemClassification.filler, [NEOTwewyItemGroup.COMBAT_PIN], "Joli bécot"
    ),
    "Leo Armo": NEOTwewyItemData(
        1128, NEOTwewyItemType.Badge, ItemClassification.filler, [NEOTwewyItemGroup.COMBAT_PIN], "Unbranded"
    ),
    "Marvelous Crash": NEOTwewyItemData(
        1129, NEOTwewyItemType.Badge, ItemClassification.filler, [NEOTwewyItemGroup.COMBAT_PIN], "Joli bécot"
    ),
    "Crater's Kiss": NEOTwewyItemData(
        1130, NEOTwewyItemType.Badge, ItemClassification.filler, [NEOTwewyItemGroup.COMBAT_PIN], "Joli bécot"
    ),
    "Cranberry Crystal": NEOTwewyItemData(
        1131, NEOTwewyItemType.Badge, ItemClassification.filler, [NEOTwewyItemGroup.COMBAT_PIN], "Joli bécot"
    ),
    "Pink Matador": NEOTwewyItemData(
        1132, NEOTwewyItemType.Badge, ItemClassification.filler, [NEOTwewyItemGroup.COMBAT_PIN], "Joli bécot"
    ),
    "Electric Manicure": NEOTwewyItemData(
        1133, NEOTwewyItemType.Badge, ItemClassification.filler, [NEOTwewyItemGroup.COMBAT_PIN], "Joli bécot"
    ),
    "Bolt of Beauty": NEOTwewyItemData(
        1134, NEOTwewyItemType.Badge, ItemClassification.filler, [NEOTwewyItemGroup.COMBAT_PIN], "Joli bécot"
    ),
    "Rex": NEOTwewyItemData(
        1135, NEOTwewyItemType.Badge, ItemClassification.filler, [NEOTwewyItemGroup.COMBAT_PIN], "Unbranded"
    ),
    "Cherry Bomb": NEOTwewyItemData(
        1136, NEOTwewyItemType.Badge, ItemClassification.filler, [NEOTwewyItemGroup.COMBAT_PIN], "Joli bécot"
    ),
    "Jealous Rage": NEOTwewyItemData(
        1137, NEOTwewyItemType.Badge, ItemClassification.filler, [NEOTwewyItemGroup.COMBAT_PIN], "Joli bécot"
    ),
    "Bad Romance": NEOTwewyItemData(
        1138, NEOTwewyItemType.Badge, ItemClassification.filler, [NEOTwewyItemGroup.COMBAT_PIN], "Joli bécot"
    ),
    "Cold Cony×Cony": NEOTwewyItemData(
        1139, NEOTwewyItemType.Badge, ItemClassification.filler, [NEOTwewyItemGroup.COMBAT_PIN], "Cony×Cony"
    ),
    "Glacial Getaway": NEOTwewyItemData(
        1140, NEOTwewyItemType.Badge, ItemClassification.filler, [NEOTwewyItemGroup.COMBAT_PIN], "Cony×Cony"
    ),
    "Polar Princess": NEOTwewyItemData(
        1141, NEOTwewyItemType.Badge, ItemClassification.filler, [NEOTwewyItemGroup.COMBAT_PIN], "Cony×Cony"
    ),
    "Creepy Crystal": NEOTwewyItemData(
        1142, NEOTwewyItemType.Badge, ItemClassification.filler, [NEOTwewyItemGroup.COMBAT_PIN], "Cony×Cony"
    ),
    "Velvet Vampire": NEOTwewyItemData(
        1143, NEOTwewyItemType.Badge, ItemClassification.filler, [NEOTwewyItemGroup.COMBAT_PIN], "Cony×Cony"
    ),
    "Calamitous Candle": NEOTwewyItemData(
        1144, NEOTwewyItemType.Badge, ItemClassification.filler, [NEOTwewyItemGroup.COMBAT_PIN], "Cony×Cony"
    ),
    "Bérangère Lapin": NEOTwewyItemData(
        1145, NEOTwewyItemType.Badge, ItemClassification.filler, [NEOTwewyItemGroup.COMBAT_PIN], "Cony×Cony"
    ),
    "Grégoire Lapin": NEOTwewyItemData(
        1146, NEOTwewyItemType.Badge, ItemClassification.filler, [NEOTwewyItemGroup.COMBAT_PIN], "Cony×Cony"
    ),
    "Popguin": NEOTwewyItemData(
        1147, NEOTwewyItemType.Badge, ItemClassification.filler, [NEOTwewyItemGroup.COMBAT_PIN], "Unbranded"
    ),
    "Topo the Generous": NEOTwewyItemData(
        1148, NEOTwewyItemType.Badge, ItemClassification.filler, [NEOTwewyItemGroup.COMBAT_PIN], "Top o' Topo"
    ),
    "Once Upon a Dream": NEOTwewyItemData(
        1149, NEOTwewyItemType.Badge, ItemClassification.filler, [NEOTwewyItemGroup.COMBAT_PIN], "Top o' Topo"
    ),
    "Music of the Woods": NEOTwewyItemData(
        1150, NEOTwewyItemType.Badge, ItemClassification.filler, [NEOTwewyItemGroup.COMBAT_PIN], "Top o' Topo"
    ),
    "Mom's Secret Ingredient": NEOTwewyItemData(
        1151, NEOTwewyItemType.Badge, ItemClassification.filler, [NEOTwewyItemGroup.COMBAT_PIN], "Top o' Topo"
    ),
    "A Mysterious Gift": NEOTwewyItemData(
        1152, NEOTwewyItemType.Badge, ItemClassification.filler, [NEOTwewyItemGroup.COMBAT_PIN], "Top o' Topo"
    ),
    "The World Within": NEOTwewyItemData(
        1153, NEOTwewyItemType.Badge, ItemClassification.filler, [NEOTwewyItemGroup.COMBAT_PIN], "Top o' Topo"
    ),
    "Topo the Ingenious": NEOTwewyItemData(
        1154, NEOTwewyItemType.Badge, ItemClassification.filler, [NEOTwewyItemGroup.COMBAT_PIN], "Top o' Topo"
    ),
    "My Precious Moments": NEOTwewyItemData(
        1155, NEOTwewyItemType.Badge, ItemClassification.filler, [NEOTwewyItemGroup.COMBAT_PIN], "Top o' Topo"
    ),
    "Topo the Beloved": NEOTwewyItemData(
        1156, NEOTwewyItemType.Badge, ItemClassification.filler, [NEOTwewyItemGroup.COMBAT_PIN], "Top o' Topo"
    ),
    "ShoGun・Void": NEOTwewyItemData(
        1157, NEOTwewyItemType.Badge, ItemClassification.filler, [NEOTwewyItemGroup.COMBAT_PIN], "RyuGu"
    ),
    "ManjuSage・Void": NEOTwewyItemData(
        1158, NEOTwewyItemType.Badge, ItemClassification.filler, [NEOTwewyItemGroup.COMBAT_PIN], "RyuGu"
    ),
    "EnJo・Blaze": NEOTwewyItemData(
        1159, NEOTwewyItemType.Badge, ItemClassification.filler, [NEOTwewyItemGroup.COMBAT_PIN], "RyuGu"
    ),
    "KoYo・Blaze": NEOTwewyItemData(
        1160, NEOTwewyItemType.Badge, ItemClassification.filler, [NEOTwewyItemGroup.COMBAT_PIN], "RyuGu"
    ),
    "Tsubaki・Frost": NEOTwewyItemData(
        1161, NEOTwewyItemType.Badge, ItemClassification.filler, [NEOTwewyItemGroup.COMBAT_PIN], "RyuGu"
    ),
    "HiGan・Frost": NEOTwewyItemData(
        1162, NEOTwewyItemType.Badge, ItemClassification.filler, [NEOTwewyItemGroup.COMBAT_PIN], "RyuGu"
    ),
    "InaZuma・Surge": NEOTwewyItemData(
        1163, NEOTwewyItemType.Badge, ItemClassification.filler, [NEOTwewyItemGroup.COMBAT_PIN], "RyuGu"
    ),
    "RaiJin・Surge": NEOTwewyItemData(
        1164, NEOTwewyItemType.Badge, ItemClassification.filler, [NEOTwewyItemGroup.COMBAT_PIN], "RyuGu"
    ),
    "Doku Doku Panic": NEOTwewyItemData(
        1165, NEOTwewyItemType.Badge, ItemClassification.filler, [NEOTwewyItemGroup.COMBAT_PIN], "croaky panic"
    ),
    "KeiRyu・Epoch": NEOTwewyItemData(
        1166, NEOTwewyItemType.Badge, ItemClassification.filler, [NEOTwewyItemGroup.COMBAT_PIN], "RyuGu"
    ),
    "RyuGu・Void": NEOTwewyItemData(
        1167, NEOTwewyItemType.Badge, ItemClassification.filler, [NEOTwewyItemGroup.COMBAT_PIN], "RyuGu"
    ),
    "HanaDoki・Void": NEOTwewyItemData(
        1168, NEOTwewyItemType.Badge, ItemClassification.filler, [NEOTwewyItemGroup.COMBAT_PIN], "RyuGu"
    ),
    "Slitherin' Snake": NEOTwewyItemData(
        1169, NEOTwewyItemType.Badge, ItemClassification.filler, [NEOTwewyItemGroup.COMBAT_PIN], "croaky panic"
    ),
    "HoGyoku・Gleam": NEOTwewyItemData(
        1170, NEOTwewyItemType.Badge, ItemClassification.filler, [NEOTwewyItemGroup.COMBAT_PIN], "RyuGu"
    ),
    "Jelly": NEOTwewyItemData(
        1171, NEOTwewyItemType.Badge, ItemClassification.filler, [NEOTwewyItemGroup.COMBAT_PIN], "Unbranded"
    ),
    "Righteous Rabbit": NEOTwewyItemData(
        1172, NEOTwewyItemType.Badge, ItemClassification.filler, [NEOTwewyItemGroup.COMBAT_PIN], "Cony×Cony"
    ),
    "Brooding Bunny": NEOTwewyItemData(
        1173, NEOTwewyItemType.Badge, ItemClassification.filler, [NEOTwewyItemGroup.COMBAT_PIN], "Cony×Cony"
    ),
    "Ring-a-Ling": NEOTwewyItemData(
        1174, NEOTwewyItemType.Badge, ItemClassification.filler, [NEOTwewyItemGroup.COMBAT_PIN], "croaky panic"
    ),
    "Flyin' High": NEOTwewyItemData(
        1175, NEOTwewyItemType.Badge, ItemClassification.filler, [NEOTwewyItemGroup.COMBAT_PIN], "croaky panic"
    ),
    "Melancony×Melancony": NEOTwewyItemData(
        1176, NEOTwewyItemType.Badge, ItemClassification.filler, [NEOTwewyItemGroup.COMBAT_PIN], "Cony×Cony"
    ),
    "ConyｘCony": NEOTwewyItemData(
        1177, NEOTwewyItemType.Badge, ItemClassification.filler, [NEOTwewyItemGroup.COMBAT_PIN], "Cony×Cony"
    ),
    "Seraphic Snow": NEOTwewyItemData(
        1178, NEOTwewyItemType.Badge, ItemClassification.filler, [NEOTwewyItemGroup.COMBAT_PIN], "Cony×Cony"
    ),
    "Raven": NEOTwewyItemData(
        1179, NEOTwewyItemType.Badge, ItemClassification.filler, [NEOTwewyItemGroup.COMBAT_PIN], "Unbranded"
    ),
    "Balloon Trip": NEOTwewyItemData(
        1180, NEOTwewyItemType.Badge, ItemClassification.filler, [NEOTwewyItemGroup.COMBAT_PIN], "Top o' Topo"
    ),
    "Riled-Up Ribbon": NEOTwewyItemData(
        1181, NEOTwewyItemType.Badge, ItemClassification.filler, [NEOTwewyItemGroup.COMBAT_PIN], "Top o' Topo"
    ),
    "Topo the Talented": NEOTwewyItemData(
        1182, NEOTwewyItemType.Badge, ItemClassification.filler, [NEOTwewyItemGroup.COMBAT_PIN], "Top o' Topo"
    ),
    "Catch a Wave": NEOTwewyItemData(
        1183, NEOTwewyItemType.Badge, ItemClassification.filler, [NEOTwewyItemGroup.COMBAT_PIN], "croaky panic"
    ),
    "Kappa Panic": NEOTwewyItemData(
        1184, NEOTwewyItemType.Badge, ItemClassification.filler, [NEOTwewyItemGroup.COMBAT_PIN], "croaky panic"
    ),
    "A Forlorn Treasure": NEOTwewyItemData(
        1185, NEOTwewyItemType.Badge, ItemClassification.filler, [NEOTwewyItemGroup.COMBAT_PIN], "Top o' Topo"
    ),
    "Cave of Secrets": NEOTwewyItemData(
        1186, NEOTwewyItemType.Badge, ItemClassification.filler, [NEOTwewyItemGroup.COMBAT_PIN], "Top o' Topo"
    ),
    "In the Snipeline": NEOTwewyItemData(
        1187, NEOTwewyItemType.Badge, ItemClassification.filler, [NEOTwewyItemGroup.COMBAT_PIN], "garagara"
    ),
    "Don't Miss Your Shot": NEOTwewyItemData(
        1188, NEOTwewyItemType.Badge, ItemClassification.filler, [NEOTwewyItemGroup.COMBAT_PIN], "garagara"
    ),
    "Any Way You Snipe It": NEOTwewyItemData(
        1189, NEOTwewyItemType.Badge, ItemClassification.filler, [NEOTwewyItemGroup.COMBAT_PIN], "garagara"
    ),
    "garagara": NEOTwewyItemData(
        1190, NEOTwewyItemType.Badge, ItemClassification.filler, [NEOTwewyItemGroup.COMBAT_PIN], "garagara"
    ),
    "Shot in the Dank": NEOTwewyItemData(
        1191, NEOTwewyItemType.Badge, ItemClassification.filler, [NEOTwewyItemGroup.COMBAT_PIN], "garagara"
    ),
    "What Can Never Be": NEOTwewyItemData(
        1192, NEOTwewyItemType.Badge, ItemClassification.filler, [NEOTwewyItemGroup.COMBAT_PIN], "IL CAVALLO DEL RE"
    ),
    "Stuck in the Middle": NEOTwewyItemData(
        1193, NEOTwewyItemType.Badge, ItemClassification.filler, [NEOTwewyItemGroup.COMBAT_PIN], "IL CAVALLO DEL RE"
    ),
    "Time in a Bottle": NEOTwewyItemData(
        1194, NEOTwewyItemType.Badge, ItemClassification.filler, [NEOTwewyItemGroup.COMBAT_PIN], "IL CAVALLO DEL RE"
    ),
    "Stay Gold": NEOTwewyItemData(
        1195, NEOTwewyItemType.Badge, ItemClassification.filler, [NEOTwewyItemGroup.COMBAT_PIN], "IL CAVALLO DEL RE"
    ),
    "Stay Beautiful": NEOTwewyItemData(
        1196, NEOTwewyItemType.Badge, ItemClassification.filler, [NEOTwewyItemGroup.COMBAT_PIN], "IL CAVALLO DEL RE"
    ),
    "Let the Storm Rage On": NEOTwewyItemData(
        1197, NEOTwewyItemType.Badge, ItemClassification.filler, [NEOTwewyItemGroup.COMBAT_PIN], "IL CAVALLO DEL RE"
    ),
    "SuiGen・Void": NEOTwewyItemData(
        1198, NEOTwewyItemType.Badge, ItemClassification.filler, [NEOTwewyItemGroup.COMBAT_PIN], "RyuGu"
    ),
    "KoCho・Void": NEOTwewyItemData(
        1199, NEOTwewyItemType.Badge, ItemClassification.filler, [NEOTwewyItemGroup.COMBAT_PIN], "RyuGu"
    ),
    "ShiDare・Shade": NEOTwewyItemData(
        1200, NEOTwewyItemType.Badge, ItemClassification.filler, [NEOTwewyItemGroup.COMBAT_PIN], "RyuGu"
    ),
    "Tsuzumi・Echo": NEOTwewyItemData(
        1201, NEOTwewyItemType.Badge, ItemClassification.filler, [NEOTwewyItemGroup.COMBAT_PIN], "RyuGu"
    ),
    "Shiba": NEOTwewyItemData(
        1202, NEOTwewyItemType.Badge, ItemClassification.filler, [NEOTwewyItemGroup.COMBAT_PIN], "Unbranded"
    ),
    "Let's Have Fungis!": NEOTwewyItemData(
        1203, NEOTwewyItemType.Badge, ItemClassification.filler, [NEOTwewyItemGroup.COMBAT_PIN], "Unbranded"
    ),
    "Fuel to the Fire": NEOTwewyItemData(
        1204, NEOTwewyItemType.Badge, ItemClassification.filler, [NEOTwewyItemGroup.COMBAT_PIN], "garagara"
    ),
    "Fire in the Belly": NEOTwewyItemData(
        1205, NEOTwewyItemType.Badge, ItemClassification.filler, [NEOTwewyItemGroup.COMBAT_PIN], "garagara"
    ),
    "Ifs, Ands, or Bolts": NEOTwewyItemData(
        1206, NEOTwewyItemType.Badge, ItemClassification.filler, [NEOTwewyItemGroup.COMBAT_PIN], "garagara"
    ),
    "Sparks Will Fly": NEOTwewyItemData(
        1207, NEOTwewyItemType.Badge, ItemClassification.filler, [NEOTwewyItemGroup.COMBAT_PIN], "garagara"
    ),
    "AraUmi・Gale": NEOTwewyItemData(
        1208, NEOTwewyItemType.Badge, ItemClassification.filler, [NEOTwewyItemGroup.COMBAT_PIN], "RyuGu"
    ),
    "FuJin・Gale": NEOTwewyItemData(
        1209, NEOTwewyItemType.Badge, ItemClassification.filler, [NEOTwewyItemGroup.COMBAT_PIN], "RyuGu"
    ),
    "IroGoi・Shift": NEOTwewyItemData(
        1210, NEOTwewyItemType.Badge, ItemClassification.filler, [NEOTwewyItemGroup.COMBAT_PIN], "RyuGu"
    ),
    "ShoRyu・Gleam": NEOTwewyItemData(
        1211, NEOTwewyItemType.Badge, ItemClassification.filler, [NEOTwewyItemGroup.COMBAT_PIN], "RyuGu"
    ),
    "The Prismatic Princess": NEOTwewyItemData(
        1212, NEOTwewyItemType.Badge, ItemClassification.filler, [NEOTwewyItemGroup.COMBAT_PIN], "Top o' Topo"
    ),
    "The Benevolent King": NEOTwewyItemData(
        1213, NEOTwewyItemType.Badge, ItemClassification.filler, [NEOTwewyItemGroup.COMBAT_PIN], "Top o' Topo"
    ),
    "Top o' Topo": NEOTwewyItemData(
        1214, NEOTwewyItemType.Badge, ItemClassification.filler, [NEOTwewyItemGroup.COMBAT_PIN], "Top o' Topo"
    ),
    "Petals of Love": NEOTwewyItemData(
        1215, NEOTwewyItemType.Badge, ItemClassification.filler, [NEOTwewyItemGroup.COMBAT_PIN], "Top o' Topo"
    ),
    "Topo the Adventurous": NEOTwewyItemData(
        1216, NEOTwewyItemType.Badge, ItemClassification.filler, [NEOTwewyItemGroup.COMBAT_PIN], "Top o' Topo"
    ),
    "Fairytale Memories": NEOTwewyItemData(
        1217, NEOTwewyItemType.Badge, ItemClassification.filler, [NEOTwewyItemGroup.COMBAT_PIN], "Top o' Topo"
    ),
    "Topo the Famished": NEOTwewyItemData(
        1218, NEOTwewyItemType.Badge, ItemClassification.filler, [NEOTwewyItemGroup.COMBAT_PIN], "Top o' Topo"
    ),
    "The Enchanted Baker": NEOTwewyItemData(
        1219, NEOTwewyItemType.Badge, ItemClassification.filler, [NEOTwewyItemGroup.COMBAT_PIN], "Top o' Topo"
    ),
    "An Inseparable Pair": NEOTwewyItemData(
        1220, NEOTwewyItemType.Badge, ItemClassification.filler, [NEOTwewyItemGroup.COMBAT_PIN], "Top o' Topo"
    ),
    "Hammond's New Home": NEOTwewyItemData(
        1221, NEOTwewyItemType.Badge, ItemClassification.filler, [NEOTwewyItemGroup.COMBAT_PIN], "Top o' Topo"
    ),
    "Mr. Mew": NEOTwewyItemData(
        1222, NEOTwewyItemType.Badge, ItemClassification.filler, [NEOTwewyItemGroup.COMBAT_PIN], "Unbranded"
    ),
    "KaChu・Blaze": NEOTwewyItemData(
        1223, NEOTwewyItemType.Badge, ItemClassification.filler, [NEOTwewyItemGroup.COMBAT_PIN], "RyuGu"
    ),
    "AkaFuji・Blaze": NEOTwewyItemData(
        1224, NEOTwewyItemType.Badge, ItemClassification.filler, [NEOTwewyItemGroup.COMBAT_PIN], "RyuGu"
    ),
    "Firestorm": NEOTwewyItemData(
        1225, NEOTwewyItemType.Badge, ItemClassification.filler, [NEOTwewyItemGroup.COMBAT_PIN], "Unbranded"
    ),
    "GoKa・Blaze": NEOTwewyItemData(
        1226, NEOTwewyItemType.Badge, ItemClassification.filler, [NEOTwewyItemGroup.COMBAT_PIN], "RyuGu"
    ),
    "Notice Me Lightning": NEOTwewyItemData(
        1227, NEOTwewyItemType.Badge, ItemClassification.filler, [NEOTwewyItemGroup.COMBAT_PIN], "NATURAL PUPPY"
    ),
    "Oh Em Gee Lightning": NEOTwewyItemData(
        1228, NEOTwewyItemType.Badge, ItemClassification.filler, [NEOTwewyItemGroup.COMBAT_PIN], "NATURAL PUPPY"
    ),
    "Trendy Tornado": NEOTwewyItemData(
        1229, NEOTwewyItemType.Badge, ItemClassification.filler, [NEOTwewyItemGroup.COMBAT_PIN], "NATURAL PUPPY"
    ),
    "Giddy Graviton": NEOTwewyItemData(
        1230, NEOTwewyItemType.Badge, ItemClassification.filler, [NEOTwewyItemGroup.COMBAT_PIN], "NATURAL PUPPY"
    ),
    "Good Mood Graviton": NEOTwewyItemData(
        1231, NEOTwewyItemType.Badge, ItemClassification.filler, [NEOTwewyItemGroup.COMBAT_PIN], "NATURAL PUPPY"
    ),
    "Relative Absoluteness": NEOTwewyItemData(
        1232, NEOTwewyItemType.Badge, ItemClassification.filler, [NEOTwewyItemGroup.COMBAT_PIN], "MONOCROW"
    ),
    "Pachy": NEOTwewyItemData(
        1233, NEOTwewyItemType.Badge, ItemClassification.filler, [NEOTwewyItemGroup.COMBAT_PIN], "Unbranded"
    ),
    "A Day Off Outside": NEOTwewyItemData(
        1234, NEOTwewyItemType.Badge, ItemClassification.filler, [NEOTwewyItemGroup.COMBAT_PIN], "Shepherd House"
    ),
    "The Cozy Hilltop Windmill": NEOTwewyItemData(
        1235, NEOTwewyItemType.Badge, ItemClassification.filler, [NEOTwewyItemGroup.COMBAT_PIN], "Shepherd House"
    ),
    "The Breezy Ovine Wind": NEOTwewyItemData(
        1236, NEOTwewyItemType.Badge, ItemClassification.filler, [NEOTwewyItemGroup.COMBAT_PIN], "Shepherd House"
    ),
    "The Ever-Arctic Treasure": NEOTwewyItemData(
        1237, NEOTwewyItemType.Badge, ItemClassification.filler, [NEOTwewyItemGroup.COMBAT_PIN], "Shepherd House"
    ),
    "A Moonlit Night Inside": NEOTwewyItemData(
        1238, NEOTwewyItemType.Badge, ItemClassification.filler, [NEOTwewyItemGroup.COMBAT_PIN], "Shepherd House"
    ),
    "The Woolly Triple Axel": NEOTwewyItemData(
        1239, NEOTwewyItemType.Badge, ItemClassification.filler, [NEOTwewyItemGroup.COMBAT_PIN], "Shepherd House"
    ),
    "Cursed Croaker": NEOTwewyItemData(
        1240, NEOTwewyItemType.Badge, ItemClassification.filler, [NEOTwewyItemGroup.COMBAT_PIN], "croaky panic"
    ),
    "Roly Poly Cricket": NEOTwewyItemData(
        1241, NEOTwewyItemType.Badge, ItemClassification.filler, [NEOTwewyItemGroup.COMBAT_PIN], "croaky panic"
    ),
    "Thirsty Frog": NEOTwewyItemData(
        1242, NEOTwewyItemType.Badge, ItemClassification.filler, [NEOTwewyItemGroup.COMBAT_PIN], "croaky panic"
    ),
    "Golden Kappa Panic": NEOTwewyItemData(
        1243, NEOTwewyItemType.Badge, ItemClassification.filler, [NEOTwewyItemGroup.COMBAT_PIN], "croaky panic"
    ),
    "Snap Crackle Popcorn": NEOTwewyItemData(
        1244, NEOTwewyItemType.Badge, ItemClassification.filler, [NEOTwewyItemGroup.COMBAT_PIN], "croaky panic"
    ),
    "Sunny Side Skillet": NEOTwewyItemData(
        1245, NEOTwewyItemType.Badge, ItemClassification.filler, [NEOTwewyItemGroup.COMBAT_PIN], "croaky panic"
    ),
    "A Tasty Ovine Snack": NEOTwewyItemData(
        1246, NEOTwewyItemType.Badge, ItemClassification.filler, [NEOTwewyItemGroup.COMBAT_PIN], "Shepherd House"
    ),
    "The Gentle Airplane Pilot": NEOTwewyItemData(
        1247, NEOTwewyItemType.Badge, ItemClassification.filler, [NEOTwewyItemGroup.COMBAT_PIN], "Shepherd House"
    ),
    "The Song of Friendship": NEOTwewyItemData(
        1248, NEOTwewyItemType.Badge, ItemClassification.filler, [NEOTwewyItemGroup.COMBAT_PIN], "Shepherd House"
    ),
    "The Woolly Jazz Player": NEOTwewyItemData(
        1249, NEOTwewyItemType.Badge, ItemClassification.filler, [NEOTwewyItemGroup.COMBAT_PIN], "Shepherd House"
    ),
    "Back to the Ewe-ture": NEOTwewyItemData(
        1250, NEOTwewyItemType.Badge, ItemClassification.filler, [NEOTwewyItemGroup.COMBAT_PIN], "Shepherd House"
    ),
    "Shark": NEOTwewyItemData(
        1251, NEOTwewyItemType.Badge, ItemClassification.filler, [NEOTwewyItemGroup.COMBAT_PIN], "Unbranded"
    ),
    "Chef Amphibie": NEOTwewyItemData(
        1252, NEOTwewyItemType.Badge, ItemClassification.filler, [NEOTwewyItemGroup.COMBAT_PIN], "croaky panic"
    ),
    "Star Quarterback": NEOTwewyItemData(
        1253, NEOTwewyItemType.Badge, ItemClassification.filler, [NEOTwewyItemGroup.COMBAT_PIN], "HOG FANG"
    ),
    "Dine 'n' Dash": NEOTwewyItemData(
        1254, NEOTwewyItemType.Badge, ItemClassification.filler, [NEOTwewyItemGroup.COMBAT_PIN], "HOG FANG"
    ),
    "Bolt Boar": NEOTwewyItemData(
        1255, NEOTwewyItemType.Badge, ItemClassification.filler, [NEOTwewyItemGroup.COMBAT_PIN], "HOG FANG"
    ),
    "Mr. Fangman": NEOTwewyItemData(
        1256, NEOTwewyItemType.Badge, ItemClassification.filler, [NEOTwewyItemGroup.COMBAT_PIN], "HOG FANG"
    ),
    "Burnin' Boar": NEOTwewyItemData(
        1257, NEOTwewyItemType.Badge, ItemClassification.filler, [NEOTwewyItemGroup.COMBAT_PIN], "HOG FANG"
    ),
    "HOG FANG": NEOTwewyItemData(
        1258, NEOTwewyItemType.Badge, ItemClassification.filler, [NEOTwewyItemGroup.COMBAT_PIN], "HOG FANG"
    ),
    "Big Bang Boar": NEOTwewyItemData(
        1259, NEOTwewyItemType.Badge, ItemClassification.filler, [NEOTwewyItemGroup.COMBAT_PIN], "HOG FANG"
    ),
    "Cervus": NEOTwewyItemData(
        1260, NEOTwewyItemType.Badge, ItemClassification.filler, [NEOTwewyItemGroup.COMBAT_PIN], "Unbranded"
    ),
    "UFO Rescue": NEOTwewyItemData(
        1261, NEOTwewyItemType.Badge, ItemClassification.filler, [NEOTwewyItemGroup.COMBAT_PIN], "HOG FANG"
    ),
    "Tigre PUNKS": NEOTwewyItemData(
        1262, NEOTwewyItemType.Badge, ItemClassification.filler, [NEOTwewyItemGroup.COMBAT_PIN], "Tigre PUNKS"
    ),
    "Bright Chord": NEOTwewyItemData(
        1263, NEOTwewyItemType.Badge, ItemClassification.filler, [NEOTwewyItemGroup.COMBAT_PIN], "Tigre PUNKS"
    ),
    "Bootleg Tune": NEOTwewyItemData(
        1264, NEOTwewyItemType.Badge, ItemClassification.filler, [NEOTwewyItemGroup.COMBAT_PIN], "Tigre PUNKS"
    ),
    "Discordance": NEOTwewyItemData(
        1265, NEOTwewyItemType.Badge, ItemClassification.filler, [NEOTwewyItemGroup.COMBAT_PIN], "Tigre PUNKS"
    ),
    "Maiden Beat": NEOTwewyItemData(
        1266, NEOTwewyItemType.Badge, ItemClassification.filler, [NEOTwewyItemGroup.COMBAT_PIN], "Tigre PUNKS"
    ),
    "Aw, That Shucks!": NEOTwewyItemData(
        1267, NEOTwewyItemType.Badge, ItemClassification.filler, [NEOTwewyItemGroup.COMBAT_PIN], "Unbranded"
    ),
    "Headliner": NEOTwewyItemData(
        1268, NEOTwewyItemType.Badge, ItemClassification.filler, [NEOTwewyItemGroup.COMBAT_PIN], "Tigre PUNKS"
    ),
    "Runaway Rocket": NEOTwewyItemData(
        1269, NEOTwewyItemType.Badge, ItemClassification.filler, [NEOTwewyItemGroup.COMBAT_PIN], "HOG FANG"
    ),
    "Clawed Guardian": NEOTwewyItemData(
        1270, NEOTwewyItemType.Badge, ItemClassification.filler, [NEOTwewyItemGroup.COMBAT_PIN], "Tigre PUNKS"
    ),
    "HOG Healer": NEOTwewyItemData(
        1271, NEOTwewyItemType.Badge, ItemClassification.filler, [NEOTwewyItemGroup.COMBAT_PIN], "HOG FANG"
    ),
    "Rip-Roarin' Red": NEOTwewyItemData(
        1272, NEOTwewyItemType.Badge, ItemClassification.filler, [NEOTwewyItemGroup.COMBAT_PIN], "HOG FANG"
    ),
    "Never Too Young": NEOTwewyItemData(
        1273, NEOTwewyItemType.Badge, ItemClassification.filler, [NEOTwewyItemGroup.COMBAT_PIN], "HOG FANG"
    ),
    "Lost in Space": NEOTwewyItemData(
        1274, NEOTwewyItemType.Badge, ItemClassification.filler, [NEOTwewyItemGroup.COMBAT_PIN], "HOG FANG"
    ),
    "Rainbow Route 66": NEOTwewyItemData(
        1275, NEOTwewyItemType.Badge, ItemClassification.filler, [NEOTwewyItemGroup.COMBAT_PIN], "HOG FANG"
    ),
    "Hogway to Heaven": NEOTwewyItemData(
        1276, NEOTwewyItemType.Badge, ItemClassification.filler, [NEOTwewyItemGroup.COMBAT_PIN], "HOG FANG"
    ),
    "Heartful Hot Dog": NEOTwewyItemData(
        1277, NEOTwewyItemType.Badge, ItemClassification.filler, [NEOTwewyItemGroup.COMBAT_PIN], "HOG FANG"
    ),
    "Rhino": NEOTwewyItemData(
        1278, NEOTwewyItemType.Badge, ItemClassification.filler, [NEOTwewyItemGroup.COMBAT_PIN], "Unbranded"
    ),
    "FANG Defender": NEOTwewyItemData(
        1279, NEOTwewyItemType.Badge, ItemClassification.filler, [NEOTwewyItemGroup.COMBAT_PIN], "HOG FANG"
    ),
    "Watch Your Step": NEOTwewyItemData(
        1280, NEOTwewyItemType.Badge, ItemClassification.filler, [NEOTwewyItemGroup.COMBAT_PIN], "MONOCROW"
    ),
    "You Can Overcome": NEOTwewyItemData(
        1281, NEOTwewyItemType.Badge, ItemClassification.filler, [NEOTwewyItemGroup.COMBAT_PIN], "MONOCROW"
    ),
    "Look Out Below": NEOTwewyItemData(
        1282, NEOTwewyItemType.Badge, ItemClassification.filler, [NEOTwewyItemGroup.COMBAT_PIN], "MONOCROW"
    ),
    "Absolute Relativity": NEOTwewyItemData(
        1283, NEOTwewyItemType.Badge, ItemClassification.filler, [NEOTwewyItemGroup.COMBAT_PIN], "MONOCROW"
    ),
    "Pig": NEOTwewyItemData(
        1284, NEOTwewyItemType.Badge, ItemClassification.filler, [NEOTwewyItemGroup.COMBAT_PIN], "Unbranded"
    ),
    "Seductive Snare": NEOTwewyItemData(
        1285, NEOTwewyItemType.Badge, ItemClassification.filler, [NEOTwewyItemGroup.COMBAT_PIN], "Joli bécot"
    ),
    "Deadly Fragrance": NEOTwewyItemData(
        1286, NEOTwewyItemType.Badge, ItemClassification.filler, [NEOTwewyItemGroup.COMBAT_PIN], "Joli bécot"
    ),
    "A Drawn Conclusion": NEOTwewyItemData(
        1287, NEOTwewyItemType.Badge, ItemClassification.filler, [NEOTwewyItemGroup.COMBAT_PIN], "garagara"
    ),
    "Gravving at Straws": NEOTwewyItemData(
        1288, NEOTwewyItemType.Badge, ItemClassification.filler, [NEOTwewyItemGroup.COMBAT_PIN], "garagara"
    ),
    "Leon": NEOTwewyItemData(
        1289, NEOTwewyItemType.Badge, ItemClassification.filler, [NEOTwewyItemGroup.COMBAT_PIN], "Unbranded"
    ),
    "Tenka Juzumaru": NEOTwewyItemData(
        1290, NEOTwewyItemType.Badge, ItemClassification.filler, [NEOTwewyItemGroup.COMBAT_PIN], "Jupiter of the Monkey"
    ),
    "Tenka Mikazuki": NEOTwewyItemData(
        1291, NEOTwewyItemType.Badge, ItemClassification.filler, [NEOTwewyItemGroup.COMBAT_PIN], "Jupiter of the Monkey"
    ),
    "Coochy-Coochy-Coo": NEOTwewyItemData(
        1292, NEOTwewyItemType.Badge, ItemClassification.filler, [NEOTwewyItemGroup.COMBAT_PIN], "Unbranded"
    ),
    "Black Cat Crush": NEOTwewyItemData(
        1293, NEOTwewyItemType.Badge, ItemClassification.filler, [NEOTwewyItemGroup.COMBAT_PIN], "Gatto Nero"
    ),
    "Black Cat Cards": NEOTwewyItemData(
        1294, NEOTwewyItemType.Badge, ItemClassification.filler, [NEOTwewyItemGroup.COMBAT_PIN], "Gatto Nero"
    ),
    "Black Cat Comet": NEOTwewyItemData(
        1295, NEOTwewyItemType.Badge, ItemClassification.filler, [NEOTwewyItemGroup.COMBAT_PIN], "Gatto Nero"
    ),
    "Black Cat Burst": NEOTwewyItemData(
        1296, NEOTwewyItemType.Badge, ItemClassification.filler, [NEOTwewyItemGroup.COMBAT_PIN], "Gatto Nero"
    ),
    "Black Cat Blades": NEOTwewyItemData(
        1297, NEOTwewyItemType.Badge, ItemClassification.filler, [NEOTwewyItemGroup.COMBAT_PIN], "Gatto Nero"
    ),
    "Black Cat Burn": NEOTwewyItemData(
        1298, NEOTwewyItemType.Badge, ItemClassification.filler, [NEOTwewyItemGroup.COMBAT_PIN], "Gatto Nero"
    ),
    "St. Ver's Uppercut": NEOTwewyItemData(
        1299, NEOTwewyItemType.Badge, ItemClassification.filler, [NEOTwewyItemGroup.COMBAT_PIN], "Gatto Nero"
    ),
    "St. Aestas' Shrapnel": NEOTwewyItemData(
        1300, NEOTwewyItemType.Badge, ItemClassification.filler, [NEOTwewyItemGroup.COMBAT_PIN], "Gatto Nero"
    ),
    "St. Autumnus' Strike": NEOTwewyItemData(
        1301, NEOTwewyItemType.Badge, ItemClassification.filler, [NEOTwewyItemGroup.COMBAT_PIN], "Gatto Nero"
    ),
    "St. Hiems' Shotgun": NEOTwewyItemData(
        1302, NEOTwewyItemType.Badge, ItemClassification.filler, [NEOTwewyItemGroup.COMBAT_PIN], "Gatto Nero"
    ),
    "Charge Punch E": NEOTwewyItemData(
        1303, NEOTwewyItemType.Badge, ItemClassification.filler, [NEOTwewyItemGroup.COMBAT_PIN], "Gatto Nero"
    ),
    "Snare Trap E": NEOTwewyItemData(
        1304, NEOTwewyItemType.Badge, ItemClassification.filler, [NEOTwewyItemGroup.COMBAT_PIN], "Gatto Nero"
    ),
    "Just Keep Swimmin'!": NEOTwewyItemData(
        1305, NEOTwewyItemType.Badge, ItemClassification.filler, [NEOTwewyItemGroup.COMBAT_PIN], "Unbranded"
    ),
    "What a Shock!": NEOTwewyItemData(
        1306, NEOTwewyItemType.Badge, ItemClassification.filler, [NEOTwewyItemGroup.COMBAT_PIN], "Unbranded"
    ),
    "Stop the Music!": NEOTwewyItemData(
        1307, NEOTwewyItemType.Badge, ItemClassification.filler, [NEOTwewyItemGroup.COMBAT_PIN], "Unbranded"
    ),
    "Thanks Very Mochi!": NEOTwewyItemData(
        1308, NEOTwewyItemType.Badge, ItemClassification.filler, [NEOTwewyItemGroup.COMBAT_PIN], "Unbranded"
    ),
    "Holy Guacamole!": NEOTwewyItemData(
        1309, NEOTwewyItemType.Badge, ItemClassification.filler, [NEOTwewyItemGroup.COMBAT_PIN], "Unbranded"
    ),
    "Exercisin' Gator": NEOTwewyItemData(
        1310, NEOTwewyItemType.Badge, ItemClassification.filler, [NEOTwewyItemGroup.COMBAT_PIN], "Unbranded"
    ),
    "Handstandin' Panda": NEOTwewyItemData(
        1311, NEOTwewyItemType.Badge, ItemClassification.filler, [NEOTwewyItemGroup.COMBAT_PIN], "Unbranded"
    ),
    "5 Yen": NEOTwewyItemData(
        5001, NEOTwewyItemType.Badge, ItemClassification.filler, [NEOTwewyItemGroup.MONEY], "Unbranded"
    ),
    "10 Yen": NEOTwewyItemData(
        5002, NEOTwewyItemType.Badge, ItemClassification.filler, [NEOTwewyItemGroup.MONEY], "Unbranded"
    ),
    "50 Yen": NEOTwewyItemData(
        5003, NEOTwewyItemType.Badge, ItemClassification.filler, [NEOTwewyItemGroup.MONEY], "Unbranded"
    ),
    "100 Yen": NEOTwewyItemData(
        5004, NEOTwewyItemType.Badge, ItemClassification.filler, [NEOTwewyItemGroup.MONEY], "Unbranded"
    ),
    "500 Yen": NEOTwewyItemData(
        5005, NEOTwewyItemType.Badge, ItemClassification.filler, [NEOTwewyItemGroup.MONEY], "Unbranded"
    ),
    "1000 Yen": NEOTwewyItemData(
        5006, NEOTwewyItemType.Badge, ItemClassification.filler, [NEOTwewyItemGroup.MONEY], "Unbranded"
    ),
    "5000 Yen": NEOTwewyItemData(
        5007, NEOTwewyItemType.Badge, ItemClassification.filler, [NEOTwewyItemGroup.MONEY], "Unbranded"
    ),
    "10000 Yen": NEOTwewyItemData(
        5008, NEOTwewyItemType.Badge, ItemClassification.filler, [NEOTwewyItemGroup.MONEY], "Unbranded"
    ),
    "100000 Yen": NEOTwewyItemData(
        5009, NEOTwewyItemType.Badge, ItemClassification.filler, [NEOTwewyItemGroup.MONEY], "Unbranded"
    ),
    "Scarletite": NEOTwewyItemData(
        5100, NEOTwewyItemType.Badge, ItemClassification.filler, [NEOTwewyItemGroup.RARE_METAL], "Unbranded"
    ),
    "Rare Metal": NEOTwewyItemData(
        5101, NEOTwewyItemType.Badge, ItemClassification.filler, [NEOTwewyItemGroup.RARE_METAL], "Unbranded"
    ),
    "Tektite": NEOTwewyItemData(
        5102, NEOTwewyItemType.Badge, ItemClassification.filler, [NEOTwewyItemGroup.RARE_METAL], "Unbranded"
    ),
    "Adamantite": NEOTwewyItemData(
        5103, NEOTwewyItemType.Badge, ItemClassification.filler, [NEOTwewyItemGroup.RARE_METAL], "Unbranded"
    ),
    "Orichalcum": NEOTwewyItemData(
        5104, NEOTwewyItemType.Badge, ItemClassification.filler, [NEOTwewyItemGroup.RARE_METAL], "Unbranded"
    ),
    "Shadow Matter": NEOTwewyItemData(
        5105, NEOTwewyItemType.Badge, ItemClassification.filler, [NEOTwewyItemGroup.RARE_METAL], "Unbranded"
    ),
    "Dark Matter": NEOTwewyItemData(
        5106, NEOTwewyItemType.Badge, ItemClassification.filler, [NEOTwewyItemGroup.RARE_METAL], "Unbranded"
    ),
    "Axion": NEOTwewyItemData(
        5107, NEOTwewyItemType.Badge, ItemClassification.filler, [NEOTwewyItemGroup.RARE_METAL], "Unbranded"
    ),
    "Dilaton": NEOTwewyItemData(
        5108, NEOTwewyItemType.Badge, ItemClassification.filler, [NEOTwewyItemGroup.RARE_METAL], "Unbranded"
    ),
    "Dibaryon": NEOTwewyItemData(
        5109, NEOTwewyItemType.Badge, ItemClassification.filler, [NEOTwewyItemGroup.RARE_METAL], "Unbranded"
    ),
    "Sfermion": NEOTwewyItemData(
        5110, NEOTwewyItemType.Badge, ItemClassification.filler, [NEOTwewyItemGroup.RARE_METAL], "Unbranded"
    ),
    "Legendary Headphones": NEOTwewyItemData(
        10000, NEOTwewyItemType.Costume, ItemClassification.filler, [], "Jupiter of the Monkey"
    ),
    "Legendary Tank Top": NEOTwewyItemData(
        10001, NEOTwewyItemType.Costume, ItemClassification.filler, [], "Jupiter of the Monkey"
    ),
    "Legendary Shorts": NEOTwewyItemData(
        10002, NEOTwewyItemType.Costume, ItemClassification.filler, [], "Jupiter of the Monkey"
    ),
    "Legendary Sneakers": NEOTwewyItemData(
        10003, NEOTwewyItemType.Costume, ItemClassification.filler, [], "Jupiter of the Monkey"
    ),
    "Legendary Music Player": NEOTwewyItemData(
        10004, NEOTwewyItemType.Costume, ItemClassification.filler, [], "Jupiter of the Monkey"
    ),
    "Flower Headband": NEOTwewyItemData(10100, NEOTwewyItemType.Costume, ItemClassification.filler, [], "Top o' Topo"),
    "Ribbon Headband": NEOTwewyItemData(10101, NEOTwewyItemType.Costume, ItemClassification.filler, [], "Top o' Topo"),
    "Topo Hat": NEOTwewyItemData(10102, NEOTwewyItemType.Costume, ItemClassification.filler, [], "Top o' Topo"),
    "Romantic Blouse": NEOTwewyItemData(10103, NEOTwewyItemType.Costume, ItemClassification.filler, [], "Top o' Topo"),
    "Fluffy Sweater": NEOTwewyItemData(10104, NEOTwewyItemType.Costume, ItemClassification.filler, [], "Top o' Topo"),
    "Top o' Topo T-Shirt": NEOTwewyItemData(
        10105, NEOTwewyItemType.Costume, ItemClassification.filler, [], "Top o' Topo"
    ),
    "Flowy Tulle Skirt": NEOTwewyItemData(
        10106, NEOTwewyItemType.Costume, ItemClassification.filler, [], "Top o' Topo"
    ),
    "Cropped Pants": NEOTwewyItemData(10107, NEOTwewyItemType.Costume, ItemClassification.filler, [], "Top o' Topo"),
    "Tasteful Dress": NEOTwewyItemData(10108, NEOTwewyItemType.Costume, ItemClassification.filler, [], "Top o' Topo"),
    "Marine Dress": NEOTwewyItemData(10109, NEOTwewyItemType.Costume, ItemClassification.filler, [], "Top o' Topo"),
    "Ribbon Pumps": NEOTwewyItemData(10110, NEOTwewyItemType.Costume, ItemClassification.filler, [], "Top o' Topo"),
    "Frilly Sandals": NEOTwewyItemData(10111, NEOTwewyItemType.Costume, ItemClassification.filler, [], "Top o' Topo"),
    "Comfy Loafers": NEOTwewyItemData(10112, NEOTwewyItemType.Costume, ItemClassification.filler, [], "Top o' Topo"),
    "Ribbon Bag": NEOTwewyItemData(10113, NEOTwewyItemType.Costume, ItemClassification.filler, [], "Top o' Topo"),
    "Modest Tote Bag": NEOTwewyItemData(10114, NEOTwewyItemType.Costume, ItemClassification.filler, [], "Top o' Topo"),
    "Cozy Cardigan": NEOTwewyItemData(10115, NEOTwewyItemType.Costume, ItemClassification.filler, [], "Top o' Topo"),
    "Airy Skirt": NEOTwewyItemData(10116, NEOTwewyItemType.Costume, ItemClassification.filler, [], "Top o' Topo"),
    "Flower Scrunchie": NEOTwewyItemData(10117, NEOTwewyItemType.Costume, ItemClassification.filler, [], "Top o' Topo"),
    "Dazzling Denim Cap": NEOTwewyItemData(
        10200, NEOTwewyItemType.Costume, ItemClassification.progression_skip_balancing, [], "Joli bécot"
    ),
    "Cattle Print Hat": NEOTwewyItemData(
        10201, NEOTwewyItemType.Costume, ItemClassification.progression_skip_balancing, [], "Joli bécot"
    ),
    "Cattle Print-Belted Cap": NEOTwewyItemData(
        10202, NEOTwewyItemType.Costume, ItemClassification.progression_skip_balancing, [], "Joli bécot"
    ),
    "Denim Jacket": NEOTwewyItemData(
        10203, NEOTwewyItemType.Costume, ItemClassification.progression_skip_balancing, [], "Joli bécot"
    ),
    "Grim Cardigan": NEOTwewyItemData(
        10204, NEOTwewyItemType.Costume, ItemClassification.progression_skip_balancing, [], "Joli bécot"
    ),
    "Open-Shoulder Top": NEOTwewyItemData(
        10205, NEOTwewyItemType.Costume, ItemClassification.progression_skip_balancing, [], "Joli bécot"
    ),
    "Lacy Bustier": NEOTwewyItemData(
        10206, NEOTwewyItemType.Costume, ItemClassification.progression_skip_balancing, [], "Joli bécot"
    ),
    "Shredded Jeans": NEOTwewyItemData(
        10207, NEOTwewyItemType.Costume, ItemClassification.progression_skip_balancing, [], "Joli bécot"
    ),
    "Marble Jeans": NEOTwewyItemData(
        10208, NEOTwewyItemType.Costume, ItemClassification.progression_skip_balancing, [], "Joli bécot"
    ),
    "Leather Miniskirt": NEOTwewyItemData(
        10209, NEOTwewyItemType.Costume, ItemClassification.progression_skip_balancing, [], "Joli bécot"
    ),
    "Pink Frilled Skort": NEOTwewyItemData(
        10210, NEOTwewyItemType.Costume, ItemClassification.progression_skip_balancing, [], "Joli bécot"
    ),
    "Trendy Two-Piece": NEOTwewyItemData(
        10211, NEOTwewyItemType.Costume, ItemClassification.progression_skip_balancing, [], "Joli bécot"
    ),
    "Sparkling Sandals": NEOTwewyItemData(
        10212, NEOTwewyItemType.Costume, ItemClassification.progression_skip_balancing, [], "Joli bécot"
    ),
    "Lace-up Knee-High Boots": NEOTwewyItemData(
        10213, NEOTwewyItemType.Costume, ItemClassification.progression_skip_balancing, [], "Joli bécot"
    ),
    "Rouge Ruched Boots": NEOTwewyItemData(
        10214, NEOTwewyItemType.Costume, ItemClassification.progression_skip_balancing, [], "Joli bécot"
    ),
    "Leather Shoes": NEOTwewyItemData(
        10215, NEOTwewyItemType.Costume, ItemClassification.progression_skip_balancing, [], "Joli bécot"
    ),
    "Shimmering Phone Case": NEOTwewyItemData(
        10216, NEOTwewyItemType.Costume, ItemClassification.progression_skip_balancing, [], "Joli bécot"
    ),
    "Pink Press-On Nails": NEOTwewyItemData(
        10217, NEOTwewyItemType.Costume, ItemClassification.progression_skip_balancing, [], "Joli bécot"
    ),
    "Golden Lighter": NEOTwewyItemData(
        10218, NEOTwewyItemType.Costume, ItemClassification.progression_skip_balancing, [], "Joli bécot"
    ),
    "Pink Sunglasses": NEOTwewyItemData(
        10219, NEOTwewyItemType.Costume, ItemClassification.progression_skip_balancing, [], "Joli bécot"
    ),
    "Red Mohawk Set": NEOTwewyItemData(10300, NEOTwewyItemType.Costume, ItemClassification.filler, [], "Tigre PUNKS"),
    "Studded Tiger Cap": NEOTwewyItemData(
        10301, NEOTwewyItemType.Costume, ItemClassification.filler, [], "Tigre PUNKS"
    ),
    "Studded Leather Cap": NEOTwewyItemData(
        10302, NEOTwewyItemType.Costume, ItemClassification.filler, [], "Tigre PUNKS"
    ),
    "Tiger Mohawk Set": NEOTwewyItemData(10303, NEOTwewyItemType.Costume, ItemClassification.filler, [], "Tigre PUNKS"),
    "Biker Jacket": NEOTwewyItemData(10304, NEOTwewyItemType.Costume, ItemClassification.filler, [], "Tigre PUNKS"),
    "Patched Biker Jacket": NEOTwewyItemData(
        10305, NEOTwewyItemType.Costume, ItemClassification.filler, [], "Tigre PUNKS"
    ),
    "Red Biker Vest": NEOTwewyItemData(10306, NEOTwewyItemType.Costume, ItemClassification.filler, [], "Tigre PUNKS"),
    "Tiger Biker Vest": NEOTwewyItemData(10307, NEOTwewyItemType.Costume, ItemClassification.filler, [], "Tigre PUNKS"),
    "Red Plaid Coat": NEOTwewyItemData(10308, NEOTwewyItemType.Costume, ItemClassification.filler, [], "Tigre PUNKS"),
    "White Linen Shirt": NEOTwewyItemData(
        10309, NEOTwewyItemType.Costume, ItemClassification.filler, [], "Tigre PUNKS"
    ),
    "Bondage Pants": NEOTwewyItemData(10310, NEOTwewyItemType.Costume, ItemClassification.filler, [], "Tigre PUNKS"),
    "Skirted Bondage Pants": NEOTwewyItemData(
        10311, NEOTwewyItemType.Costume, ItemClassification.filler, [], "Tigre PUNKS"
    ),
    "Bondage Shorts": NEOTwewyItemData(10312, NEOTwewyItemType.Costume, ItemClassification.filler, [], "Tigre PUNKS"),
    "Plaid Pants": NEOTwewyItemData(10313, NEOTwewyItemType.Costume, ItemClassification.filler, [], "Tigre PUNKS"),
    "Studded Boots": NEOTwewyItemData(10314, NEOTwewyItemType.Costume, ItemClassification.filler, [], "Tigre PUNKS"),
    "White Creepers": NEOTwewyItemData(10315, NEOTwewyItemType.Costume, ItemClassification.filler, [], "Tigre PUNKS"),
    "Tiger Creepers": NEOTwewyItemData(10316, NEOTwewyItemType.Costume, ItemClassification.filler, [], "Tigre PUNKS"),
    "Belted Boots": NEOTwewyItemData(10317, NEOTwewyItemType.Costume, ItemClassification.filler, [], "Tigre PUNKS"),
    "Spiked Wristband": NEOTwewyItemData(10318, NEOTwewyItemType.Costume, ItemClassification.filler, [], "Tigre PUNKS"),
    "Spiked Choker": NEOTwewyItemData(10319, NEOTwewyItemType.Costume, ItemClassification.filler, [], "Tigre PUNKS"),
    "Mini Shoulder Bag": NEOTwewyItemData(
        10320, NEOTwewyItemType.Costume, ItemClassification.filler, [], "Tigre PUNKS"
    ),
    "Tiger Backpack": NEOTwewyItemData(10321, NEOTwewyItemType.Costume, ItemClassification.filler, [], "Tigre PUNKS"),
    "Peach Blossom": NEOTwewyItemData(10400, NEOTwewyItemType.Costume, ItemClassification.filler, [], "Cony×Cony"),
    "Iberis": NEOTwewyItemData(10401, NEOTwewyItemType.Costume, ItemClassification.filler, [], "Cony×Cony"),
    "Scarlet Sage": NEOTwewyItemData(10402, NEOTwewyItemType.Costume, ItemClassification.filler, [], "Cony×Cony"),
    "Viola": NEOTwewyItemData(10403, NEOTwewyItemType.Costume, ItemClassification.filler, [], "Cony×Cony"),
    "Black Lily": NEOTwewyItemData(10404, NEOTwewyItemType.Costume, ItemClassification.filler, [], "Cony×Cony"),
    "Baby's Breath": NEOTwewyItemData(10405, NEOTwewyItemType.Costume, ItemClassification.filler, [], "Cony×Cony"),
    "Calla Lily": NEOTwewyItemData(10406, NEOTwewyItemType.Costume, ItemClassification.filler, [], "Cony×Cony"),
    "Black Camellia": NEOTwewyItemData(10407, NEOTwewyItemType.Costume, ItemClassification.filler, [], "Cony×Cony"),
    "Petunia": NEOTwewyItemData(10408, NEOTwewyItemType.Costume, ItemClassification.filler, [], "Cony×Cony"),
    "Hollyhock": NEOTwewyItemData(10409, NEOTwewyItemType.Costume, ItemClassification.filler, [], "Cony×Cony"),
    "Clover": NEOTwewyItemData(10410, NEOTwewyItemType.Costume, ItemClassification.filler, [], "Cony×Cony"),
    "Hyacinth": NEOTwewyItemData(10411, NEOTwewyItemType.Costume, ItemClassification.filler, [], "Cony×Cony"),
    "Buttercup": NEOTwewyItemData(10412, NEOTwewyItemType.Costume, ItemClassification.filler, [], "Cony×Cony"),
    "Canna Lily": NEOTwewyItemData(10413, NEOTwewyItemType.Costume, ItemClassification.filler, [], "Cony×Cony"),
    "Dahlia": NEOTwewyItemData(10414, NEOTwewyItemType.Costume, ItemClassification.filler, [], "Cony×Cony"),
    "Deadly Nightshade": NEOTwewyItemData(10415, NEOTwewyItemType.Costume, ItemClassification.filler, [], "Cony×Cony"),
    "Bougainvillea": NEOTwewyItemData(10416, NEOTwewyItemType.Costume, ItemClassification.filler, [], "Cony×Cony"),
    "Anthurium": NEOTwewyItemData(10417, NEOTwewyItemType.Costume, ItemClassification.filler, [], "Cony×Cony"),
    "Peony": NEOTwewyItemData(10418, NEOTwewyItemType.Costume, ItemClassification.filler, [], "Cony×Cony"),
    "Blue Rose": NEOTwewyItemData(10419, NEOTwewyItemType.Costume, ItemClassification.filler, [], "Cony×Cony"),
    "Baby Rose": NEOTwewyItemData(10420, NEOTwewyItemType.Costume, ItemClassification.filler, [], "Cony×Cony"),
    "Black Rose": NEOTwewyItemData(10421, NEOTwewyItemType.Costume, ItemClassification.filler, [], "Cony×Cony"),
    "Raven Blossom": NEOTwewyItemData(10500, NEOTwewyItemType.Costume, ItemClassification.filler, [], "RyuGu"),
    "Hollyhock Blossom": NEOTwewyItemData(10501, NEOTwewyItemType.Costume, ItemClassification.filler, [], "RyuGu"),
    "Cornflower Hemp": NEOTwewyItemData(10502, NEOTwewyItemType.Costume, ItemClassification.filler, [], "RyuGu"),
    "Sakura on Straw": NEOTwewyItemData(10503, NEOTwewyItemType.Costume, ItemClassification.filler, [], "RyuGu"),
    "Cobalt Bishamon": NEOTwewyItemData(10504, NEOTwewyItemType.Costume, ItemClassification.filler, [], "RyuGu"),
    "Black-Scarlet Blossom": NEOTwewyItemData(10505, NEOTwewyItemType.Costume, ItemClassification.filler, [], "RyuGu"),
    "Shaded Chrysanthemum": NEOTwewyItemData(10506, NEOTwewyItemType.Costume, ItemClassification.filler, [], "RyuGu"),
    "Lapis Chrysanthemum": NEOTwewyItemData(10507, NEOTwewyItemType.Costume, ItemClassification.filler, [], "RyuGu"),
    "Golden Sparrow": NEOTwewyItemData(10508, NEOTwewyItemType.Costume, ItemClassification.filler, [], "RyuGu"),
    "Flowing Indigo": NEOTwewyItemData(10509, NEOTwewyItemType.Costume, ItemClassification.filler, [], "RyuGu"),
    "Flowing Silver": NEOTwewyItemData(10510, NEOTwewyItemType.Costume, ItemClassification.filler, [], "RyuGu"),
    "Porcelain Blossom": NEOTwewyItemData(10511, NEOTwewyItemType.Costume, ItemClassification.filler, [], "RyuGu"),
    "Violet-Ebony Foxglove": NEOTwewyItemData(10512, NEOTwewyItemType.Costume, ItemClassification.filler, [], "RyuGu"),
    "Crimson Sand Blossom": NEOTwewyItemData(10513, NEOTwewyItemType.Costume, ItemClassification.filler, [], "RyuGu"),
    "Maiden Blossom": NEOTwewyItemData(10514, NEOTwewyItemType.Costume, ItemClassification.filler, [], "RyuGu"),
    "Gilded Bamboo": NEOTwewyItemData(10515, NEOTwewyItemType.Costume, ItemClassification.filler, [], "RyuGu"),
    "Flaming Blossom": NEOTwewyItemData(10516, NEOTwewyItemType.Costume, ItemClassification.filler, [], "RyuGu"),
    "Oversized Beanie": NEOTwewyItemData(10600, NEOTwewyItemType.Costume, ItemClassification.filler, [], "garagara"),
    "Cloth Headband": NEOTwewyItemData(10601, NEOTwewyItemType.Costume, ItemClassification.filler, [], "garagara"),
    "Turquoise Headband": NEOTwewyItemData(10602, NEOTwewyItemType.Costume, ItemClassification.filler, [], "garagara"),
    "Bohemian T-Shirt": NEOTwewyItemData(10603, NEOTwewyItemType.Costume, ItemClassification.filler, [], "garagara"),
    "Bohemian Pullover": NEOTwewyItemData(10604, NEOTwewyItemType.Costume, ItemClassification.filler, [], "garagara"),
    "Poncho": NEOTwewyItemData(10605, NEOTwewyItemType.Costume, ItemClassification.filler, [], "garagara"),
    "Cloak": NEOTwewyItemData(10606, NEOTwewyItemType.Costume, ItemClassification.filler, [], "garagara"),
    "Bohemian Pants": NEOTwewyItemData(10607, NEOTwewyItemType.Costume, ItemClassification.filler, [], "garagara"),
    "Harem Pants": NEOTwewyItemData(10608, NEOTwewyItemType.Costume, ItemClassification.filler, [], "garagara"),
    "Bohemian Skirt": NEOTwewyItemData(10609, NEOTwewyItemType.Costume, ItemClassification.filler, [], "garagara"),
    "Hippie Overalls": NEOTwewyItemData(10610, NEOTwewyItemType.Costume, ItemClassification.filler, [], "garagara"),
    "Hippie Dress": NEOTwewyItemData(10611, NEOTwewyItemType.Costume, ItemClassification.filler, [], "garagara"),
    "Bohemian Dress": NEOTwewyItemData(10612, NEOTwewyItemType.Costume, ItemClassification.filler, [], "garagara"),
    "Bohemian Sandals": NEOTwewyItemData(10613, NEOTwewyItemType.Costume, ItemClassification.filler, [], "garagara"),
    "Beaded Sandals": NEOTwewyItemData(10614, NEOTwewyItemType.Costume, ItemClassification.filler, [], "garagara"),
    "Bohemian Slip-ons": NEOTwewyItemData(10615, NEOTwewyItemType.Costume, ItemClassification.filler, [], "garagara"),
    "Moccasin Boots": NEOTwewyItemData(10616, NEOTwewyItemType.Costume, ItemClassification.filler, [], "garagara"),
    "Turquoise Necklace": NEOTwewyItemData(10617, NEOTwewyItemType.Costume, ItemClassification.filler, [], "garagara"),
    "Turquoise Bracelet": NEOTwewyItemData(10618, NEOTwewyItemType.Costume, ItemClassification.filler, [], "garagara"),
    "Hippie Shoulder Bag": NEOTwewyItemData(10619, NEOTwewyItemType.Costume, ItemClassification.filler, [], "garagara"),
    "Compagno": NEOTwewyItemData(10700, NEOTwewyItemType.Costume, ItemClassification.filler, [], "IL CAVALLO DEL RE"),
    "Galassia": NEOTwewyItemData(10701, NEOTwewyItemType.Costume, ItemClassification.filler, [], "IL CAVALLO DEL RE"),
    "Bellezza suprema": NEOTwewyItemData(
        10702, NEOTwewyItemType.Costume, ItemClassification.filler, [], "IL CAVALLO DEL RE"
    ),
    "Onore": NEOTwewyItemData(10703, NEOTwewyItemType.Costume, ItemClassification.filler, [], "IL CAVALLO DEL RE"),
    "Tradizione": NEOTwewyItemData(10704, NEOTwewyItemType.Costume, ItemClassification.filler, [], "IL CAVALLO DEL RE"),
    "Rispetto": NEOTwewyItemData(10705, NEOTwewyItemType.Costume, ItemClassification.filler, [], "IL CAVALLO DEL RE"),
    "Innovazione": NEOTwewyItemData(
        10706, NEOTwewyItemType.Costume, ItemClassification.filler, [], "IL CAVALLO DEL RE"
    ),
    "Inimitabile": NEOTwewyItemData(
        10707, NEOTwewyItemType.Costume, ItemClassification.filler, [], "IL CAVALLO DEL RE"
    ),
    "Notte romantica": NEOTwewyItemData(
        10708, NEOTwewyItemType.Costume, ItemClassification.filler, [], "IL CAVALLO DEL RE"
    ),
    "Futuro": NEOTwewyItemData(10709, NEOTwewyItemType.Costume, ItemClassification.filler, [], "IL CAVALLO DEL RE"),
    "Infinito": NEOTwewyItemData(10710, NEOTwewyItemType.Costume, ItemClassification.filler, [], "IL CAVALLO DEL RE"),
    "Sentiero": NEOTwewyItemData(10711, NEOTwewyItemType.Costume, ItemClassification.filler, [], "IL CAVALLO DEL RE"),
    "Vacanza": NEOTwewyItemData(10712, NEOTwewyItemType.Costume, ItemClassification.filler, [], "IL CAVALLO DEL RE"),
    "Denaro e potere": NEOTwewyItemData(
        10713, NEOTwewyItemType.Costume, ItemClassification.filler, [], "IL CAVALLO DEL RE"
    ),
    "Amore e desiderio": NEOTwewyItemData(
        10714, NEOTwewyItemType.Costume, ItemClassification.filler, [], "IL CAVALLO DEL RE"
    ),
    "Pigliatutto": NEOTwewyItemData(
        10715, NEOTwewyItemType.Costume, ItemClassification.filler, [], "IL CAVALLO DEL RE"
    ),
    "Fiore di cristallo": NEOTwewyItemData(
        10716, NEOTwewyItemType.Costume, ItemClassification.filler, [], "IL CAVALLO DEL RE"
    ),
    "Bucket Hat": NEOTwewyItemData(10800, NEOTwewyItemType.Costume, ItemClassification.filler, [], "Shepherd House"),
    "Hair Brooch": NEOTwewyItemData(10801, NEOTwewyItemType.Costume, ItemClassification.filler, [], "Shepherd House"),
    "Sheepy T-Shirt": NEOTwewyItemData(
        10802, NEOTwewyItemType.Costume, ItemClassification.filler, [], "Shepherd House"
    ),
    "Polo Shirt": NEOTwewyItemData(10803, NEOTwewyItemType.Costume, ItemClassification.filler, [], "Shepherd House"),
    "Turtleneck Sweater": NEOTwewyItemData(
        10804, NEOTwewyItemType.Costume, ItemClassification.filler, [], "Shepherd House"
    ),
    "White Shirt": NEOTwewyItemData(10805, NEOTwewyItemType.Costume, ItemClassification.filler, [], "Shepherd House"),
    "Down Jacket": NEOTwewyItemData(10806, NEOTwewyItemType.Costume, ItemClassification.filler, [], "Shepherd House"),
    "Chinos": NEOTwewyItemData(10807, NEOTwewyItemType.Costume, ItemClassification.filler, [], "Shepherd House"),
    "Corduroy Pants": NEOTwewyItemData(
        10808, NEOTwewyItemType.Costume, ItemClassification.filler, [], "Shepherd House"
    ),
    "Knee-Length Skirt": NEOTwewyItemData(
        10809, NEOTwewyItemType.Costume, ItemClassification.filler, [], "Shepherd House"
    ),
    "Wrap Skirt": NEOTwewyItemData(10810, NEOTwewyItemType.Costume, ItemClassification.filler, [], "Shepherd House"),
    "Shirt Dress": NEOTwewyItemData(10811, NEOTwewyItemType.Costume, ItemClassification.filler, [], "Shepherd House"),
    "Strapped Pumps": NEOTwewyItemData(
        10812, NEOTwewyItemType.Costume, ItemClassification.filler, [], "Shepherd House"
    ),
    "Slip-ons": NEOTwewyItemData(10813, NEOTwewyItemType.Costume, ItemClassification.filler, [], "Shepherd House"),
    "Formal Bag": NEOTwewyItemData(10814, NEOTwewyItemType.Costume, ItemClassification.filler, [], "Shepherd House"),
    "Wool Scarf": NEOTwewyItemData(10815, NEOTwewyItemType.Costume, ItemClassification.filler, [], "Shepherd House"),
    "Waterproof Hat": NEOTwewyItemData(
        10900, NEOTwewyItemType.Costume, ItemClassification.filler, [], "Jupiter of the Monkey"
    ),
    "Peacock Cap": NEOTwewyItemData(
        10901, NEOTwewyItemType.Costume, ItemClassification.filler, [], "Jupiter of the Monkey"
    ),
    "Bodhidharma Tank Top": NEOTwewyItemData(
        10902, NEOTwewyItemType.Costume, ItemClassification.filler, [], "Jupiter of the Monkey"
    ),
    "Varuna T-Shirt": NEOTwewyItemData(
        10903, NEOTwewyItemType.Costume, ItemClassification.filler, [], "Jupiter of the Monkey"
    ),
    "Amitabha Windbreaker": NEOTwewyItemData(
        10904, NEOTwewyItemType.Costume, ItemClassification.filler, [], "Jupiter of the Monkey"
    ),
    "Virupaksa Hoodie": NEOTwewyItemData(
        10905, NEOTwewyItemType.Costume, ItemClassification.filler, [], "Jupiter of the Monkey"
    ),
    "Maitreya Jersey": NEOTwewyItemData(
        10906, NEOTwewyItemType.Costume, ItemClassification.filler, [], "Jupiter of the Monkey"
    ),
    "Vaisravana Jacket": NEOTwewyItemData(
        10907, NEOTwewyItemType.Costume, ItemClassification.filler, [], "Jupiter of the Monkey"
    ),
    "Lightning Shorts": NEOTwewyItemData(
        10908, NEOTwewyItemType.Costume, ItemClassification.filler, [], "Jupiter of the Monkey"
    ),
    "Skanda Sweatpants": NEOTwewyItemData(
        10909, NEOTwewyItemType.Costume, ItemClassification.filler, [], "Jupiter of the Monkey"
    ),
    "Kumbhira Sweatpants": NEOTwewyItemData(
        10910, NEOTwewyItemType.Costume, ItemClassification.filler, [], "Jupiter of the Monkey"
    ),
    "Yama Sweatpants": NEOTwewyItemData(
        10911, NEOTwewyItemType.Costume, ItemClassification.filler, [], "Jupiter of the Monkey"
    ),
    "Om Sneakers": NEOTwewyItemData(
        10912, NEOTwewyItemType.Costume, ItemClassification.filler, [], "Jupiter of the Monkey"
    ),
    "Gekirin Sneakers": NEOTwewyItemData(
        10913, NEOTwewyItemType.Costume, ItemClassification.filler, [], "Jupiter of the Monkey"
    ),
    "Kshana Sneakers": NEOTwewyItemData(
        10914, NEOTwewyItemType.Costume, ItemClassification.filler, [], "Jupiter of the Monkey"
    ),
    "Samsara Sneakers": NEOTwewyItemData(
        10915, NEOTwewyItemType.Costume, ItemClassification.filler, [], "Jupiter of the Monkey"
    ),
    "Karma Shoulder Bag": NEOTwewyItemData(
        10916, NEOTwewyItemType.Costume, ItemClassification.filler, [], "Jupiter of the Monkey"
    ),
    "Naraka Rucksack": NEOTwewyItemData(
        10917, NEOTwewyItemType.Costume, ItemClassification.filler, [], "Jupiter of the Monkey"
    ),
    "Monochrome Cap": NEOTwewyItemData(11000, NEOTwewyItemType.Costume, ItemClassification.filler, [], "MONOCROW"),
    "Monochrome Beanie": NEOTwewyItemData(11001, NEOTwewyItemType.Costume, ItemClassification.filler, [], "MONOCROW"),
    "Monochrome T-Shirt": NEOTwewyItemData(11002, NEOTwewyItemType.Costume, ItemClassification.filler, [], "MONOCROW"),
    "Monochrome Jacket": NEOTwewyItemData(11003, NEOTwewyItemType.Costume, ItemClassification.filler, [], "MONOCROW"),
    "Monochrome Hoodie": NEOTwewyItemData(11004, NEOTwewyItemType.Costume, ItemClassification.filler, [], "MONOCROW"),
    "Criss Cross Tank Top": NEOTwewyItemData(
        11005, NEOTwewyItemType.Costume, ItemClassification.filler, [], "MONOCROW"
    ),
    "Sarouel Pants": NEOTwewyItemData(11006, NEOTwewyItemType.Costume, ItemClassification.filler, [], "MONOCROW"),
    "Monochrome Shorts": NEOTwewyItemData(11007, NEOTwewyItemType.Costume, ItemClassification.filler, [], "MONOCROW"),
    "Sporty Miniskirt": NEOTwewyItemData(11008, NEOTwewyItemType.Costume, ItemClassification.filler, [], "MONOCROW"),
    "Sporty Dress": NEOTwewyItemData(11009, NEOTwewyItemType.Costume, ItemClassification.filler, [], "MONOCROW"),
    "Leather Sneakers": NEOTwewyItemData(11010, NEOTwewyItemType.Costume, ItemClassification.filler, [], "MONOCROW"),
    "Sneaker Sandals": NEOTwewyItemData(11011, NEOTwewyItemType.Costume, ItemClassification.filler, [], "MONOCROW"),
    "Sneaker Boots": NEOTwewyItemData(11012, NEOTwewyItemType.Costume, ItemClassification.filler, [], "MONOCROW"),
    "Monochrome Watch": NEOTwewyItemData(11013, NEOTwewyItemType.Costume, ItemClassification.filler, [], "MONOCROW"),
    "Dog Tags": NEOTwewyItemData(11014, NEOTwewyItemType.Costume, ItemClassification.filler, [], "MONOCROW"),
    "Sling Bag": NEOTwewyItemData(11015, NEOTwewyItemType.Costume, ItemClassification.filler, [], "MONOCROW"),
    "Mask": NEOTwewyItemData(11016, NEOTwewyItemType.Costume, ItemClassification.filler, [], "MONOCROW"),
    "High-Class Hat": NEOTwewyItemData(11100, NEOTwewyItemType.Costume, ItemClassification.filler, [], "NATURAL PUPPY"),
    "Straw Hat": NEOTwewyItemData(11101, NEOTwewyItemType.Costume, ItemClassification.filler, [], "NATURAL PUPPY"),
    "Cute Camisole": NEOTwewyItemData(11102, NEOTwewyItemType.Costume, ItemClassification.filler, [], "NATURAL PUPPY"),
    "Crossover Cardigan": NEOTwewyItemData(
        11103, NEOTwewyItemType.Costume, ItemClassification.filler, [], "NATURAL PUPPY"
    ),
    "Chesterfield Coat": NEOTwewyItemData(
        11104, NEOTwewyItemType.Costume, ItemClassification.filler, [], "NATURAL PUPPY"
    ),
    "Tailored Jacket": NEOTwewyItemData(
        11105, NEOTwewyItemType.Costume, ItemClassification.filler, [], "NATURAL PUPPY"
    ),
    "Striped T-Shirt": NEOTwewyItemData(
        11106, NEOTwewyItemType.Costume, ItemClassification.filler, [], "NATURAL PUPPY"
    ),
    "Dandy Dress Shirt": NEOTwewyItemData(
        11107, NEOTwewyItemType.Costume, ItemClassification.filler, [], "NATURAL PUPPY"
    ),
    "White Jeans": NEOTwewyItemData(11108, NEOTwewyItemType.Costume, ItemClassification.filler, [], "NATURAL PUPPY"),
    "Flared Skirt": NEOTwewyItemData(11109, NEOTwewyItemType.Costume, ItemClassification.filler, [], "NATURAL PUPPY"),
    "Black Jeans": NEOTwewyItemData(11110, NEOTwewyItemType.Costume, ItemClassification.filler, [], "NATURAL PUPPY"),
    "Comfy Overalls": NEOTwewyItemData(11111, NEOTwewyItemType.Costume, ItemClassification.filler, [], "NATURAL PUPPY"),
    "Delightful Dress": NEOTwewyItemData(
        11112, NEOTwewyItemType.Costume, ItemClassification.filler, [], "NATURAL PUPPY"
    ),
    "Angelic Dress": NEOTwewyItemData(11113, NEOTwewyItemType.Costume, ItemClassification.filler, [], "NATURAL PUPPY"),
    "Lovely Dress": NEOTwewyItemData(11114, NEOTwewyItemType.Costume, ItemClassification.filler, [], "NATURAL PUPPY"),
    "Minimalistic Mules": NEOTwewyItemData(
        11115, NEOTwewyItemType.Costume, ItemClassification.filler, [], "NATURAL PUPPY"
    ),
    "PVC Pumps": NEOTwewyItemData(11116, NEOTwewyItemType.Costume, ItemClassification.filler, [], "NATURAL PUPPY"),
    "Chukka Boots": NEOTwewyItemData(11117, NEOTwewyItemType.Costume, ItemClassification.filler, [], "NATURAL PUPPY"),
    "Standard Tie": NEOTwewyItemData(11118, NEOTwewyItemType.Costume, ItemClassification.filler, [], "NATURAL PUPPY"),
    "Knit Tie": NEOTwewyItemData(11119, NEOTwewyItemType.Costume, ItemClassification.filler, [], "NATURAL PUPPY"),
    "Flat-Brim Snapback": NEOTwewyItemData(11200, NEOTwewyItemType.Costume, ItemClassification.filler, [], "HOG FANG"),
    "Baseball Cap": NEOTwewyItemData(11201, NEOTwewyItemType.Costume, ItemClassification.filler, [], "HOG FANG"),
    "Faux-Vintage Beanie": NEOTwewyItemData(11202, NEOTwewyItemType.Costume, ItemClassification.filler, [], "HOG FANG"),
    "Wired Hairband": NEOTwewyItemData(11203, NEOTwewyItemType.Costume, ItemClassification.filler, [], "HOG FANG"),
    "Down Vest": NEOTwewyItemData(11204, NEOTwewyItemType.Costume, ItemClassification.filler, [], "HOG FANG"),
    "Pullover Hoodie": NEOTwewyItemData(11205, NEOTwewyItemType.Costume, ItemClassification.filler, [], "HOG FANG"),
    "Printed T-Shirt": NEOTwewyItemData(11206, NEOTwewyItemType.Costume, ItemClassification.filler, [], "HOG FANG"),
    "Flannel Shirt": NEOTwewyItemData(11207, NEOTwewyItemType.Costume, ItemClassification.filler, [], "HOG FANG"),
    "M-1951 Field Jacket": NEOTwewyItemData(11208, NEOTwewyItemType.Costume, ItemClassification.filler, [], "HOG FANG"),
    "Faux-Vintage Jacket": NEOTwewyItemData(11209, NEOTwewyItemType.Costume, ItemClassification.filler, [], "HOG FANG"),
    "Cuffed Jeans": NEOTwewyItemData(11210, NEOTwewyItemType.Costume, ItemClassification.filler, [], "HOG FANG"),
    "Vintage Ripped Jeans": NEOTwewyItemData(
        11211, NEOTwewyItemType.Costume, ItemClassification.filler, [], "HOG FANG"
    ),
    "Camo Cargo Pants": NEOTwewyItemData(11212, NEOTwewyItemType.Costume, ItemClassification.filler, [], "HOG FANG"),
    "Tight Denim Skirt": NEOTwewyItemData(11213, NEOTwewyItemType.Costume, ItemClassification.filler, [], "HOG FANG"),
    "Denim Shirt Dress": NEOTwewyItemData(11214, NEOTwewyItemType.Costume, ItemClassification.filler, [], "HOG FANG"),
    "Work Boots": NEOTwewyItemData(11215, NEOTwewyItemType.Costume, ItemClassification.filler, [], "HOG FANG"),
    "High-top Sneakers": NEOTwewyItemData(11216, NEOTwewyItemType.Costume, ItemClassification.filler, [], "HOG FANG"),
    "Low-top Sneakers": NEOTwewyItemData(11217, NEOTwewyItemType.Costume, ItemClassification.filler, [], "HOG FANG"),
    "Patched-up Sneakers": NEOTwewyItemData(11218, NEOTwewyItemType.Costume, ItemClassification.filler, [], "HOG FANG"),
    "Chain Necklace": NEOTwewyItemData(11219, NEOTwewyItemType.Costume, ItemClassification.filler, [], "HOG FANG"),
    "Wallet Chain": NEOTwewyItemData(11220, NEOTwewyItemType.Costume, ItemClassification.filler, [], "HOG FANG"),
    "Sunglasses": NEOTwewyItemData(11221, NEOTwewyItemType.Costume, ItemClassification.filler, [], "HOG FANG"),
    "Retroesque Boom Box": NEOTwewyItemData(11222, NEOTwewyItemType.Costume, ItemClassification.filler, [], "HOG FANG"),
    "Denim Cap": NEOTwewyItemData(11300, NEOTwewyItemType.Costume, ItemClassification.filler, [], "Gatto Nero"),
    "Beret": NEOTwewyItemData(11301, NEOTwewyItemType.Costume, ItemClassification.filler, [], "Gatto Nero"),
    "Buckle Sleeve Shirt": NEOTwewyItemData(
        11302, NEOTwewyItemType.Costume, ItemClassification.filler, [], "Gatto Nero"
    ),
    "Zippered Shirt": NEOTwewyItemData(11303, NEOTwewyItemType.Costume, ItemClassification.filler, [], "Gatto Nero"),
    "Off-the-Shoulder Top": NEOTwewyItemData(
        11304, NEOTwewyItemType.Costume, ItemClassification.filler, [], "Gatto Nero"
    ),
    "Shirt Jacket": NEOTwewyItemData(11305, NEOTwewyItemType.Costume, ItemClassification.filler, [], "Gatto Nero"),
    "Denim Micro-Miniskirt": NEOTwewyItemData(
        11306, NEOTwewyItemType.Costume, ItemClassification.filler, [], "Gatto Nero"
    ),
    "Asymmetrical Miniskirt": NEOTwewyItemData(
        11307, NEOTwewyItemType.Costume, ItemClassification.filler, [], "Gatto Nero"
    ),
    "Frayed Cargo Pants": NEOTwewyItemData(
        11308, NEOTwewyItemType.Costume, ItemClassification.filler, [], "Gatto Nero"
    ),
    "Asymmetrical Jeans": NEOTwewyItemData(
        11309, NEOTwewyItemType.Costume, ItemClassification.filler, [], "Gatto Nero"
    ),
    "Bell-Sleeved Two-Piece": NEOTwewyItemData(
        11310, NEOTwewyItemType.Costume, ItemClassification.filler, [], "Gatto Nero"
    ),
    "Jumpsuit": NEOTwewyItemData(11311, NEOTwewyItemType.Costume, ItemClassification.filler, [], "Gatto Nero"),
    "Ankle Boots": NEOTwewyItemData(11312, NEOTwewyItemType.Costume, ItemClassification.filler, [], "Gatto Nero"),
    "Mid-Calf Boots": NEOTwewyItemData(11313, NEOTwewyItemType.Costume, ItemClassification.filler, [], "Gatto Nero"),
    "Fishnet Socks": NEOTwewyItemData(11314, NEOTwewyItemType.Costume, ItemClassification.filler, [], "Gatto Nero"),
    "Hip Pack": NEOTwewyItemData(11315, NEOTwewyItemType.Costume, ItemClassification.filler, [], "Gatto Nero"),
    "Mr. Mew Hoodie": NEOTwewyItemData(11316, NEOTwewyItemType.Costume, ItemClassification.filler, [], "Gatto Nero"),
    "Mr. Mew Phone Case": NEOTwewyItemData(
        11317, NEOTwewyItemType.Costume, ItemClassification.filler, [], "Gatto Nero"
    ),
    "Mr. Mew Pouch": NEOTwewyItemData(11318, NEOTwewyItemType.Costume, ItemClassification.filler, [], "Gatto Nero"),
    "Rainbow Afro Wig": NEOTwewyItemData(
        11400, NEOTwewyItemType.Costume, ItemClassification.filler, [], "croaky panic"
    ),
    "Samurai Wig": NEOTwewyItemData(11401, NEOTwewyItemType.Costume, ItemClassification.filler, [], "croaky panic"),
    "Bunny Maid Hairband": NEOTwewyItemData(
        11402, NEOTwewyItemType.Costume, ItemClassification.filler, [], "croaky panic"
    ),
    "Space Kitty T-Shirt": NEOTwewyItemData(
        11403, NEOTwewyItemType.Costume, ItemClassification.filler, [], "croaky panic"
    ),
    "Christmassy Coat": NEOTwewyItemData(
        11404, NEOTwewyItemType.Costume, ItemClassification.filler, [], "croaky panic"
    ),
    "Ribbit Rubber Ring": NEOTwewyItemData(
        11405, NEOTwewyItemType.Costume, ItemClassification.filler, [], "croaky panic"
    ),
    "Christmassy Pants": NEOTwewyItemData(
        11406, NEOTwewyItemType.Costume, ItemClassification.filler, [], "croaky panic"
    ),
    "Maid Costume": NEOTwewyItemData(11407, NEOTwewyItemType.Costume, ItemClassification.filler, [], "croaky panic"),
    "Ninja Costume": NEOTwewyItemData(11408, NEOTwewyItemType.Costume, ItemClassification.filler, [], "croaky panic"),
    "Stilts": NEOTwewyItemData(11409, NEOTwewyItemType.Costume, ItemClassification.filler, [], "croaky panic"),
    "Roller Skates": NEOTwewyItemData(11410, NEOTwewyItemType.Costume, ItemClassification.filler, [], "croaky panic"),
    "Half-Hearted Summer Gift": NEOTwewyItemData(
        11411, NEOTwewyItemType.Costume, ItemClassification.filler, [], "croaky panic"
    ),
    "Schnoz Spectacles": NEOTwewyItemData(
        11412, NEOTwewyItemType.Costume, ItemClassification.filler, [], "croaky panic"
    ),
    "Tomonami's Blade": NEOTwewyItemData(
        11413, NEOTwewyItemType.Costume, ItemClassification.filler, [], "croaky panic"
    ),
    "B.H.C.C Panama Hat": NEOTwewyItemData(
        11500, NEOTwewyItemType.Costume, ItemClassification.filler, [], "BLACK HONEY CHILI COOKIE"
    ),
    "B.H.C.C Baseball Cap": NEOTwewyItemData(
        11501, NEOTwewyItemType.Costume, ItemClassification.filler, [], "BLACK HONEY CHILI COOKIE"
    ),
    "B.H.C.C T-Shirt": NEOTwewyItemData(
        11502, NEOTwewyItemType.Costume, ItemClassification.filler, [], "BLACK HONEY CHILI COOKIE"
    ),
    "B.H.C.C Biker Jacket": NEOTwewyItemData(
        11503, NEOTwewyItemType.Costume, ItemClassification.filler, [], "BLACK HONEY CHILI COOKIE"
    ),
    "B.H.C.C Leather Pants": NEOTwewyItemData(
        11504, NEOTwewyItemType.Costume, ItemClassification.filler, [], "BLACK HONEY CHILI COOKIE"
    ),
    "B.H.C.C Shorts": NEOTwewyItemData(
        11505, NEOTwewyItemType.Costume, ItemClassification.filler, [], "BLACK HONEY CHILI COOKIE"
    ),
    "B.H.C.C Shoes": NEOTwewyItemData(
        11506, NEOTwewyItemType.Costume, ItemClassification.filler, [], "BLACK HONEY CHILI COOKIE"
    ),
    "B.H.C.C Side Gore Boots": NEOTwewyItemData(
        11507, NEOTwewyItemType.Costume, ItemClassification.filler, [], "BLACK HONEY CHILI COOKIE"
    ),
    "B.H.C.C Tote Bag": NEOTwewyItemData(
        11508, NEOTwewyItemType.Costume, ItemClassification.filler, [], "BLACK HONEY CHILI COOKIE"
    ),
    "FP": NEOTwewyItemData(30000, NEOTwewyItemType.Valuable, ItemClassification.filler, [], "Unbranded"),
    "Secret Report No. 1": NEOTwewyItemData(
        31000, NEOTwewyItemType.Book, ItemClassification.progression, [NEOTwewyItemGroup.SECRET_REPORT], "Unbranded"
    ),
    "Secret Report No. 2": NEOTwewyItemData(
        31001, NEOTwewyItemType.Book, ItemClassification.progression, [NEOTwewyItemGroup.SECRET_REPORT], "Unbranded"
    ),
    "Secret Report No. 3": NEOTwewyItemData(
        31002, NEOTwewyItemType.Book, ItemClassification.progression, [NEOTwewyItemGroup.SECRET_REPORT], "Unbranded"
    ),
    "Secret Report No. 4": NEOTwewyItemData(
        31003, NEOTwewyItemType.Book, ItemClassification.progression, [NEOTwewyItemGroup.SECRET_REPORT], "Unbranded"
    ),
    "Secret Report No. 5": NEOTwewyItemData(
        31004, NEOTwewyItemType.Book, ItemClassification.progression, [NEOTwewyItemGroup.SECRET_REPORT], "Unbranded"
    ),
    "Secret Report No. 6": NEOTwewyItemData(
        31005, NEOTwewyItemType.Book, ItemClassification.progression, [NEOTwewyItemGroup.SECRET_REPORT], "Unbranded"
    ),
    "Secret Report No. 7": NEOTwewyItemData(
        31006, NEOTwewyItemType.Book, ItemClassification.progression, [NEOTwewyItemGroup.SECRET_REPORT], "Unbranded"
    ),
    "Secret Report No. 8": NEOTwewyItemData(
        31007, NEOTwewyItemType.Book, ItemClassification.progression, [NEOTwewyItemGroup.SECRET_REPORT], "Unbranded"
    ),
    "Secret Report No. 9": NEOTwewyItemData(
        31008, NEOTwewyItemType.Book, ItemClassification.progression, [NEOTwewyItemGroup.SECRET_REPORT], "Unbranded"
    ),
    "Secret Report No. 10": NEOTwewyItemData(
        31009, NEOTwewyItemType.Book, ItemClassification.progression, [NEOTwewyItemGroup.SECRET_REPORT], "Unbranded"
    ),
    "Secret Report No. 11": NEOTwewyItemData(
        31010, NEOTwewyItemType.Book, ItemClassification.progression, [NEOTwewyItemGroup.SECRET_REPORT], "Unbranded"
    ),
    "Secret Report No. 12": NEOTwewyItemData(
        31011, NEOTwewyItemType.Book, ItemClassification.progression, [NEOTwewyItemGroup.SECRET_REPORT], "Unbranded"
    ),
    "Secret Report No. 13": NEOTwewyItemData(
        31012, NEOTwewyItemType.Book, ItemClassification.progression, [NEOTwewyItemGroup.SECRET_REPORT], "Unbranded"
    ),
    "Secret Report No. 14": NEOTwewyItemData(
        31013, NEOTwewyItemType.Book, ItemClassification.progression, [NEOTwewyItemGroup.SECRET_REPORT], "Unbranded"
    ),
    "Secret Report No. 15": NEOTwewyItemData(
        31014, NEOTwewyItemType.Book, ItemClassification.progression, [NEOTwewyItemGroup.SECRET_REPORT], "Unbranded"
    ),
    "Secret Report No. 16": NEOTwewyItemData(
        31015, NEOTwewyItemType.Book, ItemClassification.progression, [NEOTwewyItemGroup.SECRET_REPORT], "Unbranded"
    ),
    "Secret Report No. 17": NEOTwewyItemData(
        31016, NEOTwewyItemType.Book, ItemClassification.progression, [NEOTwewyItemGroup.SECRET_REPORT], "Unbranded"
    ),
    "Secret Report No. 18": NEOTwewyItemData(
        31017, NEOTwewyItemType.Book, ItemClassification.progression, [NEOTwewyItemGroup.SECRET_REPORT], "Unbranded"
    ),
    "Secret Report No. 19": NEOTwewyItemData(
        31018, NEOTwewyItemType.Book, ItemClassification.progression, [NEOTwewyItemGroup.SECRET_REPORT], "Unbranded"
    ),
    "Secret Report No. 20": NEOTwewyItemData(
        31019, NEOTwewyItemType.Book, ItemClassification.progression, [NEOTwewyItemGroup.SECRET_REPORT], "Unbranded"
    ),
    "Secret Report No. 21": NEOTwewyItemData(
        31020, NEOTwewyItemType.Book, ItemClassification.progression, [NEOTwewyItemGroup.SECRET_REPORT], "Unbranded"
    ),
    "Secret Report No. 22": NEOTwewyItemData(
        31021, NEOTwewyItemType.Book, ItemClassification.progression, [NEOTwewyItemGroup.SECRET_REPORT], "Unbranded"
    ),
    "Secret Report No. 23": NEOTwewyItemData(
        31022, NEOTwewyItemType.Book, ItemClassification.progression, [NEOTwewyItemGroup.SECRET_REPORT], "Unbranded"
    ),
    "Secret Report No. 24": NEOTwewyItemData(
        31023, NEOTwewyItemType.Book, ItemClassification.progression, [NEOTwewyItemGroup.SECRET_REPORT], "Unbranded"
    ),
    "Tips & Tricks Vol. 1": NEOTwewyItemData(31100, NEOTwewyItemType.Book, ItemClassification.filler, [], "Unbranded"),
    "Tips & Tricks Vol. 2": NEOTwewyItemData(31101, NEOTwewyItemType.Book, ItemClassification.filler, [], "Unbranded"),
    "Tips & Tricks Vol. 3": NEOTwewyItemData(31102, NEOTwewyItemType.Book, ItemClassification.filler, [], "Unbranded"),
    "Tips & Tricks Vol. 4": NEOTwewyItemData(31103, NEOTwewyItemType.Book, ItemClassification.filler, [], "Unbranded"),
    "Tips & Tricks Vol. 5": NEOTwewyItemData(31104, NEOTwewyItemType.Book, ItemClassification.filler, [], "Unbranded"),
    "Tips & Tricks Vol. 6": NEOTwewyItemData(31105, NEOTwewyItemType.Book, ItemClassification.filler, [], "Unbranded"),
    "Tips & Tricks Vol. 7": NEOTwewyItemData(31106, NEOTwewyItemType.Book, ItemClassification.filler, [], "Unbranded"),
    "Tips & Tricks Vol. 8": NEOTwewyItemData(31107, NEOTwewyItemType.Book, ItemClassification.filler, [], "Unbranded"),
    "Tips & Tricks Vol. 9": NEOTwewyItemData(31108, NEOTwewyItemType.Book, ItemClassification.filler, [], "Unbranded"),
    "Tips & Tricks Vol. 10": NEOTwewyItemData(31109, NEOTwewyItemType.Book, ItemClassification.filler, [], "Unbranded"),
    "Tips & Tricks Vol. 11": NEOTwewyItemData(31110, NEOTwewyItemType.Book, ItemClassification.filler, [], "Unbranded"),
    "Tips & Tricks Vol. 12": NEOTwewyItemData(31111, NEOTwewyItemType.Book, ItemClassification.filler, [], "Unbranded"),
    "Tips & Tricks Vol. 13": NEOTwewyItemData(31112, NEOTwewyItemType.Book, ItemClassification.filler, [], "Unbranded"),
    "Tips & Tricks Vol. 14": NEOTwewyItemData(31113, NEOTwewyItemType.Book, ItemClassification.filler, [], "Unbranded"),
    "Tips & Tricks Vol. 15": NEOTwewyItemData(31114, NEOTwewyItemType.Book, ItemClassification.filler, [], "Unbranded"),
    "Tips & Tricks Vol. 16": NEOTwewyItemData(31115, NEOTwewyItemType.Book, ItemClassification.filler, [], "Unbranded"),
    "Tips & Tricks Vol. 17": NEOTwewyItemData(31116, NEOTwewyItemType.Book, ItemClassification.filler, [], "Unbranded"),
    "Tips & Tricks Vol. 18": NEOTwewyItemData(31117, NEOTwewyItemType.Book, ItemClassification.filler, [], "Unbranded"),
    "Tips & Tricks Vol. 19": NEOTwewyItemData(31118, NEOTwewyItemType.Book, ItemClassification.filler, [], "Unbranded"),
    "Tips & Tricks Vol. 20": NEOTwewyItemData(31119, NEOTwewyItemType.Book, ItemClassification.filler, [], "Unbranded"),
    "Tips & Tricks Vol. 21": NEOTwewyItemData(31120, NEOTwewyItemType.Book, ItemClassification.filler, [], "Unbranded"),
    "Tips & Tricks Vol. 22": NEOTwewyItemData(31121, NEOTwewyItemType.Book, ItemClassification.filler, [], "Unbranded"),
    "Tips & Tricks Vol. 23": NEOTwewyItemData(31122, NEOTwewyItemType.Book, ItemClassification.filler, [], "Unbranded"),
    "Tips & Tricks Vol. 24": NEOTwewyItemData(31123, NEOTwewyItemType.Book, ItemClassification.filler, [], "Unbranded"),
    "Tips & Tricks Vol. 25": NEOTwewyItemData(31124, NEOTwewyItemType.Book, ItemClassification.filler, [], "Unbranded"),
    "Tips & Tricks Vol. 26": NEOTwewyItemData(31125, NEOTwewyItemType.Book, ItemClassification.filler, [], "Unbranded"),
    "Tips & Tricks Vol. 27": NEOTwewyItemData(31126, NEOTwewyItemType.Book, ItemClassification.filler, [], "Unbranded"),
    "Tips & Tricks Vol. 28": NEOTwewyItemData(31127, NEOTwewyItemType.Book, ItemClassification.filler, [], "Unbranded"),
    "Tips & Tricks Vol. 29": NEOTwewyItemData(31128, NEOTwewyItemType.Book, ItemClassification.filler, [], "Unbranded"),
    "Tips & Tricks Vol. 30": NEOTwewyItemData(31129, NEOTwewyItemType.Book, ItemClassification.filler, [], "Unbranded"),
    "Tips & Tricks Vol. 31": NEOTwewyItemData(31130, NEOTwewyItemType.Book, ItemClassification.filler, [], "Unbranded"),
    "Tips & Tricks Vol. 32": NEOTwewyItemData(31131, NEOTwewyItemType.Book, ItemClassification.filler, [], "Unbranded"),
    "Tips & Tricks Vol. 33": NEOTwewyItemData(31132, NEOTwewyItemType.Book, ItemClassification.filler, [], "Unbranded"),
    "Tips & Tricks Vol. 34": NEOTwewyItemData(31133, NEOTwewyItemType.Book, ItemClassification.filler, [], "Unbranded"),
    "Tips & Tricks Vol. 35": NEOTwewyItemData(31134, NEOTwewyItemType.Book, ItemClassification.filler, [], "Unbranded"),
    "Tips & Tricks Vol. 36": NEOTwewyItemData(31135, NEOTwewyItemType.Book, ItemClassification.filler, [], "Unbranded"),
    "Tips & Tricks Vol. 37": NEOTwewyItemData(31136, NEOTwewyItemType.Book, ItemClassification.filler, [], "Unbranded"),
    "Tips & Tricks Vol. 38": NEOTwewyItemData(31137, NEOTwewyItemType.Book, ItemClassification.filler, [], "Unbranded"),
    "Tips & Tricks Vol. 39": NEOTwewyItemData(31138, NEOTwewyItemType.Book, ItemClassification.filler, [], "Unbranded"),
    "Tips & Tricks Vol. 40": NEOTwewyItemData(31139, NEOTwewyItemType.Book, ItemClassification.filler, [], "Unbranded"),
    "Fighting as a Team": NEOTwewyItemData(31200, NEOTwewyItemType.Book, ItemClassification.filler, [], "Unbranded"),
    "Combos": NEOTwewyItemData(31201, NEOTwewyItemType.Book, ItemClassification.filler, [], "Unbranded"),
    "Dodging": NEOTwewyItemData(31202, NEOTwewyItemType.Book, ItemClassification.filler, [], "Unbranded"),
    "Noise Counterattacks": NEOTwewyItemData(31203, NEOTwewyItemType.Book, ItemClassification.filler, [], "Unbranded"),
    "Elemental Affinities": NEOTwewyItemData(31204, NEOTwewyItemType.Book, ItemClassification.filler, [], "Unbranded"),
    "Status Ailments": NEOTwewyItemData(31205, NEOTwewyItemType.Book, ItemClassification.filler, [], "Unbranded"),
    "Experience Points": NEOTwewyItemData(31206, NEOTwewyItemType.Book, ItemClassification.filler, [], "Unbranded"),
    "Killing It in Combat": NEOTwewyItemData(31207, NEOTwewyItemType.Book, ItemClassification.filler, [], "Unbranded"),
    "Powered-Up Mashups": NEOTwewyItemData(31208, NEOTwewyItemType.Book, ItemClassification.filler, [], "Unbranded"),
    "Killer Remixes": NEOTwewyItemData(31209, NEOTwewyItemType.Book, ItemClassification.filler, [], "Unbranded"),
    "Picking Up Pins": NEOTwewyItemData(31211, NEOTwewyItemType.Book, ItemClassification.filler, [], "Unbranded"),
    "Evolving Pins": NEOTwewyItemData(31212, NEOTwewyItemType.Book, ItemClassification.filler, [], "Unbranded"),
    "Pin Ensembles": NEOTwewyItemData(31213, NEOTwewyItemType.Book, ItemClassification.filler, [], "Unbranded"),
    "Uber Pins": NEOTwewyItemData(31214, NEOTwewyItemType.Book, ItemClassification.filler, [], "Unbranded"),
    "Collecting Pins": NEOTwewyItemData(31215, NEOTwewyItemType.Book, ItemClassification.filler, [], "Unbranded"),
    "Pin Decks": NEOTwewyItemData(31216, NEOTwewyItemType.Book, ItemClassification.filler, [], "Unbranded"),
    "Scanning": NEOTwewyItemData(31217, NEOTwewyItemType.Book, ItemClassification.filler, [], "Unbranded"),
    "Noise Symbols": NEOTwewyItemData(31218, NEOTwewyItemType.Book, ItemClassification.filler, [], "Unbranded"),
    "Chaining Battles": NEOTwewyItemData(31219, NEOTwewyItemType.Book, ItemClassification.filler, [], "Unbranded"),
    "Red Noise Symbols": NEOTwewyItemData(31220, NEOTwewyItemType.Book, ItemClassification.filler, [], "Unbranded"),
    "Blue Noise Symbols": NEOTwewyItemData(31221, NEOTwewyItemType.Book, ItemClassification.filler, [], "Unbranded"),
    "Pink Noise Symbols": NEOTwewyItemData(31222, NEOTwewyItemType.Book, ItemClassification.filler, [], "Unbranded"),
    "Fighting Pig Noise": NEOTwewyItemData(31223, NEOTwewyItemType.Book, ItemClassification.filler, [], "Unbranded"),
    "Pale Noise Symbols": NEOTwewyItemData(31224, NEOTwewyItemType.Book, ItemClassification.filler, [], "Unbranded"),
    "Orange Noise Symbols": NEOTwewyItemData(31225, NEOTwewyItemType.Book, ItemClassification.filler, [], "Unbranded"),
    "Farming FP": NEOTwewyItemData(31226, NEOTwewyItemType.Book, ItemClassification.filler, [], "Unbranded"),
    "Emotion Noise: Enraged": NEOTwewyItemData(
        31227, NEOTwewyItemType.Book, ItemClassification.filler, [], "Unbranded"
    ),
    "Emotion Noise: Somber": NEOTwewyItemData(31228, NEOTwewyItemType.Book, ItemClassification.filler, [], "Unbranded"),
    "Emotion Noise: Serene": NEOTwewyItemData(31229, NEOTwewyItemType.Book, ItemClassification.filler, [], "Unbranded"),
    "Emotion Noise: Fearful": NEOTwewyItemData(
        31230, NEOTwewyItemType.Book, ItemClassification.filler, [], "Unbranded"
    ),
    "ShibuPay": NEOTwewyItemData(31231, NEOTwewyItemType.Book, ItemClassification.filler, [], "Unbranded"),
    "Abilities": NEOTwewyItemData(31232, NEOTwewyItemType.Book, ItemClassification.filler, [], "Unbranded"),
    "Style": NEOTwewyItemData(31233, NEOTwewyItemType.Book, ItemClassification.filler, [], "Unbranded"),
    "Shop Quests": NEOTwewyItemData(31234, NEOTwewyItemType.Book, ItemClassification.filler, [], "Unbranded"),
    "Becoming a Regular": NEOTwewyItemData(31235, NEOTwewyItemType.Book, ItemClassification.filler, [], "Unbranded"),
    "Dining Out": NEOTwewyItemData(31236, NEOTwewyItemType.Book, ItemClassification.filler, [], "Unbranded"),
    "Favorite Foods": NEOTwewyItemData(31237, NEOTwewyItemType.Book, ItemClassification.filler, [], "Unbranded"),
    "Udagawa Graffiti Wall": NEOTwewyItemData(31238, NEOTwewyItemType.Book, ItemClassification.filler, [], "Unbranded"),
    "Scramble Slams": NEOTwewyItemData(31239, NEOTwewyItemType.Book, ItemClassification.filler, [], "Unbranded"),
    "Mental Notes": NEOTwewyItemData(31240, NEOTwewyItemType.Book, ItemClassification.filler, [], "Unbranded"),
    "Social Network Skills": NEOTwewyItemData(31241, NEOTwewyItemType.Book, ItemClassification.filler, [], "Unbranded"),
    "Side Quests": NEOTwewyItemData(31242, NEOTwewyItemType.Book, ItemClassification.filler, [], "Unbranded"),
    "Chapter Select": NEOTwewyItemData(31243, NEOTwewyItemType.Book, ItemClassification.filler, [], "Unbranded"),
    "(CD) Track 1": NEOTwewyItemData(32000, NEOTwewyItemType.Music, ItemClassification.filler, [], "Unbranded"),
    "(CD) Track 11": NEOTwewyItemData(32001, NEOTwewyItemType.Music, ItemClassification.filler, [], "Unbranded"),
    "(CD) Track 5": NEOTwewyItemData(32002, NEOTwewyItemType.Music, ItemClassification.filler, [], "Unbranded"),
    "(CD) Track 8": NEOTwewyItemData(32003, NEOTwewyItemType.Music, ItemClassification.filler, [], "Unbranded"),
    "(CD) Track 12": NEOTwewyItemData(32004, NEOTwewyItemType.Music, ItemClassification.filler, [], "Unbranded"),
    "(CD) Track 9": NEOTwewyItemData(32005, NEOTwewyItemType.Music, ItemClassification.filler, [], "Unbranded"),
    "(CD) Track 15": NEOTwewyItemData(32006, NEOTwewyItemType.Music, ItemClassification.filler, [], "Unbranded"),
    "(CD) Track 6": NEOTwewyItemData(32007, NEOTwewyItemType.Music, ItemClassification.filler, [], "Unbranded"),
    "(CD) Track 18": NEOTwewyItemData(32008, NEOTwewyItemType.Music, ItemClassification.filler, [], "Unbranded"),
    "(CD) Track 10": NEOTwewyItemData(32009, NEOTwewyItemType.Music, ItemClassification.filler, [], "Unbranded"),
    "(CD) Track 19": NEOTwewyItemData(32010, NEOTwewyItemType.Music, ItemClassification.filler, [], "Unbranded"),
    "(CD) Track 16": NEOTwewyItemData(32011, NEOTwewyItemType.Music, ItemClassification.filler, [], "Unbranded"),
    "(CD) Track 14": NEOTwewyItemData(32012, NEOTwewyItemType.Music, ItemClassification.filler, [], "Unbranded"),
    "(CD) Track 17": NEOTwewyItemData(32013, NEOTwewyItemType.Music, ItemClassification.filler, [], "Unbranded"),
    "(CD) Track 4": NEOTwewyItemData(32014, NEOTwewyItemType.Music, ItemClassification.filler, [], "Unbranded"),
    "(CD) Track 3": NEOTwewyItemData(32015, NEOTwewyItemType.Music, ItemClassification.filler, [], "Unbranded"),
    "(CD) Track 13": NEOTwewyItemData(32016, NEOTwewyItemType.Music, ItemClassification.filler, [], "Unbranded"),
    "(CD) Track 7": NEOTwewyItemData(32017, NEOTwewyItemType.Music, ItemClassification.filler, [], "Unbranded"),
    "(CD) Track 21": NEOTwewyItemData(32018, NEOTwewyItemType.Music, ItemClassification.filler, [], "Unbranded"),
    "(CD) Track 20": NEOTwewyItemData(32019, NEOTwewyItemType.Music, ItemClassification.filler, [], "Unbranded"),
    "(CD) Track 29": NEOTwewyItemData(32020, NEOTwewyItemType.Music, ItemClassification.filler, [], "Unbranded"),
    "(CD) Track 2": NEOTwewyItemData(32021, NEOTwewyItemType.Music, ItemClassification.filler, [], "Unbranded"),
    "(CD) Track 30": NEOTwewyItemData(32022, NEOTwewyItemType.Music, ItemClassification.filler, [], "Unbranded"),
    "(CD) Track 22": NEOTwewyItemData(32023, NEOTwewyItemType.Music, ItemClassification.filler, [], "Unbranded"),
    "(CD) Track 23": NEOTwewyItemData(32024, NEOTwewyItemType.Music, ItemClassification.filler, [], "Unbranded"),
    "(CD) Track 24": NEOTwewyItemData(32025, NEOTwewyItemType.Music, ItemClassification.filler, [], "Unbranded"),
    "(CD) Track 25": NEOTwewyItemData(32026, NEOTwewyItemType.Music, ItemClassification.filler, [], "Unbranded"),
    "(CD) Track 26": NEOTwewyItemData(32027, NEOTwewyItemType.Music, ItemClassification.filler, [], "Unbranded"),
    "(CD) Track 27": NEOTwewyItemData(32028, NEOTwewyItemType.Music, ItemClassification.filler, [], "Unbranded"),
    "(CD) Track 28": NEOTwewyItemData(32029, NEOTwewyItemType.Music, ItemClassification.filler, [], "Unbranded"),
    "(CD) Track 48": NEOTwewyItemData(32030, NEOTwewyItemType.Music, ItemClassification.filler, [], "Unbranded"),
    "(CD) Track 44": NEOTwewyItemData(32031, NEOTwewyItemType.Music, ItemClassification.filler, [], "Unbranded"),
    "(CD) Track 38": NEOTwewyItemData(32032, NEOTwewyItemType.Music, ItemClassification.filler, [], "Unbranded"),
    "(CD) Track 47": NEOTwewyItemData(32033, NEOTwewyItemType.Music, ItemClassification.filler, [], "Unbranded"),
    "(CD) Track 43": NEOTwewyItemData(32034, NEOTwewyItemType.Music, ItemClassification.filler, [], "Unbranded"),
    "(CD) Track 36": NEOTwewyItemData(32035, NEOTwewyItemType.Music, ItemClassification.filler, [], "Unbranded"),
    "(CD) Track 45": NEOTwewyItemData(32036, NEOTwewyItemType.Music, ItemClassification.filler, [], "Unbranded"),
    "(CD) Track 34": NEOTwewyItemData(32037, NEOTwewyItemType.Music, ItemClassification.filler, [], "Unbranded"),
    "(CD) Track 40": NEOTwewyItemData(32038, NEOTwewyItemType.Music, ItemClassification.filler, [], "Unbranded"),
    "(CD) Track 46": NEOTwewyItemData(32039, NEOTwewyItemType.Music, ItemClassification.filler, [], "Unbranded"),
    "(CD) Track 41": NEOTwewyItemData(32040, NEOTwewyItemType.Music, ItemClassification.filler, [], "Unbranded"),
    "(CD) Track 49": NEOTwewyItemData(32041, NEOTwewyItemType.Music, ItemClassification.filler, [], "Unbranded"),
    "(CD) Track 37": NEOTwewyItemData(32042, NEOTwewyItemType.Music, ItemClassification.filler, [], "Unbranded"),
    "(CD) Track 39": NEOTwewyItemData(32043, NEOTwewyItemType.Music, ItemClassification.filler, [], "Unbranded"),
    "(CD) Track 33": NEOTwewyItemData(32044, NEOTwewyItemType.Music, ItemClassification.filler, [], "Unbranded"),
    "(CD) Track 32": NEOTwewyItemData(32045, NEOTwewyItemType.Music, ItemClassification.filler, [], "Unbranded"),
    "(CD) Track 50": NEOTwewyItemData(32046, NEOTwewyItemType.Music, ItemClassification.filler, [], "Unbranded"),
    "(CD) Track 35": NEOTwewyItemData(32047, NEOTwewyItemType.Music, ItemClassification.filler, [], "Unbranded"),
    "(CD) Track 42": NEOTwewyItemData(32048, NEOTwewyItemType.Music, ItemClassification.filler, [], "Unbranded"),
    "(CD) Track 51": NEOTwewyItemData(32049, NEOTwewyItemType.Music, ItemClassification.filler, [], "Unbranded"),
    "(CD) Track 31": NEOTwewyItemData(32050, NEOTwewyItemType.Music, ItemClassification.filler, [], "Unbranded"),
    "Item": NEOTwewyItemData(33000, NEOTwewyItemType.ItemMaterial, ItemClassification.filler, [], "Unbranded"),
    "5 FP": NEOTwewyItemData(33001, NEOTwewyItemType.Valuable, ItemClassification.filler, [], "Unbranded"),
    "3x Rare Metal": NEOTwewyItemData(
        33002, NEOTwewyItemType.Badge, ItemClassification.filler, [NEOTwewyItemGroup.RARE_METAL], "Unbranded"
    ),
    "3x Tektite": NEOTwewyItemData(
        33003, NEOTwewyItemType.Badge, ItemClassification.filler, [NEOTwewyItemGroup.RARE_METAL], "Unbranded"
    ),
}
