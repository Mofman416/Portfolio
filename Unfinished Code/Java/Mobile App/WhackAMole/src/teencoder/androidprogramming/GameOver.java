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
 * Chapter 7 - Whack-A-Mole 
 * This class represents the code for the GameOver screen in the
 * "Whack-A-Mole" game.
 * @author Homeschool Programming, Inc.
 * @version 2.0
*/

package teencoder.androidprogramming;

import java.io.*;

import android.app.Activity;
import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.view.View.*;
import android.widget.*;

//The class for the GameOver screen
public class GameOver extends Activity implements OnClickListener
{
	// Use globals to define game options
	String playerName;
	int numWhacks;
	
	//**********************************************************
    // The student will complete this method for Chapter 7 Activity #2
	//
	// onCreate() should read data out of the Intent and populate
	// the controls on the screen with the game over message.
	// It will also register "this" as the button listeners and
	// save the new game over data to persistent storage.
    public void onCreate(Bundle savedInstanceState) 
	{
        super.onCreate(savedInstanceState);
        setContentView(R.layout.gameover);
        
        numWhacks = getIntent().getExtras().getInt("Hits");
        playerName = getIntent().getExtras().getString("Name");
        
        TextView tv = (TextView)findViewById(R.id.tvHits);
        tv.setText("You hit " + numWhacks + "times!");
        
        TextView tv2 = (TextView)findViewById(R.id.tvGameOver);
        tv2.setText("Game Over, " + playerName);
        
        Button playButton = (Button)findViewById(R.id.buttonPlay);
        playButton.setOnClickListener(this);
        
        Button scoreButton = (Button)findViewById(R.id.buttonScores);
        scoreButton.setOnClickListener(this);
        
        // Save the current player's score.
        //saveHighScoreInternalFile();
        saveHighScoreSD();
    }
	
	//**********************************************************
    // The student will complete this method for Chapter 7 Activity #2
	//
    // save the player's score into the specified FileOutputStream
    private void writeToFOS(FileOutputStream fos)
    {
    	try {
    		OutputStreamWriter osw = new OutputStreamWriter(fos);
    		
    		String endLine = System.getProperty("line.seperator");
    		
    		osw.write(playerName + endLine);
    		
    		osw.write(numWhacks + endLine);
    		
    		osw.flush();
    		
    		osw.close();
    		
    	}
    	
    	catch (Exception e) {
    		System.out.println(e);
    	}
    }
    
	//**********************************************************
    // The student will complete this method for Chapter 7 Activity #2
	//
    // save the player's score into the specified FileOutputStream
	// This method will save the player's score into the HighScores.txt file in Internal Memory
	private void saveHighScoreInternalFile()
	{
		try {
			FileOutputStream fos = openFileOutput("HighScores.txt", MODE_APPEND);
			
			writeToFOS(fos);
		}
		
		catch (Exception e) {
			System.out.println(e);
		}
	}
	
	//**********************************************************
    // The student will complete this method for Chapter 7 Activity #3
	//
	// This method will save the player's score into the HighScores.txt file on a SD card
	private void saveHighScoreSD()
	{
		// File operations must be done in a try/catch block
		try {
			// Get the location for this application's private SD card folder.
			File privateLocation = getExternalFilesDir(null);
			
			// Construct a file object representing the target filename
			File myFile = new File(privateLocation, "HighScores.txt");
			
			// Build a FileOutputStream and write some text data!
			// Note: We use the "true" flag to tell the compiler to append to our data in the existing file instead of overwriting it!
			FileOutputStream fos = new FileOutputStream(myFile, true);
			
			// Write our data to this fileOutputStream
			writeToFOS(fos);
		}
		
		catch (Exception e) {
			// There was a problem with the file
			System.out.println(e);
		}
	}
	//**********************************************************
	
	//**********************************************************
    // This method is provided as part of the activity starter
	//
	// Click method for all buttons in the Game Over screen
	public void onClick(View v) 
	{
		// If the user clicked the "Play Again" button
		if (v.getId() == R.id.buttonPlay)
   		{
			// Start the Game screen with an Explicit Intent
			Intent myIntent = new Intent(this, Game.class); 
			startActivity(myIntent);
			finish();	// close this activity
   		}
		// If the user clicked the "High Scores" button
		else if(v.getId() == R.id.buttonScores)
		{
			// Start the Scores screen with an Explicit Intent
			Intent myIntent = new Intent(this, HighScores.class);
			startActivity(myIntent);
			finish();	// close this activity
		}
	}
}

