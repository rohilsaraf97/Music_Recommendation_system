"""dm project.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1APm8O4Xwl8IMpj5Lljfa6WygqnHMHJMB
"""

# Commented out IPython magic to ensure Python compatibility.
from __future__ import division, print_function, unicode_literals

import numpy as np
import os
import pandas as pd

# To make this notebook's output stable across runs
np.random.seed(42)

# To plot pretty figures
# %matplotlib inline
import matplotlib as mpl
import matplotlib.pyplot as plt

mpl.rc('axes', labelsize=14)
mpl.rc('xtick', labelsize=12)
mpl.rc('ytick', labelsize=12)
import sklearn
import seaborn as sns

# set style of plots
sns.set_style('white')

# define a custom palette
customPalette = ['#630C3A', '#39C8C6', '#D3500C', '#FFB139']
sns.set_palette(customPalette)
sns.palplot(customPalette)

# Ignore useless warnings (see SciPy issue #5998)
import warnings

warnings.filterwarnings(action="ignore", message="^internal gelsd")


def genPlaylist(mood):
    songs = pd.read_csv("spotify_dataset.csv")
    songs = songs[
        ["Song.Name", "Artist", "Song.ID", "Danceability", "Loudness", "Speechiness", "Acousticness", "Liveness"]]
    # songs.info()

    # songs.describe()

    from sklearn import preprocessing
    songs.astype({'Loudness': 'float'}).dtypes
    loudness = songs[['Loudness']].values
    min_max_scaler = preprocessing.MinMaxScaler()
    loudness_scaled = min_max_scaler.fit_transform(loudness)
    songs['Loudness'] = pd.DataFrame(loudness_scaled)
    songs.hist(bins=50, figsize=(20, 15))

    songs_features = songs.copy()
    songs_features = songs_features.drop(["Song.Name", "Artist", "Song.ID"], axis=1)
    # songs_features

    from sklearn.cluster import KMeans

    Sum_of_squared_distances = []
    K = range(1, 15)
    for k in K:
        km = KMeans(n_clusters=k)
        km = km.fit(songs_features)
        Sum_of_squared_distances.append(km.inertia_)

    plt.plot(K, Sum_of_squared_distances, 'gx-')
    plt.xlabel('k')
    plt.ylabel('Sum_of_squared_distances')
    plt.title('Elbow Method For Optimal k')
    # plt.show()

    kmeans = KMeans(n_clusters=4)
    kmeans.fit(songs_features)
    from sklearn.cluster import KMeans
    from sklearn.decomposition import PCA
    y_kmeans = kmeans.predict(songs_features)
    pca = PCA(n_components=2)
    principal_components = pca.fit_transform(songs_features)

    pc = pd.DataFrame(principal_components)
    pc['label'] = y_kmeans
    pc.columns = ['x', 'y', 'label']

    # plot data with seaborn
    cluster = sns.lmplot(data=pc, x='x', y='y', hue='label',
                         fit_reg=False, legend=True, legend_out=True)

    songs['label'] = y_kmeans

    # shuffle dataset

    songs = songs.sample(frac=1)
    # songs['label'].value_counts()

    """#### Identifying the moods
  
    Now we will assign a mood to each cluster by looking at the songs within them and identifying the key emotions that one generally associates with the majority of songs in a particular cluster. We also use the metrics like Danceability, Loudness, Speechiness, Acousticness and Liveness for this purpose.
  
    #### Cluster 0
  
    After inspecting some songs of the cluster, we observe more Lo-fi and Jazz instrumentals. All these songs share one thing in common. Upon seeing the metrics summary, we notice a relatively high acousticness close to 1, indicating the use of real instruments. As most instrumental tracks are acoustic, it makes sense for them to share this attribute. 
  
    Therefore, we name this cluster as Chill. And we will use this cluster for the Neutral emotion.
    """

    # songs[songs['label']==0].head(10)

    # songs[songs['label']==0].describe()

    """#### Cluster 1
  
    After inspecting some songs of the cluster, we observe more of Hip-Hop tracks that are consistently loud and upbeat. Upon seeing the metrics summary, we notice a a higher danceability and loudness than the previous cluster. Moreover, the acousticness is a lot lower indicating the use of more electronic and synthesised sounds in these clustered songs. 
  
    Therefore, we name this cluster as Energetic. And will use this cluster for surprise and angry emotions.
    """

    # songs[songs['label']==1].head(10)

    # songs[songs['label']==1].describe()

    """#### Cluster 2
  
    Now, after inspecting some songs of the cluster, we observe more of Hip-Hop tracks that are consistently loud and upbeat, similar to the previous cluster. But unlike the previous cluster, this cluster also has a higher level of liveness which indicates a higher level of live perfomances.
  
    Therefore, we name this cluster as Cheerful. And will use this cluster for the Happy Emotion.
    """

    # songs[songs['label']==2].head(10)

    # songs[songs['label']==2].describe()

    """#### Cluster 3
  
    High level of acousticness, and relatively low danceability and loundness in this cluster indicates to soothing songs. Also, upon examination of of songs in this cluster, the abundance of soothing romantic and sad songs was clear.
  
    Therefore, we name this cluster as sad and romantic songs. And will use this cluster for the Sad emotion.
    """

    # songs[songs['label']==3].head(10)

    # songs[songs['label']==3].describe()

    # moods=['chill','energetic','cheerful','romantic']
    retrieved_mood = mood.lower()  # from facial expression detection system
    if retrieved_mood == 'angry':
        retrieved_mood = 'surprise'
    elif retrieved_mood == 'disgust':
        retrieved_mood = 'surprise'
    moods = ['neutral', 'surprise', 'happy', 'sad']
    label = moods.index(retrieved_mood)
    print("Your predicted mood was: ", mood)
    print("The recommended playlist for your mood is: \n")


    newDf=songs[songs['label'] == label][["Song.Name", "Artist"]].head(40)
    newDf.columns=["Song Name", "Artist"]
    return [mood, newDf]
    # print(songs[songs['label'] == label][["Song.Name", "Artist"]].head(40).to_string(index=False))