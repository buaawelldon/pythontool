#use for one img or a directery based on the name
import facepp
from facepp import API
from facepp import File
import cv2
from pprint import pformat
import os
import os.path
import sys
API_KEY = 'd45344602f6ffd77baeab05b99fb7730'
API_SECRET = 'jKb9XJ_GQ5cKs0QOk6Cj1HordHFBWrgL'
api = API(API_KEY, API_SECRET)
def getroi(rst):
	roi=[0,0,0,0]
	xm=rst['face'][0]['position']['center']['x']
	ym=rst['face'][0]['position']['center']['y']
	w=rst['face'][0]['position']['width']
	emx=0.5*(rst['face'][0]['position']['eye_left']['x']+rst['face'][0]['position']['eye_right']['x'])
	emy=0.5*(rst['face'][0]['position']['eye_left']['y']+rst['face'][0]['position']['eye_right']['y'])
	mmx=0.5*(rst['face'][0]['position']['mouth_left']['x']+rst['face'][0]['position']['mouth_right']['x'])
	mmy=0.5*(rst['face'][0]['position']['mouth_left']['y']+rst['face'][0]['position']['mouth_right']['y'])
	h=rst['face'][0]['position']['height']
	sch=rst['img_height']
	scw=rst['img_width']
	roi=[(ym-h/2)*sch/100,(mmy+h/2)*sch/100,(xm-w/2)*scw/100,(xm+w/2)*scw/100]
	return roi
def faceroi(path):
	#check if the path is a image file or a directory
	if os.path.isfile(path[1]):
		rst=api.detection.detect(img = File(path[1]));
		#get roi based on rst structure
		roi=getroi(rst)
		img=cv2.imread(path[1])
		print roi
		cv2.imshow('img',img[roi[0]:roi[1],roi[2]:roi[3]])
		while(True):
			k=cv2.waitKey(6000)
			#if k==21:
			#	return
			
	if os.path.isdir(path[1]):
		for rt,dr,fs in os.walk(path[1]):
			#print rt
			if not '_face' in rt:
				if dr==[] and len(fs)>5:
					for f in fs:
						if '.jpg' in f:
							try:
								imgpath=os.path.join(rt,f)
								rst=api.detection.detect(img = File(imgpath));
								roi=getroi(rst)
								img=cv2.imread(imgpath)

								neofolder=rt+'_facepp/'
								if not os.path.isdir(neofolder):
									os.mkdir(neofolder)
								cv2.imwrite(neofolder+f,img[roi[0]:roi[1],roi[2]:roi[3]])
							except:
								hehe=1 

def print_result(hint, result):
	def encode(obj):
		if type(obj) is unicode:
			return obj.encode('utf-8')
		if type(obj) is dict:
			return {encode(k): encode(v) for (k, v) in obj.iteritems()}
		if type(obj) is list:
			return [encode(i) for i in obj]
		return obj
	print hint
	result = encode(result)
	print '\n'.join(['  ' + i for i in pformat(result, width = 75).split('\n')])

def main(argv):
	

	faceroi(argv)
	#rst=api.detection.detect(img = File('/Users/wei/Documents/chiling.jpg'))
	#print_result('''here's the result''',rst)
	#print rst['face'][0]['position']['center']['x']

if __name__ == '__main__':
	main(sys.argv)

