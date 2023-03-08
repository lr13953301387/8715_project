import cv2
import os
import shutil

if __name__ == "__main__":

    path = 'CERUG_dataset/Task1/Task1_Training'
    listdir = os.listdir(path)
    newdir = os.path.join(path, 'split')  # make a new dir in dirpath.
    #print(newdir)
    if (os.path.exists(newdir) == True):

        shutil.rmtree(newdir)
        os.mkdir(newdir)
    else:
        os.mkdir(newdir)

    for i in listdir[:len(listdir)-1]:

            filepath = os.path.join(path, i)
            filename = i.split('.')[0]
            leftpath = os.path.join(newdir, filename) + "_top.png"
            rightpath = os.path.join(newdir, filename) + "_down.png"

            img = cv2.imread(filepath)
            [h, w] = img.shape[:2]
            print(filepath, (h, w))
            timg = img[0:900, 0:w]
            dimg = img[901:, :,:]

            cv2.imwrite(leftpath, timg)
            cv2.imwrite(rightpath, dimg)
