import pandas as pd

# DataFrame representando o estoque da Petrobras
estoque = pd.DataFrame({
    'produto': ['Gasolina', 'Diesel', 'Querosene', 'Lubrificante'],
    'quantidade': [1000, 500, 300, 200]
})
print('estoque: \n', estoque, '\n')
# DataFrame representando as listas de compras com IDs únicos
listas_compras = pd.DataFrame({
    'id_lista': [1, 1, 2, 2, 3, 3, 3, 4, 4, 5, 5],
    'produto': ['Gasolina', 'Diesel', 'Querosene', 'Lubrificante', 'Etanol', 'Gasolina', 'Diesel', 'Querosene', 'Lubrificante', 'Etanol', 'Querosene'],
    'quantidade': [200, 600, 100, 200, 100, 300, 200, 150, 100, 50, 100]
})
print('listas_compras: \n', listas_compras, '\n')
# Função para processar a baixa no estoque
def processar_baixa_multiplos_dataframe(estoque: pd.DataFrame, listas_compras: pd.DataFrame) -> pd.DataFrame:
    resultados = pd.DataFrame(columns=['id_lista', 'produto', 'atendidos', 'nao_atendidos', 'Status'])
    for id_lista in listas_compras['id_lista'].unique():
        lista_atual = listas_compras[listas_compras['id_lista'] == id_lista]
        for _, item in lista_atual.iterrows():
            produto = item['produto']
            quantidade_solicitada = item['quantidade']
            # Verifica se o produto está no estoque
            if produto in estoque['produto'].values:
                # Obtém a quantidade disponível no estoque
                quantidade_estoque = estoque.loc[estoque['produto'] == produto, 'quantidade'].values[0]
                if quantidade_estoque >= quantidade_solicitada:
                    # Atualiza o estoque e adiciona à lista de atendidos
                    estoque.loc[estoque['produto'] == produto, 'quantidade'] -= quantidade_solicitada
                    novo_resultado = {'id_lista': id_lista, 'produto': produto, 'atendidos': quantidade_solicitada, 'nao_atendidos': 0, 'Status': 'Atendido'}
                    # print(f"Produto {produto} atendido na lista {id_lista}. Estoque atualizado: {estoque.loc[estoque['produto'] == produto, 'quantidade']}")
                    if estoque.loc[estoque['produto'] == produto, 'quantidade'].values[0] == 0:
                        # Produto esgotado
                        estoque = estoque.loc[estoque['produto'] != produto, :]
                else:
                    # Atende parcialmente ou não atende
                    novo_resultado = {'id_lista': id_lista, 'produto': produto, 'atendidos': quantidade_estoque, 'nao_atendidos': quantidade_solicitada - quantidade_estoque, 'Status': 'Parcialmente Atendido'}
                    estoque = estoque.loc[estoque['produto'] != produto, :]
            else:
                # Produto não encontrado no estoque
                novo_resultado = {'id_lista': id_lista, 'produto': produto, 'atendidos': 0, 'nao_atendidos': quantidade_solicitada, 'Status': 'Não Atendido'}
            resultados = pd.concat([resultados, pd.DataFrame([novo_resultado])], ignore_index=True)
    return resultados 

if __name__ == "__main__":
    # Chama a função para processar a baixa no estoque
    resultados = processar_baixa_multiplos_dataframe(estoque, listas_compras)
