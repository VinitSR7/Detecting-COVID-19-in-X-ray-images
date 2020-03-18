# download data from https://www.kaggle.com/paultimothymooney/chest-xray-pneumonia
from imutils import paths
import random
import shutil
import os

basePath = "chest_xray/train/NORMAL/"
imagePaths = os.listdir(basePath)

random.seed(42)
random.shuffle(imagePaths)
imagePaths = imagePaths[:args["sample"]]

for (i, imagePath) in enumerate(imagePaths):
	outputPath = 'dataset/normal/' + filename

	shutil.copy2(basepath + imagePath, outputPath)