# import os
# import cv2

# annotation_path = "./wider_face_split/wider_face_val_bbx_gt.txt"
# image_base_path = "./WIDER_val/images"
# output_label_path = "./WIDER_val/label"

# os.makedirs(output_label_path, exist_ok=True)

# with open(annotation_path, 'r') as f:
#     lines = f.readlines()

# current_image = None
# boxes = []

# for line in lines:
#     line = line.strip()
#     if line.endswith('.jpg'):
#         if current_image is not None:
#             img = cv2.imread(os.path.join(image_base_path, current_image))
#             h, w, _ = img.shape

#             label_dir = os.path.join(output_label_path, os.path.dirname(current_image))
#             os.makedirs(label_dir, exist_ok=True)

#             label_file = os.path.join(label_dir, os.path.basename(current_image).replace('.jpg', '.txt'))
#             with open(label_file, 'w') as lf:
#                 for box in boxes:
#                     x1, y1, bw, bh = box
#                     x_center = (x1 + bw / 2) / w
#                     y_center = (y1 + bh / 2) / h
#                     box_width = bw / w
#                     box_height = bh / h
#                     lf.write(f"0 {x_center} {y_center} {box_width} {box_height}\n")

#         current_image = line
#         boxes = []

#     elif line.isdigit():
#         continue
#     else:
#         box_data = list(map(int, line.split()))
#         boxes.append(box_data[:4])

# import os
# import shutil

# image_dir = './WIDER_test/images'
# label_dir = './WIDER_test/label'
# image_output_dir = './dataset/test/image'
# label_output_dir = './dataset/test/label'

# os.makedirs(image_output_dir, exist_ok=True)
# os.makedirs(label_output_dir, exist_ok=True)

# for root, dirs, files in os.walk(image_dir):
#     for file in files:
#         if file.endswith('.jpg'):
#             img_path = os.path.join(root, file)
#             label_path = img_path.replace(image_dir, label_dir).replace('.jpg', '.txt')

#             if os.path.exists(label_path):
#                 shutil.copy(img_path, os.path.join(image_output_dir, file))
#                 shutil.copy(label_path, os.path.join(label_output_dir, file.replace('.jpg', '.txt')))
#             else:
#                 print(f"라벨 없음: {file}")

import os
import shutil

dataset_path = '/Users/kevin/Desktop/Face-Detection-YOLO/dataset/val'
image_output_path = '/Users/kevin/Desktop/Face-Detection-YOLO/dataset/val/images'
label_output_path = '/Users/kevin/Desktop/Face-Detection-YOLO/dataset/val/labels'

os.makedirs(image_output_path, exist_ok=True)
os.makedirs(label_output_path, exist_ok=True)

for file in os.listdir(dataset_path):
    if file.endswith('.jpg'):
        shutil.move(os.path.join(dataset_path, file), os.path.join(image_output_path, file))
    elif file.endswith('.txt'):
        shutil.move(os.path.join(dataset_path, file), os.path.join(label_output_path, file))

print("이미지와 라벨이 분리되었습니다.")
