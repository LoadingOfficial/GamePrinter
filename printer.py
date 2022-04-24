import win32print
import win32ui

import PIL
import PIL.Image
import PIL.ImageWin

def image(image_file = "null", rotate = "True"):
    # don't touch this eyesore plz idk what tf used for... (some Windows legacy stuff) also this is for A4 size paper
    PHYSICALWIDTH = 8 
    PHYSICALHEIGHT = 10 

    try:
        printer = win32print.GetDefaultPrinter()
    except:
        print("No printer found")
        exit()

    try:
        image = PIL.Image.open(image_file)
    except:
        print("Invalid image")
        exit()
    
    image = image.convert("RGB")

    if rotate == "True":
        if image.size[0] > image.size[1]:
            image = image.rotate(90, expand = 1)
    elif rotate == "False":
        pass
    else:
        print("Invalid rotation value")

    document = win32ui.CreateDC()
    document.CreatePrinterDC(printer)

    document.StartDoc(str(image))
    document.StartPage()

    dib = PIL.ImageWin.Dib(image)
    dib.draw(document.GetHandleOutput(), (0, 0, int(document.GetDeviceCaps(PHYSICALWIDTH) - 512), int(document.GetDeviceCaps(PHYSICALHEIGHT) - 0)))

    document.EndPage()
    document.EndDoc()
    document.DeleteDC()