#this python script is written for getting all the faces images 
#from a folder
import dlib
import cv2
from skimage import io
import os.path
import numpy as np
import sys
def main(argv):
	#initial the face detector
	detector = dlib.get_frontal_face_detector()
	if not os.path.isdir(argv[1]):
		print 'not a real directory'
		return
	else:
		for rt,dr,fps in os.walk(argv[1]):
			#nrt=rt.replace('facedowns','facecrop')
			nrt='/home/wei/caffedata/temp'
			nrt=argv[1]+'_face/'
			cnt=0
			if not os.path.exists(nrt):
				os.mkdir(nrt)			
			if len(fps)>20:
				for fp in fps:
					if ('.jpeg' in fp or '.jpg' in fp):
						#get the face abs path
						try:
							imgpath=os.path.join(rt,fp)
							imgor=io.imread(imgpath)
							facerec=detector(cv2.cvtColor(imgor,cv2.COLOR_BGR2RGB),1)
							#print facerec
							
							for k,d in enumerate(facerec):
								x0=d.left()
								xn=d.right()
								yn=d.bottom()
								y0=d.top()
								cropface=imgor[y0:yn,x0:xn,:]
								#should get a new name for the file
								#newfp=fp.replace('.jp',str(cnt)+'.jp')#incase there are many faces in one image. but this may get more wrong images
								newfp=fp
								cnt=cnt+1
								savepath=os.path.join(nrt,newfp)
								savepath=os.path.join(nrt,str(cnt)+'.jpg')

								print cropface.shape
								cv2.imwrite(savepath,cv2.cvtColor(cropface,cv2.COLOR_BGR2RGB))
						except :
							print imgpath, 'error here'


if __name__ == '__main__':
	main(sys.argv)




