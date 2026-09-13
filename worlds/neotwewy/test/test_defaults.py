from worlds.neotwewy.location_data import LOCATION_DATA, NEOTwewyLocationType
from worlds.neotwewy.test.bases import NEOTwewyTestBase


class TestDefault(NEOTwewyTestBase):
    options = {
        "minamimoto_pin": False,
        "shops": False,
        "dive": False,
        "noise_drops": False,
        "min_drop_rate": 30,
        "pig_drops": False,
    }

    def test_day_entrance_conditions(self) -> None:
        with self.subTest("Test reaching W1D2"):
            self.collect_by_name("Secret Report No. 1")
            self.assertTrue(self.can_reach_region("W1D2"))
        with self.subTest("Test reaching W1D3"):
            self.assertFalse(self.can_reach_region("W1D3"))
            self.collect_by_name("Secret Report No. 2")
            self.assertTrue(self.can_reach_region("W1D3"))

    def test_no_minamimoto_starting_pin(self):
        self.assertRaises(KeyError, self.world.get_location, "W1D1 - Minamimoto's Pin")

    def test_other_locations_not_in_world(self):
        with self.subTest("Test that no shop locations are in world"):
            for location_name, location_data in LOCATION_DATA.items():
                if location_data.location_type == NEOTwewyLocationType.Shop:
                    self.assertRaises(KeyError, self.world.get_location, location_name)
                if location_data.location_type == NEOTwewyLocationType.Dive:
                    self.assertRaises(KeyError, self.world.get_location, location_name)
                if location_data.location_type == NEOTwewyLocationType.NoiseDrop:
                    self.assertRaises(KeyError, self.world.get_location, location_name)
                if location_data.location_type == NEOTwewyLocationType.Pig:
                    self.assertRaises(KeyError, self.world.get_location, location_name)

    def test_reach_w1_d3_2(self):
        with self.subTest("Test reaching W1D3'"):
            # w1d3_2 = self.world.get_region("W1D3'")
            self.assertFalse(self.can_reach_region("W1D3'"))
            self.collect_by_name("Secret Report No. 1")
            self.collect_by_name("Secret Report No. 2")
            self.assertTrue(self.can_reach_region("W1D3'"))