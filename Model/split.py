import glob
import os
import numpy as np
import shutil
from PIL import Image

#------------------------------------------------------------
# Create a folder structure for YOLOv5 training
#------------------------------------------------------------
if not os.path.exists('dataset'):
    for folder in ['images', 'labels']:
        for split in ['train', 'val', 'test']:
            os.makedirs(f'dataset/{folder}/{split}')


#------------------------------------------------------------
# Get filenames from a folder
#------------------------------------------------------------
def get_filenames(folder):
    filenames = set()
    
    for path in glob.glob(os.path.join(folder, '*.jpg')):
        # Extract the filename
        filename = os.path.split(path)[-1]        
        filenames.add(filename)
        
    return filenames


#------------------------------------------------------------
# Dog and cat image filename sets
#------------------------------------------------------------
apple_pencil_images = get_filenames('dataset_folder/Apple Pencil/images')
bag_images = get_filenames('dataset_folder/Bag/images')
calculator_images = get_filenames('dataset_folder/Calculator/images')
card_images = get_filenames('dataset_folder/Card/images')
cup_images = get_filenames('dataset_folder/Cup/images')
earphone_images = get_filenames('dataset_folder/Earphone/images')
eyeglasses_images = get_filenames('dataset_folder/Eyeglasses/images')
flashlight_images = get_filenames('dataset_folder/Flashlight/images')
headphone_images = get_filenames('dataset_folder/Headphone/images')
helmet_images = get_filenames('dataset_folder/Helmet/images')
ipad_images = get_filenames('dataset_folder/iPad/images')
key_images = get_filenames('dataset_folder/Key/images')
laptop_images = get_filenames('dataset_folder/Laptop/images')
mouse_images = get_filenames('dataset_folder/Mouse/images')
passport_images = get_filenames('dataset_folder/Passport/images')
pen_images = get_filenames('dataset_folder/Pen/images')
phone_images = get_filenames('dataset_folder/Phone/images')
sneaker_images = get_filenames('dataset_folder/Sneaker/images')
sock_images = get_filenames('dataset_folder/Sock/images')
umbrella_images = get_filenames('dataset_folder/Umbrella/images')
watch_images = get_filenames('dataset_folder/Watch/images')
water_bottle_images = get_filenames('dataset_folder/Water Bottle/images')


#------------------------------------------------------------
# Convert the filename sets into Numpy
#------------------------------------------------------------
apple_pencil_images = np.array(list(apple_pencil_images))
bag_images = np.array(list(bag_images))
calculator_images = np.array(list(calculator_images))
card_images = np.array(list(card_images))
cup_images = np.array(list(cup_images))
earphone_images = np.array(list(earphone_images))
eyeglasses_images = np.array(list(eyeglasses_images))
flashlight_images = np.array(list(flashlight_images))
headphone_images = np.array(list(headphone_images))
helmet_images = np.array(list(helmet_images))
ipad_images = np.array(list(ipad_images))
key_images = np.array(list(key_images))
laptop_images = np.array(list(laptop_images))
mouse_images = np.array(list(mouse_images))
passport_images = np.array(list(passport_images))
pen_images = np.array(list(pen_images))
phone_images = np.array(list(phone_images))
sneaker_images = np.array(list(sneaker_images))
sock_images = np.array(list(sock_images))
umbrella_images = np.array(list(umbrella_images))
watch_images = np.array(list(watch_images))
water_bottle_images = np.array(list(water_bottle_images))


#------------------------------------------------------------
# Use the same random seed for reproducability
#------------------------------------------------------------
np.random.seed(42)
np.random.shuffle(apple_pencil_images)
np.random.shuffle(bag_images)
np.random.shuffle(calculator_images)
np.random.shuffle(card_images)
np.random.shuffle(cup_images)
np.random.shuffle(earphone_images)
np.random.shuffle(eyeglasses_images)
np.random.shuffle(flashlight_images)
np.random.shuffle(headphone_images)
np.random.shuffle(helmet_images)
np.random.shuffle(ipad_images)
np.random.shuffle(key_images)
np.random.shuffle(laptop_images)
np.random.shuffle(mouse_images)
np.random.shuffle(passport_images)
np.random.shuffle(pen_images)
np.random.shuffle(phone_images)
np.random.shuffle(sneaker_images)
np.random.shuffle(sock_images)
np.random.shuffle(umbrella_images)
np.random.shuffle(watch_images)
np.random.shuffle(water_bottle_images)

# Function to create directories if they don't exist
def create_directory(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)
        
#------------------------------------------------------------
# Split data into train, val, and test
#------------------------------------------------------------
def split_dataset(things, image_names, train_size, val_size):
    for i, image_name in enumerate(image_names):
        # Label filename
        label_name = image_name.replace('.jpg', '.txt')

        # Split into train, val, or test
        if i < train_size:
            split = 'train'
        elif i < train_size + val_size:
            split = 'val'
        else:
            split = 'test'

         # Source paths
        source_image_path = f'dataset_folder/{things}/images/{image_name}'
        source_label_path = f'dataset_folder/{things}/labels/{label_name}'

        # Destination paths
        target_image_folder = f'dataset/images/{split}'
        target_label_folder = f'dataset/labels/{split}'

        # Create directories if they don't exist
        create_directory(target_image_folder)
        create_directory(target_label_folder)

        # Copy files
        shutil.copy(source_image_path, target_image_folder)
        shutil.copy(source_label_path, target_label_folder)

split_dataset('apple pencil', apple_pencil_images, train_size=500, val_size=50)
split_dataset('bag', bag_images, train_size=500, val_size=50)
split_dataset('calculator', calculator_images, train_size=500, val_size=50)
split_dataset('card', card_images, train_size=1000, val_size=150)
split_dataset('cup', cup_images, train_size=500, val_size=50)
split_dataset('earphone', earphone_images, train_size=500, val_size=50)
split_dataset('eyeglasses', eyeglasses_images, train_size=500, val_size=50)
split_dataset('flashlight', flashlight_images, train_size=500, val_size=50)
split_dataset('headphone', headphone_images, train_size=500, val_size=50)
split_dataset('helmet', helmet_images, train_size=500, val_size=50)
split_dataset('ipad', ipad_images, train_size=500, val_size=50)
split_dataset('key', key_images, train_size=700, val_size=110)
split_dataset('laptop', laptop_images, train_size=700, val_size=110)
split_dataset('mouse', mouse_images, train_size=500, val_size=50)
split_dataset('passport', passport_images, train_size=500, val_size=50)
split_dataset('pen', pen_images, train_size=500, val_size=50)
split_dataset('phone', phone_images, train_size=900, val_size=130)
split_dataset('sneaker', sneaker_images, train_size=500, val_size=50)
split_dataset('sock', sock_images, train_size=500, val_size=50)
split_dataset('umbrella', umbrella_images, train_size=500, val_size=50)
split_dataset('watch', watch_images, train_size=500, val_size=50)
split_dataset('water bottle', water_bottle_images, train_size=500, val_size=50)