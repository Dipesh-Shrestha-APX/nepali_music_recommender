# Nepali Music Recommender System

---

## 🎯 Project Overview

This project aims to build and evaluate **two recommendation models** —  
**Collaborative Filtering** and **Content-Based Filtering** — for Nepali folk music tracks.  
The best performing model is served through a Dockerized FastAPI service.

---

## 📊 Data Collection and Preparation

- **Preorganized datasets online:**  
  ❌ Not found for Nepali folk music.

- **Spotify API:**  
  - Requires extended quota for deeper feature extraction.  
  - Requires company email, which was unavailable.

- **Data Gathering:**  
  - Used **ChatGPT and Grok** to web scrape ~100–200 songs.  
  - Augmented the rest of the dataset to reach 1,000 tracks.  
  - Main metadata stored in `sound.csv`.

- **User Interaction Data:**  
  - Created `user_liked_songs.csv` and `interaction.csv` using **GPT-generated code**.  
  - These were based on predictions from the content-based model for similar tracks.

> **⚠️ Note on GPT and Grok Usage:**  
> Throughout the project, **ChatGPT and Grok** were extensively used for:  
> - Web scraping and data augmentation  
> - Writing model training, evaluation, and prediction code  
> - Developing API endpoints and evaluation metric scripts  
> These AI tools significantly accelerated development and experimentation.

---

## 🎵 Content-Based Model

- Combined all metadata columns into a single corpus.  
- Applied **TF-IDF vectorization** on the combined text.  
- Calculated **cosine similarity** between tracks.  
- Saved vectorizer and similarity matrices as `.pkl` and CSV files in the `model/` folder.  
- Used GPT/Grok for writing evaluation metric code.

---

## 🔄 Collaborative Filtering Model

- Utilized the **implicit** Python library.  
- Implemented matrix factorization using the **ALS algorithm**.  
- Trained on user-track interaction data with play counts as implicit feedback.  
- Developed evaluation and prediction pipeline with ChatGPT/Grok help.  
- Resulted in low evaluation scores compared to content-based filtering.

---

## 📈 Evaluation Summary

| Model                 | Precision@10 | Mean Average Precision (MAP) |
|-----------------------|--------------|------------------------------|
| Content-Based Model    | Good values  | Good values                  |
| Collaborative Model    | Low values   | Low values                   |

> **Insight:** Content-based filtering performed significantly better.

---

## 🚀 API Development

- Built API endpoints using **FastAPI** with ChatGPT/Grok assistance:  
  - `/recommend_collab` — Top 10 tracks based on user history.  
  - `/recommend_content` — Top 10 similar tracks based on a given track.

- Could not implement the RESTful endpoints:  
  - `/recommend/{user_id}`  
  - `/similar/{track_id}`

---

## 🐳 Dockerization

- Created and tested a `Dockerfile` for containerizing the API service.  
- Successfully built, ran, and tested the container.  
- Verified API functionality through URL calls.

---

## 💡 Learnings & Reflections

- Gained practical experience with:  
  - Building and deploying APIs.  
  - Dockerizing an API service.  
  - Understanding differences between collaborative and content-based filtering.

- The full project scope was **not completed** within the timeline.

---

## 📂 Project Structure (Example)

