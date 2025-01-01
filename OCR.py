import pytesseract
import cv2
import PIL.Image

# reads text from the image
myconfig= r"--psm 11 --oem 3"


text=pytesseract.image_to_string(PIL.Image.open("7th.png"), config=myconfig)


print(text)


# translating it into different languages

from googletrans import Translator


target_language=input("what language you want it to be translated?['es', 'fr', 'de', 'it]")


translator = Translator()
translated_text = translator.translate(text, src='en', dest=target_language).text


print("Translated Text:", translated_text)


# plot boxes around individual words

from pytesseract import Output


image=cv2.imread("7th.png")
height, width, _ = image.shape


data=pytesseract.image_to_data(image, config=myconfig,output_type= Output.DICT)
# print(data['text'])

amount_of_boxes=len(data['text'])

for i in range(amount_of_boxes):
    if(float(data['conf'][i])>8):
        x,y,width,height=(data['left'][i],data['top'][i],data['width'][i],data['height'][i])
        image=cv2.rectangle(image,(x,y),(x+width,y+height),(0,200,0),2)

cv2.imshow("image",image)

cv2.waitKey(0)


# Save the output image
cv2.imwrite("output_image.png", image)