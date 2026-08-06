from worlds.neotwewy.locations import LOCATION_DATA, NEOTwewyLocationType
from worlds.neotwewy.test.bases import NEOTwewyTestBase


class TestDefault(NEOTwewyTestBase):
    options = {"minamimoto_pin": False, "shops": True}

    def test_shops_in_logic(self):
        with self.subTest("Test that shop locations are in world"):
            for location_name, location_data in LOCATION_DATA.items():
                if location_data.location_type == NEOTwewyLocationType.Shop:
                    try:
                        self.world.get_location(location_name)
                    except KeyError:
                        self.fail(f"Shop location {location_name} not in world")

    def reach_w1_d3_2(self):
        with self.subTest("Test reaching W1D3' requiring Joli Becot Thread"):
            w1d3_2 = self.world.get_region("W1D3'")
            self.assertFalse(w1d3_2.can_reach(self.multiworld.state))
            self.collect_by_name("Secret Report No. 1")
            self.collect_by_name("Secret Report No. 2")
            self.assertFalse(w1d3_2.can_reach(self.multiworld.state))

            self.collect_by_name("Shredded Jeans")
            self.assertTrue(w1d3_2.can_reach(self.multiworld.state))
