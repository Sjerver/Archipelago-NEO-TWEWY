
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

    IMPLEMENTED_DAY_MAX = 4

    for i in range(1,4):
        for j in range(1,8):
            secret_report_count = (i-1)*7 + j
            if secret_report_count > IMPLEMENTED_DAY_MAX:
                break
            if j < 7:
                entrance = world.get_entrance(f"W{i}D{j} to W{i}D{j+1}")
            elif i < 3:
                entrance = world.get_entrance(f"W{i}D{j} to W{i+1}D{1}")
            can_progress = HasGroup(NEOTwewyItemGroup.SECRET_REPORT.value, secret_report_count)
            world.set_rule(entrance, can_progress)

    if(IMPLEMENTED_DAY_MAX > 22):
        w3d7_to_w3d8 = world.get_entrance("W3D7 to W3D7'")
        can_progress = HasGroup(NEOTwewyItemGroup.SECRET_REPORT.value, 22)
        world.set_rule(w3d7_to_w3d8, can_progress)
    if(IMPLEMENTED_DAY_MAX > 23):
        w3d8_to_w3d9 = world.get_entrance("W3D7' to W3D7''")
        can_progress = HasGroup(NEOTwewyItemGroup.SECRET_REPORT.value, 23)
        world.set_rule(w3d8_to_w3d9, can_progress)

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
