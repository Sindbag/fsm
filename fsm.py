#!/usr/bin/env python3

import sys
from collections import defaultdict

ALPHABET = {'v': 5,
            'x': 10,
            'w': -1}


class Ticketer:
    """
    Билетёр.

    Входной алфавит: x, v, w (3 символа)
    Выходной алфавит: '', 'Ticket', 5, 0

    Состояния:
    id  #v  #x
    0   0   0
    1   1   0

    Переходы:
    #Fr #Sym    #To #Out
    0   v       1   ''
    0   x       0   'Ticket'
    0   w       0   0
    1   v       0   'Ticket'
    1   x       1   'Ticket'
    1   w       0   5
    """
    TICKET_PRICE = 10

    @classmethod
    def with_price(cls, price):
        obj = cls()
        obj.TICKET_PRICE = price
        return obj

    def __init__(self):
        self.inputs = defaultdict(int)  # reinitialize for each, non-static member

    def sum(self):
        return sum(v * ALPHABET[k] for k, v in self.inputs.items())

    def read(self, symbol):
        val = ALPHABET.get(symbol, None)
        if not val:
            raise Exception('unknown symbol')
        elif val == -1:  # hardcoded for withdraw
            ret = self.sum()
            self.inputs = defaultdict(int)
            return ret

        self.inputs[symbol] += 1

        if self.sum() >= self.TICKET_PRICE:
            count = 0
            while count < self.TICKET_PRICE:
                for sym, val in sorted(ALPHABET.items(), key=lambda x: -x[1]):
                    while (self.inputs.get(sym, 0) > 0) and count < self.TICKET_PRICE:
                        self.inputs[sym] -= 1
                        count += ALPHABET[sym]
            return 'Ticket'
        return ''


if __name__ == '__main__':
    ticketer = Ticketer()
    for line in sys.stdin.readlines():
        for sym in line.strip():
            print(ticketer.read(sym))
