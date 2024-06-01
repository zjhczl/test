# 将图像转换为NumPy数组
from PIL import Image
import numpy as np

Image.MAX_IMAGE_PIXELS = None
# 打开图像文件
img = Image.open('/home/zj/ARC/yishankou/Production_3_DSM_merge.tif')

# 将图像转换为NumPy数组
img_array = np.array(img)

# 现在 img_array 是一个NumPy数组，你可以使用NumPy库来处理它
print(img_array[6][9])  # 打印图像的尺寸和颜色通道
