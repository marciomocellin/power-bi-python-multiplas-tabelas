Power BI: Como Utilizar Python com Múltiplas Tabelas

Isso é uma prova de conceito sobre a utilisacao do script python (`prova_de_conceito.py`) no Power BI. O objetivo é utilizar a funçao `Python.Execute()` para executar um script python que utilizará dois dataframes, já carregados no Power BI, como entrada e retornará um data frame como saída.	

Foi criada uma função que se utiliza de múltiplos `for` para verificar se os produtos estão disponíveis no estoque, atualiza as quantidades e gera um relatório sobre os atendimentos realizados.


# função do Power BI com script python incluido
``` 
= Python.Execute("import pandas as pd#(lf)def processar_baixa_multiplos_dataframe(estoque: pd.DataFrame, listas_compras: pd.DataFrame) -> pd.DataFrame:#(lf)    resultados = pd.DataFrame(columns=['id_lista', 'produto', 'atendidos', 'nao_atendidos', 'Status'])#(lf)    for id_lista in listas_compras['id_lista'].unique():#(lf)        lista_atual = listas_compras[listas_compras['id_lista'] == id_lista]#(lf)        for _, item in lista_atual.iterrows():#(lf)            produto = item['produto']#(lf)            quantidade_solicitada = item['quantidade']#(lf)            # Verifica se o produto está no estoque#(lf)            if produto in estoque['produto'].values:#(lf)                # Obtém a quantidade disponível no estoque#(lf)                quantidade_estoque = estoque.loc[estoque['produto'] == produto, 'quantidade'].values[0]#(lf)                if quantidade_estoque >= quantidade_solicitada:#(lf)                    # Atualiza o estoque e adiciona à lista de atendidos#(lf)                    estoque.loc[estoque['produto'] == produto, 'quantidade'] -= quantidade_solicitada#(lf)                    novo_resultado = {'id_lista': id_lista, 'produto': produto, 'atendidos': quantidade_solicitada, 'nao_atendidos': 0, 'Status': 'Atendido'}#(lf)                    # print(f""Produto {produto} atendido na lista {id_lista}. Estoque atualizado: {estoque.loc[estoque['produto'] == produto, 'quantidade']}"")#(lf)                    if estoque.loc[estoque['produto'] == produto, 'quantidade'].values[0] == 0:#(lf)                        # Produto esgotado#(lf)                        estoque = estoque.loc[estoque['produto'] != produto, :]#(lf)                else:#(lf)                    # Atende parcialmente ou não atende#(lf)                    novo_resultado = {'id_lista': id_lista, 'produto': produto, 'atendidos': quantidade_estoque, 'nao_atendidos': quantidade_solicitada - quantidade_estoque, 'Status': 'Parcialmente Atendido'}#(lf)                    estoque = estoque.loc[estoque['produto'] != produto, :]#(lf)            else:#(lf)                # Produto não encontrado no estoque#(lf)                novo_resultado = {'id_lista': id_lista, 'produto': produto, 'atendidos': 0, 'nao_atendidos': quantidade_solicitada, 'Status': 'Não Atendido'}#(lf)            resultados = pd.concat([resultados, pd.DataFrame([novo_resultado])], ignore_index=True)#(lf)    return resultados #(lf)#(lf)if __name__ == ""__main__"":#(lf)    # Chama a função para processar a baixa no estoque#(lf)    resultados = processar_baixa_multiplos_dataframe(estoque, listas_compras)",[estoque=estoque, listas_compras=lista_comprar])
```

# Explicaçao da funçao Python.Execute
A função `Python.Execute()` é utilizada para executar scripts Python dentro do Power BI. Ela permite que você escreva código Python diretamente no Power Query Editor e utilize os resultados desse código como parte do seu modelo de dados.
A função aceita dois parâmetros principais: o código Python a ser executado e os dados de entrada. Os dados de entrada podem ser passados como tabelas do Power BI, que são convertidas em dataframes do pandas no ambiente Python.
O resultado do script Python é retornado como uma tabela do Power BI, que pode ser utilizada em relatórios e visualizações.

## Primeiro parametro: código Python
O Primeiro parametro é uma string que contém o código Python propriamente dito. A diferença é que as quebras de linhas são representadas por `#(lf)` no código. A tipica estrutura de dentação do python é respeitada, mas as quebras de linha são representadas por `#(lf)` para que o Power BI possa interpretar corretamente o código. Isso é necessário porque o Power BI não aceita quebras de linha normais dentro de strings.
Contudo isso não realmente um problema para o desenvolvimento, pois o codigo pode ser escrito normalmente em qualquer IDE e depois copiado para o Power BI. O Power BI irá automaticamente converter as quebras de linha em `#(lf)`.

## Segundo parametro: dados de entrada
O segundo parametro é um dicionário que contém os dados de entrada para o script Python. As chaves do dicionário são os nomes das tabelas do Power BI e os valores são os dataframes correspondentes no ambiente Python. Por exemplo: `[listas_compras=lista_comprar]` significa que a tabela `lista_comprar` do Power BI será convertida em um dataframe chamado `listas_compras` no ambiente Python.
O Power BI converte automaticamente as tabelas em dataframes do pandas.

# Requisitos
O Power BI exige que o Python esteja instalado e configurado corretamente no seu ambiente virtual. Além disso, as bibliotecas necessárias, pandas e matplotlib, devem estar disponíveis para uso.

# Referências
[Power BI: How to use Python with multiple tables in the Power Query Editor?](https://stackoverflow.com/questions/51947441/power-bi-how-to-use-python-with-multiple-tables-in-the-power-query-editor)