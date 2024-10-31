import pandas as pd
tabela = pd.read_excel("Relatorio.xlsx")
venda_total = tabela["Valor Final"].sum()
venda_por_loja = tabela[["ID Loja", "Valor Final"]].groupby("ID Loja").sum()

fartu_por_loja = tabela[["ID Loja", "Produto", "Valor Final"]].groupby(["ID Loja", "Produto"] ).sum()

def vendas():
	print(tabela)
	print("----------–-------------")
	print("Venda total")
	print(venda_total)
	print('-------------------------')
	print("vendas por loja")
	print(venda_por_loja)
	print('------------------------')
	print(fartu_por_loja)
vendas()	
