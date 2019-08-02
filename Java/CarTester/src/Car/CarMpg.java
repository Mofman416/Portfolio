package Car;

public class CarMpg {
	// class member variables
	  private double startMiles; 
	  private double endMiles; 
	  private double gallons; 

	// build a car with trip details
	  public CarMpg(double start, double end, double gals){
	      startMiles = start;
	      endMiles   = end;
	      gallons    = gals;
	     }
	  
	  /* set the car trip details
	  public void setTrip(double start, double end, double gals)
	  {
	      startMiles = start;
	      endMiles   = end;
	      gallons    = gals;
	  }

	  // calculate miles-per-gallon*/
	  public double calculateMPG()
	  {
	      return (endMiles - startMiles) / gallons;
	  }
}
