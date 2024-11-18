from flask import Flask, jsonify, Response
import cv2
from pyzbar.pyzbar import decode

app = Flask(__name__)

def generate_frames():
    cam = cv2.VideoCapture(0)
    cam.set(5, 640)
    cam.set(6, 480)
    while True:
        success, frame = cam.read()
        if not success:
            break

        decoded_objects = decode(frame)
        qr_data = []

        for obj in decoded_objects:
            qr_data.append({
                "type": obj.type,
                "data": obj.data.decode('utf-8')
            })

        # Yield the video frame to the frontend if needed
        _, buffer = cv2.imencode('.jpg', frame)
        frame_bytes = buffer.tobytes()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame_bytes + b'\r\n')
        
        if qr_data:
            print(qr_data)
            yield f'data: {qr_data}\n\n'.encode('utf-8')

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    
    cam.release()
    cv2.destroyAllWindows()

@app.route('/video_feed')
def video_feed():
    return Response(generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/scan_qr')
def scan_qr():
    cam = cv2.VideoCapture(0)
    cam.set(5, 640)
    cam.set(6, 480)
    success, frame = cam.read()
    qr_data = []

    if success:
        decoded_objects = decode(frame)
        for obj in decoded_objects:
            qr_data.append({
                "type": obj.type,
                "data": obj.data.decode('utf-8')
            })

    cam.release()
    return jsonify(qr_data)

if __name__ == '__main__':
    app.run(debug=True)





# from flask import Flask, request, jsonify
# import cv2
# import numpy as np
# from pyzbar.pyzbar import decode

# app = Flask(__name__)

# @app.route('/scan-qr', methods=['POST'])
# def scan_qr():
#     if 'image' not in request.files:
#         return jsonify({'error': 'No image uploaded'}), 400

#     file = request.files['image']
#     file_bytes = np.asarray(bytearray(file.read()), dtype=np.uint8)
#     image = cv2.imdecode(file_bytes, cv2.IMREAD_COLOR)

#     qr_codes = decode(image)
#     results = []

#     for qr_code in qr_codes:
#         qr_data = qr_code.data.decode('utf-8')
#         results.append({
#             'type': qr_code.type,
#             'data': qr_data
#         })

#     return jsonify(results)

# if __name__ == '__main__':
#     app.run(debug=True)
