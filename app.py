from flask import Flask
from flask import render_template
from flask import request

from video_chat import ask_video

app = Flask(__name__)

def seconds_to_hms(seconds):

    hours = int(seconds // 3600)

    minutes = int(
        (seconds % 3600) // 60
    )

    secs = int(
        seconds % 60
    )

    return (
        f"{hours:02}:"
        f"{minutes:02}:"
        f"{secs:02}"
    )

@app.route("/", methods=["GET", "POST"])
def home():

    answer = None

    relevant_mentions = []

    if request.method == "POST":

        question = request.form["question"]

        result = ask_video(question)

        answer = result["answer"]

        timestamps = result["timestamps"]

        for ts in timestamps:

            relevant_mentions.append({
                "seconds": int(ts),
                "time": seconds_to_hms(ts)
            })

    return render_template(
        "index.html",
        answer=answer,
        relevant_mentions=relevant_mentions
    )
if __name__ == "__main__":
    app.run(debug=True)