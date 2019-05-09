package mobileap.photoalbum;

import android.os.Bundle;
import android.app.Activity;
import android.view.Menu;
import android.view.View;
import android.view.View.OnClickListener;
import android.view.ViewGroup.LayoutParams;
import android.widget.*;

public class Main extends Activity implements View.OnClickListener{

	@Override
	protected void onCreate(Bundle savedInstanceState) {
		super.onCreate(savedInstanceState);
		setContentView(R.layout.main);
		
		LinearLayout myPhotos = (LinearLayout)findViewById(R.id.myPhotos);
		myPhotos.addView(createImageView(R.drawable.snow1));
		myPhotos.addView(createImageView(R.drawable.snow2));
		myPhotos.addView(createImageView(R.drawable.snow3));
	}
	
	View createImageView(int resourceID)
	{
	   ImageView iv = new ImageView(getApplicationContext());
	   iv.setPadding(5,5,5,5);
	   iv.setImageResource(resourceID);
	   iv.setLayoutParams(new LayoutParams(180, 150));
	   iv.setTag(resourceID);
	   iv.setOnClickListener(this);
	   return iv;
	}

	@Override
	public boolean onCreateOptionsMenu(Menu menu) {
		// Inflate the menu; this adds items to the action bar if it is present.
		getMenuInflater().inflate(R.menu.main, menu);
		return true;
	}

	@Override
	public void onClick(View v) {
		int recourceId = (Integer)v.getTag();
		ImageView iv2 = (ImageView)findViewById(R.id.myImageView);
		iv2.setImageResource(recourceId);
		
		//Work on this.
		
	}

}
