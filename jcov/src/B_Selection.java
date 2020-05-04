package variasisc;

import java.util.Scanner;

public class B_Selection {

	/**
	 * @param args
	 */
	public static void main(String[] args) {
		Scanner scan = new Scanner(System.in);
		B_Selection c1 = new B_Selection();
		
		// mencari bilangan terbesar dari 3 buah bilangan
		int bil1, bil2, bil3;
		bil1 = 50;
		bil2 = 40;
		bil3 = 30;
		System.out.println("bilangan terbesar adalah" + c1.cariMax3Bil_05(bil1, bil2, bil3));
		
		// menghitung nilai mutu
		double uts, uas, tugas; 
		int jumHadir;
		uts = 65;
		uas = 40;
		tugas = 30;
		jumHadir = 10;
		System.out.println("nilai Mutu" + c1.hitNilaiMutu_06(uts, uas, tugas, jumHadir));

		// menghitung jumlah hari dalam suatu bulan pada tahun tertentu
		int month, year, numDays;
		month = scan.nextInt();
		year = scan.nextInt();
		numDays = c1.getNumberDayMonth_18(month, year);
		if (numDays>0)
			System.out.println(numDays);
		else
			System.out.println("Invalid month.");
	}
	
	public int cariMax3Bil_05(int A, int B, int C) {
		int max;
		
		max = A;
		if (max < B) {
			max = B;
		}
		if (max < C) {
			max = C;
		}
		return max;
	}
	
	public char hitNilaiMutu_06(double uts, double uas, double tugas, int hadir){
		char nilaiMutu = ' ';
		float nilai, nilaiHadir;
		
		nilaiHadir = hadir / 14 * 100f;
		nilai = (float) ((0.3 * uts) + (0.4 * uas) + (0.2 * tugas) + (0.1 * nilaiHadir));
			
		if(nilai >= 85) {
			nilaiMutu = 'A';
		}else if (nilai >= 70) {
			nilaiMutu = 'B';
		} else if (nilai >= 55) {
			nilaiMutu = 'C';
		}else if (nilai >= 40) {
			nilaiMutu = 'D';
		} else {
			nilaiMutu = 'E';
		}
		return nilaiMutu;
	}
	
	public char hitNilaiMutu_062(double uts, double uas, double tugas, int hadir){
		char nilaiMutu = ' ';
		double nilai, nilaiHadir;
		
		nilaiHadir = hadir / 14f * 100f;
		nilai = (0.3f * uts) + (0.4f * uas) + (0.2f * tugas) + (0.1f * nilaiHadir);
			
		if(nilai >= 85) {
			nilaiMutu = 'A';
		}else { 
			if (nilai >= 70) {
				nilaiMutu = 'B';
			} else {
				if (nilai >= 55) {
					nilaiMutu = 'C';
				}else {
					if (nilai >= 40) {
						nilaiMutu = 'D';
					} else {
						nilaiMutu = 'E';
					}
				}
			}
		}
		return nilaiMutu;
	}
	public int getUpah_063(int jamMasuk, int jamKeluar){
		int lama, biaya;
		
		if (jamKeluar > jamMasuk) {
			lama = jamKeluar - jamMasuk;
		}else if (jamMasuk > jamKeluar) {
			lama = 12 - jamMasuk + jamKeluar;
		}else{
			lama = 0;
		} 
		if (lama <= 2) {
			biaya = 2000;
		}else {
			biaya = 2000 + ((lama-2) * 500);
		}
		return biaya;
	}

	public void menentukanBilGanjil_064(int bil){
		if (bil % 2 > 0) {
			 System.out.print("Bilangan Ganjil");
		}else{
			System.out.print("Bilangan Genap");
		}
	}
	
	public String getDayFromNumber_07(int idxDay){
		String day = "";
		
		switch(idxDay) {
			case 1: day = "Senin"; break;
			case 2: day = "Selasa"; break;
			case 3: day = "Rabu"; break;
			case 4: day = "Kamis"; break;
			case 5: day = "Jumat"; break;
			case 6: day = "Sabtu"; break;
			case 7: day = "Minggu"; break;  
		} 
		return day;
	}

	public void tukarNominalUang_08(int nominalUang, int totalBelanja) {
		int kembalian, pec50K, pec10K, pec5K, pec1K;
		
		pec50K = 0;
		pec10K = 0; 
		pec5K  = 0; 
		pec1K = 0;
		if (nominalUang > totalBelanja) { 
			kembalian = totalBelanja - nominalUang; 
			
			if(kembalian > 0){
				pec50K = kembalian / 50000; 
				pec10K = (kembalian % 50000) / 10000;
				pec5K = ((kembalian % 50000) % 10000) / 5000;
				pec1K = (((kembalian % 50000) % 10000) % 5000) / 1000;
			}
			System.out.println("Pecahan 50 ribu :" + pec50K + "lembar");
			System.out.println("Pecahan 10 ribu :" + pec10K + "lembar");
			System.out.println("Pecahan 5 ribu :" + pec5K + "lembar");
			System.out.println("Pecahan seribu :" + pec1K + "lembar");
		}
	}

	public int getKuadran_09(int x, int y){
		int kuadran = 0;
		boolean isOnSB = false;
		
		if (x==0 && y==0) {
			isOnSB = true;
		}
		if (!isOnSB) {
			if (x>0 && y>0) {
				kuadran = 1;
		   }else if(x<0 && y>0) {
			   kuadran = 2;
		   }else if(x<0 && y<0) {
			   kuadran = 3;
		   }else if(x>0 && y<0){
			   kuadran = 4;
		   }
		}
		return kuadran;
	}
	
	public void tampilSuhu_10(int suhu){
		if (suhu <0) {
	        System.out.println("Cair");
		}else {
			if ( suhu <= 100 ) {
				System.out.println("Padat");
	        }else{
	          	System.out.println("Gas");
	        }
	    }
	}

	public int getNumberDayMonth2_10(int idxMonth, int year){
		int numDays = 0;
		
		if ((idxMonth == 1) || (idxMonth == 3) || (idxMonth == 5) || (idxMonth == 1) || 
				(idxMonth == 8) || (idxMonth == 10) || (idxMonth == 12)) { 
			numDays = 31; 
		}else if ((idxMonth == 4) || (idxMonth == 6) || (idxMonth == 9) || (idxMonth == 11)){ 
			numDays = 30; 
		}else if ((idxMonth == 2)){ 
			if (((year % 4 == 0) && (year % 100 > 0)) || (year % 400 == 0)) {
				numDays = 29;
			}else {
				numDays = 28;
			} 
		}
		return numDays;
	}
	
	public char getSizeKaos_12(int T, int BB){
		char size = ' ';

		if (T > 170) {
			if ( (BB > 60) && (BB <= 80) ) {
				size = 'X';
			}
		}else { 
		     if (T > 150) {
		    	 if (BB <= 80) {
		    		 size = 'L';
		    	 }
		     }else{ 
		    	 size = 'M';
		     }
		}

		return size;
	}
	
	public int calCulateGajih_17(char gol, int durasiJamKerja) {	
		int upah=0;
		switch (gol) {
			case 'A' : upah = durasiJamKerja * 10000;
				       if (durasiJamKerja > 40) {
				    	   upah = upah + (durasiJamKerja * 5000);
					   }
				       break;
			case 'B' : upah = durasiJamKerja * 7500;
					   if (durasiJamKerja > 40) {
						   upah = upah + (durasiJamKerja * 4000);
					   }
					   break;
			case 'C' : upah = durasiJamKerja * 5000;
					   if (durasiJamKerja > 40) {
						   upah = upah + (durasiJamKerja * 3000);
					   }
					   break;
			case 'D' : upah = durasiJamKerja * 2500;
					   if (durasiJamKerja > 40) {
						   upah = upah + (durasiJamKerja * 2000);
					   }
					   break;
			default : System.out.print("Golongan tidak ada"); break;
		}
		return upah;
	}
	
	public int getNumberDayMonth_18(int idxMonth, int year){
		int numDays = 0;
		
		switch (idxMonth) {
        	case 1: 
        	case 3: 
        	case 5:
        	case 7: 
        	case 8: 
        	case 10:
        	case 12:
        		numDays = 31;
        		break;
        	case 4: 
        	case 6:
        	case 9: 
        	case 11:
        		numDays = 30;
        		break;
        	case 2:
        		if (((year % 4 == 0) && !(year % 100 == 0)) || (year % 400 == 0))
        			numDays = 29;
        		else
        			numDays = 28;
        		break;
        	default:
        		numDays = 0;
        	    break;
     }
		return numDays;
	}
	
	public void OutputOperasiPilihan_19(char pil, int bil){
		// melakukan operasi sesuai dengan pilihan
		// Pil A, --> cek bilangan apakah ganjil, genap
		// Pil B, --> cek bilangan apakah positif, negatif atau bilangan nol
		// Pil C, --> Pangkat dua, jika bilangan positif
		// Pil D, --> Absolutkan, jika bilangan negatif
		// Pil E, --> menampilkan bilangan saja
		// lain-lain --> inputan salah
		// tampilkan hasil operasi jika sudah melakukan pengoperasian
		
		int hasil;
		switch (pil) {
			case 'A': if (bil % 2 > 0) {
						System.out.println("bil (" + bil + ") adalah bilangan Ganjil");
					  }else{
						  System.out.println("bil (" + bil + ") adalah bilangan Genap");  
					  }
					  break;
			case 'B': if (bil > 0) {
						System.out.println("bil (" + bil + ") adalah bilangan Positif");
			  		  }else if(bil < 0) {
			  			System.out.println("bil (" + bil + ") adalah bilangan Negatif");  
			  		  }else{
			  			System.out.println("bil (" + bil + ") adalah bilangan nol");  
			  		  }
			  		  break;
			case 'C': if (bil > 0) {
						hasil = bil * bil;
						System.out.println(bil + "^ 2 = " + hasil);
	  		  		  }
				      break;
			case 'D': if (bil < 0) {
						hasil = bil * (-1);
		  		  	  }
					  break;
			case 'E': System.out.println(bil);
					  break;
			default : System.out.println("Pilihan Salah");
		}
	}
	
	public void OutputSwitchSwitch_20(char abjad, int bil) {	
		// print abjad dari A s.d E dan angka dari 1 s.d 5 sesuai dengan pasangannya
		// A1 --> cetak Huruf Perama - satu
		// selain itu masuk pada kategori lain-lain
		
		switch (abjad) {
			case 'A' : switch (bil) {
							case '1' :  System.out.print("Huruf Pertama - satu");
										break;
							case '2' :  System.out.print("Huruf Pertama - dua"); 
										break;
							case '3' :  System.out.print("Huruf Pertama - tiga"); 
										break;
							case '4' :  System.out.print("Huruf Pertama - empat"); 
										break;
							case '5' :  System.out.print("Huruf Pertama - lima"); 
										break;
							default : System.out.print("Pasangan A tidak ada"); break;
					   }
				       break;
			case 'B' : switch (bil) {
							case '1' :  System.out.print("Huruf Kedua - satu");
										break;
							case '2' :  System.out.print("Huruf Kedua - dua"); 
										break;
							case '3' :  System.out.print("Huruf Kedua - tiga"); 
										break;
							case '4' :  System.out.print("Huruf Kedua - empat"); 
										break;
							case '5' :  System.out.print("Huruf Kedua - lima"); 
										break;
							default : System.out.print("Pasangan B tidak ada"); break;
					   }
					   break;
			case 'C' : switch (bil) {
							case '1' :  System.out.print("Huruf Ketiga - satu");
										break;
							case '2' :  System.out.print("Huruf Ketiga - dua"); 
										break;
							case '3' :  System.out.print("Huruf Ketiga - tiga"); 
										break;
							case '4' :  System.out.print("Huruf Ketiga - empat"); 
										break;
							case '5' :  System.out.print("Huruf Ketiga - lima"); 
										break;
							default : System.out.print("Pasangan C tidak ada"); break;
						}
					   break;
			case 'D' : switch (bil) {
							case '1' :  System.out.print("Huruf Keempat - satu");
										break;
							case '2' :  System.out.print("Huruf Keempat - dua"); 
										break;
							case '3' :  System.out.print("Huruf Keempat - tiga"); 
										break;
							case '4' :  System.out.print("Huruf Keempat - empat"); 
										break;
							case '5' :  System.out.print("Huruf Keempat - lima"); 
										break;
							default : System.out.print("Pasangan D tidak ada"); break;
						}
					   break;
			case 'E' : switch (bil) {
							case '1' :  System.out.print("Huruf Kelima - satu");
										break;
							case '2' :  System.out.print("Huruf Kelima - dua"); 
										break;
							case '3' :  System.out.print("Huruf Kelima - tiga"); 
										break;
							case '4' :  System.out.print("Huruf Kelima - empat"); 
										break;
							case '5' :  System.out.print("Huruf Kelima - lima"); 
										break;
							default : System.out.print("Pasangan E tidak ada"); break;
					   }
				       break;
			default : System.out.print("Pasangan tidak terbentuk"); break;
		}
	}
	
	public void OutputSwitchSwitch_20_1(char abjad, int bil) {	
		// print abjad dari A s.d E dan angka dari 1 s.d 5 sesuai dengan pasangannya
		// A1 --> cetak Huruf Perama - satu
		// selain itu masuk pada kategori lain-lain
		
		switch (abjad) {
			case 'A' : switch (bil) {
							case '1' :  System.out.print("Huruf Pertama - satu");
										break;
							case '2' :  System.out.print("Huruf Pertama - dua"); 
										break;
							case '3' :  System.out.print("Huruf Pertama - tiga"); 
										break;
							default : System.out.print("Pasangan A tidak ada"); break;
					   }
				       break;
			case 'B' : switch (bil) {
							case '1' :  System.out.print("Huruf Kedua - satu");
										break;
							case '2' :  System.out.print("Huruf Kedua - dua"); 
										break;
							default : System.out.print("Pasangan B tidak ada"); break;
					   }
					   break;
			case 'C' : System.out.print("Huruf Ketiga - satu");
					   break;
			case 'D' :  System.out.print("Huruf Keempat");
						break;
			default : System.out.print("Pasangan tidak terbentuk"); break;
		}
	}
	
	// Selection Cukup Rumit
	public String nilaiTerbilang(int bil){
		// mengkonversikan sebuah bilangan dengan range -9999 s.d 9999
		String terbilang = "";
		int ribu, ratus, puluh, satuan;
		String[] terbilangSatuan = {"", "satu ", "dua ", "tiga ", "empat ", "lima ",  
									"enam ", "tujuh ", "delapan ", "sembilan "};
		
		if(bil<0){
			terbilang = "(negatif) ";
		}else if(bil==0){
			terbilang = "nol";
		}
		
		ribu     = bil / 1000;
		ratus    = (bil % 1000) / 100;
		puluh    = ((bil % 1000) % 100) / 10;
		satuan   = ((bil % 1000) % 100) % 10;
		
		if(ribu == 1) {
			terbilang = terbilang + "seribu";
		}else if(ribu >= 2){
			terbilang = terbilang + terbilangSatuan[ribu] + "ribu";
		}
		
		if(ratus == 1) {
			terbilang = terbilang + "seratus";
		}else if(ribu >= 2){
			terbilang = terbilang + terbilangSatuan[ratus] + "ratus";
		}
		
		if(puluh == 0){
			terbilang = terbilang + terbilangSatuan[satuan];
		}else if(puluh == 1) {
			if(satuan == 0) {
				terbilang = terbilang + "sepuluh";
			}else if(satuan == 1) {
				terbilang = terbilang + "sebelas";
			}else if(satuan >= 2){
				terbilang = terbilang + terbilangSatuan[satuan] + "belas";
			}
		}else if(puluh >= 2){
			terbilang = terbilang + terbilangSatuan[puluh] + "puluh" + terbilangSatuan[satuan];
		}
		
		return terbilang;
	}
	
}

