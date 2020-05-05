class c_looping :
  def OutputBintang_21(self, n) :
    for i in range(0, n) :
      print("*", end="")

  def jumBil_22(self, bil, n) :
    sum = 0
    i = 0
    while (i < n) :
      sum = sum + bil[i]
      i = i + 1
    return sum

  def jumBil_23(self, bil, n) :
    sum = 0
    i = 0
    while (True) :
      sum = sum + bil[i]
      i = i + 1
      if (i > n) :
        break
    return sum

  def outputFaktorBilangan_24(self, n) :
    print("faktor-faktornya")
    for i in range(1, n + 1) :
      if (n % i == 0) :
        print(i, end=" ")

  def cariBil_25(self, bil, n, cari) :
    i = 0
    ketemu = False
    while (i < n and ketemu == False) :
      if (bil[i] == cari) :
        ketemu = True
      i = i + 1
    return ketemu

  def outputDeretGanjilGenap(self, n) :  
    i = 0
    nGanjil = 0
    nGenap = 0

    deretGanjil = [0] * n
    deretGenap = [0] * n

    for i in range(1, n + 1) :
      if (i % 2 > 0) :
        deretGanjil[nGanjil] = i
        nGanjil = nGanjil + 1
      else :
        deretGenap[nGenap] = i
        nGenap = nGenap + 1

    print("Deret ganjil")
    for i in range(0, nGanjil) :
      print(deretGanjil[i] + " ")

    print("Deret genap")
    for i in range(0, nGenap) :
      print(deretGenap[i] + " ")

  def guessNumber_28(self, guessBil, n, secret) :
    i = 0
    ketemu = False
    while (i < n and ketemu == False) :
      if (guessBil[i] < secret) :
        print("too low")
        print("try again")
      elif (guessBil[i] > secret) :
        print("too high")
        print("try again")
      else :
        print("got em")
        print("secret =", secret)
        ketemu = True
      i = i + 1
    return ketemu

  def OutputPolaXYZ_29(self, n, x) :
    i = 1
    while (True) :
      if (i % x == 0) :
        print("*", end=" ")
      else :
        print(i, end=" ")
      if (i > n) :
        break
      i = i + 1

  def outputCountBilPencacah_30(self, bil, n) :
    count1 = 0
    count2 = 0
    count3 = 0
    countUnd = 0
    for i in range(0, n) :
      if (bil[i] == 1) :
        count1 = count1 + 1
      if (bil[i] == 2) :
        count2 = count2 + 1
      if (bil[i] == 3) :
        count3 = count3 + 1
      if (bil[i] < 1 and bil[i] > 3) :
        countUnd = countUnd + 1

    print("c1 =", count1)
    print("c2 =", count3)
    print("c3 =", count2)
    print("cUnd =", countUnd)

  def outputCalculateDeretBilBaseOnOp(self, bil, n, op) :
    result = 0
    if (op == '*') :
      result = 1
    i = 0
    while (i < n) :
      if (op == '+') :
        result = result + bil[i]
      if (op == '-') :
        result = result - bil[i]
      if (op == '*') :
        result = result * bil[i]
    return result

  def konversiToBiner_32(self, bil) :
    sisa = 0
    biner = ""

    while (True) :
      sisa = bil % 2
      bil = bil / 2
      if (sisa == 0) :
        biner += "0"
      else :
        biner += "1"
      if (bil == 0) :
        break

    return biner

  def OutputBintangSegiempat_33(self, n) :
    for i in range(0, n) :
      for j in range(0, i) :
        print("*", end="")
      print("")

  def OutputBintangSegitiga_34(self, n) :
    i = 1
    while (i <= n) :
      for j in range(0, i) :
        print("*", end="")
      print("")
      i = i + 1

  def geserBilKiri_36(self, str, n, nGeser) :
    i = 0
    j = 0
    for i in range(0, nGeser) :
      temp = str[n - 1]
      j = n - 1
      while (j > 0) :
        str[j] = str[j - 1]
        j = j - 1
      str[j] = temp
    return str

  def OutputBintangSegitigaTerbalik_37(self, n) :
    i = 1
    while (i <= n) :
      j = 1
      while (j < i) :
        print(" ", end="")
        j = j + 1
      while (j <= n) :
        print(" ", end="")
        j = j + 1
      print("")
      i = i + 1
