package mobileapp.myfirstproject;

import android.os.Bundle;
import android.app.Activity;
import android.view.*;
import android.view.View.*;
import android.widget.*;
import android.content.Intent;

public class MainActivity extends Activity implements OnClickListener  {

	@Override
	protected void onCreate(Bundle savedInstanceState) {
		super.onCreate(savedInstanceState);
		setContentView(R.layout.activity_main);
		
		Button myButton = (Button) findViewById(R.id.button1);
		myButton.setOnClickListener(this);
	}

	@Override
	public boolean onCreateOptionsMenu(Menu menu) {
		// Inflate the menu; this adds items to the action bar if it is present.
		getMenuInflater().inflate(R.menu.main, menu);
		return true;
	}

	@Override
	public void onClick(View v) {
		int id = v.getId(); // get ID for control that was clicked
		if (id == R.id.button1) { //if this ID equals button1's ID
			
			//Get a reference to the EditText control
			EditText et = (EditText)findViewById(R.id.editText1);
			
			//Get the string value from the EditText control
			String value = et.getText().toString();
			
			//put the string value from the edit text into the Intent
			Intent myIntent = new Intent(MainActivity.this, SecondMain.class);
			myIntent.putExtra("name", value);
			
			startActivityForResult(myIntent, 0);
		}
		
	}
	
	protected void onActivityResult(int requestCode, int resultCode, Intent data) {
		Bundle bun = data.getExtras();
		
		String value = bun.getString("name");
		
		TextView tv = (TextView)findViewById(R.id.textView1);
		tv.setText("Received name back: " + value);
	}
}
