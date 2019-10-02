import pytesseract
from PIL import Image
import cv2

pytesseract.pytesseract.tesseract_cmd = r"C:\Users\mridu\AppData\Local\Tesseract-OCR\tesseract.exe"


def im_to_text():
    im = Image.open('pic.jpg')
    text = pytesseract.image_to_string(im)

    print(text)


stream = cv2.VideoCapture(0)
a = 0
while True:
    a += 1
    check, frame = stream.read()
    cv2.imwrite('pic.jpg', frame)
    im_to_text()
    gray_img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    cv2.imshow('Capturing', gray_img)

    key = cv2.waitKey(1)

    if key == ord('q'):
        break

print('no.of frames: ', a)
stream.release()
cv2.destroyAllWindows()