## image the usage: python matmadeface   ...AFEW/*/*/*    
## argv[i] 

import numpy
import scipy.io as sio
import sys
import os
import cv2
import os.path as path
import re
import dlib
def main(argv):
	detector = dlib.get_frontal_face_detector()
	predictor_path ='./shape_predictor_68_face_landmarks.dat'
	predictor = dlib.shape_predictor(predictor_path)
	lenth=len(argv)
	temprec=dlib.rectangle()

	print lenth
	for itr in range(1,lenth):
		patt=re.compile('\d+'+'.avi')
		matpath='/home/wei/caffedata/emotiw14/Val/Val_Points/'
		#print patt.findall(argv[1])[0]
		matname=patt.findall(argv[itr])[0]
		videopath=argv[itr]
		matpath+=matname.replace('.avi','.mat')
		facepath=argv[itr].replace('.avi','_face/')
		facepathd=argv[itr].replace('.avi','_faced/')
		facepathpp=argv[itr].replace('.avi','_facepp/')
		print 'for ',videopath
		num=0
		if not os.path.exists(facepath):
			os.mkdir(facepath)
		if not os.path.exists(facepathd):
			os.mkdir(facepathd)
		try:
			ptsmat=sio.loadmat(matpath)
			num=ptsmat['pred'].shape[1]

		except:
			print 'not mat exist for ',matname
			
		#print ptsmat['pred'].shape[1]
		#print num
		#for fisrt one, it's[][][2] fot others it's [][][0], check other samples to make sure
		#print ptsmat['pred'].[1,0][0][0]
		
		# pts=ptsmat['pred'][0,1][0][0][2]
		# bbox=numpy.ndarray((2,2))
		# bbox[0,:]=numpy.amin(pts,axis=0)
		# bbox[1,:]=numpy.amax(pts,axis=0)
		#print bbox
		# print 
		# img=cv2.imread(argv[1]+'/'+'1.jpg')
		# print img.shape
		# cv2.imwrite('/Volumes/Transcend/macdata/face1.jpg',img[int(bbox[0,1]):int(bbox[1,1]),int(bbox[0,0]):int(bbox[1,0]),:])
		#cv2.imshow('wnd1',img)
		#print int(bbox[0,1]),int(bbox[1,1]),int(bbox[0,0]),int(bbox[0,1])
		#cv2.imshow('wnd2',img[int(bbox[0,1]):int(bbox[1,1]),int(bbox[0,0]):int(bbox[1,0]),:])
		#cv2.imshow('wnd2',img[164:343,333:549,:])
		#cv2.waitKey(10000)
		
		for i in range(0,num):
			if num>1:
				try:
					#standard mat give pts
					if ptsmat['pred'][0,i][0][0][0].shape==(49,2):
						pts=ptsmat['pred'][0,i][0][0][0]
					if ptsmat['pred'][0,i][0][0][2].shape==(49,2):
						pts=ptsmat['pred'][0,i][0][0][2]
					bbox=numpy.ndarray((2,2))
					#print bbox					
					bbox[0,:]=numpy.amin(pts,axis=0)
					bbox[1,:]=numpy.amax(pts,axis=0)
					h=bbox[1,0]-bbox[0,0]
					w=bbox[1,1]-bbox[0,1]
					#print bbox
					rec_l=int(bbox[0,0]-w/4)
					if rec_l<1:
						rec_l=1
					rec_t=int(bbox[0,1]-h/4)
					if rec_t<1:
						rec_t=1
					rec_r=int(bbox[1,0]+w/4)
					rec_b=int(bbox[1,1]+h/4)
					temprec=dlib.rectangle(rec_l,rec_t,rec_r,rec_b)
					#print temprec
					#print bbox
					#print videopath
					img=cv2.imread(videopath.replace('.avi','')+'/'+str(i+1)+'.jpg')
					#print img.shape
					savepath=os.path.join(facepath,str(i+1)+'.jpg')
					savepathd=os.path.join(facepathd,str(i+1)+'.jpg')
					#print savepath
					shape = predictor(img, temprec)
					
					shapenp=numpy.ndarray((68,2))
					
					for i in range(0,68):
						shapenp[i,:]=[shape.part(i).x,shape.part(i).y]
					shbox=numpy.ndarray((2,2))
					shbox[0,:]=numpy.amin(shapenp,axis=0)
					shbox[1,:]=numpy.amax(shapenp,axis=0)

					#print shapenp	
					if shbox[0,0]<=0:
						shbox[0,0]=1
					if shbox[0,1]<0:
						shbox[0,1]=1
					cv2.imwrite(savepath,img[int(bbox[0,1]):int(bbox[1,1]),int(bbox[0,0]):int(bbox[1,0]),:])
					cv2.imwrite(savepathd,img[shbox[0,1]:shbox[1,1],shbox[0,0]:shbox[1,0],:])
					numpy.save(savepathd.replace('.jpg',''),shapenp)
					#using dlib


				except Exception as e:
					print e	
			#print 'done with', matname
if __name__ == '__main__':
	main(sys.argv)
