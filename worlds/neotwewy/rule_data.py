from __future__ import annotations

from collections.abc import Callable
from typing import TYPE_CHECKING

from Options import Toggle
from rule_builder.rules import Has, HasAny, HasGroup, Rule

from .item_data import JOLI_BECOT_THREADS, NEOTwewyItemGroup

if TYPE_CHECKING:
    from .world import NEOTwewyWorld

REGION_RULES: list[tuple[str, str, Rule, Callable[[NEOTwewyWorld], bool | Toggle]]] = [
    ("W1D1", "W1D2", HasGroup(NEOTwewyItemGroup.SECRET_REPORT.value, 1), lambda world: True),
    ("W1D2", "W1D2'", Has("Midaregami"), lambda world: world.options.noise_drops),
    ("W1D2'", "W1D3", HasGroup(NEOTwewyItemGroup.SECRET_REPORT.value, 2), lambda world: True),
    ("W1D3", "W1D3'", HasAny(*JOLI_BECOT_THREADS), lambda world: world.options.shops),
    ("W1D3'", "W1D4", HasGroup(NEOTwewyItemGroup.SECRET_REPORT.value, 3), lambda world: True),
    ("W1D4", "W1D5", HasGroup(NEOTwewyItemGroup.SECRET_REPORT.value, 4), lambda world: True),
]


SKILL_EVENT_RULES: list[tuple[str, int]] = [
    ("Hard Unlocked", 4),
    ("Easy Unlocked", 1),
]
