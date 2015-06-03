#this script is for combine 4 cnn model feature to have a logistic regression output
#the code is based on CAFFE demo
#by Wei Li. CCNY Mar 2015

#1. read the feature data from .npy

import numpy as np 
import caffe
import os
import h5py
import shutil
import tempfile


modelpath='/home/wei/caffedata/feat/'
datafilesname=['id_tr.npy','id_ts.npy','et_tr.npy','et_ts.npy','ag_tr.npy',\
'ag_ts.npy','gd_tr.npy','gd_ts.npy','em_tr.npy','em_ts.npy']
lbfile=['id_trlabel.npy','id_tslabel.npy','et_trlabel.npy','et_tslabel.npy',\
'ag_trlabel.npy','ag_tslabel.npy','gd_trlabel.npy','gd_tslabel.npy','em_trlabel.npy','em_tslabel.npy']

# load the data
id_tr=np.load(modelpath+datafilesname[0])
id_ts=np.load(modelpath+datafilesname[1])
id_tr_lb=np.load(modelpath+lbfile[8])
id_ts_lb=np.load(modelpath+lbfile[9])


et_tr=np.load(modelpath+datafilesname[2])
et_ts=np.load(modelpath+datafilesname[3])
ag_tr=np.load(modelpath+datafilesname[4])
ag_ts=np.load(modelpath+datafilesname[5])
gd_tr=np.load(modelpath+datafilesname[6])
gd_ts=np.load(modelpath+datafilesname[7])
em_tr=np.load(modelpath+datafilesname[8])
em_ts=np.load(modelpath+datafilesname[9])

id_tr=np.concatenate((id_tr,et_tr,ag_tr,gd_tr,em_tr),axis=1)
id_ts=np.concatenate((id_ts,et_ts,ag_ts,gd_ts,em_ts),axis=1)

#for cross experiment, do it here



print id_tr.shape
print id_ts.shape

def npnorm(arr1,mode=1):
	#normorlize the whole arr, mode 1 means norm for each row, mode 2 mean for column
	shp=arr1.shape
	if mode==1:
		for i in range(shp[0]):
			r=np.amax(arr1[i,:])
			arr1[i,:]=arr1[i,:]/r;
		return arr1
	if mode==2:
		for i in range(shp[1]):
			r=np.amax(arr1[:,i])
			arr1[:,i]=arr1[:,i]/r;
		return arr1
	else:
		return arr1


id_tr=npnorm(id_tr,2)
it_ts=npnorm(id_ts,2)
from sklearn.utils import shuffle
id_tr,id_tr_lb=shuffle(id_tr, id_tr_lb, random_state=0)
print id_tr_lb[0:100]
dirname = os.path.abspath(modelpath+'./hdf5_classification/data')
if not os.path.exists(dirname):
    os.makedirs(dirname)

train_filename = os.path.join(dirname, 'train.h5')
test_filename = os.path.join(dirname, 'test.h5')
# HDF5DataLayer source should be a file containing a list of HDF5 filenames.
# To show this off, we'll list the same data file twice.

with h5py.File(train_filename, 'w') as f:
    f['data'] = id_tr
    f['label'] = id_tr_lb.astype(np.float32)
with open(os.path.join(dirname, 'train.txt'), 'w') as f:
    f.write(train_filename + '\n')


with h5py.File(test_filename, 'w') as f:
    f['data'] = id_ts
    f['label'] = id_ts_lb.astype(np.float32)
with open(os.path.join(dirname, 'test.txt'), 'w') as f:
    f.write(test_filename + '\n')


# def learn_and_test(solver_file):
#     #caffe.set_mode_gpu()
#     solver = caffe.get_solver(solver_file)
#     solver.solve()

#     accuracy = 0
#     test_iters = int(len(Xt) / solver.test_nets[0].blobs['data'].num)
#     for i in range(test_iters):
#         solver.test_nets[0].forward()
#         accuracy += solver.test_nets[0].blobs['accuracy'].data
#     accuracy /= test_iters
#     return accuracy

# acc = learn_and_test('hdf5_classification/solver.prototxt')
# print("Accuracy: {:.3f}".format(acc))
    
# # HDF5 is pretty efficient, but can be further compressed.
# comp_kwargs = {'compression': 'gzip', 'compression_opts': 1}
# with h5py.File(test_filename, 'w') as f:
#     f.create_dataset('data', data=Xt, **comp_kwargs)
#     f.create_dataset('label', data=yt.astype(np.float32), **comp_kwargs)
# with open(os.path.join(dirname, 'test.txt'), 'w') as f:
#     f.write(test_filename + '\n')

