from PIL import Image

# Load your image
image_path = 'notepad.png'  # Replace with the path to your image
img = Image.open(image_path)

# Convert the image to an icon (.ico)
icon_path = 'notewave.ico'  # Replace with the path where you want to save the icon
img.save(icon_path, format='ICO')

print(f"Icon saved to {icon_path}")
