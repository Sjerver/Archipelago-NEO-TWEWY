from __future__ import annotations

from dataclasses import dataclass

from Options import OptionGroup, PerGameCommonOptions, Toggle


class MinamimotoStartingPin(Toggle):
    """
    Includes additional copy of Minamimoto's Starting Pin in the location pool.
    """

    display_name = "Randomize Minamimoto's Starting Pin"

class IncludeShops(Toggle):
    """
    Includes shop item as locations.
    Additionally, splits W1D3 into two regions.
    """

    display_name = "Include Shops"


@dataclass
class NEOTwewyOptions(PerGameCommonOptions):
    minamimoto_pin: MinamimotoStartingPin
    shops: IncludeShops

option_groups = [OptionGroup("Gameplay Options", [MinamimotoStartingPin, IncludeShops])]
