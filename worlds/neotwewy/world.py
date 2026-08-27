from __future__ import annotations

from collections.abc import Mapping
from math import ceil
from typing import Any

from rule_builder.cached_world import CachedRuleBuilderWorld

from . import item_data, items, locations, regions, rules, web_world
from . import options as neo_twewy_options
from .location_data import ENEMY_DROPS


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

    origin_region_name = "W1D1"

    item_name_groups = item_data.ITEM_GROUPS

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

    def fill_slot_data(self) -> Mapping[str, Any]:
        # If you need access to the player's chosen options on the client side, there is a helper for that.
        options_dict = self.options.as_dict("prevent_out_of_logic", "min_drop_rate")

        noise_drop_reqs: dict[str, dict[str, Any]] = {
            name: {
                "min_drop_rate": max(1, ceil((self.options.min_drop_rate / 100) / data_id.chance)),
                "chainable": data_id.chainable,
                "blue_noise": data_id.blue_noise,
            }
            for name, data_id in ENEMY_DROPS.items()
        }

        return {"options": options_dict, "noise_drop_reqs": noise_drop_reqs}
