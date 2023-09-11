### Download Dataset
__Go to `Open Images Dataset V7` page__
1. Download the `downloader.py` file
2. Download the object detection dataset (Annotations and metadata - Boxes): `train`, `validation` and `test`
3. Execute `create_image_list_file.py`
```
python create_image_list_file.py
```
4. Execute `downloader.py`
```
python downloader.py $IMAGE_LIST_FILE --download_folder=$DOWNLOAD_FOLDER
```
5. Execute `create_dataset_yolo_format.py`, changing `DATA_ALL_DIR` by __$DOWNLOAD_FOLDER__
```
python create_dataset_yolo_format.py
```
---
### References
Code: https://github.com/computervisioneng/yolov8-full-tutorial
