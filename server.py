from flask import Flask, request, jsonify
import cv2
import numpy as np
from pyzbar.pyzbar import decode

app = Flask(__name__)

@app.route('/scan-qr', methods=['POST'])
def scan_qr():
    if 'image' not in request.files:
        return jsonify({'error': 'No image uploaded'}), 400

    file = request.files['image']
    file_bytes = np.asarray(bytearray(file.read()), dtype=np.uint8)
    image = cv2.imdecode(file_bytes, cv2.IMREAD_COLOR)

    qr_codes = decode(image)
    results = []

    for qr_code in qr_codes:
        qr_data = qr_code.data.decode('utf-8')
        results.append({
            'type': qr_code.type,
            'data': qr_data
        })

    return jsonify(results)

if __name__ == '__main__':
    app.run(debug=True)
