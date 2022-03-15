# an example script that extracts a zip file from caltech data
# and uses that as the data source

import caltechdata_api
from zipfile import ZipFile
import pandas as pd

# Two methods here. First, try extracting all data
# perhaps this function could be in the preamble of each document
# and it could still workt he same way.
dname = caltechdata_api.download_file('10.2202/d1.20057', 'data.zip')

with ZipFile(dname, 'r') as zip:
    zip.extractall()

# Secondly, extract individual files. This could be made into a wrapper function
# that sends files to qc.load_data()
with ZipFile(dname, 'r') as zip:
    file = zip.extract('data/Fig1/22835_3pH_4LED_EQE.csv')
    data = pd.read_csv(file)
