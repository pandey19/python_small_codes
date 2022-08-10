import os 

# Function to rename multiple files 
def main(): 
    i = 6
    path = 'G:/U-2-Net-master/1/'    
    for filename in os.listdir('G:/U-2-Net-master/1'): 
        dst = str(i) + ".jpg"
        src = path + filename 
        dst = path + dst 

        # rename() function will 
        # rename all the files 
        os.rename(src, dst) 
        i += 1

# Driver Code 
if __name__ == '__main__': 

    # Calling main() function 
    main() 