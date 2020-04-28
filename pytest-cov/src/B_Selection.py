
class b_selection :

    def __init__(self):
        super().__init__()

    # IF then EndIF
    def cariMax3Bil_05(self, A, B, C) :
        max = A # 1
        if max < B : # 2
            max = B # 3
        if max < C : # 4
            max = C # 5
        return max # 6

    # IF then-else EndIF
    def hitNilaiMutu_06(self, uts, uas, tugas, hadir) :
        nilaiHadir = hadir / 14 * 100 # 1
        nilai = (0.3 * uts) + (0.4 * uas) + (0.2 * tugas) + (0.1 * nilaiHadir)

        if(nilai >= 85) : # 2
            nilaiMutu = 'A' # 3
        elif (nilai >= 70) : # 4
            nilaiMutu = 'B' # 5
        elif (nilai >= 55) : # 6
            nilaiMutu = 'C' # 7
        elif (nilai >= 40) : # 8
            nilaiMutu = 'D' # 9
        else :
            nilaiMutu = 'E' # 10
        return nilaiMutu # 11

    # IF then-else EndIF
    def hitNilaiMutu_062(self, uts, uas, tugas, hadir) :
        nilaiHadir = hadir / 14 * 100 # 1
        nilai = (0.3 * uts) + (0.4 * uas) + (0.2 * tugas) + (0.1 * nilaiHadir)

        if nilai >= 85 : # 2
            nilaiMutu = 'A' # 3
        else :
            if nilai >= 70 : # 4
                nilaiMutu = 'B' # 5
            else :
                if nilai >= 55 : # 6
                    nilaiMutu = 'C' # 7
                else :
                    if nilai >= 40 : # 8
                        nilaiMutu = 'D' # 9
                    else :
                        nilaiMutu = 'E' # 10
        return nilaiMutu # 11

    # IF then-else EndIF
    def getUpah_063(self, jamMasuk, jamKeluar) :
        if jamKeluar > jamMasuk : # 1
            lama = jamKeluar - jamMasuk # 2
        elif jamMasuk > jamKeluar : # 3
            lama = 12 - jamMasuk + jamKeluar # 4
        else :
            lama = 0 # 5
        if lama <= 2 : # 6
            biaya = 2000 # 7
        else :
            biaya = 2000 + (lama-2) * 500 # 8
        return biaya # 9

    # IF then-else EndIF
    def menentukanBilGanjil_064(self, bil) :
        if bil % 2 > 0 : # 1
            return "Ganjil" # 2
        else :
            return "Genap" # 3

    # Switch Case lebih dari satu kondisi
    def getDayFromNumber_07(self) :
        # consist of switch case
        return "Invalid"

    # IF then [IF then EndIF] EndIF
    def tukarNominalUang_08(self, nominalUang, totalBelanja) :
        pec50K, pec10K, pec5K, pec1K = 0, 0, 0, 0 # 1
        if nominalUang >= totalBelanja : # 2
            kembalian = nominalUang - totalBelanja # 3
            if kembalian > 0 : # 4
                pec50K = int(kembalian / 50000) # 5
                pec10K = int((kembalian % 50000) / 10000)
                pec5K = int(((kembalian % 50000) % 10000) / 5000)
                pec1K = int((((kembalian % 50000) % 10000) % 5000) / 1000)
        return pec50K, pec10K, pec5K, pec1K # 6

    # IF then [IF then-else EndIF] EndIF
    def getKuadran_09(self, x, y) :
        isOnSB = False # 1
        if x==0 or y==0 : # 2
            isOnSB = True # 3
        if not isOnSB : # 4
            if x>0 and y>0 : # 5
                kuadran = 1 # 6
            elif x<0 and y>0 : # 7
                kuadran = 2 # 8
            elif x<0 and y<0 : # 9
                kuadran = 3 # 10
            elif x>0 and y<0 : # 11
                kuadran = 4 # 12
        return -1 if isOnSB else kuadran # 13

    # IF then-else [IF then EndIF] EndIF
    def tampilSuhu_10(self, suhu) :
        if suhu <= 0 : # 1
            wujud = "Padat" # 2
        else :
            if suhu <= 100 : # 3
                wujud = "Cair" # 4
            else :
                wujud = "Gas" # 5
        return wujud # 6

    # IF then-else [IF then EndIF] EndIF
    def getNumberDayMonth2_10(self, idxMonth, year) :
        if idxMonth == 1 or idxMonth == 3 or idxMonth == 5 or idxMonth == 7 \
            or idxMonth == 8 or idxMonth == 10 or idxMonth == 12 : # 1
            numDays = 31 # 2
        elif idxMonth == 4 or idxMonth == 6 or idxMonth == 9 or idxMonth == 11 : # 3
            numDays = 30 # 4
        elif idxMonth == 2 : # 5
            if (year % 4 == 0 and year % 100 > 0) or (year % 400 == 0) : # 6
                numDays = 29 # 7
            else :
                numDays = 28 # 8
        return numDays if idxMonth > 0 and idxMonth < 13 else -1 # 9

    # IF then [IF then EndIF] else [IF then-else EndIF] EndIF
    def getSizeKaos_12(self, T, BB) :
        size = ' ' # 1
        if T > 170 : # 2
            if BB > 60 and BB <= 80 : # 3
                size = 'X' # 4
        else :
            if T > 150 : # 5
                if BB <= 80 : # 6
                    size = 'L' # 7
            else :
                size = 'M' # 8
        return size # 9

    # Switch Case : Struktur IF then EndIF
    def calCulateGajih_17(self) :
        # consist of switch case
        return "Invalid"

    # Switch Case : Struktur IF then-else EndIF
    def getNumberDayMonth_18(self) :
        # consist of switch case
        return "Invalid"

    # Switch Case : Struktur IF then EndIF dan Struktur IF then-else EndIF
    def OutputOperasiPilihan_19(self) :
        # consist of switch case
        return "Invalid"

    # Switch Case : Switch Case
    def OutputSwitchSwitch_20(self) :
        # consist of switch case
        return "Invalid"

    # Switch Case : Switch Case
    def OutputSwitchSwitch_20_1(self) :
        # consist of switch case
        return "Invalid"

    # Ga tau ini variasi struktur mana sih
    def nilaiTerbilang(self, bil) :
        terbilang = '' # 1
        terbilangSatuan = ["", "satu ", "dua ", "tiga ", "empat ", "lima ",  
                            "enam ", "tujuh ", "delapan ", "sembilan "]
        
        if bil < 0 : # 2
            bil = abs(bil) # 3
            terbilang = "(negatif) "
        elif bil == 0 : # 4
            terbilang = "nol" # 5

        ribu     = int(bil / 1000) # 6
        ratus    = int((bil % 1000) / 100)
        puluh    = int(((bil % 1000) % 100) / 10)
        satuan   = int(((bil % 1000) % 100) % 10)

        if ribu == 1 : # 7
            terbilang = terbilang + "seribu" # 8
        elif ribu >= 2 : # 9
            terbilang = terbilang + terbilangSatuan[ribu] + "ribu" # 10

        if ratus == 1 : # 11
            terbilang = terbilang + "seratus" # 12
        elif ribu >= 2 : # 13
            terbilang = terbilang + terbilangSatuan[ratus] + "ratus" # 14

        if puluh == 0 : # 15
            terbilang = terbilang + terbilangSatuan[satuan] # 16
        elif puluh == 1 : # 17
            if satuan == 0 : # 18
                terbilang = terbilang + "sepuluh" # 19
            elif satuan == 1 : # 20
                terbilang = terbilang + "sebelas" # 21
            elif satuan >= 2 : # 22
                terbilang = terbilang + terbilangSatuan[satuan] + "belas" # 23
        elif puluh >= 2 : # 24
            terbilang = terbilang + terbilangSatuan[puluh] + "puluh" + terbilangSatuan[satuan] # 25

        return terbilang # 26
        