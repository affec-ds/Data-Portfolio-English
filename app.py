from flask import Flask, render_template, request
import pandas as pd
import random

app = Flask(__name__)

# Load the real dataset from CSV file
df = pd.read_csv("cleaned_dataset.csv")

# Emotion to cluster mapping
emotion_to_cluster = {
    "happiness": 2,
    "party": 2,
    "motivation": 3,
    "intensity": 3,
    "relaxation": 1,
    "sadness": 1,
    "balance": 0,
    "focus": 0
}

# Emotion to playlist name mapping
emotion_to_name = {
    "happiness": "Always Happy, Always Vibing",
    "party": "Move What Your Mama Gave You",
    "motivation": "Let’s Get It Done",
    "intensity": "Let's Fcking Go!",
    "relaxation": "Inner Peace",
    "sadness": "Off Instagram. I Need To Be Alone.",
    "balance": "Smoothly Chill",
    "focus": "Sun Salutation Mode"
}


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/generate", methods=["POST"])
def generate():
    emotion = request.form["emotion"]
    cluster_id = emotion_to_cluster.get(emotion, 2)
    playlist_name = emotion_to_name.get(emotion, "My Playlist")

    playlist = df.sample(n=5).to_dict(orient="records")

    return render_template("playlist.html", emotion=emotion.capitalize(), playlist_name=playlist_name, playlist=playlist)


if __name__ == "__main__":
    app.run(debug=True, port=5001)
