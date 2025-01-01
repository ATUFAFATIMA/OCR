# OCR
**Overview:**
    This is a project designed to scan an image containing text, and then translate it into a target language. It uses Optical Character Recognition (OCR) technology to get the text and 
    the Google Translate API for translation.


**Features:**
   It extracts text from images using Tesseract OCR.
   Translate the text into a target language, (eg.English to Spanish).


**Requirements:**
  pytesseract (for OCR) \n
  PIL (Python Imaging Library)
  googletrans (for translation)

**Example:**

**Input:**

Image (1st.png): An image with the text "This is a lot of 12 point text to test the ocr code and see if it works on all types of file format.The quick brown dog jumped over the lazy fox. The quick brown dog jumped over the lazy fox. The quick brown dog jumped over the lazy fox. The quick brown dog jumped over the lazy fox." (English).

**Output:**

**Extracted Text:**
"This is a lot of 12 point text to test the ocr code and see if it works on all types of file format.The quick brown dog jumped over the lazy fox. The quick brown dog jumped over the lazy fox. The quick brown dog jumped over the lazy fox. The quick brown dog jumped over the lazy fox."

**Translated Text:**
"Este es un montón de texto de 12 puntos para probar el código OCR y ver si funciona en todos los tipos de formato de archivo. El rápido perro marrón saltó sobre el zorro perezoso.El perro marrón rápido saltó sobre el zorro perezoso.El perro marrón rápido saltó sobre el zorro perezoso.El rápido Brown Dog saltó sobre el zorro perezoso." (in spanish)

**Script Explanation:**
   OCR (Optical Character Recognition): The pytesseract library extracts text from the image.
   Language Detection: The script uses googletrans to detect the language and translate the text into a target language (e.g., English to Spanish).



