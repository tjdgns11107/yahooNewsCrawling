import csv
import glob
import os
from pathlib import Path
import pandas as pd


data = pd.read_csv("./crawlingData_20191119/merge.csv" )
yy = data[data.duplicated(keep='last')]

print(data)