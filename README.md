# Detecting-COVID-19-in-X-ray-images
Detecting COVID-19 in X-ray images using Deep learning

# Dataset
## Covid-19 Images
For the COVID-19 X-ray images, we will take the help of this <a href = "https://github.com/ieee8023/covid-chestxray-dataset" >repo </a>, created by <a href="https://josephpcohen.com/w/">Dr. Cohen. </a>
 <ul> 
 <b>In order to create the COVID-19 X-ray image dataset</b>
 <li> We need to parse the <code class="EnlighterJSRAW enlighter-origin" data-enlighter-language="python">metadata.csv</code> file in the repo.</li>
 <li> Select all rows that are: Positive for COVID-19.</li>
 
  </ul> 
<p>Parsing Process is done in <code class="EnlighterJSRAW enlighter-origin" data-enlighter-language="python">build_covid_dataset.ipynb.</code> </p>
<h3>After parsing we were left with 25 positive COVID-19 Images</h3>

## Normal Images
<p> For the X-ray images of healty person, we will take the help of <a href = "https://www.kaggle.com/paultimothymooney/chest-xray-pneumonia" >Kaggle’s Chest X-Ray Images (Pneumonia) dataset.</a> and sample 25 X-ray images of healty paitents. </p>

<p>After gathering of dataset, we were left with 50 total images, equally split with 25 images of COVID-19 positive X-rays and 25 images of healthy patient X-rays.</p>


