from worlds.neotwewy.test.bases import NEOTwewyTestBase


class TestDefault(NEOTwewyTestBase):
    options = {
        "minamimoto_pin": False
    }

def test_no_minamimoto_starting_pin(self):
    self.assertRaises(KeyError, self.world.get_location, "W1D1 - Minamimoto's Pin")