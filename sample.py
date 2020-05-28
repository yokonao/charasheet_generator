# sending HTTP request to the server for test
import requests
import json

post_url = "http://0.0.0.0:5000/"

with open('chara.json') as f:
    json_dict = json.load(f)
# files = {"image_file": open(file_path_name, 'rb')}
json_data = json.dumps(json_dict).encode("utf-8")

headers = {"Content-Type": "multipart/form-data"}

response = requests.post(
    post_url,
    data=json_data,
    # files=files,
    headers=headers
    )

# writing binary to empty PDF file
with open('test.pdf', 'wb') as f:
    f.write(response.content)
