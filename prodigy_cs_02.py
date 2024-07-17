from PIL import Image

def encrypt_image(image_path):
    # Open the image
    img = Image.open(image_path)
    width, height = img.size

    # Encrypt the image by swapping pixel values
    for x in range(width):
        for y in range(height):
            pixel = img.getpixel((x, y))
            new_pixel = (pixel[2], pixel[0], pixel[1])  # Swap R, G, B values
            img.putpixel((x, y), new_pixel)

    # Save the encrypted image
    encrypted_path = image_path.split('.')[0] + '_encrypted.png'
    img.save(encrypted_path)
    print("Image encrypted successfully!")
    return encrypted_path

def decrypt_image(encrypted_image_path):
    # Open the encrypted image
    img = Image.open(encrypted_image_path)
    width, height = img.size

    # Decrypt the image by reversing the encryption process
    for x in range(width):
        for y in range(height):
            pixel = img.getpixel((x, y))
            new_pixel = (pixel[1], pixel[2], pixel[0])  # Reverse swapping
            img.putpixel((x, y), new_pixel)

    # Save the decrypted image
    decrypted_path = encrypted_image_path.split('_encrypted')[0] + '_decrypted.png'
    img.save(decrypted_path)
    print("Image decrypted successfully!")
    return decrypted_path

def main():
    while True:
        choice = input("Do you want to encrypt or decrypt an image? (E/D): ").strip().upper()
        if choice == "E":
            image_path = input("Enter the path to the image you want to encrypt: ")
            encrypted_image_path = encrypt_image(image_path)
            print("Encrypted image saved at:", encrypted_image_path)
        elif choice == "D":
            encrypted_image_path = input("Enter the path to the encrypted image: ")
            decrypted_image_path = decrypt_image(encrypted_image_path)
            print("Decrypted image saved at:", decrypted_image_path)
        else:
            print("Invalid choice. Please try again.")
            continue

        cont = input("Do you want to continue? (Y/N): ").strip().upper()
        if cont != "Y":
            break

if __name__ == "__main__":
    main()