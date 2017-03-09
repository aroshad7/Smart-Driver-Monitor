import cv2
import numpy as np
import os

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

find_corrupted("negFlowers")
#find_uglies("negFaces")
#rename("negFaces",1980)
