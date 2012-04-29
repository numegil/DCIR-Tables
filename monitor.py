import os, pdb, urllib2
from time import sleep
from datetime import datetime

# Change these to match your current tournament
FILE_DIRECTORY = "/Users/numegil/Downloads"
FILE_PREFIX = "WLOC"
STARTING_TABLE = 1

# Don't change this one unless you know what you're doing
WEB_URL = "http://cold-galaxy-7337.herokuapp.com/set/"

path = FILE_DIRECTORY + '/' + FILE_PREFIX + '303.dat'

m_time = 0
while(True):

    # If the file's been modified
    if m_time != os.path.getmtime(path):
        m_time = os.path.getmtime(path)
        
        # Open the file
        lines = open(path).read().split('\n')
        
        # Figure out what the current round is
        cur_round = 0
        for line in lines:
            if len(line) < 1:
                continue
            
            # First digit of each line is the round (I think...)
            if int(line[0]) < cur_round:
                break
            else:
                cur_round = int(line[0])
        
        # We only care about the most recent round
        lines = lines[cur_round-1::cur_round]
        
        # Figure out which tables don't have results yet
        outstanding = []
        for i, line in enumerate(lines):
            if len(line) < 1:
                continue
            
            chars = line.split(',')
               
            # If the second digit is a 0, this table is invalid and ignore it
            if chars[1] == '0':
                continue 
            
            # If there's no match result, append it to outstanding tables
            if chars[4] == '0' and chars[5] == '0':
                outstanding.append(str(i+STARTING_TABLE))
        
        # Construct our GET parameter
        param = ','.join(outstanding)
        
        # Visit the target URL :)
        u = urllib2.urlopen(WEB_URL + '?tables=' + param)
        
        print "Updated", datetime.time(datetime.now())
    
    # Wait for a second
    sleep(1)
