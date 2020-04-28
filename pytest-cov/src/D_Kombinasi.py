
class D_Kombinasi():

	def OutputBintang_42(self, N):
		s = ""
		if(N > 0):
			for i in range(1, N+1):
				s += "*"
		else:
			s = "N invalid, harus bernilai positif"
		return s

	def isBilPrima_43(self, bil):
		isPrima = True

		if(bil > 1):
			temp = bil-1
			while(temp > 1 and isPrima == True):
				if(bil % temp == 0):
					isPrima = False
				temp = temp - 1
		return isPrima

	def isAdaBil_45(self, bil, N, cari):
		status = "tidak ketemu"

		if(N <= 0):
			status = "Deretan Bilangan Kosong"
		else:
			for i in range(0, N):
				if(bil[i] == cari):
					status = "bilangan ketemu"

		return status

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
