import sklearn
import numpy
from sklearn.multiclass import OneVsRestClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
data=numpy.load('/home/wei/caffedata/webim/shapetr.npy')
data=numpy.reshape(data,(data.shape[0],68*2))
label=numpy.load('/home/wei/caffedata/webim/shapetrlb.npy')
datats=numpy.load('/home/wei/caffedata/webim/shapets.npy')
datats=numpy.reshape(datats,(datats.shape[0],68*2))
labelts=numpy.load('/home/wei/caffedata/webim/shapetslb.npy')
para=SVC()
rf=OneVsRestClassifier(para)
rfmodel=rf.fit(data,label)
prst=rfmodel.predict(datats)
ct=0
score=0
for lb in labelts:
	if prst[ct]==labelts[ct]:
		score=score+1
	ct=ct+1
print 'rate: ',float(score)/len(labelts), ', done.'