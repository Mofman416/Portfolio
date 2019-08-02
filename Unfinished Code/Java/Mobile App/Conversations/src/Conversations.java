
import java.util.Scanner;

public class Conversations {
	Integer int1;
	Double double1;

	public static void main(String[] args) {
		Scanner input = new Scanner(System.in);
		
		System.out.print("Put in your name: ");
		String name = input.nextLine();
		
		System.out.print("Type in a noun: ");
		String noun = input.next();
		noun = input.nextLine();
		
		System.out.print("Type in a verb: ");
		String verb = input.next();
		input.nextLine();
		
		System.out.print("Type in a number: ");
		if ( input.hasNextInt() ) {
			
			int int1 = input.nextInt();
			input.nextLine();
		}
		
		else {
			String error = input.next();
			System.out.println("Sorry, bad input!");
		}

		input.nextLine();
		
		System.out.print("Type in a real (decimal) number: ");
		if (input.hasNextDouble()) {
			
			double double1 = input.nextInt();
		}
		
		else {
			String error = input.next();
			System.out.println("Sorry, bad input!");
		}

		input.nextLine();
		
		
		
		String story = "One day, " + name + " picked up a " + noun;
		story += " and decided to " + verb + " it.\n";
		story += "After getting arrested, spending " + int1;
		story += " days in jail, and paying a $" + double1 + " fine,\n";
		story += name + " decided that was a bad idea!";

		System.out.println(story);
	}

}
