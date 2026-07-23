from __future__ import annotations
from typing import TYPE_CHECKING

from BaseClasses import Entrance, Region

if TYPE_CHECKING:
    from .world import NEOTwewyWorld

def create_and_connect_regions(world: NEOTwewyWorld) -> None:
    create_all_regions(world)
    connect_regions(world)

def create_all_regions(world: NEOTwewyWorld) -> None:
    regionNames = [
        "W1D1", "W1D2","W1D3"
    ]

    regions = [Region(name, world.player, world.multiworld) for name in regionNames]

    world.multiworld.regions += regions

def connect_regions(world: NEOTwewyWorld) -> None:
    week1_day1 = world.get_region("W1D1")
    week1_day2 = world.get_region("W1D2")

    week1_day1.connect(week1_day2, "W1D1 to W1D2")

    week1_day3 = world.get_region("W1D3")
    week1_day2.connect(week1_day3, "W1D2 to W1D3")