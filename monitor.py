import os, pdb, urllib2
from time import sleep
from datetime import datetime

FILE_DIRECTORY = "C:\\Program Files\\Wizards of the Coast\\Version3"
FILE_PREFIX = "OKRW"
WEB_URL = "http://cold-galaxy-7337.herokuapp.com/set/"

path = FILE_DIRECTORY + '\\' + FILE_PREFIX + '303.dat'

m_time = 0
while(True):

    # If the file's been modified
    if m_time != os.path.getmtime(path):
        m_time = os.path.getmtime(path)
        
        # Get every third line of the file
        lines = open(path).read().split('\n')[2::3]
        
        # Figure out which tables don't have results yet
        outstanding = []
        for i, line in enumerate(lines):
            chars = line.split(',')
            if chars[4] == '0' and chars[5] == '0':
                outstanding.append(str(i+1))
        
        # Construct our GET parameter
        param = ','.join(outstanding)
        
        # Visit the target URL :)
        u = urllib2.urlopen(WEB_URL + '?tables=' + param)
        
        print "Updated", datetime.time(datetime.now())
    
    # Wait for a second
    sleep(1)
