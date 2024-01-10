import sys
import os
from PIL import Image


first_arg = sys.argv[1]
second_arg = sys.argv[2]

if not os.path.exists(second_arg):
  os.makedirs(second_arg)

# for item in os.listdir(first_arg):
#   if item.endswith(".jpg"):
#     img = Image.open(os.path.join(first_arg, item))
#     output_filename = os.path.splitext(item)[0] + ".png"
#     output_path = os.path.join(second_arg, output_filename)
#     img.save(output_path, "PNG")

for item in os.listdir(first_arg):
  img = Image.open(f"{first_arg}/{item}")
  clean_name = os.path.splitext(item)[0]
  img.save(f'{second_arg}/{clean_name}.png', 'png')