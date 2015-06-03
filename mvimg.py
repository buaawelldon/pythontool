import os,sys
import shutil
filedir1='/home/wei/caffe-master/examples/caffedata/webim/face_sup/'
filedir2='/home/wei/caffe-master/examples/caffedata/webim/webemo/'
head='G'
itms=os.listdir(filedir1)
cnt=0;
for it in itms:
	if '.jpg' in it or '.jpeg' in it:
		src=filedir1+it
		dst=filedir2+ head+str(cnt).zfill(8)+'.jpg'
		shutil.copyfile(src,dst)
		cnt+=1
print cnt
print 'done'

