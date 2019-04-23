package teencoder.androidprogramming;

import android.app.Activity;
import android.view.View;
import android.view.View.OnClickListener;
import android.widget.ArrayAdapter;
import android.widget.Spinner;

public class Options extends Activity implements OnClickListener {

	private void setUpSpinner() {
		Spinner moles = (Spinner)findViewById(R.id.moleSpinner);
		String [] items = {"3", "4", "5", "6", "7", "8"};
		ArrayAdapter<String> myAdapter = new ArrayAdapter<String> (this,
				android.R.layout.simple_spinner_item, items);
		moles.setAdapter(myAdapter);
	}
	
	@Override
	public void onClick(View arg0) {
		// TODO Auto-generated method stub
		
	}

}
