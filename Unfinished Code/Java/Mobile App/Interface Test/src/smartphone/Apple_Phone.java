package smartphone;

public class Apple_Phone implements IDialer {

	@Override
	public void call(String phoneNumber) {
		System.out.println("IPhone calling " + phoneNumber);
		
	}

}
