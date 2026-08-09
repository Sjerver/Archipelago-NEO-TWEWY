from __future__ import annotations

from dataclasses import dataclass

from Options import OptionGroup, PerGameCommonOptions, Toggle, Visibility


class MinamimotoStartingPin(Toggle):
    """
    Includes additional copy of Minamimoto's Starting Pin in the location pool.
    Adds 1 additional location.
    """

    display_name = "Randomize Minamimoto's Starting Pin"


class IncludeShops(Toggle):
    """
    Includes shop item as locations.
    This also includes the following progress requirements:
    - Wall Reaper on W1D3 guarding Center Street from Scramble Crossing requiring 1 Joli Bécot branded thread.
    """

    display_name = "Include Shops"


class Dive(Toggle):
    """
    Includes dive rank rewards as locations.
    """

    display_name = "Dive"
    visibility = Visibility.none


@dataclass
class NEOTwewyOptions(PerGameCommonOptions):
    minamimoto_pin: MinamimotoStartingPin
    shops: IncludeShops
    dive: Dive


option_groups = [OptionGroup("Gameplay Options", [MinamimotoStartingPin, IncludeShops, Dive])]
