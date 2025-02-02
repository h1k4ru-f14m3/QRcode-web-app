import os
import qrcode
from PIL import Image

# Generate QR code
img = qrcode.make("")

# Save as file
img.save("qr.png", "PNG")

# Open file
os.system("open qr.png")