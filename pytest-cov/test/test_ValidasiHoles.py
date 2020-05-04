import unittest
from src.ValidasiHoles import ValidasiHoles

testObj = ValidasiHoles()

def test_ValidasiHoles_1_1() :
  assert testObj.countHoles("A") == 1

def test_ValidasiHoles_1_2() :
  assert testObj.countHoles("O") == 1

def test_ValidasiHoles_1_3() :
  assert testObj.countHoles("D") == 1

def test_ValidasiHoles_1_4() :
  assert testObj.countHoles("P") == 1

def test_ValidasiHoles_1_5() :
  assert testObj.countHoles("Q") == 1

def test_ValidasiHoles_1_6() :
  assert testObj.countHoles("R") == 1

def test_ValidasiHoles_2() :
  assert testObj.countHoles("B") == 2

def test_ValidasiHoles_rnd_1() :
  assert testObj.countHoles("AOPDQRBX") == 8

def test_ValidasiHoles_rnd_1() :
  assert testObj.countHoles("WWW") == 0