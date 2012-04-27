package com.alexei.dcitables;

import java.io.BufferedInputStream;
import java.io.DataInputStream;
import java.io.IOException;
import java.io.InputStream;
import java.net.MalformedURLException;
import java.net.URL;

import android.app.ListActivity;
import android.os.Bundle;
import android.view.View;
import android.widget.ArrayAdapter;
import android.widget.Button;
import android.widget.ListView;
import android.widget.TextView;

public class DCIR_TablesActivity extends ListActivity
{
	final String HEROKU_URL = "http://cold-galaxy-7337.herokuapp.com/get_api/";

	/** Called when the activity is first created. */
	@Override
	public void onCreate(Bundle icicle) {
		super.onCreate(icicle);
	    setContentView(R.layout.main);

	    refreshData();
	    
	    final Button button = (Button) findViewById(R.id.refreshButton);
        button.setOnClickListener(new View.OnClickListener() {
            public void onClick(View v) {
                refreshData();
            }
        });
	    
	    
	}
	
	// Downloads data from URL and updates the list view
	public void refreshData()
	{
		// Create an array of Strings, that will be put to our ListActivity
		String[] names = new String[] { "Error!" };

		URL u;
		InputStream is = null;
		DataInputStream dis;
		String s;
		
		// Read data from Internet and put it into names array.
		try {
			u = new URL(HEROKU_URL);
			is = u.openStream(); // throws an IOException
			dis = new DataInputStream(new BufferedInputStream(is));
			while ((s = dis.readLine()) != null) {
				names = s.split(",");
			}

		} catch (MalformedURLException mue) {

			System.out.println("Ouch - a MalformedURLException happened.");
			mue.printStackTrace();
			System.exit(1);

		} catch (IOException ioe) {

			System.out.println("Oops- an IOException happened.");
			ioe.printStackTrace();
			System.exit(1);

		} finally {

			try {
				is.close();
			} catch (IOException ioe) {
				// just going to ignore this one
			}

		} // end of 'finally' clause

		// Create an ArrayAdapter, that will actually make the Strings above appear in the ListView
		ListView lv = getListView();
		lv.setAdapter(new ArrayAdapter<String>(DCIR_TablesActivity.this, android.R.layout.simple_list_item_1, names));
		
		// Update text field
		final TextView textview = (TextView) findViewById(R.id.countTextView);
		textview.setText("There are " + names.length + " tables outstanding.");
	}

}
