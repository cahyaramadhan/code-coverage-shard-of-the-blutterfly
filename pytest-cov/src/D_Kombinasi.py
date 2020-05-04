
class D_Kombinasi():

    # IF then [For - EndFor] else EndIF
	def OutputBintang_42(self, N):
		s = ""
		if(N > 0):
			for i in range(1, N+1):
				s += "*"
		else:
			s = "N invalid, harus bernilai positif"
		return s

    # IF then [While [IF then EndIF] EndWhile] EndIF
	def isBilPrima_43(self, bil):
		isPrima = True

		if(bil > 1):
			temp = bil-1
			while(temp > 1 and isPrima == True):
				if(bil % temp == 0):
					isPrima = False
				temp = temp - 1
		return isPrima

    # IF then [DoWhile [For [If then EndIF] EndFor] EndDoWhile] EndIF
    def pengurutanBilangan_44(self) :
        # consist of do..while
        return "Invalid"

    # IF then else [For [If then EndIf] EndFor] EndIF
	def isAdaBil_45(self, bil, N, cari):
		status = "tidak ketemu"

		if(N <= 0):
			status = "Deretan Bilangan Kosong"
		else:
			for i in range(0, N):
				if(bil[i] == cari):
					status = "bilangan ketemu"

		return status

	# IF then ElseIF then [DoWhile EndDoWhile] ElseIF [IF then [While EndWhile] else EndIF] else [IF EndIF] EndIF
    def calPangkatDua_46_47(self) :
        # consist of do..while
        return "Invalid"

    # IF then [IF then else [While EndWhile] EndIF For EndFor] else [For EndFor] EndIF
	def desimalToBiner_48(self, bil):
		biner = [0] * 10
		if(bil >= 0):
			if(bil == 0):
				idx = 10
			else:
				calTemp = bil
				idx = 9
				while(calTemp != 1):
					biner[idx] = calTemp % 2
					calTemp = int(calTemp/2)
					idx = idx - 1
				biner[idx] = calTemp
			for i in range(idx-1, -1, -1):
				biner[i] = 0
		else:
			for i in range(0, 10):
				biner[i] = -1
		return biner

	# IF then [IF then [IF then EndIF] else [While [IF then EndIF] EndWhile] EndIF] EndIF
	def GetIndexByElemen_49(self, bil, N, cari):
		ketemu = False
		idx = 0
		if(N > 0):
			if(cari <= 0):
				if(cari < 0):
					idx = -1
			else:
				idx = -2
				i = 0
				# while(i < N or ketemu == True):
				while(i < N or ketemu == False):
					if(bil[i] == cari):
						ketemu = True
						idx = i
					i = i + 1
		return idx

	# IF then [IF then EndIF] else [DoWhile [IF then EndIF] EndDoWhile] EndIF
    def GetElemenTerbesar_50(self) :
        # consist of do..while
        return "Invalid"

