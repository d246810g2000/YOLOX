import os
import random

images_path = 'JPEGImages/'
xmls_path = 'Annotations/'
train_val_txt_path = 'ImageSets/Main/'
val_percent = 0.1

images_list = os.listdir(images_path)
random.shuffle(images_list)

train_images_count = int((1-val_percent)*len(images_list))
val_images_count = int(val_percent*len(images_list))

train_txt = open(os.path.join(train_val_txt_path, 'train.txt'), 'w')
train_count = 0
for i in range(train_images_count):
    text = images_list[i].split('.jpg')[0] + '\n'
    train_txt.write(text)
    train_count+=1
    print('train_count: ' + str(train_count))
train_txt.close()

val_txt = open(os.path.join(train_val_txt_path, 'val.txt'), 'w')
val_count = 0
for i in range(val_images_count):
    text = images_list[i].split('.jpg')[0] + '\n'
    val_txt.write(text)
    val_count+=1
    print('val_count: ' + str(val_count))
val_txt.close()