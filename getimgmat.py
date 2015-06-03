#search a dir and get a list of the images

import os
import sys
import re
import cv2
import numpy as np
def main(argv):
	##frist find all the patterns in the potensial strings
	grouppat=re.compile('facecrop/.-.-.')
	spacefix=re.compile('\w ')
	##prepare the files for the img list 
	#list the dict for labels
	ethnic={'A':0, 'W':1,'L':2,'F':3}
	age={'Y':0,'A':1,'O':2}
	gd={'F':0,'M':1}

	# fp1=open('ethnicimg.txt','w')
	# fp2=open('ageimg.txt','w')
	# fp3=open('gender.txt','w')
	# fp4=open('id.txt','w')
	# fp5=open('im.txt','w')

	# fp1ts=open('ethnicimg_ts.txt','w')
	# fp2ts=open('ageimg_ts.txt','w')
	# fp3ts=open('gender_ts.txt','w')
	# fp4ts=open('id_ts.txt','w')
	# fp5ts=open('im_ts.txt','w')
	import os
	classid=0
	#rename the directory with space in the string
	#otherwise it cause some trouble
	sps=re.compile('(?<=.) ')
	# for r,ds,fs in os.walk(argv[1]):
	# 	if len(ds)>0:
	# 		for d in ds:
	# 			nname=sps.sub('-',d)
	# 			print d, nname
	# 			try:
	# 				os.rename(d,nname)
	# 			except:
	# 				print 'error in renaming dir...'
	
	cnt_tr=0
	cnt_ts=0
	trdata=np.zeros((16790,50,50,3))
	tsdata=np.zeros((7244,50,50,3))
	tr_idlb=np.zeros((16790,))
	tr_gdlb=np.zeros((16790,))
	tr_etlb=np.zeros((16790,))
	tr_aglb=np.zeros((16790,))
	ts_idlb=np.zeros((7244,))
	ts_gdlb=np.zeros((7244,))
	ts_etlb=np.zeros((7244,))
	ts_aglb=np.zeros((7244,))
	import os.path
	for root,dirs,files in os.walk(argv[1]):
		# if 1:
			# d=root
			# #print "'",d,"'"
			# d=d.replace('facecrop','facecrop_agtr')
			
			# if (not os.path.exists(d)) and (not '_data' in d):
			# 	os.mkdir(d)
			# 	print 'create ',d

		if len(dirs)<5 and len(files)>20:
			filedir=grouppat.findall(root)
			import os.path
			fileconter=0
			filesnum=len(files)
			for f in files:
				if 'jpeg' in f or 'jpg' in f:
					fileconter+=1#sue this number to decide it as training or testing data
					if fileconter<filesnum*0.7:

						towrt=os.path.join(root,f)
						try:
							im=cv2.imread(towrt)
							im.shape
							im25=cv2.resize(im,(50,50))
							trdata[cnt_tr,:,:,:]=im25
							tr_idlb[cnt_tr]=classid
							tr_etlb[cnt_tr]=ethnic[filedir[0][9]]
							tr_aglb[cnt_tr]=age[filedir[0][11]]
							tr_gdlb[cnt_tr]=gd[filedir[0][13]]
							cnt_tr+=1
						except:
							print 'error at ',towrt
						# temname=towrt;
						# cpoldname=temname.replace('facecrop','facecp')
						# cpnname=sps.sub('_',temname)
						# cpnname=cpnname.replace('-','_')
						# try:						
						# 	os.rename(cpoldname,cpnname)
						# except:
						# 	print 'cp file rename error'
						#towrt=sps.sub('\ ',towrt)
						towrt=towrt.replace('/home/wei/Downloads/facecrop','')
						# fp1.write(towrt+'    '+str(ethnic[filedir[0][9]])+'\n')
						# fp2.write(towrt+'    '+str(age[filedir[0][11]])+'\n')
						# fp3.write(towrt+'    '+str(gd[filedir[0][13]])+'\n')
						# fp4.write(towrt+'    '+str(classid)+'\n')
						# fp5.write(towrt+',')
					else:
						towrt=os.path.join(root,f)
						try:
							im=cv2.imread(towrt)
							im.shape
							im25=cv2.resize(im,(50,50))
							#fileconter+=1
							tsdata[cnt_ts,:,:,:]=im25
							ts_idlb[cnt_ts]=classid
							ts_etlb[cnt_ts]=ethnic[filedir[0][9]]
							ts_aglb[cnt_ts]=age[filedir[0][11]]
							ts_gdlb[cnt_ts]=gd[filedir[0][13]]
							cnt_ts+=1
						except:
							print 'error at ',towrt
						# towrt=os.path.join(root,f)
						# #towrt=sps.sub('\ ',towrt)
						# towrt=towrt.replace('/home/wei/Downloads/facecrop/','')
						# fp1ts.write(towrt+'    '+str(ethnic[filedir[0][9]])+'\n')
						# fp2ts.write(towrt+'    '+str(age[filedir[0][11]])+'\n')
						# fp3ts.write(towrt+'    '+str(gd[filedir[0][13]])+'\n')
						# fp4ts.write(towrt+'    '+str(classid)+'\n')
						# fp5ts.write(towrt+',')
						

			classid=classid+1
	print classid
	print trdata.shape,tsdata.shape
	from sklearn.utils import shuffle
	trdata,tr_idlb,tr_gdlb,tr_aglb,tr_etlb=shuffle(trdata.reshape(16790,50*50*3),tr_idlb,tr_gdlb,tr_aglb,tr_etlb, random_state=0)
	tsdata,ts_idlb,ts_gdlb,ts_aglb,ts_etlb=shuffle(tsdata.reshape(7244,50*50*3),ts_idlb,ts_gdlb,ts_aglb,ts_etlb, random_state=0)
	import scipy.io
	scipy.io.savemat('imdbn_tr.mat',mdict={'data':trdata,'idlb':tr_idlb,'gdlb':tr_gdlb,'etlb':tr_etlb,'aglb':tr_aglb})
	scipy.io.savemat('imdbn_ts.mat',mdict={'data':tsdata,'idlb':ts_idlb,'gdlb':ts_gdlb,'etlb':ts_etlb,'aglb':ts_aglb})
	print ts_idlb[1:10], tr_aglb[1:10]
	print cnt_tr, cnt_ts
	print 'done.'



if __name__ == '__main__':
	main(sys.argv)


