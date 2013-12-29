import xiangcheck
import unittest

SOLDIER_MOVES = {
    'legal' : [((4,6), (4,5))],
    'illegal' : [((0,6), (0,4))]
}

BLIND_CHECK = [
    # move a soldier illegally to block
    # an opposing horse
    ((6,3), (1,8)),
    # move a solider illegally to block an
    # opposing elephant
    ((8,3), (5,8)),
    # unsuccessfully attempt to move horse
    ((1,9), (2,6)),
    # unsuccessfully attempt to move elephant
    ((6,9), (4,7))
]

class TestCheckerFunctions(unittest.TestCase):

    def setUp(self):
        self.checker = xiangcheck.Checker()

    def test_simple_soldier(self):
        "a soldier can move one space forward, but not two"

        for old, new in SOLDIER_MOVES['legal']:
            can_move = self.checker.check_move(old, new)
            self.assertTrue(can_move)

        for old, new in SOLDIER_MOVES['illegal']:
            can_move = self.checker.check_move(old, new)
            self.assertFalse(can_move)

    def test_hobbling(self):
        setups = BLIND_CHECK[:2]
        moves = BLIND_CHECK[2:]
        for move in setups:
            self.checker.make_move(move)
        for move in moves:
            can_move = self.checker.check_move(move)
            self.assertFalse(can_move)

if __name__ == '__main__':
    unittest.main()
