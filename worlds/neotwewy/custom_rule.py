from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING

from typing_extensions import override

from BaseClasses import CollectionState
from NetUtils import JSONMessagePart
from rule_builder.field_resolvers import resolve_field
from rule_builder.rules import Rule

from .item_data import DROP_INCREASING_THREADS, ITEM_DATA, ITEM_GROUPS
from .regions import EXPECTED_LEVEL_PER_REGION

if TYPE_CHECKING:
    from .world import NEOTwewyWorld


@dataclass()
class HasFP(Rule["NEOTwewyWorld"], game="NEO: The World Ends with You"):
    count: int = 1
    """FP required for this rule to return true"""

    @override
    def _instantiate(self, world: NEOTwewyWorld) -> Rule.Resolved:
        count = resolve_field(self.count, world, int)
        return self.Resolved(count, player=world.player, caching_enabled=True)

    class Resolved(Rule.Resolved):
        count: int = 1

        @override
        def _evaluate(self, state: CollectionState) -> bool:
            fp = (
                state.prog_items[self.player]["5 FP"] * 5
                + state.prog_items[self.player]["2 FP"] * 2
                + state.prog_items[self.player]["FP"]
            )
            return fp >= self.count

        @override
        def item_dependencies(self) -> dict[str, set[int]]:
            # this function is only required if you have caching enabled
            required_items = []
            required_items.extend(ITEM_GROUPS["FP"])
            return {i: {id(self)} for i in required_items}

        @override
        def explain_json(self, state: CollectionState | None = None) -> list[JSONMessagePart]:
            verb = "Missing " if state and not self(state) else "Has "
            messages: list[JSONMessagePart] = [{"type": "text", "text": verb}]

            if self.count > 1:
                messages.append({"type": "color", "color": "cyan", "text": str(self.count)})
                messages.append({"type": "text", "text": "x "})
            if state:
                color = "green" if self(state) else "salmon"
                messages.append({"type": "color", "color": color, "text": "FP"})
            else:
                messages.append({"type": "item_name", "flags": 0b001, "text": "FP", "player": self.player})
            return messages

        @override
        def explain_str(self, state: CollectionState | None = None) -> str:
            if state is None:
                return str(self)
            prefix = "Has" if self(state) else "Missing"
            count = f"{self.count}x " if self.count > 1 else ""
            return f"{prefix} {count} FP"

        @override
        def __str__(self) -> str:
            count = f"{self.count}x " if self.count > 1 else ""
            return f"Has {count} FP"


@dataclass()
class ReachedMinimumDropRate(Rule["NEOTwewyWorld"], game="NEO: The World Ends with You"):
    base_drop_rate: float
    """The base drop rate of the location"""

    chainable: bool = True
    """Is the location chainable?"""

    blue_noise: bool = False
    """Is the location only chainable as a blue boss symbol?"""

    @override
    def _instantiate(self, world: NEOTwewyWorld) -> Rule.Resolved:
        base_drop_rate = resolve_field(self.base_drop_rate, world, float)
        chainable = resolve_field(self.chainable, world, bool)
        blue_noise = resolve_field(self.blue_noise, world, bool)
        return self.Resolved(
            base_drop_rate,
            world.options.min_drop_rate / 100,
            chainable,
            blue_noise,
            player=world.player,
            caching_enabled=True,
        )

    class Resolved(Rule.Resolved):
        base_drop_rate: float
        min_drop_rate: float
        chainable: bool = True
        blue_noise: bool = False

        @override
        def _evaluate(self, state: CollectionState) -> bool:
            if self.base_drop_rate >= self.min_drop_rate:
                return True
            return self.calculate_drop_rate(state)[0] >= self.min_drop_rate

        def calculate_drop_rate(
            self,
            state: CollectionState,
        ) -> tuple[float, float]:
            drop_rate = 0.0 + self.base_drop_rate

            inventory = state.prog_items[self.player]

            drop_multiplier = 1.0

            level_multiplier = 1.0
            if inventory["Plentiful Pins (MKN)"] > 0:
                level_multiplier += 0.1
            if inventory["Plentiful Pins (Yoko Norimoto)"] > 0:
                level_multiplier += 0.1

            furthest_level = 1
            for region, level in EXPECTED_LEVEL_PER_REGION.items():
                if not state.can_reach_region(region, self.player):
                    break
                furthest_level = level
            drop_multiplier += furthest_level * level_multiplier

            # only once you can reach day 3 for food to get to minimum style reqs [50 max required right now]
            if inventory["Restaurant Access"] > 0:
                drop_increasing_items = DROP_INCREASING_THREADS
                for thread in drop_increasing_items:
                    if inventory[thread] > 0:
                        # TODO: Techinally we need to calculate available thread slots here
                        drop_multiplier += ITEM_DATA[thread].drop_increase

            chain_length = 1
            if self.chainable and (not self.blue_noise or (self.blue_noise and inventory["Bossy Noise"] > 0)):
                chain_length = 5
                if (
                    inventory["Chain Extender (Tsukihime)"] > 0
                    or inventory["Chain Extender (Tanzo Kubo)"] > 0
                    or inventory["Chain Extender (Seiji-of-Some-Trades)"] > 0
                ):
                    # Since everything above a 10-chain is unrealistic in a lot of areas
                    chain_length += 5

            drop_multiplier *= chain_length

            if inventory["Killer Remix"] > 0:
                drop_multiplier *= 3  # TODO: Playable Character Count * 0.5 max 3

            return min(1.0, drop_rate * drop_multiplier), drop_multiplier

        @override
        def item_dependencies(self) -> dict[str, set[int]]:
            required_items = [
                "Plentiful Pins (MKN)",
                "Plentiful Pins (Yoko Norimoto)",
                "Chain Extender (Tsukihime)",
                "Chain Extender (Tanzo Kubo)",
                "Chain Extender (Seiji-of-Some-Trades)",
                "Bossy Noise",
                "Killer Remix",
            ]
            required_items.extend(DROP_INCREASING_THREADS)
            return {i: {id(self)} for i in required_items}

        @override
        def region_dependencies(self) -> dict[str, set[int]]:
            return {region_name: {id(self)} for region_name in EXPECTED_LEVEL_PER_REGION.keys()}

        @override
        def explain_json(self, state: CollectionState | None = None) -> list[JSONMessagePart]:
            if state is None:
                drop_rate = self.base_drop_rate
                drop_multiplier = 1.0
            else:
                drop_rate, drop_multiplier = self.calculate_drop_rate(state)

            required_drop_modifier = self.min_drop_rate / self.base_drop_rate
            has_min_drop_rate = drop_rate >= self.min_drop_rate

            # Requires a minimum drop rate of X / drop rate multiplier of Y
            color = "yellow"

            start = "Requires a minimum drop rate of "
            mid = " / a drop rate multiplier of "
            end = ""
            drop_rate_string = f"{self.min_drop_rate * 100}%"
            drop_modifier_string = f"{required_drop_modifier}"
            drop_modifier_end_string = ""
            if has_min_drop_rate:
                # Drop rate of x can be achieved with drop rate multiplier z
                start = "Drop rate of "
                mid = " can be achieved with drop rate multiplier "
                end = "(Required: "
                drop_rate_string = f"{self.min_drop_rate * 100}%"
                drop_modifier_string = f"{drop_multiplier}"
                drop_modifier_end_string = f"{required_drop_modifier})"
            elif state is not None:
                # Drop rate of x cannot be achieved with drop rate multiplier z. Needs to be at least y
                start = "Drop rate of "
                mid = " cannot be achieved with drop rate multiplier "
                end = ". Needs to be at least "
                drop_rate_string = f"{self.min_drop_rate * 100}%"
                drop_modifier_string = f"{drop_multiplier}"
                drop_modifier_end_string = f"{required_drop_modifier}"
            return [
                {"type": "text", "text": start},
                {"type": "color", "color": color, "text": drop_rate_string},
                {"type": "text", "text": mid},
                {"type": "color", "color": color, "text": drop_modifier_string},
                {"type": "text", "text": end},
                {"type": "color", "color": color, "text": drop_modifier_end_string},
            ]

        @override
        def explain_str(self, state: CollectionState | None = None) -> str:
            required_drop_modifier = self.min_drop_rate / self.base_drop_rate
            if self.base_drop_rate >= self.min_drop_rate:
                return (
                    f"Drop rate of {self.min_drop_rate * 100}% can be achieved with "
                    "drop rate multiplier 1"
                    f"(Required: {required_drop_modifier})"
                )
            if state is None:
                return str(self)
            drop_rate, drop_multiplier = self.calculate_drop_rate(state)
            has_min_drop_rate = drop_rate >= self.min_drop_rate

            if has_min_drop_rate:
                return (
                    f"Drop rate of {self.min_drop_rate * 100}% can be achieved with "
                    f"drop rate multiplier {drop_multiplier}."
                    f"(Required: {required_drop_modifier})"
                )
            return (
                f"Drop rate of {self.min_drop_rate * 100}% cannot be achieved with "
                f"drop rate multiplier {drop_multiplier}."
                f". Needs to be at least {required_drop_modifier}"
            )

        @override
        def __str__(self) -> str:
            required_drop_modifier = self.min_drop_rate / self.base_drop_rate
            return f"Requires drop rate of {self.min_drop_rate * 100}% / drop rate modifier of {required_drop_modifier}"
