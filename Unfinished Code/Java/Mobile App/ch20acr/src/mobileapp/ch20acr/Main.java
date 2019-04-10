package mobileapp.ch20acr;

import android.os.Bundle;
import android.app.Activity;
import android.view.*;
import android.view.View.*;
import android.widget.*;
import android.content.Intent;

public class Main extends Activity implements OnClickListener {

	@Override
	protected void onCreate(Bundle savedInstanceState) {
		super.onCreate(savedInstanceState);
		setContentView(R.layout.main);
		Button osbutton = (Button)findViewById(R.id.osversion);
		osbutton.setOnClickListener(this);
		Button timebutton = (Button)findViewById(R.id.emulatortime);
		timebutton.setOnClickListener(this);
		Button colorbutton = (Button)findViewById(R.id.colors);
		colorbutton.setOnClickListener(this);
	}

	@Override
	public boolean onCreateOptionsMenu(Menu menu) {
		// Inflate the menu; this adds items to the action bar if it is present.
		getMenuInflater().inflate(R.menu.main, menu);
		return true;
	}

	@Override
	public void onClick(View v) {
		int id = v.getId();
		if (id == R.id.osversion) {
			Intent startosscreen = new Intent(Main.this, Second.class);
			startosscreen.putExtra("build", android.os.Build.VERSION.RELEASE);
			startActivity(startosscreen);
			
		}
		
		else if (id == R.id.emulatortime) {
			Intent starttimescreen = new Intent(Main.this, Second.class);
			starttimescreen.putExtra("time", android.os.SystemClock.uptimeMillis() );
			startActivity(starttimescreen);
		}
		
		else if (id == R.id.colors) {
			Intent startcolorsscreen = new Intent(Main.this, Third.class);
			startActivityForResult(startcolorsscreen, 0);
		}
		
	}
	protected void onActivityResult(int requestCode, int resultCode, Intent data) {
		Bundle bun = data.getBundleExtra("color");
		String strval = "";
		if (strval != null) {
			strval = bun.getString("color");
			TextView tv = (TextView)findViewById(R.id.maintextview);
			tv.setText("Received Color back: " + strval);
		}
	}
	
}
