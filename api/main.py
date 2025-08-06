# import sys
# import os

# # Add current directory to path
# sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# from fastapi import FastAPI, HTTPException, Query
# from recommend_content import recommend

# app = FastAPI()

# MODEL_PATH = "app/model/als_model.pkl"
# TRACKS_PATH = "app/data/tracks.csv"
# INTERACTIONS_PATH = "app/data/interactions.csv"


# @app.get("/")
# def root():
#     return {"message": "Recommender System running."}

# @app.get("/recommend_content/")
# def get_recommendations(song_title: str = Query(..., alias="title"), top_n: int = 10):
#     results = recommend(song_title, top_n)
#     if not results:
#         raise HTTPException(status_code=404, detail="Song not found")
#     return {"input": song_title, "recommendations": results}

# @app.get("/recommend_collab/")
# def get_recommendations(song_title: str = Query(..., alias="title"), top_n: int = 10):
#     results = recommend(song_title, top_n)
#     if not results:
#         raise HTTPException(status_code=404, detail="Song not found")
#     return {"input": song_title, "recommendations": results}
# main.py

import sys
import os

print("Python sys.path:", sys.path)
print("Current working dir:", os.getcwd())


# Ensure local imports work regardless of working directory
# sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from fastapi import FastAPI, HTTPException, Query
from recommend_collab import load_model, load_data, get_user_recommendations
from recommend_content import recommend as content_recommend


app = FastAPI()

# Load collab model and data at startup
collab_model, user_map, track_map = load_model()
tracks_df, interactions_df = load_data()

@app.get("/")
def root():
    return {"message": "Recommender System running."}

@app.get("/recommend_content/")
def get_recommendations(song_title: str = Query(..., alias="title"), top_n: int = 10):
    results = content_recommend(song_title, top_n)
    if not results:
        raise HTTPException(status_code=404, detail="Song not found")
    return {"input": song_title, "recommendations": results}

@app.get("/recommend_collab/")
def get_user_recommendations_api(user_id: str = Query(...), top_n: int = 10):
    results = get_user_recommendations(user_id, collab_model, user_map, track_map, tracks_df, interactions_df, n=top_n)
    if isinstance(results, str):
        raise HTTPException(status_code=404, detail=results)
    return {"user_id": user_id, "recommendations": results}
