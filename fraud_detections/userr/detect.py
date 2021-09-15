import pickle
from sklearn.model_selection import train_test_split
import pandas as pd

data=pd.read_csv('../media/csvfile/data/test.csv')                                    # test data

filename= '../media/savfile/finalized_model.sav'                    # random forest
loaded_model = pickle.load(open(filename, 'rb'))

print(loaded_model.predict(data))
