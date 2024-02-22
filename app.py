from flask import Flask, render_template, request
import numpy as np
from PIL import Image

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        file = request.files["file"]
        image = Image.open(file.stream)
        matrix = np.array(image)
        reshaped = matrix.reshape(-1, 3)

        colors, count = np.unique(reshaped, axis=0, return_counts=True)

        indices = np.argsort(-count)

        top_colors = colors[indices[:10]]

        return render_template('index.html', top_colors=top_colors)

    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
