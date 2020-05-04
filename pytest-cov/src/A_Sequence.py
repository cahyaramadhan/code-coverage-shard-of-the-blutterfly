
class A_Sequence():

    # Ekspresi Aritmatika Sederhana
	def luasLimas(self, sisiAlas, tinggiMiring):
		return (sisiAlas * sisiAlas) + (4 * (sisiAlas * tinggiMiring / 2))
		
    # Ekspresi Aritmatika Sederhana
	def persamaanLinear(self, x):
		return 3 * x - 4

    # Ekspresi Aritmatika Sederhana
	def addDetikWithJam(self, detik, hour, minute, second):
		return detik + (hour * 3600) + (minute * 60) + second

    # Ekspresi Aritmatika Rumit
	def sisaTukarNominalPec1Kdgn50K10K5K(self, nominalUang):
		pec50K = nominalUang / 50000
		pec10K = (nominalUang % 50000) / 10000
		pec5K = ((nominalUang % 50000) % 10000) / 5000
		pec1K = (((nominalUang % 50000) % 10000) % 5000) / 1000
		return int(pec1K)

    # Ekspresi Arimatika Rumit dan Boolean
	def isYearKabisat(self, year):
		return ((year % 4 == 0) and (year % 100 > 0)) or (year % 400 == 0)

    # Ekspresi Relational dan Boolean
	def isPointOrigin(self, x, y):
		return (x == 0) and (y == 0)

    # Ekspresi Relational dan Boolean
	def isPointKuadran1(self, x, y):
		return (x > 0) and (y > 0)

    # Ekspresi Relational dan Boolean
	def isPointKuadran2(self, x, y):
		return (x < 0) and (y > 0)

    # Ekspresi Relational dan Boolean
	def isPointKuadran3(self, x, y):
		return (x < 0) and (y < 0)

    # Ekspresi Relational dan Boolean
	def isPointKuadran4(self, x, y):
		return (x > 0) and not(y >= 0)

    # Ekspresi Relational dan Boolean
	def isPointNotOrigin(self, x, y):
		return (x != 0) or (y != 0)

    # Ekspresi Relational dan Boolean
	def isSuhuPadat(self, suhu):
		return (suhu <= 0)

    # Ekspresi Relational dan Boolean
	def isSuhuCair(self, suhu):
		return (suhu >= 0 and suhu <= 100)

    # Ekspresi Relational dan Boolean
	def isSuhuUap(self, suhu):
		return (suhu >= 100)
