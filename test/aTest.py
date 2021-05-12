import unittest
import sys
import os
ruta = os.path.abspath(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(ruta)
from src.Chain_of_resp import *

class aTest(unittest.TestCase):
    def test_1_Monkey_Squirrel_not_equal(self):
        a = MonkeyHandler()
        b = SquirrelHandler()
        self.assertNotEquals(a.handle,b.handle)

    def test_2(self):
        a = MonkeyHandler()
        b = MonkeyHandler()
        self.assertNotEquals(a,b)
    
    def test_3(self):
       a = MonkeyHandler()
       b = DogHandler()
       self.assertFalse(a == b)


if __name__ == '_main_': unittest.main()