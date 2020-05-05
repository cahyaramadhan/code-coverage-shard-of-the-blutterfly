from src.B_Selection import b_selection
import unittest

class b_selection_Test(unittest.TestCase) :

    def test_method(self) :
        bi = b_selection() # b_selection instance

        # variasi 5
        self.assertEqual(bi.cariMax3Bil_05(3, 2, 1), 3) # 1 2 4 6
        self.assertEqual(bi.cariMax3Bil_05(3, 4, 1), 4) # 1 2 3 4 6
        self.assertEqual(bi.cariMax3Bil_05(3, 2, 4), 4) # 1 2 4 5 6
        self.assertEqual(bi.cariMax3Bil_05(3, 4, 5), 5) # 1 2 3 4 5 6

        # variasi 6 v1
        self.assertEqual(bi.hitNilaiMutu_06(85, 85, 85, 14), 'A') # 1 2 3 11
        self.assertEqual(bi.hitNilaiMutu_06(70, 70, 70, 14), 'B') # 1 2 4 5 11
        self.assertEqual(bi.hitNilaiMutu_06(55, 55, 55, 14), 'C') # 1 2 4 6 7 11
        self.assertEqual(bi.hitNilaiMutu_06(40, 40, 40, 14), 'D') # 1 2 4 6 8 9 11
        self.assertEqual(bi.hitNilaiMutu_06(25, 25, 25, 14), 'E') # 1 2 4 6 8 10 11

        # variasi 6 v2
        self.assertEqual(bi.hitNilaiMutu_062(85, 85, 85, 14), 'A') # 1 2 3 11
        self.assertEqual(bi.hitNilaiMutu_062(70, 70, 70, 14), 'B') # 1 2 4 5 11
        self.assertEqual(bi.hitNilaiMutu_062(55, 55, 55, 14), 'C') # 1 2 4 6 7 11
        self.assertEqual(bi.hitNilaiMutu_062(40, 40, 40, 14), 'D') # 1 2 4 6 8 9 11
        self.assertEqual(bi.hitNilaiMutu_062(25, 25, 25, 14), 'E') # 1 2 4 6 8 10 11

        # variasi 6 v3
        self.assertEqual(bi.getUpah_063(7, 9), 2000) # 1 2 6 7 9
        self.assertEqual(bi.getUpah_063(7, 15), 5000) # 1 2 6 8 9
        self.assertEqual(bi.getUpah_063(12, 2), 2000) # 1 3 4 6 7 9
        self.assertEqual(bi.getUpah_063(12, 8), 5000) # 1 3 4 6 8 9
        self.assertEqual(bi.getUpah_063(12, 12), 2000) # 1 3 5 6 7 9
        # no case for 1 3 5 6 8 9
        
        # variasi 6 v4
        self.assertEqual(bi.menentukanBilGanjil_064(1), "Ganjil") # 1 2
        self.assertEqual(bi.menentukanBilGanjil_064(2), "Genap") # 1 3

        # variasi 8
        self.assertEqual(bi.tukarNominalUang_08(100000, 3000), (1, 4, 1, 2)) # 1 2 3 4 5 6
        self.assertEqual(bi.tukarNominalUang_08(100000, 100000), (0, 0, 0, 0)) # 1 2 3 4 6
        self.assertEqual(bi.tukarNominalUang_08(100000, 150000), (0, 0, 0, 0)) # 1 2 6

        # variasi 9
        self.assertEqual(bi.getKuadran_09(0, 0), -1) # 1 2 3 4 13
        self.assertEqual(bi.getKuadran_09(1, 1), 1) # 1 2 4 5 6 13
        self.assertEqual(bi.getKuadran_09(-1, 1), 2) # 1 2 4 5 7 8 13
        self.assertEqual(bi.getKuadran_09(-1, -1), 3) # 1 2 4 5 7 9 10 13
        self.assertEqual(bi.getKuadran_09(1, -1), 4) # 1 2 4 5 7 11 12 13
        # no case for 1 2 4 5 7 11 13
        # no case for 1 2 3 4 [other node] 13
        # no case for 1 2 4 13

        # variasi 10 v1
        self.assertEqual(bi.tampilSuhu_10(0), "Padat") # 1 2 6
        self.assertEqual(bi.tampilSuhu_10(100), "Cair") # 1 3 4 6
        self.assertEqual(bi.tampilSuhu_10(10000), "Gas") # 1 3 5 6

        # variasi 10 v2
        self.assertEqual(bi.getNumberDayMonth2_10(1, 2020), 31) # 1 2 9
        self.assertEqual(bi.getNumberDayMonth2_10(4, 2020), 30) # 1 3 4 9
        self.assertEqual(bi.getNumberDayMonth2_10(2, 2100), 28) # 1 3 5 6 7 9
        self.assertEqual(bi.getNumberDayMonth2_10(2, 2000), 29) # 1 3 5 6 8 9
        self.assertEqual(bi.getNumberDayMonth2_10(13, 2000), -1) # 1 3 5 9

        # variasi 12
        self.assertEqual(bi.getSizeKaos_12(180, 70), 'X') # 1 2 3 4 9
        self.assertEqual(bi.getSizeKaos_12(180, 100), 'Unknown') # 1 2 3 9
        self.assertEqual(bi.getSizeKaos_12(160, 70), 'L') # 1 2 5 6 7 9
        self.assertEqual(bi.getSizeKaos_12(160, 100), 'Unknown') # 1 2 5 6 9
        self.assertEqual(bi.getSizeKaos_12(140, 70), 'M') # 1 2 5 8 9

        # Invalid
        self.assertEqual(bi.getDayFromNumber_07(), "Invalid")
        self.assertEqual(bi.calCulateGajih_17(), "Invalid")
        self.assertEqual(bi.getNumberDayMonth_18(), "Invalid")
        self.assertEqual(bi.OutputOperasiPilihan_19(), "Invalid")
        self.assertEqual(bi.OutputSwitchSwitch_20(), "Invalid")
        self.assertEqual(bi.OutputSwitchSwitch_20_1(), "Invalid")