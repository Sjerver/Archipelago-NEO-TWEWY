from __future__ import annotations
from typing import TYPE_CHECKING

from .item_data import ITEM_DATA, NEOTwewyItemGroup

from BaseClasses import Item, ItemClassification

if TYPE_CHECKING:
    from .world import NEOTwewyWorld

ITEM_NAME_TO_ID = {item_name: item_data.id for item_name, item_data in ITEM_DATA.items()}

DEFAULT_ITEM_CLASSIFICATIONS = {item_name: item_data.itemClassification for item_name, item_data in ITEM_DATA.items()}

ITEM_GROUPS = {group.value: [] for group in NEOTwewyItemGroup}

for item,data in ITEM_DATA.items():
    for group in data.itemGroups:
        ITEM_GROUPS[group.value].append(item)

ITEM_TO_GROUPS = {}

for group, items in ITEM_GROUPS.items():
    for item in items:
        ITEM_TO_GROUPS.setdefault(item, []).append(group)

class NEOTwewyItem(Item):
    game = "NEO The World Ends with You"

def get_item_groups(item: Item) -> list[str] | list[None]:
    return ITEM_TO_GROUPS.get(item.name, [None])

def get_random_filler_item_name(world: NEOTwewyWorld) -> str:
    return "5 Yen"

def create_item_with_correct_classification(world: NEOTwewyWorld, name: str) -> NEOTwewyItem:
    classification = DEFAULT_ITEM_CLASSIFICATIONS[name]
    return NEOTwewyItem(name, classification, ITEM_NAME_TO_ID[name], world.player)

def create_all_items(world: NEOTwewyWorld) -> None:

    itempool: list[Item] = [
        world.create_item("Firestorm"),
        world.create_item("Secret Report No. 1"),
        world.create_item("Secret Report No. 2"),
        world.create_item("Azamaru"),
        world.create_item("Sugar Beam"),
        world.create_item("Marvelous Crash"),
    ]

    number_of_items = len(itempool)
    number_of_unfilled_locations = len(world.multiworld.get_unfilled_locations(world.player))
    needed_number_of_filler_items = number_of_unfilled_locations - number_of_items
    itempool += [world.create_filler() for _ in range(needed_number_of_filler_items)]
    world.multiworld.itempool += itempool

