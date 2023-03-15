import requests

class TestCursos:
    headers = {'Authorization': 'Token 8bab091f896c8a3fd370f5908c4ad614afcd1460'}

    url_base_cursos = 'http://localhost:8000/api/v2/cursos/'

    def test_get_cursos(self):
        cursos = requests.get(url=self.url_base_cursos, headers=self.headers)

        assert cursos.status_code == 200
        
    def test_get_curso(self):
        curso = requests.get(url=f'{self.url_base_cursos}2/', headers=self.headers)

        assert curso.status_code == 200

    def test_post_curso(self):
        novo = {
            "titulo": "Curso de Programação Flutter",
            "url": "https://flutter.dev",
        }
        resposta = requests.post(url=self.url_base_cursos, headers=self.headers, data=novo)

        assert resposta.status_code == 201
        assert resposta.json()['titulo'] == novo['titulo']

    def test_put_curso(self):
        atualizado = {
            "titulo": "Novo Curso de Flutter 2",
            "url": "https://flutter.dev/2",
        }

        resposta = requests.put(url=f'{self.url_base_cursos}3/', headers=self.headers, data=atualizado)

        assert resposta.status_code == 200
    
    def test_put_titulo_curso(self):
        atualizado = {
            "titulo": "Novo Curso de Flutter 3",
            "url": "https://flutter.dev/3",
        }

        resposta = requests.put(url=f'{self.url_base_cursos}3/', headers=self.headers, data=atualizado)

        assert resposta.json()['titulo'] == atualizado['titulo']

    def test_delete_curso(self):
        resposta = requests.delete(url=f'{self.url_base_cursos}3/', headers=self.headers)

        assert resposta.status_code == 204 and len(resposta.text) == 0