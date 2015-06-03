#run in python, getimgfromvideo videoname imgsfolder N, the 
#parameters:  videoname, name of the video to be processed, just need to be imported by opencv
#             imgfolder : the imag sequence to be saved in
#             N : sampling rate, original video may be 30HZ, but you may not need so high intensity
import cv2
import numpy as np 
import sys
import os
def main(argv):
	
	print len(argv)
	N=argv[1];

	for i in range(2,len(argv)):
		vname=argv[i]
		#print vname, savefolder, N
		cap=cv2.VideoCapture()
		cap.open(vname)
		num=0;
		itor=0;
		if not (os.path.isdir(vname.replace('.mp4',''))):
			f=os.mkdir(vname.replace('.mp4','/'))
		try:
			while (cap.isOpened()):
				ret, frame=cap.read()
				framegr=cv2.cvtColor(frame,cv2.COLOR_RGB2GRAY)
				rzimg=cv2.resize(framegr,(960,540))
				#cv2.imshow('show',rzimg)		
				#cv2.waitKey(10)
				num=num+1;


				#print num 
				if num==int(N):
					#print 'ready to save'
					num=0;
					itor=itor+1;
					cv2.imwrite(vname.replace('.mp4','')+r'/'+vname.replace('.mp4','_')+str(itor)+'.jpg',rzimg)
		except Exception as e:
			print e


	print " that's it. "




if __name__ == '__main__':
	main(sys.argv)