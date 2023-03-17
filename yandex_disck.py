import requests


class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def upload(self, file_path: str):
        host = 'https://cloud-api.yandex.net'
        upload_url = host + '/v1/disk/resources/upload'
        headers = {
            'Content-Type': 'application/json',
            'Authorization': 'OAuth {}'.format(self.token)
                   }
        params = {'path': file_path, 'overwrite': 'true'}
        response = requests.get(upload_url, headers=headers, params=params)
        data = response.json()
        href = data.get('href')
        open(file_path, 'w').closed
        response = requests.put(href, data=open(file_path, 'rb'))
        if response.status_code == 201:
            print('Файл загружен')



