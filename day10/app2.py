import cv2

img = cv2.imread("qrcode.png")

detector = cv2.QRCodeDetector()

data, bbox, _ = detector.detectAndDecode(img)

print("QR Content:", data)