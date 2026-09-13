from worlds.neotwewy.location_data import LOCATION_DATA, NEOTwewyLocationType
from worlds.neotwewy.test.bases import NEOTwewyTestBase

# Current known lowest drop rate: Swing Shark HARD Drop of 0.08


class Test0Drops(NEOTwewyTestBase):
    options = {
        "minamimoto_pin": False,
        "shops": True,
        "dive": True,
        "noise_drops": True,
        "min_drop_rate": 0,
        "pig_drops": False,
    }

    def test_noise_drops_exist(self):
        with self.subTest("Test that noise_drops locations are in world"):
            for location_name, location_data in LOCATION_DATA.items():
                if location_data.location_type == NEOTwewyLocationType.NoiseDrop:
                    try:
                        self.world.get_location(location_name)
                    except KeyError:
                        self.fail(f"Noise Drop location {location_name} not in world")

    def test_0_drops(self) -> None:
        self.assertFalse(self.can_reach_location("Swing Shark HARD Drop"))

        # Reaching W1D4
        self.collect_by_name("Secret Report No. 1")
        self.collect_by_name("Secret Report No. 2")
        self.collect_by_name("Secret Report No. 3")

        with self.subTest("Test reaching W1D2' without Midaregami"):
            self.assertFalse(self.can_reach_region("W1D2'"))
            self.collect_by_name("Midaregami")
            self.assertTrue(self.can_reach_region("W1D2'"))

        self.collect_by_name("Dazzling Denim Cap")

        self.assertFalse(self.can_reach_location("Swing Shark HARD Drop"))

        # Should unlock Hard Mode
        self.collect_by_name("5 FP")
        self.collect_by_name("5 FP")

        self.assertTrue(self.can_reach_location("Swing Shark HARD Drop"))


class Test1000Drops(NEOTwewyTestBase):
    options = {
        "minamimoto_pin": False,
        "shops": True,
        "dive": True,
        "noise_drops": True,
        "min_drop_rate": 100,
        "pig_drops": False,
    }

    def test_lowest_drops(self) -> None:
        self.assertFalse(self.can_reach_location("Swing Shark HARD Drop"))

        # Reaching W1D4
        self.collect_by_name("Secret Report No. 1")
        self.collect_by_name("Secret Report No. 2")
        self.collect_by_name("Secret Report No. 3")
        self.collect_by_name("Midaregami")
        self.collect_by_name("Dazzling Denim Cap")

        self.assertFalse(self.can_reach_location("Swing Shark HARD Drop"))

        # Should unlock Hard Mode
        self.collect_by_name("5 FP")
        self.collect_by_name("5 FP")
        # Since we can chain should be true
        self.assertTrue(self.can_reach_location("Swing Shark HARD Drop"))
        # self.assertFalse(self.can_reach_location("Swing Shark HARD Drop"))
        # #Increases drop rate by 1 -> Multiplier = 18
        # self.collect_by_name("Oversized Beanie")
        #
        # self.assertFalse(self.can_reach_location("Swing Shark HARD Drop"))
        # #Increases drop rate by 5
        # self.collect_by_name("Hippie Shoulder Bag")
        #
        # self.assertTrue(self.can_reach_location("Swing Shark HARD Drop"))
