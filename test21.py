# 数据流压缩
# pip install brotli
import brotli


def compress_data(data):
    # 使用Brotli算法压缩数据
    compressed_data = brotli.compress(data)
    return compressed_data


def decompress_data(compressed_data):
    # 使用Brotli算法解压缩数据
    decompressed_data = brotli.decompress(compressed_data)
    return decompressed_data


# 测试数据
original_data = b"Lorem ipsum dolor sit amet, consectetur adipis\r\n/r/ncing elit."
print("Original data:", original_data)

# 压缩数据
compressed_data = compress_data(original_data)
print("Compressed data:", compressed_data)

# 解压缩数据
decompressed_data = decompress_data(compressed_data)
print("Decompressed data:", decompressed_data.decode())
