
from __future__ import annotations
from typing import TYPE_CHECKING
from BaseClasses import ItemClassification, Location

from . import items

if TYPE_CHECKING:
    from .world import NEOTwewyWorld

#TODO: Figure out a better way to load them from a json/csv file?
LOCATION_NAME_TO_ID = {
    "W1D1 - Minamimoto's Pin": 110010,
    "W1D1 - Shibuya Hikarie": 110020,
    "W1D1 - Cleared Day": 99999,
    "W1D2 - 104/Dogenzaka":120010,
    "W1D2 - Dogenzaka/O-EAST":120020,
    "W1D2 - TSUTAYA O-EAST":120030,
    "W1D2 - Cleared Day": 99999+1,
}



LOCATION_EXCEPTIONS = ["W1D1 - Minamimoto's Pin"]

class NEOTwewyLocation(Location):
    game = "NEO: The World Ends with You"

def get_location_names_with_ids(location_names: list[str]) -> dict[str, int | None]:
    return {location_name: LOCATION_NAME_TO_ID[location_name] for location_name in location_names}


def create_all_locations(world: NEOTwewyWorld) -> None:
    create_regular_locations(world)
    create_events(world)

def create_regular_locations(world: NEOTwewyWorld) -> None:
    region_names = ["W1D1","W1D2","W1D3"]

    regions = [world.get_region(name) for name in region_names]

    for region in regions:
        locationNames = [location_name for location_name in LOCATION_NAME_TO_ID.keys() if region.name in location_name and location_name not in LOCATION_EXCEPTIONS]
        locations = get_location_names_with_ids(locationNames)
        region.add_locations(locations, NEOTwewyLocation)

    if world.options.minamimoto_pin:
        world.get_region("W1D1").add_locations(get_location_names_with_ids(["W1D1 - Minamimoto's Pin"]), NEOTwewyLocation)

  
def create_events(world: NEOTwewyWorld) -> None:
    w1d2 = world.get_region("W1D3")
    
    w1d2.add_event("Reached Day 3", "Victory", location_type = NEOTwewyLocation, item_type = items.NEOTwewyItem)