import requests
from my_token import TOKEN

class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def upload(self, file_path: str):
        upload_url = "https://cloud-api.yandex.net/v1/disk/resources/upload"
        headers = {'Content-Type': 'application/json', 'Authorization': 'OAuth {}'.format(self.token)}
        filename = file_path.split('/', )[-1]
        params = {"path": f"Загрузки/{filename}", "overwrite": "true"}
        _response = requests.get(upload_url, headers=headers, params=params).json()
        href = _response.get("href", "")
        response = requests.put(href, data=open(file_path, 'rb'))
        response.raise_for_status()
        if response.status_code == 201:
            return "Файл загружен"
        else:
            return f"Код ошибки: {response.status_code}"

if __name__ == '__main__':
    path_to_file = 'food_list.txt'
    token = TOKEN
    uploader = YaUploader(token)
    result = uploader.upload(path_to_file)
    print(result)

