package mobileapp.ch20acr;

import android.app.Activity;
import android.content.Intent;
import android.os.Bundle;
import android.widget.TextView;

public class Second extends Activity {
	@Override
	protected void onCreate(Bundle savedInstanceState) {
		super.onCreate(savedInstanceState);
		setContentView(R.layout.second);
		Intent secondintent = getIntent();
		Bundle bun = secondintent.getExtras();
		String strMsg = "";
		if (bun.getString("build") != null) {
			strMsg = "Your device is runnig Android version: " + bun.getString("build");
		}
		else if (bun.getLong("time") > 0) {
			strMsg = "The emulator has been running for: " + bun.getLong("time") + " milliseconds.";
		}
		
		TextView tv = (TextView)findViewById(R.id.secondmessage);
		tv.setText(strMsg);
	}
}
