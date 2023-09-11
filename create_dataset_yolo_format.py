import os
import shutil

from decouple import config

BASE_DIR = config('BASE_DIR')
DATA_ALL_DIR = os.path.join(BASE_DIR, "weapons")
DATA_OUT_DIR = os.path.join(BASE_DIR, 'data')

if not os.path.exists(DATA_OUT_DIR):
    os.makedirs(DATA_OUT_DIR)

for set_ in ['train', 'validation', 'test']:
    for dir_ in [os.path.join(DATA_OUT_DIR, set_),
                 os.path.join(DATA_OUT_DIR, set_, 'images'),
                 os.path.join(DATA_OUT_DIR, set_, 'labels')]:
        if os.path.exists(dir_):
            shutil.rmtree(dir_)
        os.mkdir(dir_)

image_id = config('IMAGE_ID')  # label for Weapon. Ex: '/m/083kb'

train_bboxes_filename = os.path.join(BASE_DIR, 'oidv6-train-annotations-bbox.csv')
validation_bboxes_filename = os.path.join(BASE_DIR, 'validation-annotations-bbox.csv')
test_bboxes_filename = os.path.join(BASE_DIR, 'test-annotations-bbox.csv')

for j, filename in enumerate([train_bboxes_filename, validation_bboxes_filename, test_bboxes_filename]):
    set_ = ['train', 'validation', 'test'][j]
    print(filename)
    with open(filename, 'r') as f:
        line = f.readline()
        while len(line) != 0:
            _id, _, class_name, _, x1, x2, y1, y2, _, _, _, _, _ = line.split(',')[:13]
            if class_name in [image_id]:
                if not os.path.exists(os.path.join(DATA_OUT_DIR, set_, 'images', '{}.jpg'.format(_id))):
                    shutil.copy(os.path.join(DATA_ALL_DIR, '{}.jpg'.format(_id)),
                                os.path.join(DATA_OUT_DIR, set_, 'images', '{}.jpg'.format(_id)))
                with open(os.path.join(DATA_OUT_DIR, set_, 'labels', '{}.txt'.format(_id)), 'a') as f_ann:
                    # class_id, xc, yx, w, h
                    x1, x2, y1, y2 = [float(j) for j in [x1, x2, y1, y2]]
                    xc = (x1 + x2) / 2
                    yc = (y1 + y2) / 2
                    w = x2 - x1
                    h = y2 - y1

                    f_ann.write('0 {} {} {} {}\n'.format(xc, yc, w, h))
                    f_ann.close()

            line = f.readline()
