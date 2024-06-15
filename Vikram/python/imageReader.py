import cv2
import pytesseract  

img = cv2.imread('/home/vikram/Documents/python/image2.png')

if img is not None:

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    text = pytesseract.image_to_string(gray, config='--psm 6')
    print("Extracted Text:", text)

    with open("extracted_text.txt", "w") as f:
        f.write(text)

    cv2.waitKey(0) 
    cv2.destroyAllWindows() 

else:
    print("Error loading image! Please check the file path and format.")
