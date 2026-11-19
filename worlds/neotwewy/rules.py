from __future__ import annotations

import random
from typing import TYPE_CHECKING

from BaseClasses import Location
from rule_builder.rules import False_, Has, HasGroup, True_
from worlds.generic.Rules import add_item_rule
from .custom_rule import ReachedMinimumDropRate, HasFP
from .item_data import NEOTwewyItemGroup
from .items import get_item_groups
from .location_data import LOCATION_DATA, NEOTwewyLocationType
from .regions import REGION_NAMES
from .rule_data import REGION_RULES, SKILL_EVENT_RULES

if TYPE_CHECKING:
    from .world import NEOTwewyWorld

NEW_FP_COSTS = {}

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
    set_vip_rules(world)
    if world.options.noise_drops:
        set_noise_drop_location_rules(world)
    if world.options.pig_drops:
        set_pig_drop_location_rules(world)
    set_skill_rules(world)
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
    for skill, rule in SKILL_EVENT_RULES:
        loc = world.get_location(skill)
        world.set_rule(loc, rule)


def set_vip_rules(world: NEOTwewyWorld) -> None:
    for location, data in LOCATION_DATA.items():
        if world.options.shops and data.location_type == NEOTwewyLocationType.Shop:
            if "(VIP" in location:
                world_location = world.get_location(location)
                vip_level = int(location[-2:-1]) - 1
                brand = data.brand

                item_name = "Progressive VIP " + brand

                has_vip_level = Has(item_name, vip_level)
                world.set_rule(world_location, has_vip_level)
        elif world.options.sns and data.location_type == NEOTwewyLocationType.SocialNode:
            if "Reach VIP Level 3 for" in location:
                world_location = world.get_location(location)
                brand = location.split("Reach VIP Level 3 for ")[1]
                item_name = "Progressive VIP " + brand

                has_vip_level = Has(item_name, 2)
                world.set_rule(world_location, has_vip_level)
        elif data.location_type == NEOTwewyLocationType.VIP:
            world_location = world.get_location(location)
            brand = data.brand
            vip_level = int(location[-1:]) - 1
            item_name = "Progressive VIP " + brand
            has_vip_level = Has(item_name, vip_level)
            world.set_rule(world_location, has_vip_level)


def set_noise_drop_location_rules(world: NEOTwewyWorld) -> None:
    for location, data in LOCATION_DATA.items():
        if data.location_type == NEOTwewyLocationType.NoiseDrop:
            world_location = world.get_location(location)

            # Difficulty Availabilty
            difficulty_available = False_()
            if "EASY" in location:
                difficulty_available = Has("EASY Difficulty")
            elif "NORMAL" in location:
                difficulty_available = True_()
            elif "HARD" in location:
                difficulty_available = Has("HARD Difficulty")
            elif "ULTIMATE" in location:
                difficulty_available = Has("ULTIMATE Difficulty")
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


def set_skill_rules(world: NEOTwewyWorld) -> None:
    if getattr(world.multiworld, "generation_is_fake", False) and "fp_costs" not in world.slot_data_UT:
        print("Early rule skill stop")
        return
    items = world.multiworld.get_items()

    five = [5 for i in items if i.name == "5 FP"]
    two = [2 for i in items if i.name == "2 FP"]
    one = [1 for i in items if i.name == "FP"]

    available_fp = len(five) * 5 + len(two) * 2 + len(one)
    total_cost = 0
    current_total_cost = 0

    skill_locations: list[Location] = []
    for location, location_data in LOCATION_DATA.items():
        if location_data.location_type == NEOTwewyLocationType.Skill:
            loc = world.get_location(location)
            skill_locations.append(loc)
            total_cost += location_data.fp_cost

    fp_limit = min(available_fp, total_cost)
    if world.options.fp_cost == world.options.fp_cost.option_cumulative:
        skill_locations = sorted(skill_locations, key=lambda x: REGION_NAMES.index(LOCATION_DATA[x.name].region))
    elif world.options.fp_cost == world.options.fp_cost.option_randomize:
        random.shuffle(skill_locations)

    fp_random = [random.randint(1, fp_limit) for _ in skill_locations]

    for index, location in enumerate(skill_locations):
        name = location.name
        data = LOCATION_DATA[name]

        fp_rule = True_()
        if world.options.fp_cost.value == world.options.fp_cost.option_cumulative:
            current_total_cost = min(current_total_cost + data.fp_cost, fp_limit)
            fp_rule = HasFP(current_total_cost)
            NEW_FP_COSTS[data.id] = current_total_cost
        elif world.options.fp_cost.value == world.options.fp_cost.option_randomize:
            # UT Logic for skill rules
            if getattr(world.multiworld, "generation_is_fake", False) and "fp_costs" in world.slot_data_UT:
                print(world.slot_data_UT)
                fp_cost = world.slot_data_UT["fp_costs"][location.address]
            else:
                fp_cost = fp_random[index]
            fp_rule = HasFP(fp_cost)
            NEW_FP_COSTS[data.id] = fp_cost
        elif world.options.fp_cost.value == world.options.fp_cost.option_vanilla:
            fp_rule = HasFP(data.fp_cost)

        chara_name = name[8:]
        item_name = "SNS Node: " + chara_name
        item_rule = Has(item_name)

        parent_rule = True_()
        for parent in data.parent_nodes:
            parent_rule = parent_rule & Has(parent)

        total_rule = fp_rule & item_rule & parent_rule
        world.set_rule(location, total_rule)
