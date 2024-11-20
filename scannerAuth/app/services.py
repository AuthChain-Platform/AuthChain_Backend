from authChain_qrScannerInterface.authchainscanner import scan_qr_code_from_camera, scan_qr_code_from_image

def process_qr_code(image_bytes=None):
    if image_bytes:
        return scan_qr_code_from_image(image_bytes)
    return scan_qr_code_from_camera()
