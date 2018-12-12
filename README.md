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

├── train

│   ├──drink

│   └── sit...

├── test

│   ├──drink

│   └──sit...

└── val

│   ├──drink

│   └──sit...

# Installation



