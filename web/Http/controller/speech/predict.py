import librosa
import pandas as pd
import numpy as np
import pickle
import csv
import sys
import os

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler
from split import chunks_audio
from collections import Counter

genresArr = ['blues', 'classical', 'country', 'disco', 'hiphop', 'jazz', 'metal', 'pop', 'reggae', 'rock']

# load csv file
load_file = pd.read_csv(os.path.join(os.path.dirname(sys.argv[0]), "data/data.csv"))
genre_list = load_file.iloc[:, -1]

encoder = LabelEncoder()
y = encoder.fit_transform(genre_list)

# split train and test dataset
X_train, X_test, y_train, y_test = train_test_split(load_file.iloc[:, :-1], y, test_size=0.2)

scale = StandardScaler()
X = scale.fit_transform(X_train)

# feature extraction function
def feature_audio_file(file_path):
    header = 'poly_features chroma_cens chroma_cqt chroma_stft tempogram spectral_centroid spectral_bandwidth spectral_rolloff spectral_contrast spectral_flatness zero_crossing_rate rmse'

    for i in range(1, 31):
        header += f' mfcc{i}'
    header = header.split()

    file = open(os.path.join(os.path.dirname(sys.argv[0]), 'data/test.csv'), 'w', newline='')
    with file:
        writer = csv.writer(file)
        writer.writerow(header)

    y, sr = librosa.load(file_path, sr=22050)

    mfcc = librosa.feature.mfcc(y, n_mfcc=30)
    poly_features = librosa.feature.poly_features(y)
    chroma_cens = librosa.feature.chroma_cens(y)
    chroma_cqt = librosa.feature.chroma_cqt(y)
    chroma_stft = librosa.feature.chroma_stft(y)
    tempogram = librosa.feature.tempogram(y)

    spectral_centroid = librosa.feature.spectral_centroid(y)
    spectral_bandwitdh = librosa.feature.spectral_bandwidth(y)
    spectral_rolloff = librosa.feature.spectral_rolloff(y)
    spectral_contrast = librosa.feature.spectral_contrast(y)
    spectral_flatness = librosa.feature.spectral_flatness(y)
    zero_crossing_rate = librosa.feature.zero_crossing_rate(y)

    rmse = librosa.feature.rmse(y)

    tmp = ""

    tmp = f'{np.mean(poly_features)} {np.mean(chroma_cens)} {np.mean(chroma_cqt)} {np.mean(chroma_stft)} {np.mean(tempogram)} {np.mean(spectral_centroid)} {np.mean(spectral_bandwitdh)} {np.mean(spectral_rolloff)} {np.mean(spectral_contrast)} {np.mean(spectral_flatness)} {np.mean(zero_crossing_rate)} {np.mean(rmse)}'

    for i in mfcc:
        tmp += f' {np.mean(i)}'

    file = open(os.path.join(os.path.dirname(sys.argv[0]), 'data/test.csv'), 'a', newline='')
    with file:
        writer = csv.writer(file)
        writer.writerow(tmp.split())


filename = sys.argv[1]

num_of_chunks = chunks_audio(os.path.join(os.path.dirname(sys.argv[0]), f'uploads/{filename}'))

result_arr = []

for i in range(num_of_chunks):
    feature_audio_file(os.path.join(os.path.dirname(sys.argv[0]), f'test_data/chunks/chunks{i+1}.mp3'))
    testFile = pd.read_csv(os.path.join(os.path.dirname(sys.argv[0]), "data/test.csv"))

    Z = scale.transform(np.array(testFile.iloc[:, :], dtype=float))

    # load model
    load_model = pickle.load(open(os.path.join(os.path.dirname(sys.argv[0]), 'model/model_svm.sav'), 'rb'))
    result = load_model.predict(Z)
    result_arr.append(genresArr[result[0]])

category = Counter(result_arr)
tmp_arr = [name for name, freq in category.most_common(2)]
string_result = tmp_arr[0] + ", " + tmp_arr[1]
print(string_result, flush=True)
