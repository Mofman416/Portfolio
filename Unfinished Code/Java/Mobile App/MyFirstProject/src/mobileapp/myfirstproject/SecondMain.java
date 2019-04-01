package mobileapp.myfirstproject;

import android.app.Activity;
import android.os.Bundle;
import android.content.Intent;
import android.widget.*;

public class SecondMain extends Activity {
	
	public void onCreate(Bundle savedInstanceState) {
		super.onCreate(savedInstanceState);
		setContentView(R.layout.secondmain);
		
		//Get Intent that launched this activity
		Intent myIntent = getIntent();
		
		//Get Bundle that contains extra data
		Bundle bun = myIntent.getExtras();
		
		//Pull the value from the bundle using our key
		String value = bun.getString("name");
		
		//Get the TextView control and update the displayed text
		TextView tv = (TextView)findViewById(R.id.textView1);
		tv.setText("Hello " + value);
	}

}
