from flask import Flask, jsonify, request
from flask_cors import CORS
from PIL import Image
import base64
from io import BytesIO

app = Flask(__name__)
CORS(app)

def base64_to_pil(img_str):
    if "base64," in img_str:
        # DARA URI の場合、data:[<mediatype>][;base64], を除く
        img_str = img_str.split(",")[1]
    img_raw = base64.b64decode(img_str)
    img = Image.open(BytesIO(img_raw))

    return img


@app.route('/')
def index():
    return 'hello'

@app.route('/image', methods=['POST'])
def draw():
    data = request.get_json()
    img_base64 = data["image"]
    img = base64_to_pil(img_base64)
    img_resize = img.resize((320, 120))
    img_mono = img_resize.convert("1")
    img_mono.save("sample.png")

    return data



if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')