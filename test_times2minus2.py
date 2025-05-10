import unittest
from seq import Seq

class TestTimes2Minus2(unittest.TestCase):
    def test_times2minus2(self): 
        seq = Seq()
        self.assertEqual(seq.times2minus2(3), 4)
unittest.main()