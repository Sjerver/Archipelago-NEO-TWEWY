from __future__ import annotations

from dataclasses import dataclass

from Options import OptionGroup, PerGameCommonOptions, Toggle


class MinamimotoStartingPin(Toggle):
    """
    Includes Minamimoto's Starting Pin in the item pool.
    """

    display_name = "Randomize Minamimoto's Starting Pin"


@dataclass
class NEOTwewyOptions(PerGameCommonOptions):
    minamimoto_pin: MinamimotoStartingPin

option_groups = [OptionGroup("Gameplay Options", [MinamimotoStartingPin])]