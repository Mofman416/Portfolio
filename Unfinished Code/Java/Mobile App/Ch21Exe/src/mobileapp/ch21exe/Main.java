package mobileapp.ch21exe;

import android.os.Bundle;
import android.app.Activity;
import android.view.Menu;
import android.view.View;
import android.view.View.OnClickListener;
import android.widget.Button;
//import android.widget.EditText;
import android.widget.RadioButton;
import android.widget.TextView;

public class Main extends Activity implements OnClickListener{

	@Override
	protected void onCreate(Bundle savedInstanceState) {
		super.onCreate(savedInstanceState);
		setContentView(R.layout.main);
		Button but1 = (Button)findViewById(R.id.but1);
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
		int id = v.getId();
		if (id == R.id.but1) {
			TextView tv = (TextView)findViewById(R.id.textView1);
			//EditText et = (EditText)findViewById(R.id.editText1);
			//myText = et.getText().toString();
			
			RadioButton rbred = (RadioButton)findViewById(R.id.rbred);
			RadioButton rbblue = (RadioButton)findViewById(R.id.rbblue);
			if (rbred.isChecked()) {
				myText = rbred.getText().toString();
			}
			else if (rbblue.isChecked()) {
				myText = rbblue.getText().toString();
			}
			tv.setText(myText);
		}
		
	}

}
