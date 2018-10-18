import os
import sys

if len(sys.argv) > 2:
	source = sys.argv[1]
	dest = sys.argv[2]
	sourceDir = '/home/' + source
	destDir = '/home/' + dest
	print "Copying " + sourceDir + " to " + destDir
	
else:
	print "Please supply a source and destination user"

