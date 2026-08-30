from __future__ import annotations

from dataclasses import dataclass

from Options import Choice, OptionGroup, PerGameCommonOptions, Range, Toggle, Visibility


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


class NoiseDrops(Toggle):
    """
    Includes drops from noise as locations.
    This also includes the following progress requirements:
    - Wall Reaper on W1D2 guarding Dogenzaka from 104 requiring Midaregami.
    """

    display_name = "Noise Drops"


class MinimumDropRateForLogic(Range):
    """
    The minimum drop rate in % a drop needs to be able to reach after modifiers to be considered in logic.
    The following things affect drop rate:
    - Furthest day reached & expected level reduction bonus (+ level - 1)
    - Skill Plentiful Pins (up to x1.2 to level reduction bonus)
    - Skill Chain Extender (up to x20)
    - Killer Remix (x3)
    - Threads with drop rate increasing abilities while having access to
    an efficient source of style [Muscat Grape Crêpe or Air in Can]
    """

    display_name = "Minimum achievable Drop Rate required for Drop to be in Logic"
    range_start = 0
    range_end = 100
    default = 30


class DeprioritizeNonChainable(Toggle):
    """
    Deprioritize drops of noise that cannot be chained, so they do not contain progression items.
    This affects mostly bosses unless the "Bossy Noise" skill is randomized.
    """

    display_name = "Deprioritize Non-Chainable Drops"


class PreventOutOfLogicDrops(Toggle):
    """
    This prevent noise drops that are considered out of logic to occur.
    A common example would be: the EASY drop of a noise can occur even though EASY is not unlocked by failing the rng
    roll for the NORMAL drop but succeeding the one for the EASY drop.
    This option would prevent this from happening.
    """

    display_name = "Prevent out-of-logic Noise Drops"

class PigDrops(Toggle):
    """
    Includes drops from pigs as locations.
    This also includes the following logic requirements:
    - Pig Carols require pins of the corresponding affinity.
    """

    display_name = "Pig Drops"

class DLCOptions(Choice):
    """
    Decide how to handle the "Legendary Threads Set" and the "Reapers' Game Survival Set".
    This setting can add 7 seven locations.
    - vanilla: Keep them as they are normally.
    - disable: Sets will not be given out when starting a new game.
    - randomize: Randomize the sets as locations and include their items in the item pool.
    - randomize_without_content: Randomize the sets as locations and do not include their items in the item pool.
    """

    display_name = "DLC Options"

    option_vanilla = 0
    option_disable = 1
    option_randomize = 2
    option_randomize_without_content = 3

    default = option_vanilla

@dataclass
class NEOTwewyOptions(PerGameCommonOptions):
    minamimoto_pin: MinamimotoStartingPin
    shops: IncludeShops
    dive: Dive
    noise_drops: NoiseDrops
    min_drop_rate: MinimumDropRateForLogic
    deprioritize_non_chain: DeprioritizeNonChainable
    prevent_out_of_logic: PreventOutOfLogicDrops
    pig_drops: PigDrops
    dlc_options: DLCOptions


option_groups = [
    OptionGroup("General Gameplay Options", [MinamimotoStartingPin, IncludeShops, Dive, PigDrops, DLCOptions]),
    OptionGroup(
        "Noise Options", [NoiseDrops, MinimumDropRateForLogic, DeprioritizeNonChainable, PreventOutOfLogicDrops]
    ),
]
