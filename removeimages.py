import os
import glob

images = glob.glob('data/*/#*.png')

for im in images:
    os.remove(im)
