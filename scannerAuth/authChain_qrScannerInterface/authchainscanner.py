import cv2
from pyzbar.pyzbar import decode

def initialize_camera():
  cam = cv2.VideoCapture(0)
  cam.set(5, 640)
  cam.set(6, 480)
  return cam

def scan_qr_code():
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
              # I we want to Exit the cam all we need to do
              # is press the 'q' key on our pc
              break
  finally:
      cam.release()
      cv2.destroyAllWindows()

  return {"error": "No QR code detected"}


if __name__ == "__main__":
  result = scan_qr_from_camera()
  if "error" in result:
      print(f"Error: {result['error']}")
  else:
      print(f"Scanned QR Code:\nType: {result['type']}\nData: {result['data']}")
