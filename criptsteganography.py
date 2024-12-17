from PIL import Image

def decode_image(image_path):
    img = Image.open(image_path)
    binary_message = ""
    img = img.convert("RGB")
    width, height = img.size

    for y in range(height):
        for x in range(width):
            r, g, b = img.getpixel((x, y))
            
            binary_message += str(r & 1)  
            binary_message += str(g & 1)  
            binary_message += str(b & 1)  

    message = ""
    for i in range(0, len(binary_message), 8):
        byte = binary_message[i:i+8]
        if len(byte) < 8:
            break
        message += chr(int(byte, 2))
        
    return message

def main():
    image_path = "steghide.png"
    
    hidden_message = decode_image(image_path)
    
    if hidden_message:
        print("Hidden message:", hidden_message)
    else:
        print("No hidden message found in the image.")

if __name__ == "__main__":
    main()