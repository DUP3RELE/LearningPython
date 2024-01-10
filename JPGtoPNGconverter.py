import sys
import os
from PIL import Image

if len(sys.argv) >= 3:
  first_arg = sys.argv[1]
  second_arg = sys.argv[2]

  if not os.path.exists(second_arg):
    os.makedirs(second_arg)

  for item in os.listdir(first_arg):
    if item.endswith(".jpg"):
      img = Image.open(os.path.join(first_arg, item))
      output_filename = os.path.splitext(item)[0] + ".png"
      output_path = os.path.join(second_arg, output_filename)
      img.save(output_path, "PNG")

else:
  print("Please provide at least two arguments.")
