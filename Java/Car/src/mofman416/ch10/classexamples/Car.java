package mofman416.ch10.classexamples;

public class Car {
	String color = "blue";
	int year = 2019;
	//Engine myengine = new engine();
	
	
	void start() {
		System.out.println("Your car has started.");
	}
	
	void stop() {
		System.out.println("Your car has stopped.");
	}
	
	
	public static void main(String[] args) {
		Car car1 = new Car();
		Car car2 = new Car();
		
		car1.start();
		car2.start();
		car1.stop();
		car2.stop();
	}
}
