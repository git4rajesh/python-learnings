import os

from PIL import Image

image_path = r'D:\Knowledge\EIP3.0\Week4\tiny-imagenet-200\val1\images'

files = []
# r=root, d=directories, f = files
for r, d, f in os.walk(image_path):
    for file in f:
        if '.JPEG' in file:
            files.append(os.path.join(r, file))

for filename in files:
    print(filename)
    with Image.open(filename) as image:
        width, height = image.size
        if width != 64:
            print(width, height)
            print('****************')


# filename = r'D:\Knowledge\EIP3.0\Week4\tiny-imagenet-200\val2\images\val_9896.JPEG'
# with Image.open(filename) as image:
#     width, height = image.size
#
#
# print(width, height)