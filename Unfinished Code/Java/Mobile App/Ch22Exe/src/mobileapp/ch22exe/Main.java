package mobileapp.ch22exe;

import android.os.Bundle;
import android.app.Activity;
import android.view.Menu;
import android.view.View;
import android.view.View.OnClickListener;
import android.widget.*;

public class Main extends Activity implements OnClickListener{

	@Override
	protected void onCreate(Bundle savedInstanceState) {
		super.onCreate(savedInstanceState);
		setContentView(R.layout.main);
		Button butt1 = (Button)findViewById(R.id.button1);
		butt1.setOnClickListener(this);
		
		String[] pets = {"Dog", "Cat", "Bird", "Hamster",
				"Ferret", "Snake"};
		
		ArrayAdapter<String> myAdapter = new ArrayAdapter<String>(this,
				android.R.layout.simple_spinner_item, pets);
		
		Spinner spn = (Spinner)findViewById(R.id.spinner1);
		spn.setAdapter(myAdapter);
		spn.setSelection(3);
		
		SeekBar sb = (SeekBar)findViewById(R.id.seekBar1);
		sb.setProgress(20);
		sb.setMax(100);
		}

	@Override
	public boolean onCreateOptionsMenu(Menu menu) {
		// Inflate the menu; this adds items to the action bar if it is present.
		getMenuInflater().inflate(R.menu.main, menu);
		return true;
	}

	@Override
	public void onClick(View v) {
		String myString = "I have ";
		
		
	}

}
