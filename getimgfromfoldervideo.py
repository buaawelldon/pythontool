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
	#print argv[2]
	for i in range(3,len(argv)):
		vname=argv[i]
		print vname
		#print vname, savefolder, N
		cap=cv2.VideoCapture()
		cap.open(vname)
		num=0;
		itor=0;
		fileext='.mp4';
		#if not (os.path.isdir(vname.replace(filext,''))):
		#	f=os.mkdir(vname.replace(fileext,'/'))
		
		while (cap.isOpened()):
			ret, frame=cap.read()
				
			try:
				#framegr=cv2.cvtColor(frame,cv2.COLOR_RGB2GRAY)
				#rzimg=cv2.resize(frame,(720,576))
				#cv2.imshow('show',rzimg)		
				#cv2.waitKey(10)
				num=num+1;
				print frame.shape

				#print num 
				if num==int(N):
					#print 'ready to save'
					num=0;
					itor=itor+1;
					savepath=argv[2].replace(fileext,'')+'/'+str(itor)+'.jpg'
					if not os.path.isdir(argv[2].replace(fileext,'')):
						os.mkdir(argv[2].replace(fileext,''))
					cv2.imwrite(savepath,frame)
				#print 'save it'
					#print savepath
			except Exception as e:
				print e


	print " that's it. "




if __name__ == '__main__':
	main(sys.argv)
