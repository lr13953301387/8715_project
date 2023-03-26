# International collaborate on hand-writing project





### 1. MileStones and Current Objective:

#### TODO: 

1.3.1 Data preparations of the 300 digital version of historical artifacts

- [ ] Standardizing the files and images:

The files are given in a mix of file extensions (pdf, JFIF, JPEG, jpg). The challenging bit is to understand the given files and how to preprocess the images with computer vision tools(potentially to be done with OpenCV python library) to standardize the size (Character Detection), format and orientation. Further image enhancement techniques can be applied such as normalization, binarization and noise reduction to improve the quality of the images.

for the image processing bit, our main goal is to have the image to be read 
- [X] a) in greyscale, 
- [ ] b) perform noise reduction, 
- [X] c) perform normalization so that pixel values are in range of 0-1 or 0-255,
- [ ] d) the main body of the leaflet to be centre-cropped with the correct orientation,
- [ ] e) finally standardize the size of all images(i.e. 32x32).

- [ ] Extract features: 

*Revisiting* Histogram of Oriented Gradients(HOG), Scale-Invariant Feature Transform(SIFT) and *Learning* Local Binary Patterns(LBP) can be used to capture unique characteristics of the handwriting style of each writer.



- [ ] Running a K means clustering algorithm and inspecting the performance visually to get an idea how well it can classify them, since (like most real world data) the war artifacts were not provided with ground truth label and we are nowhere to infer the actual correct ones.

1.3.2 Introducing CERUG Dataset and the pilot dataset (see Project Description-Background):

- [ ] For the CERUG dataset, we will be utilizing CERUG-cn which contains a set of Chinese handwritings that can be used to train the network to learn writing styles, since Japanese and Chinese writings are alike.
Data preparation: split each image(by paragraph) into images that only contains a single paragraph so that to increase the size of the dataset.

- [ ] Evaluate model performance on test dataset
Improvement of feature extraction techniques or machine learning algorithms to improve the model’s performance.
Deploying the model once achieves satisfactory results.

### 2. Workspace and Communication channels:

Here is our group’s landing page: https://docs.google.com/document/d/1IfB7Yy_RHFtP7vITMqCr6VszqwX8z4nqkPvJ8s6wOA0/edit
 
Google Drive:https://drive.google.com/drive/folders/1hecIuxT4ad-6tQBP7q64SHWG3DRKsFKW

Miro: https://miro.com/app/board/uXjVPjUkjFU=/?share_link_id=70743626073
 
Statement of Work(also linked within landing page): https://docs.google.com/document/d/1EtdTE8EcNiLc0zZhhfSrFLprn_pdXndhCRASWU9sTWw/edit?pli=1#heading=h.rp8cc29r2wlp
 
project management tools: Mondays,GitHubbranches, discord, and Slack(previously)
 
Communication channels: 

discord channel: [https://discord.gg/FKX85jvkdy,](https://discord.gg/sBrUTEFzvF) 


And workspace on slack(prev): https://anutechlaunch-ye91222.slack.com/archives/C04QZCV0F7W
