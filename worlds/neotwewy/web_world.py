from __future__ import annotations

from BaseClasses import Tutorial
from worlds.AutoWorld import WebWorld

from .options import option_groups


class NEOTwewyWebWorld(WebWorld):
    game = "NEO The World Ends with You"

    theme = "stone"

    setup_en = Tutorial(
            "Multiworld Setup Guide",
            "A guide to setting up NEO The World Ends with You for MultiWorld.",
            "English",
            "setup_en.md",
            "setup/en",
            ["Sjerver"],
        )
    tutorials = [setup_en]  # noqa: RUF012
    option_groups = option_groups
