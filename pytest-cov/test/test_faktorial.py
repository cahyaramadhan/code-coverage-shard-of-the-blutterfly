import unittest
from src.faktorial import faktorial

testObj = faktorial()

def test_faktorial_3() :
  assert testObj.factorial(3) == 6

def test_faktorial_5() :
  assert testObj.factorial(5) == 120

def test_faktorial_wrong() :
  assert testObj.factorial(-2) == -1
