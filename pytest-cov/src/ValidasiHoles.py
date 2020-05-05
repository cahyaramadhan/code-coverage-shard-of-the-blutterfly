class ValidasiHoles :
  def countHoles(self, sentence) :
    jumlahLubang = 0

    for i in range(0, len(sentence)) :
      if (sentence[i] == 'A' or sentence[i] == 'D' or \
          sentence[i] == 'O' or sentence[i] == 'P' or \
          sentence[i] == 'Q' or sentence[i] == 'R') :
        jumlahLubang = jumlahLubang + 1
      elif (sentence[i] == 'B') :
        jumlahLubang = jumlahLubang + 2

    return jumlahLubang
