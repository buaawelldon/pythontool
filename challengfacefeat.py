import sklearn
import os
import sys
import numpy
import re
import os.path
def main(argv):
	dic={'Angry':0,'Disgust':1,'Fear':2,'Happy':3,'Neutral':4,'Sad':5,'Surprise':6}
	pathrt=argv[1]
	patt=re.compile('\w+')
	datatr=numpy.ndarray((578,70))
	lbtr=numpy.ndarray((578,))
	fderter=0
	# protostr='/home/wei/caffe-master/examples/facemodel/emo_quick_train_test_deploy.prototxt'
	# caffemodel='/home/wei/caffe-master/examples/facemodel/emo_iter_20000.caffemodel'
	# net = caffe.Classifier(protostr,caffemodel)


	# net.set_phase_test()
	# net.set_mode_gpu()
	# # input preprocessing: 'data' is the name of the input blob == net.inputs[0]
	# net.set_mean('data', '/home/wei/caffe-master/examples/facemodel/face_id_mean.npy')  # ImageNet mean
	# net.set_channel_swap('data', (2,1,0))  # the reference model has channels in BGR order instead of RGB
	# net.set_input_scale('data', 255)  # the reference model operates on images in [0,255] range instead of [0,1]
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
			sumarr=numpy.zeros((1,7))
			arrcnt=0
			#print fs
			try:
				while flag:
					cnt+=1
					fname=str(cnt)+'.npy'
					#print fname
					if fname in fs:
						npscr=numpy.load(os.path.join(rt,fname))
						#print npscr
						# img=caffe.io.load_image(fname)
						# imgr=cv2.resize(img,(100,100))
						# score = net.predict([imgr])
						sumarr+=npscr
						if arrcnt<10:
							datatr[fderter,arrcnt*7:arrcnt*7+7]=npscr
							arrcnt+=1						
					if cnt==numofnpy:
						flag=False
				avescr=sumarr/float(cnt)
				ave_resh=numpy.reshape(avescr,(7,1))
				#print classlb, avescr
				#datatr[fderter,:]=avescr
				lbtr[fderter]=classlb
				fderter+=1
			except:
				a=1
				#print rt
	print fderter
	print datatr.shape, lbtr.shape
	#boundray of Train and Val
			
	datats=numpy.ndarray((383,70))
	lbts=numpy.ndarray((383,))
	fderter=0
	pathrt=argv[2]
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
			sumarr=numpy.zeros((1,7))
			arrcnt=0
			#print fs
			while flag:
				cnt+=1
				fname=str(cnt)+'.npy'
				#print fname
				if fname in fs:
					npscr=numpy.load(os.path.join(rt,fname))
					#print npscr
					sumarr+=npscr
					if arrcnt<10:
						datats[fderter,arrcnt*7:arrcnt*7+7]=npscr
						arrcnt+=1
				if cnt==numofnpy:
					flag=False
			avescr=sumarr/float(cnt)
			ave_resh=numpy.reshape(avescr,(7,1))
			#print classlb, avescr
			#datats[fderter,:]=avescr
			lbts[fderter]=classlb
			fderter+=1

	print fderter


	print datats[10,:], lbts.shape

	#now the learning part
	from sklearn.multiclass import OneVsRestClassifier
	from sklearn.ensemble import RandomForestClassifier
	from sklearn.svm import SVC
	#para=SVC()
	para=RandomForestClassifier()
	rf=OneVsRestClassifier(para)
	rfmodel=rf.fit(datatr,lbtr)
	prst=rfmodel.predict(datatr)
	ct=0
	score=0
	for lb in lbtr:
		#print prst[ct],lb
		if prst[ct]==lb:
			score=score+1
		ct=ct+1
	print 'rate: ',float(score)/len(lbtr), ', done.'
if __name__ == '__main__':
	main(sys.argv)






