from PIL import Image
import imagehash

# Load the images
hash0 = imagehash.average_hash(Image.open('screenshot/20231229-110210_screenshot.png'))
hash1 = imagehash.average_hash(Image.open('screenshot/20231229-110129_screenshot.png'))

cutoff = 5  # maximum bits that could be different between the hashes.

if hash0 - hash1 < cutoff:
  print('images are similar')
else:
  print('images are not similar')