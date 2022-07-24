#      base da url                parâmetros da url
url = "https://bytebanck.com/cambio?moedaOrigem=real&moedaDestino=dolar&quantidade=100"
print(url)
indice = url.find('?')
# Fatiamento de strings 
# Strings são sequências que podemos acessar por meio de seu indice, assim como definir um intervalo de fatiamento
url_base = url[0:indice] # Valor inicial é incluso e o valor final não do intervalo
print(url_base)

url_parametros = url[indice+1:]
print(url_parametros)