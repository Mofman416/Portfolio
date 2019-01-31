package smartphone;

public class Android implements IDialer{

	@Override
	public void call(String phoneNumber) {
		System.out.println("Android calling " + phoneNumber);
		
	}


}
