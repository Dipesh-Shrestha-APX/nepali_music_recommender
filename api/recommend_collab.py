import os
import pickle
import pandas as pd
from scipy.sparse import coo_matrix

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_PATH = os.path.join(BASE_DIR, "collab_model", "als_model.pkl")
TRACKS_PATH = os.path.join(BASE_DIR, "collab_model", "sound.csv")
INTERACTIONS_PATH = os.path.join(BASE_DIR, "collab_model", "interaction.csv")

def load_model():
    with open(MODEL_PATH, 'rb') as f:
        saved_data = pickle.load(f)
    return saved_data['model'], saved_data['user_map'], saved_data['track_map']

def load_data():
    tracks_df = pd.read_csv(TRACKS_PATH)
    if 'track_id' not in tracks_df.columns:
        tracks_df["track_id"] = [f"Track_{i+1}" for i in range(len(tracks_df))]
    tracks_df['track_id'] = tracks_df['track_id'].astype(str)

    interactions_df = pd.read_csv(INTERACTIONS_PATH)
    interactions_df['track_id'] = interactions_df['track_id'].astype(str)
    interactions_df['user_id'] = interactions_df['user_id'].astype(str)

    return tracks_df, interactions_df

def get_user_recommendations(user_id, model, user_map, track_map, tracks_df, interactions_df, n=10):
    if user_id not in user_map:
        return f"User {user_id} not found."

    user_idx = user_map[user_id]
    if user_idx >= model.user_factors.shape[0]:
        return f"User index {user_idx} out of bounds."

    user_interactions = interactions_df[interactions_df['user_id'] == user_id]
    if user_interactions.empty:
        return f"No interactions for user {user_id}."

    num_items = model.item_factors.shape[1]
    cols, data = [], []
    for tid, play_count in zip(user_interactions['track_id'], user_interactions['play_count']):
        if tid in track_map and track_map[tid] < num_items:
            cols.append(track_map[tid])
            data.append(play_count)

    if not cols:
        return f"No valid track interactions for user {user_id}."

    user_matrix = coo_matrix((data, ([0] * len(cols), cols)), shape=(1, num_items)).tocsr()

    try:
        item_ids, _ = model.recommend(user_idx, user_matrix, N=n, filter_already_liked_items=True)
    except Exception as e:
        return f"Error generating recommendations: {str(e)}"

    track_id_map = {idx: tid for tid, idx in track_map.items()}
    recommended_track_ids = [track_id_map[i] for i in item_ids if i in track_id_map]

    recommended_songs = tracks_df[tracks_df['track_id'].isin(recommended_track_ids)][['track_id', 'title', 'artist']]
    ordered_recommendations = pd.DataFrame({'track_id': recommended_track_ids}).merge(
        recommended_songs, on='track_id', how='left'
    )

    return ordered_recommendations[['title', 'artist']].rename(
        columns={'title': 'track_name', 'artist': 'artist_name'}
    ).to_dict('records')
