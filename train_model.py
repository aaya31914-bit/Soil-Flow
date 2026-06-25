import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import joblib

# 1-read data from the file
df = pd.read_csv('soil_data.csv')

# 2-define the input and output for the Ai
X = df[['Temperature', 'TDS', 'Soil_Moisture']]
y = df['Status']


#3- train the model
model = RandomForestClassifier(n_estimators=100)
model.fit(X, y)

# 4. save the (training) in external file such as pkl
joblib.dump(model, 'soil_ai_model.pkl')

