
import os
import torch
from torchvision import transforms

from image_dataloader import CustomDataset

transform = transforms.Compose([
        transforms.ToTensor(),
        transforms.Resize((224, 224)),
        transforms.Normalize((0.5), (0.5)),

])

data_dir = 'CERUG_dataset/Task1/'

print(os.path.join(data_dir, 'Task1_Training'))
train_data = CustomDataset(os.path.join(data_dir, 'Task1_Training'), transform)

test_data = CustomDataset(os.path.join(data_dir, 'Task1_Validation/Training'), transform)
print("123")
# Define the dataloaders to iterate over the data in batches
train_loader = torch.utils.data.DataLoader(train_data, batch_size=64, shuffle=True)

test_loader = torch.utils.data.DataLoader(test_data, batch_size=64)
print("321")

for data in train_loader:
        imgs,label=data
        print("imngs: ", imgs)
        print("label: ",label)