import sklearn
import os
import sys
import numpy
import re
import os.path
dic={'Angry':0,'Disgust':1,'Fear':2,'Happy':3,'Neutral':4,'Sad':5,'Surprise':6}
pathrt='/home/wei/caffedata/emotiw14/AFEW_4_0/Train/'
patt=re.compile('\w+')
fp1=open('/home/wei/caffedata/emotiw14/emotiw_tr.txt','w')
for rt, dr,fs in os.walk(pathrt):
	if '_faced' in rt:

		k=re.findall(patt,rt)
		classlb=dic[k[-2]]#here's the class id 
		#now calculate all the score and then get average
		cnt=0
		allter=0
		#this is to make sure the order in right
		numofnpy=len(fs)/2
		flag=True
		arrcnt=0
		#print fs
		try:
			while flag:
				cnt+=1
				fname=str(cnt)+'.jpg'
				#print fname
				if fname in fs:
					#npscr=numpy.load(os.path.join(rt,fname))
					#print npscr
					# img=caffe.io.load_image(fname)
					# imgr=cv2.resize(img,(100,100))
					# score = net.predict([imgr])
					imgfile=rt.replace(pathrt,'')
					toprint=imgfile+'/'+fname+' '+str(classlb)+'\n'
					fp1.write(toprint)
				if cnt==numofnpy:
					flag=False
			#print classlb, avescr
			#datatr[fderter,:]=avescr
			
		except:
			hehe=1