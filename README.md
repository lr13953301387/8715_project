# 8715_project

1.3.1 Data preparations of the 300 digital version of historical artifacts

Standardizing the files and images:

The files are given in a mix of file extensions (pdf, JFIF, JPEG, jpg). The challenging bit is to understand the given files and how to preprocess the images with computer vision tools(potentially to be done with OpenCV python library) to standardize the size (Character Detection), format and orientation. Further image enhancement techniques can be applied such as normalization, binarization and noise reduction to improve the quality of the images.

Extract features: 

*Revisiting* Histogram of Oriented Gradients(HOG), Scale-Invariant Feature Transform(SIFT) and *Learning* Local Binary Patterns(LBP) can be used to capture unique characteristics of the handwriting style of each writer.

Introducing Unsupervised Learning - K Means Clustering:

Running a K means clustering algorithm and inspecting the performance visually to get an idea how well it can classify them, since (like most real world data) the war artifacts were not provided with ground truth label and we are nowhere to infer the actual correct ones.

1.3.2 Introducing CERUG Dataset and the pilot dataset (see Project Description-Background):

For the CERUG dataset, we will be utilizing CERUG-cn which contains a set of Chinese handwritings that can be used to train the network to learn writing styles, since Japanese and Chinese writings are alike.
Data preparation: split each image(by paragraph) into images that only contains a single paragraph so that to increase the size of the dataset.

Evaluate model performance on test dataset
Improvement of feature extraction techniques or machine learning algorithms to improve the model’s performance.
Deploying the model once achieves satisfactory results.

