from __future__ import annotations

from typing import TYPE_CHECKING

from rule_builder.rules import False_, Has, HasGroup, True_
from worlds.generic.Rules import add_item_rule

from .custom_rule import HasFP, ReachedMinimumDropRate
from .item_data import NEOTwewyItemGroup
from .items import get_item_groups
from .location_data import LOCATION_DATA, NEOTwewyLocationType
from .rule_data import REGION_RULES, SKILL_EVENT_RULES

if TYPE_CHECKING:
    from .world import NEOTwewyWorld

def set_all_rules(world: NEOTwewyWorld) -> None:
    set_all_entrance_rules(world)
    set_all_location_rules(world)
    set_completion_condition(world)
    set_item_exception_rules(world)

def set_all_entrance_rules(world: NEOTwewyWorld) -> None:
    for start, end, rule, condition in REGION_RULES:
        if condition(world):
            entrance = world.get_entrance(f"{start} to {end}")
            world.set_rule(entrance, rule)

def set_all_location_rules(world: NEOTwewyWorld) -> None:
    if world.options.noise_drops:
        set_noise_drop_location_rules(world)
    if world.options.pig_drops:
        set_pig_drop_location_rules(world)
    set_event_location_rules(world)


def set_completion_condition(world: NEOTwewyWorld) -> None:
    world.set_completion_rule(Has("Victory"))


def set_item_exception_rules(world: NEOTwewyWorld) -> None:
    for location, data in LOCATION_DATA.items():
        if data.combat_pin_only:
            if data.option == "" or data.option is None or getattr(world.options, data.option):
                add_item_rule(
                    world.get_location(location),
                    lambda item: NEOTwewyItemGroup.COMBAT_PIN.value in get_item_groups(item),
                )


def set_event_location_rules(world: NEOTwewyWorld) -> None:
    for skill, fp in SKILL_EVENT_RULES:
        loc = world.get_location(skill)
        has_fp = HasFP(fp)
        world.set_rule(loc, has_fp)


def set_noise_drop_location_rules(world: NEOTwewyWorld) -> None:
    for location, data in LOCATION_DATA.items():
        if data.location_type == NEOTwewyLocationType.NoiseDrop:
            world_location = world.get_location(location)

            # Difficulty Availabilty
            difficulty_available = False_()
            if "EASY" in location:
                difficulty_available = Has("EASY DIFFICULTY")
            elif "NORMAL" in location:
                difficulty_available = True_()
            elif "HARD" in location:
                difficulty_available = Has("HARD DIFFICULTY")
            elif "ULTIMATE" in location:
                difficulty_available = Has("ULTIMATE DIFFICULTY")
            # If we aren't randomizing noise drops we just need to check for difficulty availability
            if not world.options.noise_drops:
                world.set_rule(world_location, difficulty_available)
                continue

            can_reasonably_drop = ReachedMinimumDropRate(data.chance, data.chainable, data.blue_noise)

            can_reasonably_drop = can_reasonably_drop & difficulty_available
            world.set_rule(world_location, can_reasonably_drop)


def set_pig_drop_location_rules(world: NEOTwewyWorld) -> None:
    for location, data in LOCATION_DATA.items():
        if data.location_type == NEOTwewyLocationType.Pig:
            world_location = world.get_location(location)
            if len(data.elements) > 0:
                elemental_rule = True_()
                for element in data.elements:
                    elemental_rule = elemental_rule & HasGroup(element)
                world.set_rule(world_location, elemental_rule)



