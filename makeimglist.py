#search a dir and get a list of the images

import os
import sys
import re

def main(argv):
	##frist find all the patterns in the potensial strings
	grouppat=re.compile('facecrop_agtr/.-.-.')
	spacefix=re.compile('\w ')
	##prepare the files for the img list 
	#list the dict for labels
	ethnic={'A':0, 'W':1,'L':2,'F':3}
	age={'Y':0,'A':1,'O':2}
	gd={'F':0,'M':1}

	fp1=open('ethnicimg.txt','w')
	fp2=open('ageimg.txt','w')
	fp3=open('gender.txt','w')
	fp4=open('id.txt','w')
	fp5=open('im.txt','w')

	fp1ts=open('ethnicimg_ts.txt','w')
	fp2ts=open('ageimg_ts.txt','w')
	fp3ts=open('gender_ts.txt','w')
	fp4ts=open('id_ts.txt','w')
	fp5ts=open('im_ts.txt','w')
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
					fileconter=fileconter+1 #sue this number to decide it as training or testing data
					if fileconter<filesnum*0.7:
						towrt=os.path.join(root,f)
						# temname=towrt;
						# cpoldname=temname.replace('facecrop','facecp')
						# cpnname=sps.sub('_',temname)
						# cpnname=cpnname.replace('-','_')
						# try:						
						# 	os.rename(cpoldname,cpnname)
						# except:
						# 	print 'cp file rename error'
						# towrt=sps.sub('\ ',towrt)
						towrt=towrt.replace('/home/wei/Downloads/facecrop_agtr','')
						fp1.write(towrt+'    '+str(ethnic[filedir[0][14]])+'\n')
						fp2.write(towrt+'    '+str(age[filedir[0][16]])+'\n')
						fp3.write(towrt+'    '+str(gd[filedir[0][18]])+'\n')
						fp4.write(towrt+'    '+str(classid)+'\n')
						fp5.write(towrt+',')
					else:
						towrt=os.path.join(root,f)
						#towrt=sps.sub('\ ',towrt)
						towrt=towrt.replace('/home/wei/Downloads/facecrop_agtr/','')
						fp1ts.write(towrt+'    '+str(ethnic[filedir[0][14]])+'\n')
						fp2ts.write(towrt+'    '+str(age[filedir[0][16]])+'\n')
						fp3ts.write(towrt+'    '+str(gd[filedir[0][18]])+'\n')
						fp4ts.write(towrt+'    '+str(classid)+'\n')
						fp5ts.write(towrt+',')

			classid=classid+1
	print classid
	print 'done.'



if __name__ == '__main__':
	main(sys.argv)


