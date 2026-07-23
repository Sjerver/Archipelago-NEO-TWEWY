from __future__ import annotations
from enum import Enum
from typing import Dict, NamedTuple, Optional

class NEOTwewyLocationType(Enum):
    ScenarioReward = 0

class NEOTwewyLocationData(NamedTuple):
    """Special data container to contain the metadata of each item to make filtering work."""

    id: int
    ogItem: str

    region: str
    location_type: NEOTwewyLocationType

    combatPinOnly: bool

    addToGame: bool
    option: Optional[str]

LOCATION_DATA: Dict[str, NEOTwewyLocationData] = {
    "W1D1 - Minamimoto's Pin": NEOTwewyLocationData(110010, "Joli bécot", "W1D1", NEOTwewyLocationType.ScenarioReward,
                                                    True, False, "minamimoto_pin"),
    "W1D1 - Shibuya Hikarie": NEOTwewyLocationData(110020, "Firestorm", "W1D1", NEOTwewyLocationType.ScenarioReward,
                                                   False, False, ""),
    "W1D2 - 104/Dogenzaka": NEOTwewyLocationData(120010, "Sugar Beam", "W1D2", NEOTwewyLocationType.ScenarioReward,
                                                 False, False, ""),
    "W1D2 - Dogenzaka/O-EAST": NEOTwewyLocationData(120020, "Marvelous Crash", "W1D2",
                                                    NEOTwewyLocationType.ScenarioReward, False, False, ""),
    "W1D2 - TSUTAYA O-EAST": NEOTwewyLocationData(120030, "Azamaru", "W1D2", NEOTwewyLocationType.ScenarioReward, False,
                                                  False, ""),
    "W1D1 - Day Cleared": NEOTwewyLocationData(101, "Secret Report No. 1", "W1D1", NEOTwewyLocationType.ScenarioReward,
                                               False, True, ""),
    "W1D2 - Day Cleared": NEOTwewyLocationData(102, "Secret Report No. 2", "W1D2", NEOTwewyLocationType.ScenarioReward,
                                               False, True, ""),

}