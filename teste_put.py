import requests 

headers = {'Authorization': 'Token 8bab091f896c8a3fd370f5908c4ad614afcd1460'}

url_base_cursos = 'http://localhost:8000/api/v2/cursos/'
url_base_avaliacoes = 'http://localhost:8000/api/v2/avaliacoes/'


curso_atualizado = {
    "titulo": "Novo Curso de Scrum 3",
    "url": "http://www.geekuniversity.com.br/ncs3"
}

# Buscando o curso com ID 3
# curso = requests.get(f'{url_base_cursos}3/', headers=headers)

# print(curso.json())

resultado = requests.put(url=f'{url_base_cursos}3/', headers=headers, data=curso_atualizado)

# Testando o código de status HTTP
assert resultado.status_code == 200

# Testando uo título
assert resultado.json(['titulo']) == curso_atualizado["titulo"]