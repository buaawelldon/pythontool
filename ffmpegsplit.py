import subprocess as sp
import numpy
import matplotlib.pyplot as plt
import cv2
import sys
import dlib
def main(argv):
	detector = dlib.get_frontal_face_detector()
	FFMPEG_BIN = "ffmpeg"
	command = [ FFMPEG_BIN,
	            '-i', argv[1],
	            '-f', 'image2pipe',
	            '-pix_fmt', 'rgb24',
	            '-vcodec', 'rawvideo', '-']
	pipe = sp.Popen(command, stdout = sp.PIPE, stderr=sp.PIPE, bufsize=10**8)
	print pipe

	# raw_image = pipe.stdout.read(1280*720*3)
	# # transform the byte read into a numpy array
	# image =  numpy.fromstring(raw_image, dtype='uint8')
	# image = image.reshape((720,1280,3))
	# print image
	# # throw away the data in the pipe's buffer.
	# pipe.stdout.flush()
	framecter=0
	savepath=argv[1].replace('.avi','')
	import os.path 
	if not os.path.isdir(savepath):
		os.mkdir(savepath)
	cnt=0
	while(1):
		img=pipe.stdout.read(720*576*3)
		#print len(img)
		if (len(img)==720*576*3):
			imgshow=numpy.fromstring(img,dtype='uint8')		
			imgshow=imgshow.reshape(576,720,3)
			destRGB = cv2.cvtColor(imgshow, cv2.COLOR_BGR2RGB)

			try:
				facerec=detector(destRGB,1)				
				for k,d in enumerate(facerec):
					x0=d.left()
					xn=d.right()
					yn=d.bottom()
					y0=d.top()
					cropface=imgshow[y0:yn,x0:xn,:]
					#should get a new name for the file
					#newfp=fp.replace('.jp',str(cnt)+'t.jp')#incase there are many faces in one image. but this may get more wrong images
					cnt=cnt+1
					
					filename=os.path.join(savepath,str(cnt)+'.jpg')
					#print cropface.shape
					cv2.imwrite(filename,cv2.cvtColor(cropface,cv2.COLOR_BGR2RGB))
			except:
				print 'no face here.'
			# cv2.imshow('window',destRGB)
			# framecter+=1
			# cv2.waitKey(1)
		else:
			print 'end of file, exit'
			break
	#print 'total frames is ', str(framecter)
	#print 'done...'
if __name__ == '__main__':
	main(sys.argv)


