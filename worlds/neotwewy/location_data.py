from __future__ import annotations

from enum import Enum
from typing import NamedTuple


class NEOTwewyLocationType(Enum):
    ScenarioReward = 0
    Shop = 1


class NEOTwewyLocationData(NamedTuple):
    """Special data container to contain the metadata of each item to make filtering work."""

    id: int
    og_item: str

    region: str
    location_type: NEOTwewyLocationType

    combat_pin_only: bool

    add_to_game: bool
    option: str


SCENARIO_REWARDS: dict[str, NEOTwewyLocationData] = {
    "W1D1 - Minamimoto's Pin": NEOTwewyLocationData(
        110010, "Joli bécot", "W1D1", NEOTwewyLocationType.ScenarioReward, True, False, "minamimoto_pin"
    ),
    "W1D1 - Shibuya Hikarie": NEOTwewyLocationData(
        110020, "Firestorm", "W1D1", NEOTwewyLocationType.ScenarioReward, False, False, ""
    ),
    "W1D2 - 104/Dogenzaka": NEOTwewyLocationData(
        120010, "Sugar Beam", "W1D2", NEOTwewyLocationType.ScenarioReward, False, False, ""
    ),
    "W1D2 - Dogenzaka/O-EAST": NEOTwewyLocationData(
        120020, "Marvelous Crash", "W1D2", NEOTwewyLocationType.ScenarioReward, False, False, ""
    ),
    "W1D2 - TSUTAYA O-EAST": NEOTwewyLocationData(
        120030, "Azamaru", "W1D2", NEOTwewyLocationType.ScenarioReward, False, False, ""
    ),
    "W1D1 - Day Cleared": NEOTwewyLocationData(
        101, "Secret Report No. 1", "W1D1", NEOTwewyLocationType.ScenarioReward, False, True, ""
    ),
    "W1D2 - Day Cleared": NEOTwewyLocationData(
        102, "Secret Report No. 2", "W1D2", NEOTwewyLocationType.ScenarioReward, False, True, ""
    ),
    "W1D3 - Scramble/Center": NEOTwewyLocationData(
        130010, "5000 Yen", "W1D3", NEOTwewyLocationType.ScenarioReward, False, False, ""
    ),
    "W1D3 - Center Street": NEOTwewyLocationData(
        130020, "1000 Yen", "W1D3", NEOTwewyLocationType.ScenarioReward, False, False, ""
    ),
    "W1D3 - Scramble (10:50)": NEOTwewyLocationData(
        130030, "Tigre PUNKS", "W1D3", NEOTwewyLocationType.ScenarioReward, False, False, ""
    ),
    "W1D4 - Tipsy Tose Hall": NEOTwewyLocationData(
        140005, "5 FP", "W1D4", NEOTwewyLocationType.ScenarioReward, False, False, ""
    ),
    "W1D4 - Shinji-of-Some-Trades Dive": NEOTwewyLocationData(
        140010, "ShoGun・Void", "W1D4", NEOTwewyLocationType.ScenarioReward, False, False, ""
    ),
    "W1D4 - Center/Scramble": NEOTwewyLocationData(
        140020, "5000 Yen", "W1D4", NEOTwewyLocationType.ScenarioReward, False, False, ""
    ),
    "W1D4 - Seiji-of-Some-Trades Dive": NEOTwewyLocationData(
        140030, "Onimaru", "W1D4", NEOTwewyLocationType.ScenarioReward, False, False, ""
    ),
    "W1D4 - Scramble/TOWER RECORDS": NEOTwewyLocationData(
        140040, "Thunder and Lightning", "W1D4", NEOTwewyLocationType.ScenarioReward, False, False, ""
    ),
    "W1D4 - Eiji Oji Quest (Item)": NEOTwewyLocationData(
        140050, "1000 Yen", "W1D4", NEOTwewyLocationType.ScenarioReward, False, False, ""
    ),
    "W1D4 - Eiji Oji Quest (FP)": NEOTwewyLocationData(
        140055, "5 FP", "W1D4", NEOTwewyLocationType.ScenarioReward, False, False, ""
    ),
    "W1D4 - The Don Quest (Item)": NEOTwewyLocationData(
        140060, "Axion", "W1D4", NEOTwewyLocationType.ScenarioReward, False, False, ""
    ),
    "W1D4 - The Don Quest (FP)": NEOTwewyLocationData(
        140065, "5 FP", "W1D4", NEOTwewyLocationType.ScenarioReward, False, False, ""
    ),
    "W1D4 - Katsuhiko Tanimaru Quest (Item)": NEOTwewyLocationData(
        140070, "1000 Yen", "W1D4", NEOTwewyLocationType.ScenarioReward, False, False, ""
    ),
    "W1D4 - Katsuhiko Tanimaru Quest (FP)": NEOTwewyLocationData(
        140075, "5 FP", "W1D4", NEOTwewyLocationType.ScenarioReward, False, False, ""
    ),
    "W1D4 - Phone Number Obtained": NEOTwewyLocationData(
        140080, "5000 Yen", "W1D4", NEOTwewyLocationType.ScenarioReward, False, False, ""
    ),
    "W1D4 - Vending Machine": NEOTwewyLocationData(
        140090, "5000 Yen", "W1D4", NEOTwewyLocationType.ScenarioReward, False, False, ""
    ),
    "W1D3 - Day Cleared": NEOTwewyLocationData(
        103, "Secret Report No. 3", "W1D3", NEOTwewyLocationType.ScenarioReward, False, True, ""
    ),
    "W1D4 - Day Cleared": NEOTwewyLocationData(
        104, "Secret Report No. 4", "W1D4", NEOTwewyLocationType.ScenarioReward, False, True, ""
    ),
}

SHOP_REWARDS: dict[str, NEOTwewyLocationData] = {
    "TOWER RECORDS SHIBUYA (CD) Track 11": NEOTwewyLocationData(
        202102, "(CD) Track 11", "W1D4", NEOTwewyLocationType.Shop, False, False, ""
    ),
    "TOWER RECORDS SHIBUYA (CD) Track 8": NEOTwewyLocationData(
        202104, "(CD) Track 8", "W1D4", NEOTwewyLocationType.Shop, False, False, ""
    ),
    "TOWER RECORDS SHIBUYA (CD) Track 12": NEOTwewyLocationData(
        202105, "(CD) Track 12", "W1D4", NEOTwewyLocationType.Shop, False, False, ""
    ),
    "TOWER RECORDS SHIBUYA (CD) Track 6": NEOTwewyLocationData(
        202108, "(CD) Track 6", "W1D4", NEOTwewyLocationType.Shop, False, False, ""
    ),
    "TOWER RECORDS SHIBUYA (CD) Track 18": NEOTwewyLocationData(
        202109, "(CD) Track 18", "W1D4", NEOTwewyLocationType.Shop, False, False, ""
    ),
    "TOWER RECORDS SHIBUYA (CD) Track 4": NEOTwewyLocationData(
        202115, "(CD) Track 4", "W1D4", NEOTwewyLocationType.Shop, False, False, ""
    ),
    "TOWER RECORDS SHIBUYA (CD) Track 3": NEOTwewyLocationData(
        202116, "(CD) Track 3", "W1D4", NEOTwewyLocationType.Shop, False, False, ""
    ),
    "TOWER RECORDS SHIBUYA (CD) Track 13": NEOTwewyLocationData(
        202117, "(CD) Track 13", "W1D4", NEOTwewyLocationType.Shop, False, False, ""
    ),
    "TOWER RECORDS SHIBUYA (CD) Track 7": NEOTwewyLocationData(
        202118, "(CD) Track 7", "W1D4", NEOTwewyLocationType.Shop, False, False, ""
    ),
    "TOWER RECORDS SHIBUYA (CD) Track 23": NEOTwewyLocationData(
        202125, "(CD) Track 23", "W1D4", NEOTwewyLocationType.Shop, False, False, ""
    ),
    "TOWER RECORDS SHIBUYA (CD) Track 24": NEOTwewyLocationData(
        202126, "(CD) Track 24", "W1D4", NEOTwewyLocationType.Shop, False, False, ""
    ),
    "TOWER RECORDS SHIBUYA (CD) Track 25": NEOTwewyLocationData(
        202127, "(CD) Track 25", "W1D4", NEOTwewyLocationType.Shop, False, False, ""
    ),
    "TOWER RECORDS SHIBUYA (CD) Track 26": NEOTwewyLocationData(
        202128, "(CD) Track 26", "W1D4", NEOTwewyLocationType.Shop, False, False, ""
    ),
    "TOWER RECORDS SHIBUYA (CD) Track 28": NEOTwewyLocationData(
        202130, "(CD) Track 28", "W1D4", NEOTwewyLocationType.Shop, False, False, ""
    ),
    "Taiseido Fighting as a Team": NEOTwewyLocationData(
        200101, "Fighting as a Team", "W1D3", NEOTwewyLocationType.Shop, False, False, ""
    ),
    "Taiseido Combos": NEOTwewyLocationData(200102, "Combos", "W1D3", NEOTwewyLocationType.Shop, False, False, ""),
    "Taiseido Dodging": NEOTwewyLocationData(200103, "Dodging", "W1D3", NEOTwewyLocationType.Shop, False, False, ""),
    "Taiseido Noise Counterattacks": NEOTwewyLocationData(
        200104, "Noise Counterattacks", "W1D3", NEOTwewyLocationType.Shop, False, False, ""
    ),
    "Taiseido Elemental Affinities": NEOTwewyLocationData(
        200105, "Elemental Affinities", "W1D3", NEOTwewyLocationType.Shop, False, False, ""
    ),
    "Taiseido Status Ailments": NEOTwewyLocationData(
        200106, "Status Ailments", "W1D3", NEOTwewyLocationType.Shop, False, False, ""
    ),
    "Taiseido Experience Points": NEOTwewyLocationData(
        200107, "Experience Points", "W1D3", NEOTwewyLocationType.Shop, False, False, ""
    ),
    "Taiseido Killing It in Combat": NEOTwewyLocationData(
        200108, "Killing It in Combat", "W1D3", NEOTwewyLocationType.Shop, False, False, ""
    ),
    "Taiseido Picking Up Pins": NEOTwewyLocationData(
        200112, "Picking Up Pins", "W1D3", NEOTwewyLocationType.Shop, False, False, ""
    ),
    "Taiseido Evolving Pins": NEOTwewyLocationData(
        200113, "Evolving Pins", "W1D3", NEOTwewyLocationType.Shop, False, False, ""
    ),
    "Taiseido Pin Decks": NEOTwewyLocationData(
        200117, "Pin Decks", "W1D4", NEOTwewyLocationType.Shop, False, False, ""
    ),
    "Taiseido Scanning": NEOTwewyLocationData(200118, "Scanning", "W1D4", NEOTwewyLocationType.Shop, False, False, ""),
    "Taiseido Noise Symbols": NEOTwewyLocationData(
        200119, "Noise Symbols", "W1D4", NEOTwewyLocationType.Shop, False, False, ""
    ),
    "Taiseido Chaining Battles": NEOTwewyLocationData(
        200120, "Chaining Battles", "W1D4", NEOTwewyLocationType.Shop, False, False, ""
    ),
    "Taiseido Farming FP": NEOTwewyLocationData(
        200127, "Farming FP", "W1D4", NEOTwewyLocationType.Shop, False, False, ""
    ),
    "Taiseido Emotion Noise: Enraged": NEOTwewyLocationData(
        200128, "Emotion Noise: Enraged", "W1D4", NEOTwewyLocationType.Shop, False, False, ""
    ),
    "Taiseido Emotion Noise: Somber": NEOTwewyLocationData(
        200129, "Emotion Noise: Somber", "W1D4", NEOTwewyLocationType.Shop, False, False, ""
    ),
    "Taiseido Emotion Noise: Serene": NEOTwewyLocationData(
        200130, "Emotion Noise: Serene", "W1D4", NEOTwewyLocationType.Shop, False, False, ""
    ),
    "Taiseido Emotion Noise: Fearful": NEOTwewyLocationData(
        200131, "Emotion Noise: Fearful", "W1D4", NEOTwewyLocationType.Shop, False, False, ""
    ),
    "Taiseido ShibuPay": NEOTwewyLocationData(200132, "ShibuPay", "W1D4", NEOTwewyLocationType.Shop, False, False, ""),
    "Taiseido Mental Notes": NEOTwewyLocationData(
        200141, "Mental Notes", "W1D4", NEOTwewyLocationType.Shop, False, False, ""
    ),
    "Taiseido Social Network Skills": NEOTwewyLocationData(
        200142, "Social Network Skills", "W1D4", NEOTwewyLocationType.Shop, False, False, ""
    ),
    "Taiseido Side Quests": NEOTwewyLocationData(
        200143, "Side Quests", "W1D4", NEOTwewyLocationType.Shop, False, False, ""
    ),
    "Joli bécot 104 Branch Dazzling Denim Cap": NEOTwewyLocationData(
        200401, "Dazzling Denim Cap", "W1D3", NEOTwewyLocationType.Shop, False, False, ""
    ),
    "Joli bécot 104 Branch Denim Jacket": NEOTwewyLocationData(
        200404, "Denim Jacket", "W1D4", NEOTwewyLocationType.Shop, False, False, ""
    ),
    "Joli bécot 104 Branch Open-Shoulder Top": NEOTwewyLocationData(
        200406, "Open-Shoulder Top", "W1D4", NEOTwewyLocationType.Shop, False, False, ""
    ),
    "Joli bécot 104 Branch Shredded Jeans": NEOTwewyLocationData(
        200408, "Shredded Jeans", "W1D3", NEOTwewyLocationType.Shop, False, False, ""
    ),
    "Joli bécot 104 Branch Leather Miniskirt": NEOTwewyLocationData(
        200410, "Leather Miniskirt", "W1D4", NEOTwewyLocationType.Shop, False, False, ""
    ),
    "Joli bécot 104 Branch Golden Lighter (VIP 2)": NEOTwewyLocationData(
        200419, "Golden Lighter", "W1D4", NEOTwewyLocationType.Shop, False, False, ""
    ),
    "Joli bécot 104 Branch Cherry Bomb": NEOTwewyLocationData(
        200421, "Cherry Bomb", "W1D3", NEOTwewyLocationType.Shop, False, False, ""
    ),
    "Top o' Topo SHIBUYA Flower Headband": NEOTwewyLocationData(
        200501, "Flower Headband", "W1D3", NEOTwewyLocationType.Shop, False, False, ""
    ),
    "Top o' Topo SHIBUYA Romantic Blouse": NEOTwewyLocationData(
        200504, "Romantic Blouse", "W1D3", NEOTwewyLocationType.Shop, False, False, ""
    ),
    "Top o' Topo SHIBUYA Flowy Tulle Skirt": NEOTwewyLocationData(
        200507, "Flowy Tulle Skirt", "W1D4", NEOTwewyLocationType.Shop, False, False, ""
    ),
    "Top o' Topo SHIBUYA Cropped Pants": NEOTwewyLocationData(
        200508, "Cropped Pants", "W1D3", NEOTwewyLocationType.Shop, False, False, ""
    ),
    "Top o' Topo SHIBUYA Ribbon Pumps": NEOTwewyLocationData(
        200511, "Ribbon Pumps", "W1D4", NEOTwewyLocationType.Shop, False, False, ""
    ),
    "Top o' Topo SHIBUYA Comfy Loafers (VIP 2)": NEOTwewyLocationData(
        200513, "Comfy Loafers", "W1D4", NEOTwewyLocationType.Shop, False, False, ""
    ),
    "Gatto Nero Beret": NEOTwewyLocationData(200602, "Beret", "W1D3", NEOTwewyLocationType.Shop, False, False, ""),
    "Gatto Nero Buckle Sleeve Shirt": NEOTwewyLocationData(
        200603, "Buckle Sleeve Shirt", "W1D3", NEOTwewyLocationType.Shop, False, False, ""
    ),
    "Gatto Nero Off-the-Shoulder Top": NEOTwewyLocationData(
        200605, "Off-the-Shoulder Top", "W1D4", NEOTwewyLocationType.Shop, False, False, ""
    ),
    "Gatto Nero Denim Micro-Miniskirt (VIP 2)": NEOTwewyLocationData(
        200607, "Denim Micro-Miniskirt", "W1D4", NEOTwewyLocationType.Shop, False, False, ""
    ),
    "Gatto Nero Frayed Cargo Pants": NEOTwewyLocationData(
        200609, "Frayed Cargo Pants", "W1D3", NEOTwewyLocationType.Shop, False, False, ""
    ),
    "Shepherd House 1st Bucket Hat": NEOTwewyLocationData(
        200701, "Bucket Hat", "W1D3", NEOTwewyLocationType.Shop, False, False, ""
    ),
    "Shepherd House 1st Sheepy T-Shirt": NEOTwewyLocationData(
        200703, "Sheepy T-Shirt", "W1D4", NEOTwewyLocationType.Shop, False, False, ""
    ),
    "Shepherd House 1st White Shirt (VIP 2)": NEOTwewyLocationData(
        200706, "White Shirt", "W1D4", NEOTwewyLocationType.Shop, False, False, ""
    ),
    "Shepherd House 1st Chinos": NEOTwewyLocationData(
        200708, "Chinos", "W1D3", NEOTwewyLocationType.Shop, False, False, ""
    ),
    "Shepherd House 1st Slip-ons": NEOTwewyLocationData(
        200714, "Slip-ons", "W1D3", NEOTwewyLocationType.Shop, False, False, ""
    ),
    "Shepherd House 1st The Great Magma Escape": NEOTwewyLocationData(
        200717, "The Great Magma Escape", "W1D3", NEOTwewyLocationType.Shop, False, False, ""
    ),
    "HOG FANG Flat-Brim Snapback": NEOTwewyLocationData(
        200801, "Flat-Brim Snapback", "W1D3", NEOTwewyLocationType.Shop, False, False, ""
    ),
    "HOG FANG Baseball Cap": NEOTwewyLocationData(
        200802, "Baseball Cap", "W1D3", NEOTwewyLocationType.Shop, False, False, ""
    ),
    "HOG FANG Wired Hairband": NEOTwewyLocationData(
        200804, "Wired Hairband", "W1D4", NEOTwewyLocationType.Shop, False, False, ""
    ),
    "HOG FANG Pullover Hoodie": NEOTwewyLocationData(
        200806, "Pullover Hoodie", "W1D3", NEOTwewyLocationType.Shop, False, False, ""
    ),
    "HOG FANG Tight Denim Skirt": NEOTwewyLocationData(
        200814, "Tight Denim Skirt", "W1D4", NEOTwewyLocationType.Shop, False, False, ""
    ),
    "HOG FANG High-top Sneakers": NEOTwewyLocationData(
        200817, "High-top Sneakers", "W1D3", NEOTwewyLocationType.Shop, False, False, ""
    ),
    "HOG FANG Chain Necklace (VIP 2)": NEOTwewyLocationData(
        200820, "Chain Necklace", "W1D4", NEOTwewyLocationType.Shop, False, False, ""
    ),
    "garagara Oversized Beanie": NEOTwewyLocationData(
        201901, "Oversized Beanie", "W1D4", NEOTwewyLocationType.Shop, False, False, ""
    ),
    "garagara Bohemian T-Shirt": NEOTwewyLocationData(
        201904, "Bohemian T-Shirt", "W1D4", NEOTwewyLocationType.Shop, False, False, ""
    ),
    "garagara Poncho (VIP 2)": NEOTwewyLocationData(
        201906, "Poncho", "W1D4", NEOTwewyLocationType.Shop, False, False, ""
    ),
    "garagara Bohemian Pants": NEOTwewyLocationData(
        201908, "Bohemian Pants", "W1D4", NEOTwewyLocationType.Shop, False, False, ""
    ),
    "garagara Bohemian Sandals": NEOTwewyLocationData(
        201914, "Bohemian Sandals", "W1D4", NEOTwewyLocationType.Shop, False, False, ""
    ),
    "garagara Hippie Shoulder Bag": NEOTwewyLocationData(
        201920, "Hippie Shoulder Bag", "W1D4", NEOTwewyLocationType.Shop, False, False, ""
    ),
    "garagara Chain Is Gonna Come": NEOTwewyLocationData(
        201921, "Chain Is Gonna Come", "W1D4", NEOTwewyLocationType.Shop, False, False, ""
    ),
    "Cony×Cony Peach Blossom": NEOTwewyLocationData(
        202801, "Peach Blossom", "W1D4", NEOTwewyLocationType.Shop, False, False, ""
    ),
    "Cony×Cony Baby's Breath": NEOTwewyLocationData(
        202806, "Baby's Breath", "W1D4", NEOTwewyLocationType.Shop, False, False, ""
    ),
    "Cony×Cony Black Camellia": NEOTwewyLocationData(
        202808, "Black Camellia", "W1D4", NEOTwewyLocationType.Shop, False, False, ""
    ),
    "Cony×Cony Clover": NEOTwewyLocationData(202811, "Clover", "W1D4", NEOTwewyLocationType.Shop, False, False, ""),
    "Cony×Cony Deadly Nightshade": NEOTwewyLocationData(
        202816, "Deadly Nightshade", "W1D4", NEOTwewyLocationType.Shop, False, False, ""
    ),
    "Tigre PUNKS Studded Tiger Cap": NEOTwewyLocationData(
        202902, "Studded Tiger Cap", "W1D4", NEOTwewyLocationType.Shop, False, False, ""
    ),
    "Tigre PUNKS Biker Jacket": NEOTwewyLocationData(
        202905, "Biker Jacket", "W1D4", NEOTwewyLocationType.Shop, False, False, ""
    ),
    "Tigre PUNKS Bondage Pants": NEOTwewyLocationData(
        202911, "Bondage Pants", "W1D4", NEOTwewyLocationType.Shop, False, False, ""
    ),
    "Tigre PUNKS Studded Boots": NEOTwewyLocationData(
        202915, "Studded Boots", "W1D4", NEOTwewyLocationType.Shop, False, False, ""
    ),
    "Tigre PUNKS Spiked Wristband": NEOTwewyLocationData(
        202919, "Spiked Wristband", "W1D4", NEOTwewyLocationType.Shop, False, False, ""
    ),
    "Tigre PUNKS Grin Reaper": NEOTwewyLocationData(
        202923, "Grin Reaper", "W1D4", NEOTwewyLocationType.Shop, False, False, ""
    ),
    "RyuGu Raven Blossom": NEOTwewyLocationData(
        203501, "Raven Blossom", "W1D4", NEOTwewyLocationType.Shop, False, False, ""
    ),
    "RyuGu Black-Scarlet Blossom": NEOTwewyLocationData(
        203506, "Black-Scarlet Blossom", "W1D4", NEOTwewyLocationType.Shop, False, False, ""
    ),
    "RyuGu Lapis Chrysanthemum": NEOTwewyLocationData(
        203508, "Lapis Chrysanthemum", "W1D4", NEOTwewyLocationType.Shop, False, False, ""
    ),
    "RyuGu Violet-Ebony Foxglove": NEOTwewyLocationData(
        203513, "Violet-Ebony Foxglove", "W1D4", NEOTwewyLocationType.Shop, False, False, ""
    ),
    "TOKYU HANDS 2F Dazzling Denim Cap": NEOTwewyLocationData(
        201401, "Dazzling Denim Cap", "W1D3", NEOTwewyLocationType.Shop, False, False, ""
    ),
    "TOKYU HANDS 2F Flat-Brim Snapback": NEOTwewyLocationData(
        201402, "Flat-Brim Snapback", "W1D3", NEOTwewyLocationType.Shop, False, False, ""
    ),
    "TOKYU HANDS 2F Baseball Cap": NEOTwewyLocationData(
        201403, "Baseball Cap", "W1D3", NEOTwewyLocationType.Shop, False, False, ""
    ),
    "TOKYU HANDS 2F Beret": NEOTwewyLocationData(201404, "Beret", "W1D3", NEOTwewyLocationType.Shop, False, False, ""),
    "TOKYU HANDS 1F Shockwave": NEOTwewyLocationData(
        201301, "Shockwave", "W1D3", NEOTwewyLocationType.Shop, False, False, ""
    ),
    "TOKYU HANDS 1F Force Rounds": NEOTwewyLocationData(
        201302, "Force Rounds", "W1D3", NEOTwewyLocationType.Shop, False, False, ""
    ),
    "TOKYU HANDS 1F Firestorm": NEOTwewyLocationData(
        201303, "Firestorm", "W1D3", NEOTwewyLocationType.Shop, False, False, ""
    ),
    "TOKYU HANDS 1F Angelic Kick": NEOTwewyLocationData(
        201304, "Angelic Kick", "W1D3", NEOTwewyLocationType.Shop, False, False, ""
    ),
    "TOKYU HANDS 1F Azamaru": NEOTwewyLocationData(
        201305, "Azamaru", "W1D3", NEOTwewyLocationType.Shop, False, False, ""
    ),
    "TOKYU HANDS 1F Marvelous Crash": NEOTwewyLocationData(
        201306, "Marvelous Crash", "W1D3", NEOTwewyLocationType.Shop, False, False, ""
    ),
    "TOKYU HANDS 1F Joli bécot": NEOTwewyLocationData(
        201311, "Joli bécot", "W1D3", NEOTwewyLocationType.Shop, False, False, ""
    ),
    "TOKYU HANDS 3F Rare Metal": NEOTwewyLocationData(
        201501, "3x Rare Metal", "W1D3", NEOTwewyLocationType.Shop, False, False, ""
    ),
    "TOKYU HANDS 3F Tektite": NEOTwewyLocationData(
        201502, "3x Tektite", "W1D3", NEOTwewyLocationType.Shop, False, False, ""
    ),
}

LOCATION_DATA: dict[str, NEOTwewyLocationData] = SCENARIO_REWARDS | SHOP_REWARDS
