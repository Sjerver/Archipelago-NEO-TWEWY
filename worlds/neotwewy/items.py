from __future__ import annotations

from typing import TYPE_CHECKING

from BaseClasses import Item, ItemClassification

from .item_data import (
    DEFAULT_ITEM_CLASSIFICATIONS,
    DROP_INCREASING_THREADS,
    ITEM_DATA,
    ITEM_GROUPS,
    ITEM_NAME_TO_ID,
    ITEM_TO_GROUPS,
    JOLI_BECOT_THREADS,
)
from .location_data import LOCATION_DATA, LOCATION_INCLUSION, PROGRESSIVE_ELEMENTS

if TYPE_CHECKING:
    from .world import NEOTwewyWorld

class NEOTwewyItem(Item):
    game = "NEO: The World Ends with You"

def get_item_groups(item_to_get: Item) -> list[str] | list[None]:
    return ITEM_TO_GROUPS.get(item_to_get.name, [None])

def get_random_filler_item_name(world: NEOTwewyWorld) -> str:
    return "5 Yen"

def update_progression(old_classification: ItemClassification) -> ItemClassification:
    if old_classification == ItemClassification.skip_balancing:
        old_classification = ItemClassification.progression_skip_balancing
    else:
        old_classification = ItemClassification.progression
    return old_classification


def create_item_with_correct_classification(world: NEOTwewyWorld, name: str) -> NEOTwewyItem:
    base_classification = DEFAULT_ITEM_CLASSIFICATIONS[name]
    item_data = ITEM_DATA[name]
    if (
        (name in JOLI_BECOT_THREADS and world.options.shops)
        or (name == "Midaregami" and world.options.noise_drops)
        or (name in DROP_INCREASING_THREADS and world.options.noise_drops)  # Location access rule is option dependant
        or name in ITEM_GROUPS["FP"]
        or (item_data.element in PROGRESSIVE_ELEMENTS and world.options.pig_drops)
    ):
        base_classification = update_progression(base_classification)

    return NEOTwewyItem(name, base_classification, ITEM_NAME_TO_ID[name], world.player)


def create_item_in_locked_location(world: NEOTwewyWorld, name: str, loc_name: str) -> None:
    created_item = world.create_item(name)
    location = world.get_location(loc_name)
    location.place_locked_item(created_item)

def create_all_items(world: NEOTwewyWorld) -> None:
    item_pool: list[Item] = []
    for location_name, location_data in LOCATION_DATA.items():
        if not LOCATION_INCLUSION[location_data.location_type](world):
            continue
        # These items can be in item pool
        if location_data.option == "" or location_data.option is None:
            item_pool.append(world.create_item(location_data.og_item))
        else:
            if getattr(world.options, location_data.option):
                item_pool.append(world.create_item(location_data.og_item))

    number_of_items = len(item_pool)
    number_of_unfilled_locations = len(world.multiworld.get_unfilled_locations(world.player))
    needed_number_of_filler_items = number_of_unfilled_locations - number_of_items
    item_pool += [world.create_filler() for _ in range(needed_number_of_filler_items)]
    world.multiworld.itempool += item_pool

