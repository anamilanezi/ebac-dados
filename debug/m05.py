# def retorno(juros: float):
#   return lambda investimento: investimento * (1 + juros)
#  
# retorno_5_porcento = retorno(juros=0.05)
# retorno_10_porcento = retorno(juros=0.10)
# 
# anos = 10
# valor_inicial = 1000
# valor_final = valor_inicial
# 
# for ano in range(1, anos+1):
#   valor_final = retorno_5_porcento(investimento=valor_final)
# 
# valor_final = round(valor_final, 2)
# print(valor_final)

# numeros = [1, 2, 3]
# 
# numeros_ao_cubo = map(lambda num: num ** 3, numeros)
# 
# print(list(numeros_ao_cubo))

anos = [10, 10, 10]
taxas_juros = [0.05, 0.1, 0.15]
valores_iniciais = [1000, 1000, 1000]

def retorno(valor_inicial: float, taxa_juros: float, anos:int) -> float:
	valor_final = valor_inicial
	for ano in range(1,anos+1):
		valor_final = valor_final * (1 + taxa_juros)
	return round(valor_final, 2)

cenarios = list(map(retorno, valores_iniciais, taxas_juros, anos))