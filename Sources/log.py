import os

def create_pos_n_neg(folder):
    for file_type in [folder]:
        
        for img in os.listdir(file_type):

            if file_type == 'pos':
                line = file_type+'/'+img+' 1 0 0 50 50\n'
                with open('info.dat','a') as f:
                    f.write(line)
            elif file_type == folder:
                line = file_type+'/'+img+'\n'
                with open('bg.txt','a') as f:
                    f.write(line)



create_pos_n_neg("")		#Enter the folder name
