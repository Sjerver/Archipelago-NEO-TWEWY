from __future__ import annotations

from collections.abc import Mapping
from typing import Any

from worlds.AutoWorld import World

# Imports of your world's files must be relative.
from . import items, locations, regions, rules, web_world
from . import options as neo_twewy_options


class NEOTwewyWorld(World):
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

    item_name_groups = items.ITEM_GROUPS

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
            return self.options.as_dict("minamimoto_pin")