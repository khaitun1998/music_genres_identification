import pandas as pd
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler
import pickle as pk

# load csv file
load_file = pd.read_csv("data/data.csv")
genre_list = load_file.iloc[:, -1]

encoder = LabelEncoder()
y = encoder.fit_transform(genre_list)

# split train and test dataset
X_train, X_test, y_train, y_test = train_test_split(load_file.iloc[:, :-1], y, test_size=0.2)

scale = StandardScaler()
X = scale.fit_transform(X_train)

model = SVC(max_iter=1000)
model.fit(X, y_train)

# save model
filename = 'model/model_svm.sav'
pk.dump(model, open(filename, 'wb'))

# evaluate model
test_sample = scale.transform(X_test)
print(model.score(test_sample, y_test))
