from __future__ import annotations

from typing import TYPE_CHECKING

from BaseClasses import Item

from .item_data import ITEM_DATA, NEOTwewyItemGroup
from .location_data import LOCATION_DATA, NEOTwewyLocationType

if TYPE_CHECKING:
    from .world import NEOTwewyWorld

ITEM_NAME_TO_ID = {item_name: item_data.id for item_name, item_data in ITEM_DATA.items()}

DEFAULT_ITEM_CLASSIFICATIONS = {item_name: item_data.item_classification for item_name, item_data in ITEM_DATA.items()}

ITEM_GROUPS = {group.value: [] for group in NEOTwewyItemGroup}

for item,data in ITEM_DATA.items():
    for group in data.item_groups:
        ITEM_GROUPS[group.value].append(item)

ITEM_TO_GROUPS = {}

for group, items in ITEM_GROUPS.items():
    for item in items:
        ITEM_TO_GROUPS.setdefault(item, []).append(group)

class NEOTwewyItem(Item):
    game = "NEO: The World Ends with You"

def get_item_groups(item_to_get: Item) -> list[str] | list[None]:
    return ITEM_TO_GROUPS.get(item_to_get.name, [None])

def get_random_filler_item_name(world: NEOTwewyWorld) -> str:
    return "5 Yen"

def create_item_with_correct_classification(world: NEOTwewyWorld, name: str) -> NEOTwewyItem:
    classification = DEFAULT_ITEM_CLASSIFICATIONS[name]
    return NEOTwewyItem(name, classification, ITEM_NAME_TO_ID[name], world.player)

def create_all_items(world: NEOTwewyWorld) -> None:

    item_pool: list[Item] = []
    for location_data in LOCATION_DATA.values():
        if not world.options.shops and location_data.location_type == NEOTwewyLocationType.Shop:
            # Shop locations only added when we have shops activated
            continue
        if not world.options.dive and location_data.location_type == NEOTwewyLocationType.Dive:
            continue
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

