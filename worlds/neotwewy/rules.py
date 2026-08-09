
from __future__ import annotations

from typing import TYPE_CHECKING

from rule_builder.rules import Has, HasAny, HasGroup
from worlds.generic.Rules import add_item_rule

from .item_data import ITEM_DATA, NEOTwewyItemType
from .items import NEOTwewyItemGroup, get_item_groups
from .location_data import LOCATION_DATA

if TYPE_CHECKING:
    from .world import NEOTwewyWorld

def set_all_rules(world: NEOTwewyWorld) -> None:
    set_all_entrance_rules(world)
    set_all_location_rules(world)
    set_completion_condition(world)
    set_item_exception_rules(world)

def set_all_entrance_rules(world: NEOTwewyWorld) -> None:

    report_rules = [
        ("W1D1", "W1D2", 1),
        ("W1D2", "W1D3", 2),
        ("W1D3", "W1D3'", None),
        ("W1D3'", "W1D4", 3),
        ("W1D4", "W1D5", 4),
    ]

    for start, end, report in report_rules:
        if report is None:
            continue
        entrance = world.get_entrance(f"{start} to {end}")
        world.set_rule(entrance, HasGroup(NEOTwewyItemGroup.SECRET_REPORT.value, report))

    if world.options.shops:
        wall_reaper_w1d3 = world.get_entrance("W1D3 to W1D3'")
        joli_becot_threads = [
            itemName
            for itemName, itemData in ITEM_DATA.items()
            if itemData.brand == "Joli bécot" and itemData.item_type == NEOTwewyItemType.Costume
        ]
        has_1_joli_becot = HasAny(*joli_becot_threads)
        world.set_rule(wall_reaper_w1d3, has_1_joli_becot)

def set_all_location_rules(world: NEOTwewyWorld) -> None:
    pass

def set_completion_condition(world: NEOTwewyWorld) -> None:
    world.set_completion_rule(Has("Victory"))

def set_item_exception_rules(world: NEOTwewyWorld) -> None:
    for location, data in LOCATION_DATA.items():
        if data.combat_pin_only:
            if data.option == "" or data.option is None or getattr(world.options, data.option):
                add_item_rule(world.multiworld.get_location(location,world.player),
                          lambda item: NEOTwewyItemGroup.COMBAT_PIN.value in get_item_groups(item))
