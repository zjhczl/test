# 绘制折线图x
import re
import matplotlib.pyplot as plt

# 数据文件路径
file_path = '/home/zj/1.txt'

# 正则表达式匹配模式
pattern = re.compile(
    r'linear_acceleration:\s*?\n\s*x:\s*([-+]?[0-9]*\.?[0-9]+)')

# 用于存储 x 轴数据
x_data = []

# 读取并解析数据文件
with open(file_path, 'r') as file:
    content = file.read()
    matches = pattern.findall(content)
    x_data = [float(match) for match in matches]

# 绘制折线图
plt.plot(x_data, label='Linear Acceleration X')
plt.xlabel('Sample Index')
plt.ylabel('Linear Acceleration X')
plt.title('Linear Acceleration X Over Time')
plt.legend()
plt.grid(True)
plt.show()
# 111
