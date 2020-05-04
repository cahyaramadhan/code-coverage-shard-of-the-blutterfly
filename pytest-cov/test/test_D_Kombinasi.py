import unittest
from src.D_Kombinasi import D_Kombinasi

testObj = D_Kombinasi()

def test_OutputBintang_42():
	assert testObj.OutputBintang_42(5) == "*****"
	assert testObj.OutputBintang_42(-5) == "N invalid, harus bernilai positif"

def test_isBilPrima_43():
	assert testObj.isBilPrima_43(0) == False
	assert testObj.isBilPrima_43(1) == False
	assert testObj.isBilPrima_43(7) == True
	assert testObj.isBilPrima_43(10) == False

def test_pengurutanBilangan_44():
	assert testObj.pengurutanBilangan_44() == "Invalid"

def test_isAdaBil_45():
	deret = []
	assert testObj.isAdaBil_45(deret, len(deret), 5) == "Deretan Bilangan Kosong"
	deret = [1,2,3,4,5]
	assert testObj.isAdaBil_45(deret, len(deret), 6) == "tidak ketemu"
	assert testObj.isAdaBil_45(deret, len(deret), 5) == "bilangan ketemu"

def test_calPangkatDua_46_47():
	assert testObj.calPangkatDua_46_47() == "Invalid"


def test_desimalToBiner_48():
	assert testObj.desimalToBiner_48(-10) == [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1]
	assert testObj.desimalToBiner_48(1) == [0,0,0,0,0,0,0,0,0,1]
	assert testObj.desimalToBiner_48(7) == [0,0,0,0,0,0,0,1,1,1]
	assert testObj.desimalToBiner_48(0) == [0,0,0,0,0,0,0,0,0,0]

def test_GetIndexByElemen_49():
	deret = []
	assert testObj.GetIndexByElemen_49(deret, len(deret), 5) == -1
	deret = [1,2,3,4,5]
	assert testObj.GetIndexByElemen_49(deret, len(deret), 6) == -1
	assert testObj.GetIndexByElemen_49(deret, len(deret), 5) == 4
	assert testObj.GetIndexByElemen_49(deret, len(deret), 0) == -1
	assert testObj.GetIndexByElemen_49(deret, len(deret), -1) == -1

def test_GetElemenTerbesar_50():
	assert testObj.GetElemenTerbesar_50() == "Invalid"