from worlds.neotwewy.location_data import LOCATION_DATA, NEOTwewyLocationType
from worlds.neotwewy.test.bases import NEOTwewyTestBase


class TestDefault(NEOTwewyTestBase):
    options = {"sns": True}

    def test_vip_node_location(self):
        with self.subTest("Test that VIP node location can be accessed"):
            vip_location = "[SNS] Yudai Miki: Reach VIP Level 3 for HOG FANG"

            self.assertFalse(self.can_reach_location(vip_location))

            # Reaching day 3
            self.collect_by_name("Secret Report No. 1")
            self.collect_by_name("Secret Report No. 2")
            self.assertFalse(self.can_reach_location(vip_location))

            # Collect VIP levels
            prog = self.get_item_by_name("Progressive VIP HOG FANG")
            self.collect(prog)
            self.assertFalse(self.can_reach_location(vip_location))
            self.collect(prog)
            self.assertTrue(self.can_reach_location(vip_location))


class TestSNSOff(NEOTwewyTestBase):
    options = {"sns": False}

    def test_sns_off_locked_locations(self):
        with self.subTest("Test that locked sns locations are in world"):
            for location_name, location_data in LOCATION_DATA.items():
                if location_data.location_type == NEOTwewyLocationType.SocialNode:
                    if location_data.lock:
                        try:
                            self.world.get_location(location_name)
                        except KeyError:
                            self.fail(f"Shop location {location_name} not in world")
