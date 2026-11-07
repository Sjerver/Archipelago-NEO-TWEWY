from __future__ import annotations

from typing import TYPE_CHECKING

from BaseClasses import Location, LocationProgressType
from . import items
from .location_data import LOCATION_DATA, LOCATION_INCLUSION, NEOTwewyLocationType

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
    for location, location_data in LOCATION_DATA.items():
        if not LOCATION_INCLUSION[location_data.location_type](world) and not location_data.lock:
            continue
        if location_data.option == "" or location_data.option is None:
            world.get_region(location_data.region).add_locations(
                get_location_names_with_ids([location]), NEOTwewyLocation
            )

            # Exclude non chainable noise
            if (
                    world.options.deprioritize_non_chain
                    and location_data.location_type == NEOTwewyLocationType.NoiseDrop
                    and (not location_data.chainable or location_data.blue_noise)  # TODO: Bossy noise check
            ):
                world.get_location(location).progress_type = LocationProgressType.EXCLUDED
        else:
            if getattr(world.options, location_data.option):
                world.get_region(location_data.region).add_locations(
                    get_location_names_with_ids([location]), NEOTwewyLocation
                )
        if location_data.lock and not LOCATION_INCLUSION[location_data.location_type](world):
            items.create_item_in_locked_location(world, location_data.og_item, location)


def create_events(world: NEOTwewyWorld) -> None:
    # Victory Condition
    w1d5 = world.get_region("W1D5")
    w1d5.add_event("Reached Day 5", "Victory", location_type=NEOTwewyLocation, item_type=items.NEOTwewyItem)

    # Difficulty fake events
    w1d1 = world.get_region("W1D1")
    w1d1.add_event("Easy Unlocked", "EASY DIFFICULTY", location_type=NEOTwewyLocation, item_type=items.NEOTwewyItem)

    w1d4 = world.get_region("W1D4")
    w1d4.add_event("Hard Unlocked", "HARD DIFFICULTY", location_type=NEOTwewyLocation, item_type=items.NEOTwewyItem)
