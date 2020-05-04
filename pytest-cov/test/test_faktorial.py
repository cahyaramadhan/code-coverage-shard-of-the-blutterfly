import unittest
from faktorial import *

def test_faktorial_3() :
  assert factorial(3) == 6

def test_faktorial_5() :
  assert factorial(5) == 120

def test_faktorial_wrong() :
  assert factorial(-2) == -1