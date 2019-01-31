package moodyCat;

public class Kitty {
	   // static mood variable
	   private static String mood = "happy";

	   // individual object name
	   private String myName;

	   public static void main(String[] args) 
	   {
	      // create 3 different Kitty objects
	      Kitty cat1 = new Kitty("Grump");
	      Kitty cat2 = new Kitty("Boots");
	      Kitty cat3 = new Kitty("Tiger");

	      // greet each cat
	      cat1.greet();
	      cat2.greet();
	      cat3.greet();

	      // change the mood of all cats
	      Kitty.setMood("angry");

	      // duck and cover
	      cat1.greet();
	      cat2.greet();
	      cat3.greet();
	    }

	   // constructor simply stores the cat's name
	   public Kitty(String name)
	   {
	      myName = name;
	   }

	   // this static function can only use static variables
	   public static void setMood(String newMood)
	   {
	      mood = newMood;
	   }

	   // make use of the static mood and the 
	   // individual cat's name to build a response
	   public void greet()
	   {
	      String response;
	      if (mood.equals("happy"))
	      {
	         response = "purr";
	      }
	      else
	      {
	         response = "claw";
	      }

	      System.out.println(myName + " responds with " + response);
	   }
	} 