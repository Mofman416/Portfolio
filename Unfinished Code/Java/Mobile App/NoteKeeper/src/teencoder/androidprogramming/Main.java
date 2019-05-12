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
 * Chapter 8 Activity - NoteKeeper Bugs 
 * This class represents the code for the main screen in the
 * "NoteKeeper" application.
 * @author Homeschool Programming, Inc.
 * @version 2.0
*/


package teencoder.androidprogramming;

import java.io.BufferedReader;
import java.io.File;
import java.io.FileInputStream;
import java.io.FileOutputStream;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;

import android.app.Activity;
import android.os.Bundle;
import android.os.Environment;
import android.widget.Button;
import android.widget.EditText;
import android.widget.Toast;
import android.view.View;
import android.view.View.*;

public class Main extends Activity implements OnClickListener
{
    /** Called when the activity is first created. */
    @Override
    public void onCreate(Bundle savedInstanceState) 
    {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.main);
        
        // Get a handle to the save button and set it's click listener
        Button btnSave = (Button)findViewById(R.id.btnSave);
        btnSave.setOnClickListener(this);
        
    }
    
    // This method will load the note from the SD Card
 	public void loadNote()
 	{
 		// Get handle to EditText control on the screen
 		EditText etNote = (EditText)findViewById(R.id.etNote);
 		
 		// Check to make sure we can access SD Card
 	 	String state = Environment.getExternalStorageState();
 		if (state.equals(Environment.MEDIA_MOUNTED))
 		{
 			// All file operations must be placed in a try/catch block
 			try 
 	 		{
	 			// Get the location of the SD Card on the device
 				File sdCardLocation = getExternalFilesDir(null);
 				
 				// Build a path to our directory on the SD Card
	 			String filePath = sdCardLocation.getAbsolutePath();
	 			
	 			// Open our file from the SD Card
	 			File myFile = new File(filePath, "mynote.txt");
	 			
	 			// Capture the file in a FileInputStream object and 
	 			// then an InputStreamReader object
	 			FileInputStream fIn = new FileInputStream(myFile);
	 			InputStreamReader isr = new InputStreamReader(fIn);
	 			
	 			// Place the contents in a BufferedReader object to make reading easier
	 			BufferedReader buffreader = new BufferedReader(isr);
	 			
	 			// Read in the data, line-by-line
	 			String note = buffreader.readLine();
	 			
	 			// While we still have valid data
	 			while (note != null) 
	 			{
	 				etNote.append(note);
	 				// Read in the next line in the file
	 				note = buffreader.readLine();
 		    }
	 			
	 			// Close the BufferedReader object
	 			buffreader.close();
 	 		}
	
	 		// Catch any file errors that occurred
	 		catch (Exception e) 
	 		{
	 			// Send a Toast message telling user there was an error
	 			Toast myToast = Toast.makeText(this, "Exception!", 7000);
	 			myToast.show();
	 		}
 		}
 	}
 	
 	// This method will save the note to the SD Card
 	public void saveNote()
 	{
 		// Get the contents of the EditText control on the screen
 		EditText note = (EditText)findViewById(R.id.etNote);
 		String strNote = note.getText().toString();

 		// Make sure we have access to the SD Card
 		String state = Environment.getExternalStorageState();
 		if (state.equals(Environment.MEDIA_MOUNTED))
 		{
 			// All file operations must be placed in a try/catch block
 			try 
 	 		{
 				// Get the location of the SD Card on the device
 				File sdCardLocation = getExternalFilesDir(null);
	 			
 				// Build a path to our directory on the SD Card
 				String filePath = sdCardLocation.getAbsolutePath();
	 			
 				// Open our file from the SD Card
	 			File myFile = new File(filePath, "note.txt");

	 			FileOutputStream fos = new FileOutputStream(myFile);
	 			OutputStreamWriter osr = new OutputStreamWriter(fos);
	 			
	 			// Write the players name to the file 
	 			osr.write(strNote);
	  			
	 			// Make sure all data has been sent out to the file
	 			osr.flush();
	 			
	 			// Close the file
	 			osr.close();
 	 		}
 			catch (Exception e)
 			{
 				// Send a Toast message telling user there was an error
 				Toast myToast = Toast.makeText(this, "Exception!", 7000);
	 			myToast.show();
 			}
 		}
 		

 	}

	public void onClick(View v) 
	{
		// If the user has clicked on the Save Button
		if (v.getId() == R.id.btnSave)
		{
			saveNote();	// call the saveNote method
		}
		
		// If the user clicked on the Load Button
		else if (v.getId() == R.id.btnLoad)
		{
			loadNote();	// call the loadNote method
		}
		
	}
}
