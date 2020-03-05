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
'''
from requests import get
from hashlib import sha1
import string
import json

alfabeto = list(string.ascii_lowercase)

descriptografado = ""


api = get("https://api.codenation.dev/v1/challenge/dev-ps/generate-data?token=b1a53f0d8478a6cf3664d4a918221650"
                   "d98cca71")

api_json = api.json() #API em formato de dicionario

cifrado = api_json['cifrado'].lower() 

def criamod_json(api_em_dict):
    with open("answer.json", "w") as f:
        json.dump(api_em_dict, f)

criamod_json(api_json)

for c in cifrado:
    if c in alfabeto:
        descriptografado += alfabeto[(alfabeto.index(c))-(api_json['numero_casas'])]
          #MUDAR O 2
    else:
        descriptografado += c

result_sha1 = sha1(descriptografado.encode()) #Criptografando no formato SHA1

#ATUALIZANDO JSON
api_json['resumo_criptografico'] = (result_sha1.hexdigest())
resumo = (result_sha1.hexdigest())
api_json['decifrado'] = descriptografado

criamod_json(api_json)

#atualizando_json(descriptografado, resumo)
arquivo_json = open("answer.json", 'r')
dados_json = json.load(arquivo_json)
dados_json["decifrado"] = descriptografado

print(f'\n ==> CIFRADO: {cifrado}')
print(f'\n ==> DESCIFRADO: {descriptografado}')
print(f'\n ==> SHA1: {(result_sha1.hexdigest())} \n')
