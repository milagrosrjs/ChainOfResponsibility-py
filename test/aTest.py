import unittest
import sys
import os
ruta = os.path.abspath(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(ruta)
from src.main import *

class aTest(unittest.TestCase):
    def test_1(self):
        a = Successor1()
        b = Successor2()
        self.assertNotEquals(a,b)
    
    def test_2(self):
        a = Successor1()
        b = Successor1()
        self.assertEquals(a.handle(1), b.handle(1))

    def test_3(self):
        a = Successor1()
        b = Successor2()
        self.assertNotEquals(a.handle(1), b.handle(1))
    


if __name__ == '_main_': unittest.main()