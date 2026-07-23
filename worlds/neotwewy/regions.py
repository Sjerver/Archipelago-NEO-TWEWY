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
        "W1D1", "W1D2","W1D3","W1D4","W1D5","W1D6","W1D7",
        "W2D1","W2D2","W2D3","W2D4","W2D5","W2D6","W2D7",
        "W3D1","W3D2","W3D3","W3D4","W3D5","W3D6","W3D7","W3D7'","W3D7''"
    ]

    regions = [Region(name, world.player, world.multiworld) for name in regionNames]

    world.multiworld.regions += regions

def connect_regions(world: NEOTwewyWorld) -> None:
    for i in range(1,3):
        for j in range(1,7):
            if j < 7:
                day_prev = world.get_region(f"W{i}D{j}")
                day_next = world.get_region(f"W{i}D{j+1}")
                day_prev.connect(day_next, f"W{i}D{j} to W{i}D{j+1}")
            elif i < 3:
                day_prev = world.get_region(f"W{i}D{j}")
                day_next = world.get_region(f"W{i+1}D{1}")
                day_prev.connect(day_next, f"W{i}D{j} to W{i+1}D{1}")
    world.get_region("W3D7").connect(world.get_region("W3D7'"), "W3D7 to W3D7'")
    world.get_region("W3D7'").connect(world.get_region("W3D7''"), "W3D7' to W3D7''")