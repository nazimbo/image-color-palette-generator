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
        print(matrix.shape)
        reshaped = matrix.reshape(-1, matrix.shape[-1])
        print(reshaped.shape)

        colors, count = np.unique(reshaped, axis=0, return_counts=True)

        indices = np.argsort(-count)

        palette_color_count = request.form.get('color-count')

        top_colors = colors[indices[:int(palette_color_count)]]
        top_colors_hex = ['#{:02x}{:02x}{:02x}'.format(
            *rgb) for rgb in top_colors]

        return render_template('index.html', colors=top_colors_hex)

    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
