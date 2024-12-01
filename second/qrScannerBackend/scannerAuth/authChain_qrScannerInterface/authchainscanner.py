import cv2
from pyzbar.pyzbar import decode
import numpy as np

def initialize_camera():
    cam = cv2.VideoCapture(0)
    cam.set(3, 640)  # This is the Width and w ecan adjust it to our choice
    cam.set(4, 480)  # Same as this, which is the Height
    return cam

def scan_qr_code_from_camera():
    cam = initialize_camera()
    try:
        while True:
            success, frame = cam.read()
            if not success:
                return {"error": "Failed to capture frame"}

            for qr_code in decode(frame):
                result = {
                    "type": qr_code.type,
                    "data": qr_code.data.decode("utf-8"),
                }
                cam.release()
                cv2.destroyAllWindows()
                return result

            cv2.imshow("QR Code Scanner", frame)
            if cv2.waitKey(1) & 0xFF == ord("q"):
                break
    finally:
        cam.release()
        cv2.destroyAllWindows()

    return {"error": "No QR code detected"}

# def scan_qr_code_from_image(image_bytes):
#     try:
#         np_image = np.frombuffer(image_bytes, np.uint8)
#         image = cv2.imdecode(np_image, cv2.IMREAD_COLOR)

#         for qr_code in decode(image):
#             return {
#                 "type": qr_code.type,
#                 "data": qr_code.data.decode("utf-8"),
#             }

#         return {"error": "No QR code detected"}
#     except Exception as e:
#         return {"error": f"Failed to process image: {str(e)}"}
