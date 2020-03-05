import string
alfabeto = list(string.ascii_lowercase)

cifrado = "kpukfg gxgta nctig rtqitco, vjgtg ku c rtqitco vtakpi vq igv qwv. e.c.t. jqctg"
descriptografado = ""
for c in cifrado:
    if c in alfabeto:
num_casa = api_json['numero_casas']
        descriptografado += alfabeto[(alfabeto.index(c))-(num_casa)]
          #MUDAR O 2
    else:
        descriptografado += c

print(descriptografado)