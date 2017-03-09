import urllib		#.requestrequest for python3
import cv2
import numpy as np
import os
import socket
import sys  

reload(sys)  
sys.setdefaultencoding('utf8')
socket.setdefaulttimeout(10)

def store_raw_images2(folder,url):
    neg_images_link = url
    neg_image_urls = urllib.urlopen(neg_images_link).read().decode()						#urllib.request.urlopen(neg_images_link).read().decode()
    pic_num = 1
    url_num = 1
    lenS = str(len(neg_image_urls.split('\n')))
    
    if not os.path.exists(folder):
        os.makedirs(folder)
        
    for i in neg_image_urls.split('\n'):

        try:
            print(i)
            print("....................................................." + str(url_num) + " of " + lenS)
            url_num += 1
            urllib.urlretrieve(i, folder+"/"+str(pic_num)+".jpg")
            img = cv2.imread(folder+"/"+str(pic_num)+".jpg",cv2.IMREAD_GRAYSCALE)
            # should be larger than samples / pos pic (so we can place our image on it)
            resized_image = cv2.resize(img, (100, 100))
            cv2.imwrite(folder+"/"+str(pic_num)+".jpg",img)
            pic_num += 1
            
        except Exception as e:
            pic_num += 1
            url_num += 1
            print(str(e))  


def find_corrupted(folder):
    match = False
    for file_type in [folder]:
        for img in os.listdir(file_type):
               try:
                   current_image_path = str(file_type)+'/'+str(img)
                   question = cv2.imread(current_image_path)
		   cv2.imshow("a",question)
		   cv2.destroyAllWindows()                    
		   print(current_image_path)
               except Exception as e:
                   print(str(e))
		   print("Corrupted -----> " + current_image_path)
		   os.remove(current_image_path)	



def find_uglies(folder):
    match = False
    for file_type in [folder]:
        for img in os.listdir(file_type):
            for ugly in os.listdir('uglies'):
                try:
                    current_image_path = str(file_type)+'/'+str(img)
                    ugly = cv2.imread('uglies/'+str(ugly))
                    question = cv2.imread(current_image_path)
                    if ugly.shape == question.shape and not(np.bitwise_xor(ugly,question).any()):
                        print('That is one ugly pic! Deleting!')
                        print(current_image_path)
                        os.remove(current_image_path)
                except Exception as e:
                    print(str(e))


def rename(folder,start_num):
    match = False
    pic_num = start_num
    for file_type in [folder]:
        for img in os.listdir(file_type):
               try:
                   current_image_path = str(file_type)+'/'+str(img)
                   img = cv2.imread(current_image_path)
		   cv2.imwrite(folder + "/" + str(pic_num)+".jpg",img)
		   os.remove(current_image_path)                   
		   print(pic_num)
		   pic_num += 1
               except Exception as e:
                   print(str(e))
		   pic_num += 1

#store_raw_images2("negWalls","http://image-net.org/api/text/imagenet.synset.geturls?wnid=n14564779")
#find_corrupted("negWalls")
#find_uglies("negWalls")
rename("negWalls",6000)



