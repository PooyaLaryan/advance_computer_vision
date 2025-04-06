import tensorflow as tf
import os

url = "https://github.com/brendenlake/omniglot/raw/master/python/images_background.zip"
path_to_zip = tf.keras.utils.get_file("images_background.zip", origin=url, extract=True)

def get_image_paths_and_labels(base_dir):
    image_paths = []
    labels = []
    for root, dirs, files in os.walk(base_dir):
        for file in files:
            if file.endswith('.png') or file.endswith('.jpg'):
                image_paths.append(os.path.join(root, file))
                # Use os.path.split() for more reliable path splitting
                character_folder = os.path.basename(os.path.dirname(root))
                labels.append(character_folder)
    return image_paths, labels

# Get the path where keras downloaded and extracted the data
data_dir = os.path.dirname(path_to_zip)
base_dir = os.path.join(data_dir, 'images_background')

image_paths, labels = get_image_paths_and_labels(base_dir)
print(f"Total images: {len(image_paths)}, Total labels: {len(set(labels))}")
