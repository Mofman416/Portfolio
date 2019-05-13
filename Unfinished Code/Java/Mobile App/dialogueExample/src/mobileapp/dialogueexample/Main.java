package mobileapp.dialogueexample;

import android.os.Bundle;
import android.app.Activity;
import android.view.Menu;
import android.view.View;
import android.view.View.OnClickListener;

import java.util.Calendar;

import android.app.*;
import android.content.DialogInterface;
import android.widget.*;
import android.app.TimePickerDialog;

public class Main extends Activity {
	   static String[] pets = {"Dog", "Cat", "Horse"};  
	   // data array for alert list 
	
	   public static class MyDatePicker extends DialogFragment 
       implements DatePickerDialog.OnDateSetListener  
{
public Dialog onCreateDialog(Bundle savedInstanceState) 
{
// Use the current date as the default date in the picker
Calendar c = Calendar.getInstance();
int year = c.get(Calendar.YEAR);
int month = c.get(Calendar.MONTH);
int day = c.get(Calendar.DAY_OF_MONTH);

// Create a new instance of DatePickerDialog and return it
return new DatePickerDialog(getActivity(), this, 
                 year, month, day);
}

@Override

public void onDateSet(DatePicker view, int year, int monthOfYear, 
        int dayOfMonth)
{
Main myActivity = (Main)getActivity();
TextView myView 
       = (TextView)myActivity.findViewById(R.id.textView1);
myView.setText(year + "/" + Integer.toString(monthOfYear + 1) + "/" + dayOfMonth);
}
}  // end of MyDatePicker

	@Override
	protected void onCreate(Bundle savedInstanceState) {
		super.onCreate(savedInstanceState);
		setContentView(R.layout.main);
		
		 Button b = (Button)findViewById(R.id.button1);
		 b.setOnClickListener(new OnClickListener());
	}

	@Override
	public boolean onCreateOptionsMenu(Menu menu) {
		// Inflate the menu; this adds items to the action bar if it is present.
		getMenuInflater().inflate(R.menu.main, menu);
		return true;
	}

}
