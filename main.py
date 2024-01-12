import os
from PIL import Image, UnidentifiedImageError
import imageio.v3 as iio

source_directory = r'F:\Bas The Creative Technologist\Hanco Kolk webshop\content-voor-de-site'
destination_directory = r'F:\Bas The Creative Technologist\Hanco Kolk webshop\converted tifs-pngs'

for filename in os.listdir(source_directory):
    if filename.endswith('.tif'):
        tif_path = os.path.join(source_directory, filename)

        png_filename = f"{os.path.splitext(filename)[0]}.png"
        png_path = os.path.join(destination_directory, png_filename)

        if os.path.exists(png_path):
            print(f"Skipping {png_filename}, already exists.")
            continue

        try:
            img = iio.imread(tif_path)

            if img.shape[-1] != 3:
                img = img[..., :3]

            img = Image.fromarray(img)

            if img.mode == "CMYK":
                img = img.convert("RGB")

            img.save(png_path, 'PNG')

        except UnidentifiedImageError as e:
            print(f"Cannot identify image file {filename}: {e}")
        except Exception as e:
            print(f"Error processing file {filename}: {e}")

print("Conversion complete. All convertable .tif files have been converted to .png format.")
