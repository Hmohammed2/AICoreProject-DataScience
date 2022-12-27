import boto3
import os
from PIL import Image

def download_images(bucketname, remotedirectoryname):
    s3 = boto3.resource("s3")
    bucket = s3.Bucket(bucketname)
    for obj in bucket.objects.filter(Prefix = remotedirectoryname):
        if not os.path.exists(os.path.dirname(obj.key)):
            os.makedirs(os.path.dirname(obj.key))
        bucket.download_file(obj.key, obj.key) # save to same path

def resize_images(loaded_image=str, vertical=int, width=int, path=str):
    image = Image.open(loaded_image)
    image.thumbnail((vertical, width)) # thumbnail method keeps the aspect ratio
    user_input = input("Do you want to save your data? (yes/no): ")
    while True:
        if user_input.lower() == "yes":
            image.save(path)
            break
        elif user_input.lower() == "no":
            break

# resize_images("images/0a26e526-1adf-4a2a-888d-a05f7f0a2f33/0a26e526-1adf-4a2a-888d-a05f7f0a2f33-a.png",
#                    400, 400, "processed_images/new_image.png")

image = Image.open("processed_images/new_image.png")
print(image.size)
