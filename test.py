
import unittest
from seq import Seq

class TestSeq(unittest.TestCase):
    def test_times2minus2(self):
        seq = Seq()
        self.assertEqual(seq.times2minus2(3), 4)
        self.assertEqual(seq.times2minus2(-1), -4)
        self.assertEqual(seq.times2minus2(0), -2)

unittest.main()
