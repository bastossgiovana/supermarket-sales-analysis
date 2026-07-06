#importando bibliotecas
import pandas as pd
import matplotlib.pyplot as plt

# Carregamento do dataset
dataframe = pd.read_csv('supermarket_sales.csv')

# Exploração inicial
print(dataframe.columns)
print("Valores duplicados:", dataframe.duplicated().sum())

# Análises
faturamento_total = dataframe['revenue'].sum()
print(f'Faturamento total: R$ {faturamento_total:,.2f}'.replace(',', 'X').replace('.', ',').replace('X', '.'))

quantidade_itens_vendidos = dataframe.shape[0]
print(f'Quantidade total de vendas: {quantidade_itens_vendidos}')

faturamento_por_produto = dataframe.groupby('product_line')['revenue'].sum().sort_values(ascending=False)

print("Linha de produto com maior faturamento:", faturamento_por_produto.index[0])
print(f'Faturamento: R$ {faturamento_por_produto.iloc[0]:,.2f}'.replace(',', 'X').replace('.', ',').replace('X', '.'))

faturamento_por_cidade = dataframe.groupby('city')['revenue'].sum().sort_values(ascending=False)

print("Cidade com maior faturamento:", faturamento_por_cidade.index[0])
print(f'Faturamento: R$ {faturamento_por_cidade.iloc[0]:,.2f}'.replace(',', 'X').replace('.', ',').replace('X', '.'))

quantidade_vendas_pagamento = dataframe['payment_method'].value_counts()

print("Forma de pagamento mais utilizada:", quantidade_vendas_pagamento.index[0])
print("Vezes utilizada:", quantidade_vendas_pagamento.iloc[0])

media_avaliacao_por_produto = dataframe.groupby('product_line')['rating'].mean().round(2)
print('A média de avaliação por cada linha de produto é igual a: ')
print(media_avaliacao_por_produto)



#Visualiações por gráficos

plt.figure(figsize=(8,5))
faturamento_por_produto.plot(kind='bar')
plt.title('Faturamento por linha de produto')
plt.xlabel('Linha de produto')
plt.ylabel('Faturamento')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('faturamento_produto.png', dpi=300, bbox_inches='tight')

plt.show()

plt.figure(figsize=(8,5))
faturamento_por_cidade.plot(kind='bar')
plt.title('Faturamento por cidade')
plt.xlabel('Cidade')
plt.ylabel('Faturamento')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('faturamento_cidade.png', dpi=300, bbox_inches='tight')

plt.show()

plt.figure(figsize=(6,6))
quantidade_vendas_pagamento.plot(kind='pie', autopct=lambda p: f'{p:.1f}%', startangle=90)
plt.title('Distribuição das vendas por forma de pagamento')
plt.savefig('pagamento.png', dpi=300, bbox_inches='tight')

plt.show()

#insights
print("\nINSIGHTS:")
print(f"- A linha de produto mais lucrativa é {top_produto}, indicando maior demanda nesse segmento.")
print(f"- A cidade com maior faturamento é {top_cidade}, sugerindo maior concentração de vendas.")
print(f"- O método de pagamento mais usado é {top_pagamento}, mostrando preferência dos clientes.")