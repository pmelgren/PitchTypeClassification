# PitchTypeClassification
#### Notebooks and apps to cluster and classify pitch types based on Trackman data.
Pete Melgren January 2019

## Overview
There are 2 separate sections of this project. A simple notebook is contained under the R folder, while a more complex classification ecosystem can be found in the python folder.

### R
This is an adaption of a coding interview I did as part of a baseball application. Given a sample of Trackman data, I was asked cluster the data into pitch types and output a csv of pitch type classifications. The subfolder contains the .Rmd file, along with the knitted notebook and the source data.

### Python
The point of the files under the Python folder is to explore a process to automatically classify a certain pitcher's arsenal. This folder contains a notebook to classify a singe pitcher's arsenal, including sample data for a singe pitcher. The folder also contains a .py file that builds a Streamlit app to view real-time classifications of a pitcher's arsenal based on changing hyperparameters of the DBSCAN clustering algorithm.
