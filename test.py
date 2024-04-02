# 生成目录
import os


def generate_readme(root_folder, readme_file):
    files = []

    for root, dirs, filenames in os.walk(root_folder):
        for filename in filenames:
            if filename.endswith(".py"):
                files.append(filename)

    files.sort()  # 按文件名称排序

    with open(readme_file, 'w') as f:
        f.write("# 文件功能目录\n\n")

        for file in files:
            file_path = os.path.join(root_folder, file)
            function_name = get_function_name(file_path)
            if function_name:
                f.write(f"- [{file}](#{file})\n")

        f.write("\n")

        for file in files:
            file_path = os.path.join(root_folder, file)
            function_name = get_function_name(file_path)
            if function_name:
                f.write(f"## {file}\n\n")
                f.write(f"功能：{function_name}\n\n")


def get_function_name(file_path):
    with open(file_path, 'r') as f:
        first_line = f.readline().strip()
        if first_line.startswith("#"):
            return first_line[1:].strip()
    return None


# 设置根文件夹和readme文件名
root_folder = "./"
readme_file = "./readme.md"

# 生成readme文件
generate_readme(root_folder, readme_file)
