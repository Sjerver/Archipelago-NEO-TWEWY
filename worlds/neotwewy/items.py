from __future__ import annotations

import random
from typing import TYPE_CHECKING

from BaseClasses import Item, ItemClassification
from .item_data import (
    DEFAULT_ITEM_CLASSIFICATIONS,
    DROP_INCREASING_THREADS,
    ITEM_DATA,
    ITEM_GROUPS,
    ITEM_NAME_TO_ID,
    ITEM_TO_GROUPS,
    JOLI_BECOT_THREADS, NEOTwewyItemType,
)
from .location_data import LOCATION_DATA, LOCATION_INCLUSION, PROGRESSIVE_ELEMENTS, NEOTwewyLocationType

if TYPE_CHECKING:
    from .world import NEOTwewyWorld


class NEOTwewyItem(Item):
    game = "NEO: The World Ends with You"


def get_item_groups(item_to_get: Item) -> list[str] | list[None]:
    return ITEM_TO_GROUPS.get(item_to_get.name, [None])


def get_random_filler_item_name(world: NEOTwewyWorld) -> str:
    # TODO: How do we reduce chance of duplicate items???
    filler_items = [item for item, data in ITEM_DATA.items() if
                    data.item_classification in [ItemClassification.filler, ItemClassification.skip_balancing]]
    return random.choice(filler_items)


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
            or (
            name in DROP_INCREASING_THREADS and world.options.noise_drops)  # Location access rule is option dependant
            or name in ITEM_GROUPS["FP_ITEM"]
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
        if (
                location_data.location_type == NEOTwewyLocationType.DLC
                and world.options.dlc_options == world.options.dlc_options.option_randomize_without_content
        ):
            # DLC can be included without its "original item"
            continue
        # These items can be in item pool
        if location_data.option == "" or location_data.option is None:
            item_pool.append(world.create_item(location_data.og_item))
        else:
            if getattr(world.options, location_data.option):
                item_pool.append(world.create_item(location_data.og_item))

    # Remove duplicate filler items
    # print(len(item_pool))
    discarded_items = []
    unique_filler = set()
    new_item_pool = []
    for item in item_pool:
        if item.classification in [ItemClassification.filler, ItemClassification.skip_balancing]:
            item_data = ITEM_DATA[item.name]
            if unique_filler.__contains__(item.name) or item_data.item_type == NEOTwewyItemType.Book:
                discarded_items.append(item.name)
            else:
                unique_filler.add(item.name)
                new_item_pool.append(item)

        else:
            new_item_pool.append(item)
    item_pool = new_item_pool
    random.shuffle(discarded_items)
    # print(f"Unique filler {len(unique_filler)}")
    # print(len(item_pool))

    # Add Conditional Items without locations

    # Fill up with duplicate Filler items again
    # print(len(item_pool))
    number_of_items = len(item_pool)
    number_of_unfilled_locations = len(world.multiworld.get_unfilled_locations(world.player))
    needed_number_of_filler_items = number_of_unfilled_locations - number_of_items

    new_filler = [world.create_filler(discarded_items) for _ in range(needed_number_of_filler_items)]
    item_pool += new_filler
    world.multiworld.itempool += item_pool
