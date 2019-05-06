package mobileapp.wammerge;

import android.os.Bundle;
import android.app.Activity;
import android.view.Menu;
import android.view.View;
import android.view.ViewGroup.LayoutParams;
import android.widget.ImageView;
import android.widget.LinearLayout;

public class MainActivity extends Activity {

	@Override
	protected void onCreate(Bundle savedInstanceState) {
		super.onCreate(savedInstanceState);
		setContentView(R.layout.activity_main);
		
		LinearLayout myPhotos = (LinearLayout)findViewById(R.id.myPhotos);
		myPhotos.addView(createImageView(R.drawable.grass));
		myPhotos.addView(createImageView(R.drawable.grass));
		myPhotos.addView(createImageView(R.drawable.grass));
	}

	private View createImageView(int grass) {
		ImageView iv = new ImageView(getApplicationContext());
		iv.setPadding(5, 5, 5, 5);
		iv.setImageResource(grass);
		iv.setLayoutParams(new LayoutParams(100, 150));
		iv.setScaleType(ImageView.ScaleType.FIT_XY);
		return iv;
	}

	@Override
	public boolean onCreateOptionsMenu(Menu menu) {
		// Inflate the menu; this adds items to the action bar if it is present.
		getMenuInflater().inflate(R.menu.main, menu);
		return true;
	}

}
