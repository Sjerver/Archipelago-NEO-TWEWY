
from __future__ import annotations

from typing import TYPE_CHECKING

from BaseClasses import Location

from . import items
from .location_data import LOCATION_DATA

if TYPE_CHECKING:
    from .world import NEOTwewyWorld


LOCATION_NAME_TO_ID = {location_name: location_data.id for location_name, location_data in LOCATION_DATA.items()}


class NEOTwewyLocation(Location):
    game = "NEO: The World Ends with You"

def get_location_names_with_ids(location_names: list[str]) -> dict[str, int | None]:
    return {location_name: LOCATION_NAME_TO_ID[location_name] for location_name in location_names}


def create_all_locations(world: NEOTwewyWorld) -> None:
    create_regular_locations(world)
    create_events(world)

def create_regular_locations(world: NEOTwewyWorld) -> None:

    for location,data in LOCATION_DATA.items():
        if data.option == "" or data.option is None:
            world.get_region(data.region).add_locations(get_location_names_with_ids([location]), NEOTwewyLocation)
        else:
            if getattr(world.options, data.option):
                world.get_region(data.region).add_locations(get_location_names_with_ids([location]), NEOTwewyLocation)

def create_events(world: NEOTwewyWorld) -> None:
    w1d2 = world.get_region("W1D3")
    w1d2.add_event("Reached Day 3", "Victory", location_type = NEOTwewyLocation, item_type = items.NEOTwewyItem)