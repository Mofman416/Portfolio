
public class RaceCar implements IRacer{
	String myName;
	double myMaxSpeed;
	double myAcceleration;
	double myCurrentSpeed;
	@Override
	public String getName() {
		
		return myName;
	}
	@Override
	public double getCurrentSpeed() {
		// TODO Auto-generated method stub
		return myCurrentSpeed;
	}
	@Override
	public void resetCurrentSpeed() {
		// TODO Auto-generated method stub
	    myCurrentSpeed = 0.0;
		
	}
	@Override
	public void accelerate() {
		// TODO Auto-generated method stub
		myCurrentSpeed += myAcceleration;
		if (myCurrentSpeed > myMaxSpeed){
			myCurrentSpeed = myMaxSpeed;
		}

		
	}
	public RaceCar(String myName, double myMaxSpeed, double myAcceleration) {
		super();
		this.myName = myName;
		this.myMaxSpeed = myMaxSpeed;
		this.myAcceleration = myAcceleration;
		this.myCurrentSpeed = 0.0;
	}
}
