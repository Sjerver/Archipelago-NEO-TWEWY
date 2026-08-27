from __future__ import annotations

from typing import TYPE_CHECKING

from BaseClasses import Region

if TYPE_CHECKING:
    from .world import NEOTwewyWorld

REGION_NAMES = [
    "W1D1",
    "W1D2",
    "W1D2'",
    "W1D3",
    "W1D3'",
    "W1D4",
    "W1D5",
    # Everything after this point is not fully implemented
    "W1D6",
    "W1D7",
    "W2D1",
    "W2D2",
    "W2D3",
    "W2D4",
    "W2D5",
    "W2D6",
    "W2D7",
    "W3D1",
    "W3D2",
    "W3D3",
    "W3D4",
    "W3D5",
    "W3D6",
    "W3D7",
    "W3D7'",
    "W3D7''",
    "W4D1",  # Another Day
]

EXPECTED_LEVEL_PER_REGION: dict[str, int] = {
    "W1D1": 2,
    "W1D2": 4,
    "W1D3": 7,
    "W1D4": 9,
    "W1D5": 14,
    "W1D6": 20,
    "W1D7": 25,
    "W2D1": 26,
    "W2D2": 27,
    "W2D3": 29,
    "W2D4": 32,
    "W2D5": 34,
    "W2D6": 35,
    "W2D7": 36,
    "W3D1": 37,
    "W3D2": 38,
    "W3D3": 40,
    "W3D4": 45,
    "W3D5": 47,
    "W3D6": 50,
    "W3D7": 53,
    "W4D1": 80,
}

def create_and_connect_regions(world: NEOTwewyWorld) -> None:
    create_all_regions(world)
    connect_regions(world)

def create_all_regions(world: NEOTwewyWorld) -> None:

    regions = [Region(name, world.player, world.multiworld) for name in REGION_NAMES]

    world.multiworld.regions += regions

def connect_regions(world: NEOTwewyWorld) -> None:
    for i in range(REGION_NAMES.__len__()):
        if i > len(REGION_NAMES) - 2:
            break
        world.get_region(REGION_NAMES[i]).connect(
            world.get_region(REGION_NAMES[i + 1]), f"{REGION_NAMES[i]} to {REGION_NAMES[i + 1]}"
        )
