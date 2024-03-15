from flask import Flask, render_template, request
import colorgram
from PIL import Image

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        # Get the file from the request
        file = request.files["file"]

        # Get the number of colors to extract
        palette_color_count = request.form.get('color-count')

        # Extract the colors
        colors = colorgram.extract(file, int(palette_color_count))
        top_colors = [color.rgb for color in colors]
        top_colors_hex = ['#{:02x}{:02x}{:02x}'.format(
            *rgb) for rgb in top_colors]

        return render_template('index.html', colors=top_colors_hex)

    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
