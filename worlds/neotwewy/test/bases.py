from test.bases import WorldTestBase
from worlds.neotwewy import NEOTwewyWorld


class NEOTwewyTestBase(WorldTestBase):
    game = "NEO: The World Ends with You"
    world: NEOTwewyWorld
