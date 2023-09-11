import os

from decouple import config

image_id = config('IMAGE_ID')  # label for Weapon. Ex: '/m/083kb'

BASE_DIR = config('BASE_DIR')  # root
train_bboxes_filename = os.path.join(BASE_DIR, 'oidv6-train-annotations-bbox.csv')
validation_bboxes_filename = os.path.join(BASE_DIR, 'validation-annotations-bbox.csv')
test_bboxes_filename = os.path.join(BASE_DIR, 'test-annotations-bbox.csv')

image_list_file_path = os.path.join(BASE_DIR, 'image_list_file')

image_list_file_list = []
for j, filename in enumerate([train_bboxes_filename, validation_bboxes_filename, test_bboxes_filename]):
    print(filename)
    with open(filename, 'r') as f:
        line = f.readline()
        while len(line) != 0:
            _id, _, class_name, _, x1, x2, y1, y2, _, _, _, _, _ = line.split(',')[:13]
            if class_name in [image_id] and _id not in image_list_file_list:
                image_list_file_list.append(_id)
                with open(image_list_file_path, 'a') as fw:
                    fw.write('{}/{}\n'.format(['train', 'validation', 'test'][j], _id))
            line = f.readline()

        f.close()
