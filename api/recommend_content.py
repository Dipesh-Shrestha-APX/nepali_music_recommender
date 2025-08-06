# import pickle
# import pandas as pd

# import os

# BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# with open(os.path.join(BASE_DIR, "content_model", "tfidf_vectorizer.pkl"), "rb") as f:
#     tfidf = pickle.load(f)

# with open(os.path.join(BASE_DIR, "content_model", "tfidf_matrix.pkl"), "rb") as f:
#     tfidf_matrix = pickle.load(f)

# with open(os.path.join(BASE_DIR, "content_model", "similarity_matrix.pkl"), "rb") as f:
#     similarity_df = pickle.load(f)

# songs = pd.read_csv(os.path.join(BASE_DIR, "content_model", "songs_with_features.csv"))

# # Recommendation function
# def recommend(song_reference, top_n=10):
#     if song_reference not in similarity_df.index:
#         return []
#     # Get similar songs
#     song_index = similarity_df.index.get_loc(song_reference)
#     top = similarity_df.iloc[song_index].sort_values(ascending=False)[1:top_n+1]
#     return [{"title": title, "score": float(score)} for title, score in top.items()]



import os
import pickle
import pandas as pd

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

with open(os.path.join(BASE_DIR, "content_model", "tfidf_vectorizer.pkl"), "rb") as f:
    tfidf = pickle.load(f)

with open(os.path.join(BASE_DIR, "content_model", "tfidf_matrix.pkl"), "rb") as f:
    tfidf_matrix = pickle.load(f)

with open(os.path.join(BASE_DIR, "content_model", "similarity_matrix.pkl"), "rb") as f:
    similarity_df = pickle.load(f)

songs = pd.read_csv(os.path.join(BASE_DIR, "content_model", "songs_with_features.csv"))

def recommend(song_reference, top_n=10):
    if song_reference not in similarity_df.index:
        return []
    song_index = similarity_df.index.get_loc(song_reference)
    top = similarity_df.iloc[song_index].sort_values(ascending=False)[1:top_n+1]
    return [{"title": title, "score": float(score)} for title, score in top.items()]
