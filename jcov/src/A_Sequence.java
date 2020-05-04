public class A_Sequence {

    // Ekspresi Aritmatika Sederhana
	public float luasLimas(float sisiAlas, float tinggiMiring) {
		float luas;
		luas = (sisiAlas * sisiAlas) + (4 * (sisiAlas * tinggiMiring / 2));
		return luas;	
	}
	
    // Ekspresi Aritmatika Sederhana
	public int persamaanLinear(int x) {
		int y;	
		y = 3 * x - 4;		
		return y;	
	}
	
    // Ekspresi Aritmatika Sederhana
	public int addDetikWithJam(int detik, int hour, int minute, int second){
		int s;
		
		s = (hour * 3600) + (minute * 60) + second;
		detik = detik + s;
		return detik;
	}
	
    // Ekspresi Aritmatika Rumit
	public int sisaTukarNominalPec1Kdgn50K10K5K(int nominalUang){
		int pec50K, pec10K, pec5K, pec1K;
		
		pec50K = nominalUang / 50000;
		pec10K = (nominalUang % 50000) / 10000;
		pec5K = ((nominalUang % 50000) % 10000) / 5000;
		pec1K = (((nominalUang % 50000) % 10000) % 5000) / 1000;
		return pec1K;	
	}
	
    // Ekspresi Arimatika Rumit dan Boolean
	public boolean isYearKabisat(int idxMonth, int year){
		boolean isKabisat;
		
		isKabisat = ((year % 4 == 0) && (year % 100 > 0)) || (year % 400 == 0); 
		return isKabisat;
	}
	
    // Ekspresi Relational dan Boolean
	public boolean isPointOrigin(int x, int y){
		boolean isOrigin;
		
		isOrigin = (x == 0)  && (y == 0); 
		return isOrigin;
	}
	
    // Ekspresi Relational dan Boolean
	public boolean isPointKuadran1(int x, int y){
		boolean isKuadran1;
		
		isKuadran1 = (x > 0)  && (y > 0); 
		return isKuadran1;
	}
	
    // Ekspresi Relational dan Boolean
	public boolean isPointKuadran2(int x, int y){
		boolean isKuadran2;
		
		isKuadran2 = (x < 0)  && (y > 0); 
		return isKuadran2;
	}
	
    // Ekspresi Relational dan Boolean
	public boolean isPointKuadran3(int x, int y){
		boolean isKuadran3;
		
		isKuadran3 = (x < 0)  && (y < 0); 
		return isKuadran3;
	}
	
    // Ekspresi Relational dan Boolean
	public boolean isPointKuadran4(int x, int y){
		boolean isPointKuadran4;
		
		isPointKuadran4 = (x > 0)  && !(y >= 0); 
		return isPointKuadran4;
	}
	
    // Ekspresi Relational dan Boolean
	public boolean isPointNotOrigin(int x, int y){
		boolean isNotOrigin;
		
		isNotOrigin = (x != 0) || (y != 0); 
		return isNotOrigin;
	}
	
    // Ekspresi Relational dan Boolean
	public boolean isSuhuPadat(int suhu){
		boolean isPadat;
		
		isPadat = (suhu<= 0); 
		return isPadat;
	}
	
    // Ekspresi Relational dan Boolean
	public boolean isSuhuCair(int suhu){
		boolean isCair;
		
		isCair = (suhu >=0 && suhu<= 100);
		return isCair;
	}
	
    // Ekspresi Relational dan Boolean
	public boolean isSuhuUap(int suhu){
		boolean isUap;
		
		isUap = (suhu >= 100); 
		return isUap;
	}
}
