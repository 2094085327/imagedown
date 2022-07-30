import os
import glob

path = ["E:/学习/image/星空", "E:/学习/image/竖屏"]
for p in path:
    print(p)
    print("删除前有: ", len(os.listdir(p)), " 个文件...")
    # if p == "E:/学习/image/星空":
    # try:
    for infile in glob.glob(os.path.join(p, '*.tmp')):
        img_name_2 = infile.split(".")[-3]
        img_name_3 = img_name_2.split('\\')[-1]
        print(img_name_3)
        # os.remove(infile)
    print("删除后: ", len(os.listdir(p)), "\n\n")
# except:
#  continue
