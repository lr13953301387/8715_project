import os

import cv2
import numpy as np
import torch
from torchvision import datasets, transforms
from PIL import Image

class CustomDataset(torch.utils.data.Dataset):
    def __init__(self, data_dir, transform):
        self.data = []
        self.targets = []
        for filename in os.listdir(data_dir):
            # label_dir = os.path.join(data_dir, label)
            # for filename in os.listdir(label_dir):
            self.data.append(os.path.join(data_dir,filename))
            #print(filename.split(".")[0][-1])
            self.targets.append(int(filename[:3]))

        self.transform = transform

    def __len__(self):
        return len(self.data)

    def __getitem__(self, index):

        image_path = self.data[index]
        target = self.targets[index]

        img = cv2.imread(image_path)
        img = img.astype(np.float32)
        # img=img[0]
        # print(img.shape)
        if self.transform is not None:
            img = self.transform(img)

        label = np.array(target)
        # print("label: ",label)
        label = torch.from_numpy(label).float()
        return img, label
