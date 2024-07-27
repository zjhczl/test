# webhook
from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route('/webhook', methods=['POST'])
def webhook():
    if request.method == 'POST':
        data = request.json
        if data:
            # 打印接收到的回调数据
            print('Received webhook data:')
            print(f"notify_type: {data.get('notify_type')}")
            print(f"org_id: {data.get('org_id')}")
            print(f"org_name: {data.get('org_name')}")
            print(f"prj_id: {data.get('prj_id')}")
            print(f"prj_name: {data.get('prj_name')}")
            print(f"sn: {data.get('sn')}")

            task_info = data.get('task_info', {})
            print(f"task_id: {task_info.get('task_id')}")
            print(f"task_type: {task_info.get('task_type')}")
            print(f"tags: {task_info.get('tags')}")

            files = data.get('files', [])
            for file in files:
                print(f"\nFile ID: {file.get('id')}")
                print(f"UUID: {file.get('uuid')}")
                print(f"File Type: {file.get('file_type')}")
                print(f"Sub File Type: {file.get('sub_file_type')}")
                print(f"Name: {file.get('name')}")
                print(f"Key: {file.get('key')}")

            folder_info = data.get('folder_info', {})
            print(f"\nFolder Info:")
            print(
                f"Expected File Count: {folder_info.get('expected_file_count')}")
            print(
                f"Uploaded File Count: {folder_info.get('uploaded_file_count')}")
            print(f"Folder ID: {folder_info.get('folder_id')}")

            return jsonify({'status': 'success'}), 200
        else:
            return jsonify({'status': 'bad request'}), 400
    else:
        return jsonify({'status': 'method not allowed'}), 405


if __name__ == '__main__':
    app.run(port=5000)
