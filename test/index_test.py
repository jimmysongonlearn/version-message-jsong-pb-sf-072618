from unittest import TestCase
from ipynb.fs.full.index import *


class VersionMessageTest(TestCase):

    def test_serialize(self):
        v = VersionMessage(timestamp=0, nonce=b'\x00' * 8)
        self.assertEqual(v.serialize().hex(), '7f11010000000000000000000000000000000000000000000000000000000000000000000000ffff000000008d20000000000000000000000000000000000000ffff000000008d2000000000000000001b2f70726f6772616d6d696e67626c6f636b636861696e3a302e312f0000000001')
