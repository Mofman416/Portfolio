package mobileapp.mypetactivity;

import android.app.ListActivity;
import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.*;

public class MyPetActivity extends ListActivity {
	String[] pets = {"Dog", "Cat", "Bird", "Hamster",
			"Ferret", "Snake"};
	public void onCreate(Bundle savedInstanceState) {

		super.onCreate(savedInstanceState);
		

		ArrayAdapter<String> myAdapter =
			new ArrayAdapter<String> (this,
									android.R.layout.simple_list_item_1, pets);
		setListAdapter(myAdapter);
		}
	protected void onListItemClick(ListView l, View v,
			int position, long id) {
		String selection = pets[position];
		
		Intent resultIntent = new Intent();
		
		resultIntent.putExtra("pet", selection);
		setResult(RESULT_OK, resultIntent);
		finish();
	}
	}
