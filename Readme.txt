This simple app allows you to view outstanding tables in DCIR on your phone while running a tournament.

There are three components:
1) Python script named 'monitor.py' which must run continuously on the computer running DCIR.  You need to set the FILE_DIRECTORY and FILE_PREFIX variables in the script to match the tournament you're running.
2) The webserver backend.  This is in the 'dcif_tables' directory of the repository.  I have the code deployed to Heroku, so you probably don't need to worry about this part.
3) The client.  Currently, only an iPhone version of the client exists.  I hope to add an Android version soon.  Additionally, you can visit the web server att 'http://cold-galaxy-7337.herokuapp.com/get/' to view the current outstandingg tables.

This is all a very hastily put together rough draft of the app.  There's a bajillion features missing;  I want to try it first to see if it's worth more of my time.
