import numpy
import cv2

def gettranmat(shm,shape):

	


def main():
	shapall=numpy.load('/home/wei/caffedata/webim/shape.npy')
	shape_mean=numpy.mean(shapall,axis=0)
	img=cv2.imread('')
	predictor_path ='./shape_predictor_68_face_landmarks.dat'
	detector = dlib.get_frontal_face_detector()
	predictor = dlib.shape_predictor(predictor_path)
	dets = detector(img, 1)
    #print("Number of faces detected: {}".format(len(dets)))
	shapenp=numpy.ndarray((68,2))
	for k, d in enumerate(dets):
		# print("Detection {}: Left: {} Top: {} Right: {} Bottom: {}".format(
		#     k, d.left(), d.top(), d.right(), d.bottom()))
		# # Get the landmarks/parts for the face in box d.
		#print type(d)
		lbdic=f.replace(argv[1],'')
		temprec=d
		shape = predictor(img, d)                   
		for i in range(0,68):
			shapenp[i,:]=[shape.part(i).x,shape.part(i).y]
	gettranmat(shape_mean,shapenp)

if __name__ == '__main__':
	main()