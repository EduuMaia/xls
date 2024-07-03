import pandas as pd

with open('vendas.txt', 'r') as file:
    data = file.read().split('\n\n')  # Dividir as vendas por linhas em branco

vendas = []
datas = []
nomes = []
valores = []

# Processar os dados
for item in data:
    lines = item.split('\n')
    if len(lines) == 4:
        vendas.append(lines[0].split()[1])  # nrVenda
        datas.append(lines[1])  # Data
        nomes.append(lines[2])  # nome
        valores.append(lines[3].replace('R$ ', '').replace(',', '.'))  # Valor

# Criar um DataFrame
df = pd.DataFrame({
    'Venda': vendas,
    'Data': datas,
    'Nome': nomes,
    'Valor': valores
})

# Converter a coluna de valores para float
df['Valor'] = df['Valor'].astype(float)

# Salvar o DataFrame no xlsx
df.to_excel('vendas.xlsx', index=False)
