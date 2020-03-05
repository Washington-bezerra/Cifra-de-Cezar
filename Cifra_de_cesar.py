'''
Criado por: Washington Bezerra
Git: Washington-bezerra - https://github.com/Washington-bezerra
Linkedin: https://www.linkedin.com/in/washington-luis-3b463a162/

Versão: 1.0.0  - Criação
04/03/2020 - 19:53

Versão: 1.1.0 - Adicionado a criptograia  SHA1
04/03/2020 - 20:51

'''
from requests import get
from hashlib import sha1

descripitografado = ""
alfabeto = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u",
            "v", "w", "x", "y", "z"]

api = get("https://api.codenation.dev/v1/challenge/dev-ps/generate-data?token=b1a53f0d8478a6cf3664d4a918221650"
                   "d98cca71")

api_json = api.json()
cifrado = api_json['cifrado']
for c in cifrado:
    if c in alfabeto:
        descripitografado += alfabeto[alfabeto.index(c)-2]
        '''MUDAR O 2'''
    else:
        descripitografado += c

print(cifrado)
print(descripitografado)
result = sha1(descripitografado.encode())
print("The hexadecimal equivalent of SHA1 is : {}" .format(result.hexdigest()))
