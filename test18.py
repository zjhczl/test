# 绘制折线图z
import matplotlib.pyplot as plt
import re


def parse_data(file_path):
    # 读取文件内容
    with open(file_path, 'r') as file:
        data = file.read()

    # 提取linear_acceleration中的z数据
    pattern = re.compile(r'linear_acceleration:\s*[^z]*\s*z:\s*(-?\d+\.\d+)')
    z_values = [float(match.group(1)) for match in pattern.finditer(data)]
    return z_values


def plot_data(z_values):
    # 绘制折线图
    plt.plot(z_values, marker='o', linestyle='-')
    plt.title('Linear Acceleration Z-Axis')
    plt.xlabel('Sample Index')
    plt.ylabel('Linear Acceleration (z)')
    plt.grid(True)
    plt.show()


if __name__ == "__main__":
    file_path = '/home/zj/1.txt'  # 你可以将这个路径改为你的数据文件路径
    z_values = parse_data(file_path)
    plot_data(z_values)
