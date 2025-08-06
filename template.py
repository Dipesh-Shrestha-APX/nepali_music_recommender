import os

# Base path is current directory where this script runs
base_path = "."

structure = {
    "data": [
        "raw/songs_raw.csv",
        "processed/songs_with_features.csv",
        "processed/interaction.csv",
        "processed/user_like_songs.csv",
        "README.md"
    ],
    "models": [
        "collab_model/als_model.pkl",
        "collab_model/user_map.pkl",
        "collab_model/track_map.pkl",
        "content_model/tfidf_vectorizer.pkl",
        "content_model/tfidf_matrix.pkl",
        "content_model/similarity_matrix.pkl",
        "metrics/evaluation_results.json"
    ],
    "api": [
        "main.py",
        "collab_recommend.py",
        "content_recommend.py",
        "utils.py"
    ],
    "notebooks": [
        "01_data_exploration.ipynb",
        "02_collaborative_model.ipynb",
        "03_content_model.ipynb",
        "04_evaluation.ipynb",
        "05_model_comparison.ipynb"
    ],
    "docker": [
        "Dockerfile"
    ],
    "demo": [
        "api_demo.gif",
        "sample_output.json"
    ],
    ".": [
        "requirements.txt",
        "README.md",
        ".gitignore"
    ]
}

def create_structure(base_path, structure_dict):
    for folder, files in structure_dict.items():
        for file in files:
            full_path = os.path.join(base_path, folder, file)
            os.makedirs(os.path.dirname(full_path), exist_ok=True)
            # Create empty file if it doesn't exist
            if not os.path.exists(full_path):
                with open(full_path, "w") as f:
                    if file.endswith(".md"):
                        f.write(f"# {os.path.basename(file).replace('_', ' ').replace('.md', '')}\n")
                    elif file.endswith(".py"):
                        f.write(f"# {file} - placeholder\n")
                    elif file.endswith(".ipynb"):
                        f.write("")  # blank notebook
                    elif file.endswith(".gitignore"):
                        f.write("__pycache__/\n*.pkl\n*.csv\n*.json\n.ipynb_checkpoints/\n")
                    elif file.endswith("requirements.txt"):
                        f.write("fastapi\nuvicorn\npandas\nscikit-learn\nimplicit\n")
                    elif file.endswith("Dockerfile"):
                        f.write("# Dockerfile placeholder\n")
                    elif file.endswith(".json"):
                        f.write("{}\n")
                    else:
                        f.write("")

if __name__ == "__main__":
    create_structure(base_path, structure)
    print("Project structure created in current directory ✔")
