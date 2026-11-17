from __future__ import annotations

from collections.abc import Mapping
from typing import Any

from rule_builder.cached_world import CachedRuleBuilderWorld
from . import item_data, items, locations, regions, rules, web_world
from . import options as neo_twewy_options


class NEOTwewyWorld(CachedRuleBuilderWorld):
    """
    NEO: The World Ends with You is a game that needs a description
    """

    game = "NEO: The World Ends with You"

    web = web_world.NEOTwewyWebWorld()

    options_dataclass = neo_twewy_options.NEOTwewyOptions
    options: neo_twewy_options.NEOTwewyOptions

    location_name_to_id = locations.LOCATION_NAME_TO_ID
    item_name_to_id = items.ITEM_NAME_TO_ID

    origin_region_name = "W1D0"

    item_name_groups = item_data.ITEM_GROUPS

    slot_data_UT: dict[str, Any] = {}

    def create_regions(self) -> None:
        regions.create_and_connect_regions(self)
        locations.create_all_locations(self)

    def set_rules(self) -> None:
        rules.set_all_rules(self)

    def create_items(self) -> None:
        items.create_all_items(self)

    def create_item(self, name: str) -> items.NEOTwewyItem:
        return items.create_item_with_correct_classification(self, name)

    def get_filler_item_name(self) -> str:
        return items.get_random_filler_item_name(self)

    def create_filler(self, filler_first: list[str] = []) -> items.NEOTwewyItem:
        if filler_first.__len__() > 0:
            return self.create_item(filler_first.pop())
        return self.create_item(self.get_filler_item_name())

    def fill_slot_data(self) -> Mapping[str, Any]:
        # If you need access to the player's chosen options on the client side, there is a helper for that.
        options_dict = self.options.as_dict("prevent_out_of_logic", "min_drop_rate", "dlc_options",
                                            "soundsurf", "sns", "shops", "cutscene_skip_speed", "shop_hints",
                                            "skill_hints")
        options_dict["fp_costs"] = rules.NEW_FP_COSTS

        if self.options.secret_report_hints:
            secret_report_hints: dict[int, tuple[int, int | None, int]] = {}
            for item in self.item_name_groups["Secret Report"]:
                item_in_pool = next(
                    (pool_item.name == item for pool_item in self.multiworld.itempool if pool_item.name == item), False)
                if item_in_pool:
                    loc = self.multiworld.find_item(item, self.player)
                    for index, sphere in enumerate(self.multiworld.get_spheres()):
                        if loc in sphere:
                            secret_report_hints[item_data.ITEM_DATA[item].id] = (loc.player, loc.address, index)

            options_dict["secret_report_hints"] = secret_report_hints
        return {"options": options_dict}

    def interpret_slot_data(self, slot_data: dict[str, Any]) -> None:
        if "options" in slot_data:
            if "fp_costs" in slot_data["options"]:
                self.slot_data_UT["fp_costs"] = {int(address): fp_cost for address, fp_cost in
                                                 slot_data["options"]["fp_costs"].items()}
                print(self.slot_data_UT["fp_costs"])
        rules.set_skill_rules(self)
