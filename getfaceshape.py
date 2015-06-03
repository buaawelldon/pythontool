#!/usr/bin/python
# The contents of this file are in the public domain. See LICENSE_FOR_EXAMPLE_PROGRAMS.txt
#
#   This example program shows how to find frontal human faces in an image and
#   estimate their pose.  The pose takes the form of 68 landmarks.  These are
#   points on the face such as the corners of the mouth, along the eyebrows, on
#   the eyes, and so forth.
#
#   This face detector is made using the classic Histogram of Oriented
#   Gradients (HOG) feature combined with a linear classifier, an image pyramid,
#   and sliding window detection scheme.  The pose estimator was created by
#   using dlib's implementation of the paper:
#      One Millisecond Face Alignment with an Ensemble of Regression Trees by
#      Vahid Kazemi and Josephine Sullivan, CVPR 2014
#   and was trained on the iBUG 300-W face landmark dataset.
#
#   Also, note that you can train your own models using dlib's machine learning
#   tools. See train_shape_predictor.py to see an example.
#
#   You can get the shape_predictor_68_face_landmarks.dat file from:
#   http://sourceforge.net/projects/dclib/files/dlib/v18.10/shape_predictor_68_face_landmarks.dat.bz2
#
# COMPILING THE DLIB PYTHON INTERFACE
#   Dlib comes with a compiled python interface for python 2.7 on MS Windows. If
#   you are using another python version or operating system then you need to
#   compile the dlib python interface before you can use this file.  To do this,
#   run compile_dlib_python_module.bat.  This should work on any operating
#   system so long as you have CMake and boost-python installed.
#   On Ubuntu, this can be done easily by running the command:
#       sudo apt-get install libboost-python-dev cmake
import sys
import os
import dlib
import glob
from skimage import io
import getfacepp
import numpy
# if len(sys.argv) != 3:
#     print(
#         "Give the path to the trained shape predictor model as the first "
#         "argument and then the directory containing the facial images.\n"
#         "For example, if you are in the python_examples folder then "
#         "execute this program by running:\n"
#         "    ./face_landmark_detection.py shape_predictor_68_face_landmarks.dat ../examples/faces\n"
#         "You can download a trained facial shape predictor from:\n"
#         "    http://sourceforge.net/projects/dclib/files/dlib/v18.10/shape_predictor_68_face_landmarks.dat.bz2")
#     exit()
def main(argv):
    pass
    predictor_path ='./shape_predictor_68_face_landmarks.dat' 
    faces_folder_path = sys.argv[1]
    dic={'A':0,'B':1,'C':2,'D':3,'E':4,'F':5,'G':6}

    detector = dlib.get_frontal_face_detector()
    predictor = dlib.shape_predictor(predictor_path)
    #win = dlib.image_window()
    temprec=dlib.rectangle()
    
    num=len(glob.glob(os.path.join(faces_folder_path, "*.jpg")))
    data=numpy.ndarray((8382,68,2))
    label=numpy.ndarray((8382,))
    cnt=0
    for f in glob.glob(os.path.join(faces_folder_path, "*.jpg")):
        #print("Processing file: {}".format(f))
        img = io.imread(f)

        #win.clear_overlay()
        #win.set_image(img)

        # Ask the detector to find the bounding boxes of each face. The 1 in the
        # second argument indicates that we should upsample the image 1 time. This
        # will make everything bigger and allow us to detect more faces.
        dets = detector(img, 1)
        #print("Number of faces detected: {}".format(len(dets)))
        for k, d in enumerate(dets):
            # print("Detection {}: Left: {} Top: {} Right: {} Bottom: {}".format(
            #     k, d.left(), d.top(), d.right(), d.bottom()))
            # # Get the landmarks/parts for the face in box d.
            #print type(d)
            lbdic=f.replace(argv[1],'')
            temprec=d
            shape = predictor(img, d)
            shapenp=numpy.ndarray((68,2))                    
            for i in range(0,68):
                shapenp[i,:]=[shape.part(i).x,shape.part(i).y]
            data[cnt,:]=shapenp
            label[cnt]=dic[lbdic[0]]
            cnt+=1
            #print (shape.part(0).x)
            #print("Part 0: {}, Part 1: {} ...".format(shape.part(0),
            #                                          shape.part(1)))
            # Draw the face landmarks on the screen.
            # win.add_overlay(shape)
    numpy.save('/home/wei/caffedata/webim/shapetr',data)
    numpy.save('/home/wei/caffedata/webim/shapetrlb',label)
    print cnt
    print data.shape
    # if len(dets)==0:
    #     shape = predictor(img, temprec)
    #     win.add_overlay(shape)
    #win.add_overlay(dets)
    #raw_input("Hit enter to continue")
if __name__ == '__main__':
    main(sys.argv)