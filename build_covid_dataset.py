import pandas as pd
import shutil
import os

csvPath = "metadata.csv"
df = pd.read_csv(csvPath)

for (i, row) in df.iterrows():
	if row["finding"] != "COVID-19" or row["view"] != "PA":
		continue
	imagePath =  "covid-chestxray-dataset/images/" + row["filename"]

	if not os.path.exists(imagePath):
		continue
	outputPath = "dataset/covid/" + row["filename"]

	shutil.copy2(imagePath, outputPath)