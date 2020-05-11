import java.util.*;

public class Main {

		public static String alphabetSoup(){
	        String result ="";
                  	char[] charAr = new char[]{'a','b','r','a','c','a','d','e','r','a'};
		for (int i = 0; i < charAr.length; i++) 
        {
                       if(charAr[i] =='a')
                         result = result +"hi"   ;
                       else
                          result = result +  charAr[i] ;
        }
		
		return result;
	}
	
	public static void main(String[] args) {
		
		System.out.println(alphabetSoup());
	}
}

//O/P-hibrhichiderhi
