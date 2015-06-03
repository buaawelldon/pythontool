import h5py
import sklearn
import sklearn.datasets
import sklearn.cross_validation
import numpy as np
import os

x,y =sklearn.datasets.make_classification(
	n_samples=1000,
	n_features=30,
	);


emgmat=sio.loadmat(r'../EMG/dataemg.mat');
emgdata=emgmat['data'];
data=np.ndarray((110*23,2000));
label=np.ndarray((110*23,))
for i in range(23):
	for j in range(110):
		data[i*110+j,:]=emgdata[i,j*4040:(j+1)*4040,1];
		classid=j%22;
		if classid==0:
			classid=22;
		label[i*110+j,:]=i.astype(np.float32)




x,xt,y,yt=sklearn.cross_validation.train_test_split(data,label);





dirname=os.path.abspath('data')
if not os.path.exists(dirname):
	os.mkdir(dirname)
train_filename=os.path.join(dirname,'train.h5')
test_filename=os.path.join(dirname,'test.h5')

with h5py.File(train_filename,'w') as f:
	f['data']=x
	f['label']=y.astype(np.float32)
print x
with open(os.path.join(dirname,'train.txt'),'w') as f:
	f.write(train_filename+'\n')

with h5py.File(test_filename,'w') as f:
	f['data']=xt
	f['label']=yt.astype(np.float32)

with open(os.path.join(dirname,'test.txt'),'w') as f:
	f.write(test_filename+'\n')
	
