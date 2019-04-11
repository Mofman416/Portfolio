package mobileapp.ch20act;

import android.app.Activity;
import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.view.View.OnClickListener;
import android.widget.*;

public class Third extends Activity implements OnClickListener {
	@Override
	protected void onCreate(Bundle savedInstanceState) {
		super.onCreate(savedInstanceState);
		setContentView(R.layout.third);
		Button bluebutton = (Button)findViewById(R.id.bluebutton);
		bluebutton.setOnClickListener(this);
		Button redbutton = (Button)findViewById(R.id.redbutton);
		redbutton.setOnClickListener(this);
		
		
		
	}

	@Override
	public void onClick(View v) {
		int id = v.getId();
		Intent colorIntent = new Intent();
		if (id == R.id.bluebutton) {
			colorIntent.putExtra("color", "blue");
		}
		else if (id == R.id.redbutton) {
			colorIntent.putExtra("color", "red");
		}
		setResult(RESULT_OK, colorIntent);
		finish();
		
	}
}
