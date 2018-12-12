# Human-activity-recognition
Optimized 3D CNN model for Human activity recognition
# Download dataset and Extract

Download the dataset from http://serre-lab.clps.brown.edu/resource/hmdb-a-large-human-motion-database/#Downloads

Four actions that I have used to train:

1 drink

2 shake_hands

3 sit

4 smile

command to extract: inside hmdb51_dataset folder place the .rar files of the activity and extract them

cd hmdb51_dataset

unrar x smile.rar

unrar x drink.rar

unrar x sit.rar

unrar x shake_hands.rar

The filders inside hmdb51_dataset will be as below:

├── drink

│   ├──.....avi

│   └── ...

├── shake_hands

│   ├── ....avi

│   └── ...

└── sit

│   ├──.....avi

│   └── ...

└── smile

│   ├── .....avi

│   └── ...

Now inside hmdb51_preprocess folder create train,test and val folder as below-

cd /hmdb51_preprocess/train

mkdir drink

mkdir sit

mkdir smile

mkdir shake_hands

├── train

│   ├──drink

│   └── sit...

├── test

│   ├──drink

│   └──sit...

└── val

│   ├──drink

│   └──sit...


# Installation:GPU

custom (10 vCPUs, 45 GB memory),1 x NVIDIA Tesla P100,

Install CUDA Toolkit v9.0 and cuDNN v7.0

For PyTorch dependency, see pytorch.org for more details

sudo apt-get update

pip3 install tensorflow-gpu==1.5

pip3 install tensorboardX

pip3 install sklearn

pip3 install opencv-python

pip3 install torch

pip3 install torchvision

pip3 install tqdm

Now follow the steps:

1. Download pretrained model

2. Configure your dataset and pretrained model path in mypath.py

3. To train the model

python3 train100_SGD.py

python3 train100_Adam.py

4. To test the model

python3 train100_Adam.py

# Tensorboard:To visualize the accuracy and loss after every epoch

tensorboard --logdir='./logs' --port=5006



