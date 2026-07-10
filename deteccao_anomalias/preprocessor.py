import os
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

def analisar_dados(df):
    """
    Exibe uma análise exploratória rápida comparando transações normais e anômalas.
    """
    print("=== ANÁLISE EXPLORATÓRIA DOS DADOS ===")
    print(f"Total de registros: {len(df)}")
    print(df['is_anomalia'].value_counts(normalize=True).rename({0: 'Normais', 1: 'Anômalias'}) * 100)
    print("\nEstatísticas Médias por Tipo de Transação:")
    
    # Agrupa por anomalia e calcula a média das variáveis contínuas
    media_grupo = df.groupby('is_anomalia')[['valor', 'hora_dia', 'distancia_habitual', 'dispositivo_novo']].mean()
    # Mapeia o índice do grupo para nomes mais amigáveis
    media_grupo.index = media_grupo.index.map({0: 'Normais (Legítimas)', 1: 'Anômalas (Suspeitas)'})
    print(media_grupo.to_string())
    print("======================================\n")

def preparar_dados(caminho_csv='dados/transacoes.csv', test_size=0.2, random_state=42):
    """
    Carrega o dataset, realiza a separação entre treino/teste e aplica o escalonamento das features.
    
    Retorna:
    - X_train, X_test (features padronizadas)
    - y_train, y_test (labels)
    """
    if not os.path.exists(caminho_csv):
        raise FileNotFoundError(f"Arquivo de dados não encontrado em: '{caminho_csv}'. Execute o gerador de dados primeiro.")
        
    df = pd.read_csv(caminho_csv)
    
    # Exibe a análise exploratória na primeira execução
    analisar_dados(df)
    
    # Separando Features (X) e Target (y)
    X = df.drop(columns=['is_anomalia'])
    y = df['is_anomalia']
    
    # Divisão em Treino e Teste (80% / 20%)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size, random_state=random_state, stratify=y)
    
    # Escalonamento (Padronização) das features numéricas contínuas
    # Deixamos 'dispositivo_novo' fora da padronização por ser binária (0 ou 1)
    colunas_continuas = ['valor', 'hora_dia', 'distancia_habitual']
    
    scaler = StandardScaler()
    
    # Ajusta o scaler com os dados de treino e transforma
    X_train_scaled = X_train.copy()
    X_test_scaled = X_test.copy()
    
    X_train_scaled[colunas_continuas] = scaler.fit_transform(X_train[colunas_continuas])
    X_test_scaled[colunas_continuas] = scaler.transform(X_test[colunas_continuas])
    
    print(f"Dados preparados com sucesso!")
    print(f"Tamanho do conjunto de Treino: {X_train_scaled.shape[0]} amostras")
    print(f"Tamanho do conjunto de Teste: {X_test_scaled.shape[0]} amostras\n")
    
    return X_train_scaled, X_test_scaled, y_train, y_test

if __name__ == "__main__":
    # Teste rápido do script
    X_train, X_test, y_train, y_test = preparar_dados()
    print("Primeiras linhas do conjunto de treino padronizado:")
    print(X_train.head())
