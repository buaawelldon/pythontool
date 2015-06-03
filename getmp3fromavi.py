import subprocess
import sys
import os

def main(argv):
	n=len(argv)
	print n
	for i in range(1,n):
		command=['ffmpeg', '-i',\
		argv[i], '-acodec', 'copy',\
		argv[i].replace('.avi','.mp3')]
		#print command
		subprocess.call(command)
if __name__ == '__main__':
	main(sys.argv)