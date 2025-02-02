import qrcode
from PIL import Image
from flask import render_template, Flask, request, send_file
import io
import base64

app = Flask(__name__)
app.config["TEMPLATES_AUTO_RELOAD"] = True

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "GET":
        return render_template("home.html")
    
    elif request.method == "POST":
        data = request.form.get('data')

        image = qrcode.make(data)

        img_io = io.BytesIO()
        image.save(img_io, 'PNG')
        img_io.seek(0)  # Reset stream position to the beginning

        img_mem = base64.b64encode(img_io.getvalue()).decode('utf-8')

        return render_template("home.html", image_data=img_mem)

    # image_buffer = io.BytesIO()
    # image.save(image_buffer, format="png")
    # image_buffer.seek(0)
    # encoded_image_data = base64.b64encode(image_buffer.getvalue())
    
    
    # return render_template("home.html", image_data=encoded_image_data.decode('utf-8'))