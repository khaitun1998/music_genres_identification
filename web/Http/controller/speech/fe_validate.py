import time
import librosa
import numpy as np
import os
import csv
import sys

start_time = time.clock()

# header for csv file
header = 'poly_features chroma_cens chroma_cqt chroma_stft tempogram spectral_centroid spectral_bandwidth spectral_rolloff spectral_contrast spectral_flatness zero_crossing_rate rmse'
for i in range(1, 31):
    header += f' mfcc{i}'
header += ' label'
header = header.split()

file = open(os.path.abspath(os.path.join(os.path.dirname(sys.argv[0]), 'data/retrain.csv')), 'w', newline='')
with file:
    writer = csv.writer(file)
    writer.writerow(header)

genres = 'blues classical country disco hiphop jazz metal pop reggae rock'.split()
count = 0

print("Begin feature extraction.")

# feature extraction function
for genre in genres:
    for filename in os.listdir(os.path.abspath(os.path.join(os.path.dirname(sys.argv[0]), f'./validate/{genre}'))):
        count += 1
        song = os.path.abspath(os.path.join(os.path.dirname(sys.argv[0]), f'./validate/{genre}/{filename}'))
        # print("Featuring file {}".format(song))
        y, sr = librosa.load(song)

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

        percentage = round((count/300)*100, 3)

        print(f'Stats: {percentage}%')

        tmp = ""

        tmp = f'{np.mean(poly_features)} {np.mean(chroma_cens)} {np.mean(chroma_cqt)} {np.mean(chroma_stft)} {np.mean(tempogram)} {np.mean(spectral_centroid)} {np.mean(spectral_bandwitdh)} {np.mean(spectral_rolloff)} {np.mean(spectral_contrast)} {np.mean(spectral_flatness)} {np.mean(zero_crossing_rate)} {np.mean(rmse)}'

        for i in mfcc:
            tmp += f' {np.mean(i)}'
        tmp += f' {genre}'

        file = open(os.path.abspath(os.path.join(os.path.dirname(sys.argv[0]), 'data/retrain.csv')), 'a', newline='')
        with file:
            writer = csv.writer(file)
            writer.writerow(tmp.split())

print("Finish feature extraction.")

print(f'Time: {(time.clock() - start_time)/60} min')
