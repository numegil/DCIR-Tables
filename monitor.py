import os, pdb, urllib2
from time import sleep
from datetime import datetime

# Change these to match your current tournaments
FILE_DIRECTORIES = ["C:\\Users\\numegil\\Dropbox\\oakland\\Sunday\\Sealed", "C:\\Users\\numegil\\Dropbox\\oakland\\Sunday\\Standard"]
FILE_PREFIXES = ["NPFK", "PIQA"]
STARTING_TABLES = [1, 125]

# Don't change this one unless you know what you're doing
WEB_URL = "http://cold-galaxy-7337.herokuapp.com/set/"

paths = []
for i in range(len(FILE_DIRECTORIES)):
	paths.append(FILE_DIRECTORIES[i] + '\\' + FILE_PREFIXES[i] + '303.dat')

m_time = 0
while(True):

	for i in range(len(FILE_DIRECTORIES)):

		# If the file's been modified
		if m_time != os.path.getmtime(paths[i]):
			m_time = os.path.getmtime(paths[i])
			
			# Open the file (It's possible to get an IOError if the file is currently being written to)
			worked = False
			while not worked:
				try:
					lines = open(paths[i]).read().split('\n')
					worked = True
				except IOError:
					sleep(1)
			
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
				if chars[4] == '0' and chars[5] == '0' and chars[6] == '0':
					outstanding.append(str(i+STARTING_TABLES[i]))
			
			# Construct our GET parameter
			param = ','.join(outstanding)
			
			# Visit the target URL :)
			u = urllib2.urlopen(WEB_URL + '?tables=' + param + '&tournament=' + FILE_PREFIXES[i])
			
			print 'Updated', FILE_PREFIXES[i], 'at', datetime.time(datetime.now())
		
		# Wait for a second
		sleep(1)
