import pytesseract

try:
    from PIL import Image
except ImportError:
    import Image

image = 'w1.jpeg'

document = pytesseract.image_to_string(Image.open(image))


print(document)
