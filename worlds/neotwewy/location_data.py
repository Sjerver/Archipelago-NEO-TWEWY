from __future__ import annotations

from enum import Enum
from typing import NamedTuple


class NEOTwewyLocationType(Enum):
    ScenarioReward = 0


class NEOTwewyLocationData(NamedTuple):
    """Special data container to contain the metadata of each item to make filtering work."""

    id: int
    og_item: str

    region: str
    location_type: NEOTwewyLocationType

    combat_pin_only: bool

    add_to_game: bool
    option: str


LOCATION_DATA: dict[str, NEOTwewyLocationData] = {
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
