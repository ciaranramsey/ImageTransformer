import PIL.Image
import os

ASCII_CHARS = ["@", "#", "S", "%", "?", "*", "+", ";", ":", ",", "."]

def resize_image(image, new_width=100):
    width, height = image.size
    ratio = height / width
    new_height = int(new_width * ratio)
    resized_image = image.resize((new_width, new_height))
    return(resized_image)

def grayify(image):
    grayscale_image = image.convert("L")
    return(grayscale_image)

def pixles_to_ascii(image):
    pixles = image.getdata()
    characters = "".join([ASCII_CHARS[pixel//25] for pixel in pixles])
    return(characters)

def main(new_width=100):
    path = input("pathname to img")
    try:
        image = PIL.Image.open(path)
    except:
        print(path, "not valid pathway")
    
    new_image_data = pixles_to_ascii(grayify(resize_image(image)))
    
    pixel_count = len(new_image_data)
    ascii_image = "\n".join(new_image_data[i:(i+new_width)] for i in range(0, pixel_count, new_width))
    
    print(ascii_image)
   
    with open("ascii_image.txt", "w") as f:
        f.write(ascii_image)
    
    size1 = os.path.getsize(path)
    size1 = size1/1000 
    size2 = os.path.getsize("ascii_image.txt")
    size2 = size2/1000
    print("INFORMATION CONTENT OF IMAGES AS FOLLOWS")
    print("Size of input image is "+str(size1)+"kb")
    print("Size of output image is "+str(size2)+"kb")

    
main()