from worlds.neotwewy.test.bases import NEOTwewyTestBase


class TestPigs(NEOTwewyTestBase):
    options = {
        "minamimoto_pin": False,
        "shops": True,
        "dive": False,
        "noise_drops": True,
        "min_drop_rate": 0,
        "pig_drops": True,
    }

    def test_elemental_pig(self) -> None:
        self.assertFalse(self.can_reach_location("W1D3 - Pig Carol (104 Building)"))

        # Reaching W1D3
        self.collect_by_name("Secret Report No. 1")
        self.collect_by_name("Secret Report No. 2")
        self.collect_by_name("Midaregami")

        self.assertFalse(self.can_reach_location("W1D3 - Pig Carol (104 Building)"))

        self.collect_by_name("Firestorm")
        self.assertTrue(self.can_reach_location("W1D3 - Pig Carol (104 Building)"))
