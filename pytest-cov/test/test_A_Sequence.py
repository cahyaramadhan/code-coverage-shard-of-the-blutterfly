import unittest
from src.A_Sequence import A_Sequence

testObj = A_Sequence()

def test_luasLimas():
	assert testObj.luasLimas(2, 3) == 16

def test_persamaanLinear():
	assert testObj.persamaanLinear(10) == 26

def test_addDetikWithJam():
	assert testObj.addDetikWithJam(500, 1, 10, 50) == 4750

def test_sisaTukarNominalPec1Kdgn50K10K5K():
	assert testObj.sisaTukarNominalPec1Kdgn50K10K5K(1002000) == 2

def test_isYearKabisat():
	assert testObj.isYearKabisat(2020) == True
	assert testObj.isYearKabisat(2019) == False

def test_isPointOrigin():
	assert testObj.isPointOrigin(0,0) == True
	assert testObj.isPointOrigin(2,0) == False
	assert testObj.isPointOrigin(0,2) == False

def test_isPointKuadran1():
	assert testObj.isPointKuadran1(2,2) == True
	assert testObj.isPointKuadran1(0,2) == False
	assert testObj.isPointKuadran1(2,0) == False

def test_isPointKuadran2():
	assert testObj.isPointKuadran2(-2,2) == True
	assert testObj.isPointKuadran2(0,2) == False
	assert testObj.isPointKuadran2(-2,0) == False

def test_isPointKuadran3():
	assert testObj.isPointKuadran3(-2,-2) == True
	assert testObj.isPointKuadran3(0,-2) == False
	assert testObj.isPointKuadran3(-2,0) == False

def test_isPointKuadran4():
	assert testObj.isPointKuadran4(2,-2) == True
	assert testObj.isPointKuadran4(0,-2) == False
	assert testObj.isPointKuadran4(2,0) == False

def test_isPointNotOrigin():
	assert testObj.isPointNotOrigin(2,0) == True
	assert testObj.isPointNotOrigin(0,2) == True
	assert testObj.isPointNotOrigin(0,0) == False

def test_isSuhuPadat():
	assert testObj.isSuhuPadat(-50) == True
	assert testObj.isSuhuPadat(0) == True
	assert testObj.isSuhuPadat(50) == False

def test_isSuhuCair():
	assert testObj.isSuhuCair(-50) == False
	assert testObj.isSuhuCair(0) == True
	assert testObj.isSuhuCair(50) == True
	assert testObj.isSuhuCair(100) == True
	assert testObj.isSuhuCair(150) == False

def test_isSuhuUap():
	assert testObj.isSuhuUap(50) == False
	assert testObj.isSuhuUap(100) == True
	assert testObj.isSuhuUap(150) == True
