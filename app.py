from flask import Flask, request, render_template, url_for
import qrcode
from io import BytesIO
import base64

app = Flask(__name__)

@app.route('/')
def home():
    """Render the home page with the QR code form."""
    return render_template('index.html', qr_code=None)

@app.route('/generate', methods=['GET'])
def generate_qr_code():
    """Generate a QR code and display it on the page."""
    # Get the data from the query parameter
    data = request.args.get('data')
    fill_color = request.args.get('fill_color')
    back_color = request.args.get('back_color')

    # Generate the QR code
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)

    # Create an image from the QR code
    img = qr.make_image(fill_color=fill_color, back_color=back_color)

    # Convert the image to a base64 string
    buffer = BytesIO()
    img.save(buffer, format="PNG")
    buffer.seek(0)
    img_str = base64.b64encode(buffer.getvalue()).decode('utf-8')
    # Pass the image data back to the template
    return render_template('index.html', qr_code=img_str, data = data)

if __name__ == '__main__':
    app.run(debug=True)
