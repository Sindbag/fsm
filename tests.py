import unittest

from fsm import Ticketer


class Tests(unittest.TestCase):
    """
    test.exe -i test.fsm -o 0.seq -m black_box -mt hsi

    v/'' v/Ticket v/''
    v/'' x/Ticket v/Ticket
    v/'' w/5 v/''
    x/Ticket v/''
    w/0 v/''

    mut.py –target fsm –unit-test tests -m
    """
    def setUp(self):
        self.ticketer = Ticketer()

    def test1(self):
        out = []
        for i in ['v', 'v', 'v']:
            out.append(self.ticketer.read(i))
        self.assertEqual(out, ['', 'Ticket', ''])

    def test2(self):
        out = []
        for i in ['v', 'x', 'v']:
            out.append(self.ticketer.read(i))
        self.assertEqual(out, ['', 'Ticket', 'Ticket'])

    def test3(self):
        out = []
        for i in ['v', 'w', 'v']:
            out.append(self.ticketer.read(i))
        self.assertEqual(out, ['', 5, ''])

    def test4(self):
        out = []
        for i in ['x', 'v']:
            out.append(self.ticketer.read(i))
        self.assertEqual(out, ['Ticket', ''])

    def test5(self):
        out = []
        for i in ['w', 'v']:
            out.append(self.ticketer.read(i))
        self.assertEqual(out, [0, ''])
