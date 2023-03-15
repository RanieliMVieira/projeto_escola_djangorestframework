import requests 

headers = {'Authorization': 'Token 8bab091f896c8a3fd370f5908c4ad614afcd1460'}

url_base_cursos = 'http://localhost:8000/api/v2/cursos/'
url_base_avaliacoes = 'http://localhost:8000/api/v2/avaliacoes/'


resultado = requests.delete(url=f'{url_base_cursos}3/', headers=headers)

# Testando o código HTTP
assert resultado.status_code == 204

# Testando se o tamanho do conteúdo retorno é 0
assert len(resultado.text) == 0