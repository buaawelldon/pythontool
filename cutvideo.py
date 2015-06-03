import subprocess as sp
import numpy
import matplotlib.pyplot as plt
import cv2
import sys
def main(argv):
	FFMPEG_BIN = "ffmpeg"
	N=len(argv)
	print N
	for i in range(1,N):
		command = [ FFMPEG_BIN,
		            '-i', argv[i],
		            '-f', 'image2pipe',
		            '-pix_fmt', 'rgb24',
		            '-vcodec', 'rawvideo', '-']
		pipe = sp.Popen(command, stdout = sp.PIPE, stderr=sp.PIPE, bufsize=10**8)
		print argv[i]
		#print pipe

		# raw_image = pipe.stdout.read(1280*720*3)
		# # transform the byte read into a numpy array
		# image =  numpy.fromstring(raw_image, dtype='uint8')
		# image = image.reshape((720,1280,3))
		# print image
		# # throw away the data in the pipe's buffer.
		# pipe.stdout.flush()
		savepath=argv[i].replace('.avi','')
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
				# cv2.imshow('window',imgshow)
				# cv2.waitKey(1)
				cnt+=1
				filename=os.path.join(savepath,str(cnt)+'.jpg')
						#print cropface.shape
				cv2.imwrite(filename,cv2.cvtColor(imgshow,cv2.COLOR_BGR2RGB))
			else:
				print 'end of file, exit'
				break

	print 'done...'
if __name__ == '__main__':
	main(sys.argv)


