package mobileapp.dialogueexample;

import android.os.Bundle;
import android.app.Activity;
import android.view.Menu;
import android.view.View;
import android.view.View.OnClickListener;
import android.app.*;
import android.content.DialogInterface;
import android.widget.*;

public class Main extends Activity implements OnClickListener {
	
	
	public static class MyAlertDialog extends DialogFragment{
		public Dialog onCreateDialog(Bundle savedInstanceState) {
			AlertDialog.Builder builder = new AlertDialog.Builder(getActivity());
			
			builder.setMessage("Hello World!");
			builder.setCancelable(true);
			builder.setPositiveButton("Yes", new DialogInterface.OnClickListener() {
				
				@Override
				public void onClick(DialogInterface dialog, int id) {
					Main myActivity = (Main)getActivity();
					TextView myView =
							(TextView)myActivity.findViewById(R.id.textview1);
					myView.setText("I agree!");
					
				}
			});
			
			builder.setNegativeButton("No", new DialogInterface.OnClickListener() {
				
				@Override
				public void onClick(DialogInterface dialog, int id) {
					Main myActivity = (Main)getActivity();
					TextView myView =
							(TextView)myActivity.findViewById(R.id.textview1);
					myView.setText("I disagree!");
					
				}
			});
			
			builder.setNeutralButton("Maybe", new DialogInterface.OnClickListener() {
				
				@Override
				public void onClick(DialogInterface dialog, int id) {
					Main myActivity = (Main)getActivity();
					TextView myView =
							(TextView)myActivity.findViewById(R.id.textview1);
					myView.setText("I don't care!");
					
				}
			});
			
			return builder.create();
		}
	}

	@Override
	protected void onCreate(Bundle savedInstanceState) {
		super.onCreate(savedInstanceState);
		setContentView(R.layout.main);
		
		 Button b = (Button)findViewById(R.id.button1);
		 b.setOnClickListener(this);
	}

	@Override
	public boolean onCreateOptionsMenu(Menu menu) {
		// Inflate the menu; this adds items to the action bar if it is present.
		getMenuInflater().inflate(R.menu.main, menu);
		return true;
	}

	@Override
	public void onClick(View arg0) {
		DialogFragment newFragment = new MyAlertDialog();
		newFragment.show(getFragmentManager(), "myDialog");
		
	}

}
