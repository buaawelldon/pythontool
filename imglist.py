#prepare data set for deep expression learning, make sure the training data will have same number of samples
import os
import numpy
import random
import sys
#write the file names to the file
def main(argv):
	tslst=os.listdir('/home/wei/caffedata/webim/webemo_tsag/')
	dic={'A':0,'B':1,'C':2,'D':3,'E':4,'F':5,'G':6}
	fp=open('/home/wei/caffe-master/examples/facemodel/emo_ts.txt','w')
	for ss in tslst:
		if '.jp' in ss:
			fp.write(ss+' '+dic[ss[0]]+'\n')
	fp.close()

if __name__ == '__main__':
	main(sys.argv)