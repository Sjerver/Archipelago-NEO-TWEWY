
from __future__ import annotations

from typing import TYPE_CHECKING

from rule_builder.rules import Has, HasGroup
from worlds.generic.Rules import add_item_rule

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

    w1d1_to_w1d2 = world.get_entrance("W1D1 to W1D2")

    can_progress = HasGroup(NEOTwewyItemGroup.SECRET_REPORT.value, 1)
    world.set_rule(w1d1_to_w1d2, can_progress)

    w1d2_to_w1d3 = world.get_entrance("W1D2 to W1D3")
    
    can_progress = HasGroup(NEOTwewyItemGroup.SECRET_REPORT.value, 2)
    world.set_rule(w1d2_to_w1d3, can_progress)

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