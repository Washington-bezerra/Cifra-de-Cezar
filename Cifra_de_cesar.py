'''
Criado por: Washington Bezerra
Git: Washington-bezerra - https://github.com/Washington-bezerra
Linkedin: https://www.linkedin.com/in/washington-luis-3b463a162/

Versão: 1.0.0  - Criação
04/03/2020 - 19:53

Versão: 1.1.0 - Adicionado a criptograia  SHA1
04/03/2020 - 20:51

Versão: 2.0.0 - Cria e atualiza o json
05/03/2020 - 18:31

Versão: 3.0.0 - Realiza o post do JSON na API
06/03/2020
'''

import requests
from hashlib import sha1
import string
import json

API_URL = "https://api.codenation.dev/v1/challenge/dev-ps/submit-solution?token=b1a53f0d8478a6cf3664d4a918221650d98cca71"
api_post = "https://api.codenation.dev/v1/challenge/dev-ps/submit-solution?token=b1a53f0d8478a6cf3664d4a918221650d98cca71"
alfabeto = list(string.ascii_lowercase)

descriptografado = ""

api = requests.get("https://api.codenation.dev/v1/challenge/dev-ps/generate-data?token=b1a53f0d8478a6cf3664d4a918221650d98cca71")

api_json = api.json() #API em formato de dicionario

cifrado = api_json['cifrado'].lower() 

result_sha1 = sha1(descriptografado.encode()) #Criptografando no formato SHA1

#Função que cria e modifica o JSON
def criamod_json(api_em_dict):
    with open("answer.json", "w") as f:
        json.dump(api_em_dict, f)

criamod_json(api_json)

for c in cifrado:
    if c in alfabeto:
        descriptografado += alfabeto[(alfabeto.index(c))-(api_json['numero_casas'])]

    else:
        descriptografado += c

#Dados que atualiza o dict
api_json['resumo_criptografico'] = (result_sha1.hexdigest())
api_json['decifrado'] = descriptografado

#Chama a função e modifica o JSON o dicionario atualizado
criamod_json(api_json)

#Fazendo o post do JSON na API
file = {'answer': open('C:\\Users\\WashingtonSantosBeze\\Desktop\\Cifra de Cezar\\Cifra-de-Cezar\\answer.json','rb')}
print (file)
try:
    submit = requests.post(api_post, files=file)
    print(submit.text)

except ValueError:
    print(ValueError)