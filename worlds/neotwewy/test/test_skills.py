from worlds.neotwewy.location_data import LOCATION_DATA, NEOTwewyLocationType
from worlds.neotwewy.options import FPCost
from worlds.neotwewy.rules import NEW_FP_COSTS
from worlds.neotwewy.test.bases import NEOTwewyTestBase

TEST_SKILL = "[Skill] Hirofumi Itoguchi"


class TestSkill(NEOTwewyTestBase):
    options = {"skills": True}

    def test_skills(self):
        with self.subTest(f"Test skill {TEST_SKILL} with vanilla FP costs"):
            self.assertFalse(self.can_reach_location(TEST_SKILL))

            # Reaching day 4
            self.collect_by_name("Secret Report No. 1")
            self.collect_by_name("Secret Report No. 2")
            self.collect_by_name("Secret Report No. 3")
            self.assertTrue(self.can_reach_location(TEST_SKILL))


class TestSkillVanillaFP(NEOTwewyTestBase):
    options = {"skills": True, "sns": True, "dive": True}

    def test_skills_vanilla_fp(self):
        with self.subTest(f"Test skill {TEST_SKILL} with vanilla FP costs"):
            self.assertFalse(self.can_reach_location(TEST_SKILL))

            # Reaching day 4
            self.collect_by_name("Secret Report No. 1")
            self.collect_by_name("Secret Report No. 2")
            self.collect_by_name("Secret Report No. 3")
            self.assertFalse(self.can_reach_location(TEST_SKILL))

            # FP Requirement
            skill_data = LOCATION_DATA[TEST_SKILL]
            fp_cost = skill_data.fp_cost
            current_fp = 0
            items = self.multiworld.get_items()
            state = self.multiworld.state
            fp_items = [i for i in items if i.name == "5 FP" or i.name == "2 FP" or i.name == "FP"]
            while current_fp < fp_cost:
                self.collect(fp_items.pop())
                current_fp = (
                        state.prog_items[self.player]["5 FP"] * 5
                        + state.prog_items[self.player]["2 FP"] * 2
                        + state.prog_items[self.player]["FP"]
                )

            # Parent Nodes
            skill_data = LOCATION_DATA[TEST_SKILL]
            for parent_name in skill_data.parent_nodes:
                parent = self.get_item_by_name(parent_name)
                self.collect(parent)
            self.assertFalse(self.can_reach_location(TEST_SKILL))

            # Own Node
            chara_name = TEST_SKILL[8:]
            self.collect(self.get_item_by_name("SNS Node: " + chara_name))
            self.assertTrue(self.can_reach_location(TEST_SKILL))


class TestSkillCumulativeFP(NEOTwewyTestBase):
    options = {"skills": True, "fp_cost": FPCost.option_cumulative, "sns": True, "dive": True}

    def test_skills_cumulative_fp(self):
        with self.subTest(f"Test skill {TEST_SKILL} work with cumulative FP costs"):

            self.assertFalse(self.can_reach_location(TEST_SKILL))

            # Reaching day 4
            self.collect_by_name("Secret Report No. 1")
            self.collect_by_name("Secret Report No. 2")
            self.collect_by_name("Secret Report No. 3")
            self.assertFalse(self.can_reach_location(TEST_SKILL))

            # FP Requirement
            location = self.world.get_location(TEST_SKILL)
            fp_cost = NEW_FP_COSTS[location.address]
            current_fp = 0
            items = self.multiworld.get_items()
            state = self.multiworld.state
            fp_items = [i for i in items if i.name == "5 FP" or i.name == "2 FP" or i.name == "FP"]
            while current_fp < fp_cost:
                self.collect(fp_items.pop())
                current_fp = (
                        state.prog_items[self.player]["5 FP"] * 5
                        + state.prog_items[self.player]["2 FP"] * 2
                        + state.prog_items[self.player]["FP"]
                )

            # Parent Nodes
            skill_data = LOCATION_DATA[TEST_SKILL]
            for parent_name in skill_data.parent_nodes:
                parent = self.get_item_by_name(parent_name)
                self.collect(parent)
            self.assertFalse(self.can_reach_location(TEST_SKILL))

            # Own Node
            chara_name = TEST_SKILL[8:]
            self.collect(self.get_item_by_name("SNS Node: " + chara_name))
            self.assertTrue(self.can_reach_location(TEST_SKILL))


class TestSkillRandomFP(NEOTwewyTestBase):
    options = {"skills": True, "fp_cost": FPCost.option_randomize, "sns": True, "dive": True}

    def test_skills_cumulative_fp(self):
        with self.subTest(f"Test {TEST_SKILL} work with cumulative FP costs"):

            self.assertFalse(self.can_reach_location(TEST_SKILL))

            # Reaching day 4
            self.collect_by_name("Secret Report No. 1")
            self.collect_by_name("Secret Report No. 2")
            self.collect_by_name("Secret Report No. 3")
            self.assertFalse(self.can_reach_location(TEST_SKILL))

            # FP Requirement
            location = self.world.get_location(TEST_SKILL)
            fp_cost = NEW_FP_COSTS[location.address]
            current_fp = 0
            items = self.multiworld.get_items()
            state = self.multiworld.state
            fp_items = [i for i in items if i.name == "5 FP" or i.name == "2 FP" or i.name == "FP"]
            while current_fp < fp_cost:
                self.collect(fp_items.pop())
                current_fp = (
                        state.prog_items[self.player]["5 FP"] * 5
                        + state.prog_items[self.player]["2 FP"] * 2
                        + state.prog_items[self.player]["FP"]
                )

            # Parent Nodes
            skill_data = LOCATION_DATA[TEST_SKILL]
            for parent_name in skill_data.parent_nodes:
                parent = self.get_item_by_name(parent_name)
                self.collect(parent)
            self.assertFalse(self.can_reach_location(TEST_SKILL))

            # Own Node
            chara_name = TEST_SKILL[8:]
            self.collect(self.get_item_by_name("SNS Node: " + chara_name))
            self.assertTrue(self.can_reach_location(TEST_SKILL))


class TestSkillsOff(NEOTwewyTestBase):
    options = {"skill": False}

    def test_sns_off_locked_locations(self):
        with self.subTest("Test that locked skills locations are in world"):
            for location_name, location_data in LOCATION_DATA.items():
                if location_data.location_type == NEOTwewyLocationType.Skill:
                    if location_data.lock:
                        try:
                            self.world.get_location(location_name)
                        except KeyError:
                            self.fail(f"Skill location {location_name} not in world")
                    else:
                        try:
                            self.world.get_location(location_name)
                            self.fail(f"Skill location {location_name} not in world")
                        except KeyError:
                            pass
