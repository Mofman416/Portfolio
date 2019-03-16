import java.util.Calendar;

public class StringTheory {

	public static void main(String[] args) {
		String str1 = "Bibbety";
		String str2 = "Bobbity";
		String str3 = "Boo";
		String str4 = "BIBBETY";
		
		System.out.println("str1 equals str4: " + str1.equals(str4));
		System.out.println("str1 equals str4 (ignore case): " + str1.equalsIgnoreCase(str4));
		System.out.println("str1 switches its b's with p's.: " + str1.replace("b", "p"));
		System.out.println("str2 first three characters: " + str2.substring(0, 3));
		System.out.println("str3 to the  first uppercase: " + str3.toUpperCase());
		
		System.out.println("The current time is: " + String.format( "%tr", 
				Calendar.getInstance()));
		
		System.out.println("Str1 + Str2: " + (str1 + str2));
		System.out.println("parseInt results: " + Integer.parseInt("5"));
		System.out.println("location of 'e' in str1: " + str1.indexOf("e"));
		
	}

}
