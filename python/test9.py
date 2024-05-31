# 监控文件变化
# pip install watchdog
import os
import shutil
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler


class RosbagHandler(FileSystemEventHandler):
    def __init__(self, source_directory, target_directory):
        self.source_directory = source_directory
        self.target_directory = target_directory

    def on_created(self, event):
        if event.is_directory:
            return
        if event.src_path.endswith('.bag'):
            self.compress_and_move(event.src_path)

    def on_deleted(self, event):
        if event.is_directory:
            return
        if event.src_path.endswith('.bag'):
            target_path = os.path.join(
                self.target_directory, os.path.basename(event.src_path) + '.zip')
            if os.path.exists(target_path):
                os.remove(target_path)
                print(f"Removed compressed file: {target_path}")

    def compress_and_move(self, file_path):
        file_name = os.path.basename(file_path)
        compressed_file_name = file_name + '.zip'
        compressed_file_path = os.path.join(
            self.target_directory, compressed_file_name)
        shutil.make_archive(compressed_file_path.replace(
            '.zip', ''), 'zip', os.path.dirname(file_path), file_name)
        print(f"Compressed and moved: {compressed_file_path}")


# Set up the source and target directories
source_directory = '/home/zj/rosbag'
target_directory = '/home/zj/rosbag-zip'

# Create the target directory if it doesn't exist
if not os.path.exists(target_directory):
    os.makedirs(target_directory)

# Compress existing rosbags
for file_name in os.listdir(source_directory):
    if file_name.endswith('.bag'):
        file_path = os.path.join(source_directory, file_name)
        handler = RosbagHandler(source_directory, target_directory)
        handler.compress_and_move(file_path)

# Set up the observer
event_handler = RosbagHandler(source_directory, target_directory)
observer = Observer()
observer.schedule(event_handler, source_directory, recursive=False)
observer.start()


while True:
    time.sleep(1)
