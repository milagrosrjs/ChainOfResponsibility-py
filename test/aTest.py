import unittest
import sys
import os
ruta = os.path.abspath(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(ruta)
from src.Chain_of_resp import *

class aTest(unittest.TestCase):
    def test_1_should_be_true_if_Monkey_and_Squirrel_are_not_equals(self):
        a = MonkeyHandler()
        b = SquirrelHandler()
        self.assertNotEquals(a.handle,b.handle)

    def test_2_should_be_true_if_differents_monkeyHandlers_are_not_equals(self):
        a = MonkeyHandler()
        b = MonkeyHandler()
        self.assertNotEquals(a,b)
    
    def test_3_should_be_true_if_Monkey_and_Dog_are_differents(self):
       a = MonkeyHandler()
       b = DogHandler()
       self.assertFalse(a == b)


if __name__ == '_main_': unittest.main()