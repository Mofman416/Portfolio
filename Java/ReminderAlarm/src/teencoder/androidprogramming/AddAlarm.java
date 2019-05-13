////////////////////////////////////////////////////////////////
//Copyright 2013, Homeschool Programming, Inc.
//
//This source code is for use by the students and teachers who 
//have purchased the corresponding TeenCoder or KidCoder product.
//It may not be transmitted to other parties for any reason
//without the written consent of Homeschool Programming, Inc.
//This source is provided as-is for educational purposes only.
//Homeschool Programming, Inc. makes no warranty and assumes
//no liability regarding the functionality of this program.
//
////////////////////////////////////////////////////////////////

/** TeenCoder: Android Programming
 * Chapter 10-11 - Reminder application
 * This class represents the code for the Add Alarm 
 * screen for this application.
 * @author Homeschool Programming, Inc.
 * @version 2.0
*/

package teencoder.androidprogramming;

import java.util.Calendar;

import android.app.*;
import android.content.DialogInterface;
import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.view.View.OnClickListener;
import android.widget.*;

public class AddAlarm extends Activity implements OnClickListener
{
    // All class variables are pre-defined as part of the activity starter
    
    // Create a global instance of AlarmKeeper. This will allow us to access this variable
    // anywhere in our class
    AlarmKeeper thisAlarm;
    
    // used to track the selected alarm from a list
    int index = -1;
    
    // This method is provided complete as part of the activity starter
    public void onCreate(Bundle savedInstanceState) 
    {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.addalarm);
        
        // Get handlers to all of our buttons
        Button saveButton = (Button)findViewById(R.id.saveButton);
        Button timeButton = (Button)findViewById(R.id.timeButton);
        Button dateButton = (Button)findViewById(R.id.dateButton);
        
        // Set the button's onClickListeners
        saveButton.setOnClickListener(this);
        timeButton.setOnClickListener(this);
        dateButton.setOnClickListener(this);
        
        // Initialize the AlarmKeeper object
        thisAlarm = new AlarmKeeper();
        
        // Get information from the incoming Intent
        Bundle extras = getIntent().getExtras();
        
        if (extras != null)
        {
          // Retrieve the alarm information in string format
          String alarmString = extras.getString("alarm");
          
          // Get the index value for the alarm
          index = extras.getInt("index");
        
          // If we have a valid alarm
          if ((index >= 0) && (alarmString != null))
          {
            // Build an AlarmKeeper object from the alarm string
            thisAlarm.fromString(alarmString);
            displayAlarm(); // show the alarm information!
          }
                    
        }
 
    }
        
    // This method is provided complete in the activity starter
    private void displayAlarm()
    {
        EditText desc = (EditText)findViewById(R.id.etDesc);
        EditText name = (EditText)findViewById(R.id.etAlarmName);
        Button dateButton = (Button)findViewById(R.id.dateButton);
        Button timeButton = (Button)findViewById(R.id.timeButton);
    
        // Set the alarm description and name
        desc.setText(thisAlarm.alarmDesc);
        name.setText(thisAlarm.alarmName);
        
        // Set the alarm date as the text for the Date Button
        dateButton.setText((thisAlarm.alarmMonth + 1) + "/" + thisAlarm.alarmDay + "/" + thisAlarm.alarmYear);
                
        // Create a string to use for the AM/PM value in the time
        String AMPM = " AM";
        
        // Create a string value to format the minute field in the time
        String strMinute;
        
        //Adjust hour to 12-hour time
        int hour = thisAlarm.alarmHour;
        if (hour > 12)
        {
          hour = hour - 12;
          AMPM = " PM"; // Add the AM/PM value
        }
        
        // Format the minute value to be two-digit value
        if (thisAlarm.alarmMinute < 10)
          strMinute = "0" + thisAlarm.alarmMinute;
        else
          strMinute = "" + thisAlarm.alarmMinute;
        
        // Place the time value into the Time Button
        timeButton.setText(hour + ":" + strMinute + AMPM);
    }
   
    //**********************************************************
    // This method is completed by the student in the Chapter 10 Activity
    //
    // This method is called whenever a user clicks one of the buttons on the screen
    public void onClick(View v) 
    {
    	int id = v.getId();
    	if (id == R.id.saveButton) {
    		
    		// Get the values in the name and description fields
    		EditText desc = (EditText)findViewById(R.id.etDesc);
    		EditText name = (EditText)findViewById(R.id.etAlarmName);
    		
    		thisAlarm.alarmDesc = desc.getText().toString();
    		thisAlarm.alarmName = name.getText().toString();
    		
    		// Creates and display the MyAlertDialog
    		DialogFragment newFragment = new MyAlertDialog();
    		newFragment.show(getFragmentManager(), "MyAlertDialog");
    	}
    	
    	else if (id == R.id.dateButton) {
    		// Creates and display the MyDatePicker
    		DialogFragment newFragment = new MyDatePicker();
    		newFragment.show(getFragmentManager(), "MyDatePicker");
    	}
    	
    	else if (id == R.id.timeButton) {
    		// Creates and display the MyTimePicker
    		DialogFragment newFragment = new MyTimePicker();
    		newFragment.show(getFragmentManager(), "MyTimePicker");
    	}
    	
    }
    //**********************************************************
  
  
    //**********************************************************
    // This class is completed by the student in the Chapter 10 Activity
    //
    public static class MyDatePicker extends DialogFragment 
                                     implements DatePickerDialog.OnDateSetListener
    {
        // This method is completed by the student in the Chapter 10 Activity
        public  Dialog onCreateDialog(Bundle savedInstanceState) 
        {	
        	Calendar now = Calendar.getInstance();
        	int year = now.get(Calendar.YEAR);
        	int month = now.get(Calendar.MONTH);
        	int day = now.get(Calendar.DAY_OF_MONTH);
            
            return new DatePickerDialog(getActivity(), this, year, month, day);  // replace with your new Dialog object
        }

        // This method is completed by the student in the Chapter 10 Activity
        public void onDateSet(DatePicker view, int year, int month, int day) 
        {
        	AddAlarm activity = (AddAlarm)getActivity();
        	activity.thisAlarm.alarmYear = year;
        	activity.thisAlarm.alarmMonth = month;
        	activity.thisAlarm.alarmDay = day;
        	
        	// Set the text of the button to reflect the user's date
        	Button dateButton = (Button)activity.findViewById(R.id.dateButton);
        	dateButton.setText(Integer.toString(month + 1) + "/" + day + "/" + year);
        }
    }
    //**********************************************************
  
    //**********************************************************
    // This class is completed by the student in the Chapter 10 Activity
    //
    public static class MyTimePicker extends DialogFragment 
                                     implements TimePickerDialog.OnTimeSetListener
    {
        // This method is completed by the student in the Chapter 10 Activity
        public  Dialog onCreateDialog(Bundle savedInstanceState) 
        {
        	Calendar now = Calendar.getInstance();
        	int hour = now.get(Calendar.HOUR_OF_DAY);
        	int minute = now.get(Calendar.MINUTE);
        	
            return new TimePickerDialog(getActivity(),this,hour,minute,false); // replace with your new Dialog object
        }
    
        // This method is completed by the student in the Chapter 10 Activity
        public void onTimeSet(TimePicker view, int hourOfDay, int minute) 
        {
        	// Set the time information in the AlarmKeeper object
        	AddAlarm activity = (AddAlarm)getActivity();
        	activity.thisAlarm.alarmHour = hourOfDay;
        	activity.thisAlarm.alarmMinute = minute;
        	
        	// Set the text of the time button to reflect the user's time.
        	Button timeButton = (Button)activity.findViewById(R.id.timeButton);
        	
        	String AMPM = " AM";
        	String strMinute;
        	
        	// Adjust the hour to 12 hour time
        	if (hourOfDay > 12) {
        		hourOfDay = hourOfDay - 12;
        		AMPM = " PM";
        	}
        	if (minute > 10) {
        		strMinute = "0" + minute;
        	}
        	else {
        		strMinute = "" + minute;
        		timeButton.setText(hourOfDay + ":" + strMinute + AMPM);
        	}
        }
    }
    //**********************************************************
    
    //**********************************************************
    // This class is completed by the student in the Chapter 10 Activity
    //
    public static class MyAlertDialog extends DialogFragment 
    {
        // This metohd is completed by the student in the Chapter 10 Activity
        public  Dialog onCreateDialog(Bundle savedInstanceState) 
        {
        	// Use the builder to create a new AlertDialog
        	AlertDialog.Builder builder = new AlertDialog.Builder(getActivity());
        	builder.setMessage("Are you sure you want to set this alarm?");
        	builder.setCancelable(false);
        	
        	// Create a "Yes" button in the dialog
        	builder.setPositiveButton("Yes", 
        			new DialogInterface.OnClickListener() {
						
						@Override
						public void onClick(DialogInterface arg0, int id) {
							AddAlarm activity = (AddAlarm)getActivity();
							// Verify a valid alarm was configured
							if ((activity.thisAlarm.alarmName == null) || (activity.thisAlarm.alarmName.length() == 0)) {
								return;
							}
							if ((activity.thisAlarm.alarmDesc == null) || (activity.thisAlarm.alarmDesc.length() == 0)) {
								return;
							}
							if ((activity.thisAlarm.alarmYear == 0)) {
								return;
							}
							activity.thisAlarm.setAlarm(activity);
							
						}
					});
        	
        	builder.setNegativeButton("No", 
        			new DialogInterface.OnClickListener() {
						
						public void onClick(DialogInterface dialog, int id) {
							// There is no need to do anything in this method, since the
							// user cancelled the save action.
						}
					});
        	
            return builder.create();  // replace with your new Dialog object
        }
    }
  //**********************************************************
  
  // This method is provided complete in the activity starter
  public void clearAlarmScreen()
  {
    // Get a handle to the relevant controls on the screen
    Button timeButton = (Button)findViewById(R.id.timeButton);
    Button dateButton = (Button)findViewById(R.id.dateButton);
    EditText desc = (EditText)findViewById(R.id.etDesc);
    EditText name = (EditText)findViewById(R.id.etAlarmName);
    
    // Reset all fields back to their initial state
    timeButton.setText("Set Time");
    dateButton.setText("Set Date");
    desc.setText("");
    name.setText("");
    
    // Call the clear() method on the AlarmKeeper object to clear out all data
    thisAlarm.clear();
  }
  
  //This method is provided complete in the activity starter
  public void closeAlarmScreen()
  {
    // Build a string from all the alarm information
    String alarmString = thisAlarm.buildString();
      
    // Pass the alarm string in a new Intent to the Alarm List class
    Intent listIntent = new Intent(AddAlarm.this, AlarmList.class);
    listIntent.putExtra("alarm", alarmString);
    listIntent.putExtra("index", index);
        
    // Sent the resulting intent back to the AlarmList screen
    setResult(RESULT_OK, listIntent);
        
    // Close this screen
    finish();
  }
}