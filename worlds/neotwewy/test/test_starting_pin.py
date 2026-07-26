from worlds.neotwewy.test.bases import NEOTwewyTestBase


class TestStartingPin(NEOTwewyTestBase):
    options = {
        "minamimoto_pin": True
    }

def test_day_entrance_conditions(self):
    with self.subTest("Test reaching W1D2"):
        self.collect_by_name("Secret Report No. 1")
        self.assertTrue(self.can_reach_region("W1D2"))
    with self.subTest("Test reaching W1D3"):
        self.collect_by_name("Secret Report No. 1")
        self.assertFalse(self.can_reach_region("W1D3"))

        self.collect_by_name("Secret Report No. 2")
        self.assertTrue(self.can_reach_region("W1D3"))

def test_minamimoto_starting_pin(self):
    try:
        self.world.get_location("W1D1 - Minamimoto's Pin")
    except KeyError:
        self.fail("Minamimoto's Pin should exist, but it doesn't.")