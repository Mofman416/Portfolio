package teencoder.androidprogramming;

import android.app.Activity;
import android.content.Intent;
import android.content.SharedPreferences;
import android.os.Bundle;
import android.view.View;
import android.view.View.OnClickListener;
import android.widget.ArrayAdapter;
import android.widget.Button;
import android.widget.EditText;
import android.widget.RadioButton;
import android.widget.SeekBar;
import android.widget.Spinner;
import android.widget.TextView;

public class Options extends Activity implements OnClickListener {
	
	public void onCreate(Bundle savedInstanceState) {
		super.onCreate(savedInstanceState);
		setContentView(R.layout.options);
	
		
		setUpSpinner();
		
		Button playButton = (Button)findViewById(R.id.buttonPlay);
		playButton.setOnClickListener(this);
		
		loadSettings();

	}
	
	private void saveSettingsInIntent(int difficulty, String name,
									  int numMoles, int duration, Intent myIntent) {
		myIntent.putExtra("Name", name);
		myIntent.putExtra("Difficulty", difficulty);
		myIntent.putExtra("Moles", numMoles);
		myIntent.putExtra("Duration", duration);
	}
	

	private void setUpSpinner() {
		Spinner moles = (Spinner)findViewById(R.id.moleSpinner);
		String [] items = {"3", "4", "5", "6", "7", "8"};
		ArrayAdapter<String> myAdapter = new ArrayAdapter<String> (this,
				android.R.layout.simple_spinner_item, items);
		moles.setAdapter(myAdapter);
	}
	
	@Override
	public void onClick(View v) {
		
		if (v.getId() != R.id.buttonPlay) {
			return;
		}
		
		Intent myIntent = new Intent(this, Game.class);
		
		
		int difficulty = 0;
		
		//Get references to all the controls on your screen.
		EditText ev = (EditText)findViewById(R.id.namePrompt);
		RadioButton easy = (RadioButton)findViewById(R.id.radioEasy);
		RadioButton medium = (RadioButton)findViewById(R.id.radioMedium);
		RadioButton hard = (RadioButton)findViewById(R.id.radioHard);
		SeekBar sb = (SeekBar)findViewById(R.id.lengthBar);
		Spinner sp = (Spinner)findViewById(R.id.moleSpinner);
		
		if (easy.isChecked()) {
			difficulty = 3;
		}
		if (medium.isChecked()) {
			difficulty = 2;
		}
		if (hard.isChecked()) {
			difficulty = 1;
		}
		
		String name = ev.getText().toString();
		int duration = sb.getProgress();
		
		int numMoles = sp.getSelectedItemPosition() + 3;
		
		saveSettingsInPrefs(difficulty, name, numMoles, duration);
		
		//saveSettingsInPrefs(difficulty, name, numMoles, duration);
		
		startActivity(myIntent);
		
	}
	
	private void saveSettingsInPrefs(int difficulty, String name,
									 int numMoles, int duration) {
		SharedPreferences prefs = getSharedPreferences("WhackSettings", MODE_PRIVATE);
		
		//Get an editor object that we can use to write our option settings.
		SharedPreferences.Editor editor = prefs.edit();
		
		//Save Option information to the shared preferences area.
		editor.putString("Name", name);
		editor.putInt("Difficulty", difficulty);
		editor.putInt("Moles", numMoles);
		editor.putInt("Duration", duration);
		
		//Commit changes!
		editor.commit();
	}

	private void loadSettings() {
		
		SharedPreferences prefs = getSharedPreferences("WhackSettings", MODE_PRIVATE);
		
		//Get the player name, number of moles and duration values.
		String playerName = prefs.getString("Name", "Default");
		int difficultyLevel = prefs.getInt("Difficulty", 2);
		int numMoles = prefs.getInt("Moles", 8);
		int duration = prefs.getInt("Duration", 20);
		
		//Get references to all the controls on your screen.
		EditText ev = (EditText)findViewById(R.id.namePrompt);
		RadioButton easy = (RadioButton)findViewById(R.id.radioEasy);
		RadioButton medium = (RadioButton)findViewById(R.id.radioMedium);
		RadioButton hard = (RadioButton)findViewById(R.id.radioHard);
		SeekBar sb = (SeekBar)findViewById(R.id.lengthBar);
		Spinner sp = (Spinner)findViewById(R.id.moleSpinner);
		
		ev.setText(playerName);
		sp.setSelection(numMoles -3);
		sb.setProgress(duration);
		
		if (difficultyLevel == 3) {
			easy.setChecked(true);
		}
		else if (difficultyLevel == 2) {
			medium.setChecked(true);
		}
		else {
			hard.setChecked(true);
		}
		
		//String name = ev.getText().toString();
		//int duration = sb.getProgress();
		
		//int numMoles = sp.getSelectedItemPosition() + 3;
		
		//saveSettingsInPrefs(difficulty, name, numMoles, duration);
	}
}
