from worlds.neotwewy.test.bases import NEOTwewyTestBase


class TestStartingPin(NEOTwewyTestBase):
    options = {
        "minamimoto_pin": True
    }

    def test_minamimoto_starting_pin(self) -> None:
        try:
            self.world.get_location("W1D1 - Minamimoto's Pin")
        except KeyError:
            self.fail("Minamimoto's Pin should exist, but it doesn't.")
