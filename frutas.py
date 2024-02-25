from flask import Flask, render_template
import os
import random

app = Flask(__name__)

images = {
    "Manzana": "https://www.smartnfinal.com.mx/tienda/frutas-y-verduras/manzana-roja",
    "Kiwi": "https://adomicilio.merco.mx/p/kiwi-pieza-10244906",
    "Mango": "https://biotrendies.com/frutas/fresa",
    # Agrega más frutas según sea necesario
}

@app.route("/")
def index():
    fruta = random.choice(list(images.keys()))
    url = images[fruta]
    return render_template("index.html", fruta=fruta, url=url)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
