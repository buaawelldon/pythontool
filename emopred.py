import numpy
import os
import sys
# Make sure that caffe is on the python path:
import caffe
import cv2
def main(argv):

    ##the face gender recognition model
    #net = caffe.Classifier('deploy_face64by64.prototxt','face_gender_iter_20000')
    protostr='/home/wei/caffe-master/examples/facemodel/emo_quick_train_test_deploy.prototxt'
    caffemodel='/home/wei/caffe-master/examples/facemodel/emo_iter_20000.caffemodel'
    # imgtsfolder='/home/wei/Downloads/facecrop/'
    # imglist='/home/wei/Documents/pythontool/ageimg.txt'
    # blockname='gd.mat'
    #print 'length of argv is ',len(argv)

    # if len(argv)==6:
    #     protostr=argv[1]
    #     caffemodel=argv[2]
    #     imgtsfolder=argv[3]
    #     imglist=argv[4]
    #     blockname=argv[5]
    #     print 'parsing arguments done.'
    ##the expression model

    net = caffe.Classifier(protostr,caffemodel)


    net.set_phase_test()
    net.set_mode_gpu()
    # input preprocessing: 'data' is the name of the input blob == net.inputs[0]
    net.set_mean('data', '/home/wei/caffe-master/examples/facemodel/face_id_mean.npy')  # ImageNet mean
    net.set_channel_swap('data', (2,1,0))  # the reference model has channels in BGR order instead of RGB
    net.set_input_scale('data', 255)  # the reference model operates on images in [0,255] range instead of [0,1]
    
    #use for one img
    if os.path.isfile(argv[1]):
        img=caffe.io.load_image(argv[1])
        imgr=cv2.resize(img,(100,100))
        scores = net.predict([imgr])
        print scores

    #for a whole folder
    if os.path.isdir(argv[1]):
        for rt,dr,fps in os.walk(argv[1]):
            if '_faced' in rt:
                #print 'processing ',rt
                if dr==[] and fps!=[]:
                    n=len(fps)
                    scr=numpy.ndarray((n,7))
                    cnt=0
                    #print fps
                    for f in fps:
                        try:
                            if '.jpg' in f:
                                img=caffe.io.load_image(os.path.join(rt,f))
                                imgr=cv2.resize(img,(100,100))
                                #print img.shape,imgr.shape
                                #soame possible processing can be done here

                                scores = net.predict([imgr])
                                numpy.save(os.path.join(rt,f.replace('.jpg','')),scores)
                                scr[cnt,:]=scores
                                print scores
                                cnt+=1
                                
                        except:
                            print 'error in ',rt
                    numpy.save(os.path.join(rt,'scr'),scr)
                    import scipy.io
                    scipy.io.savemat(os.path.join(rt,'scr.mat'),mdict={'data':scr})        
    # print 'the data blobs:'

    # ####display and save the blob data
    # # for k, v in net.blobs.items():
    # #     print k, v.data.shape
    # #     outdata=net.blobs[k].data
    # #     shp=outdata.shape
    # #     fp=open('feat/blob_w_'+str(k)+r'.txt','w')
    # #     c=0
    # #     #print shp
    # #     for i in range(shp[0]):
    # #         for j in range(shp[1]):
    # #             for k in range(shp[2]):
    # #                 for l in range(shp[3]):
    # #                     datastr=str(outdata[i,j,k,l])+'  '
    # #                     fp.write(datastr)
    # #                     c+=1
    # #                     if c==shp[3]:
    # #                         fp.write('\n')
    # #                         c=0
    # #     fp.close()
    # lastlayer=net.blobs['ip1'].data
    # print lastlayer[0,:,0,0]

    # fr=open(imglist,'r')
    # datalines=fr.readlines()
    # print len(datalines)
    # outnumpy=np.ndarray((len(datalines),lastlayer.shape[1]))
    # outlabel=np.ndarray((len(datalines),))
    # cn=0;
    # #return
    # for line in datalines:
    #     line2=line.split('    ')
    #     imgname=imgtsfolder+line2[0]
    #     try:
    #         scores = net.predict([caffe.io.load_image(imgname)])
    #         lastlayer=net.blobs['ip1'].data
    #         outnumpy[cn,:]= lastlayer[0,:,0,0]
    #         outlabel[cn,]=int(line2[1])
    #         cn=cn+1
    #         #print int(line2[1])
    #     except:
    #         print 'error occur in ',imgname 
    #     if cn%500==0:
    #         print 'processing ',cn
    # finalnumpy=outnumpy[0:cn-1,:]
    # finallb=outlabel[0:cn-1]
    # print 'the new data ',finalnumpy.shape
    #     #print 'img: ',line2[0], line2[1][0]
    # import scipy.io
    # scipy.io.savemat(blockname,mdict={'data':finalnumpy,'outlabel':finallb})
    # npname=blockname.replace('.mat','')
    # np.save(npname,finalnumpy)
    # npnamelb=npname+'label'
    # np.save(npnamelb,finallb)



if __name__ == '__main__':
    main(sys.argv)