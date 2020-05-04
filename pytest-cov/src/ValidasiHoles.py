class ValidasiHoles :
  def countHoles(sentence) :
    jumlahLubang = 0

    for i in range(0, len(sentence)) :
      if (sentence[i] == 'A' || sentence[i] == 'D' || 
          sentence[i] == 'O' || sentence[i] == 'P' || 
          sentence[i] == 'Q' || sentence[i] == 'R') :
        jumlahLubang = jumlahLubang + 1
      else if (sentence[i] == 'B')
        jumlahLubang = jumlahLubang + 2

    return jumlahLubang
