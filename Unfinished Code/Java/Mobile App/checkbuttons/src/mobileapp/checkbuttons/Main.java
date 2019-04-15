package mobileapp.checkbuttons;

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
		Button but1 = (Button)findViewById(R.id.button1);
		but1.setOnClickListener(this);
	}

	@Override
	public boolean onCreateOptionsMenu(Menu menu) {
		// Inflate the menu; this adds items to the action bar if it is present.
		getMenuInflater().inflate(R.menu.main, menu);
		return true;
	}

	@Override
	public void onClick(View v) {
		String myText = "";
		TextView tv = (TextView)findViewById(R.id.textView1);
		int id = v.getId();
		if (id == R.id.button1) {
			CheckBox cbcat = (CheckBox)findViewById(R.id.checkBox1);
			CheckBox cbdog = (CheckBox)findViewById(R.id.checkBox2);
			CheckBox cbbird = (CheckBox)findViewById(R.id.checkBox3);
			if (cbcat.isChecked()) {
				myText += cbcat.getText().toString()+"\n";
			}
			if (cbdog.isChecked()) {
				myText += cbdog.getText().toString()+"\n";
			}
			if (cbbird.isChecked()) {
				myText += cbbird.getText().toString()+"\n";
			}
			tv.setText(myText);
		}
		
	}

}
