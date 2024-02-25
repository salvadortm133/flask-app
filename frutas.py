from flask import Flask, render_template
import os
import random

app = Flask(__name__)

images = {
    "Manzana": "URL_DE_MANZANA",
    "Kiwi": "URL_DE_KIWI",
    "Mango": "URL_DE_MANGO",
    # Agrega más frutas según sea necesario
}

@app.route("/")
def index():
    fruta = random.choice(list(images.keys()))
    url = images[fruta]
    return render_template("index.html", fruta=fruta, url=url)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
