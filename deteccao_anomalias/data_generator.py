import os
import numpy as np
import pandas as pd

def gerar_transacoes(n_transacoes=5000, proporcao_anomalias=0.03, random_state=42):
    """
    Gera um dataset sintético de transações bancárias contendo transações normais e anomalias.
    
    Parâmetros:
    - n_transacoes: número total de transações a serem geradas.
    - proporcao_anomalias: percentual de transações que serão anômalas (fraudes).
    - random_state: semente aleatória para reprodutibilidade.
    """
    np.random.seed(random_state)
    
    n_anomalias = int(n_transacoes * proporcao_anomalias)
    n_normais = n_transacoes - n_anomalias
    
    print(f"Gerando {n_transacoes} transações no total...")
    print(f"- Normais: {n_normais}")
    print(f"- Anômalias (Fraudes): {n_anomalias} ({proporcao_anomalias * 100}%)")
    
    # --- 1. GERANDO TRANSAÇÕES NORMAIS ---
    # Valores: a maioria das compras cotidianas (média de 80 reais, variando de forma realista)
    valores_normais = np.random.exponential(scale=80, size=n_normais) + 5
    
    # Horários: distribuídos ao longo do dia (foco em horário comercial, entre 08h e 22h)
    # Vamos gerar horas de 0 a 24 usando distribuição normal centrada às 15h
    horas_normais = np.random.normal(loc=15, scale=4, size=n_normais) % 24
    
    # Distância (km do local de residência): a maioria perto de casa
    distancia_normais = np.random.exponential(scale=10, size=n_normais)
    
    # Novo Dispositivo: probabilidade muito baixa (apenas 2% das vezes é um celular/PC novo)
    dispositivo_novo_normais = np.random.choice([0, 1], size=n_normais, p=[0.98, 0.02])
    
    # Labels
    labels_normais = np.zeros(n_normais, dtype=int)
    
    # --- 2. GERANDO TRANSAÇÕES ANÔMALAS ---
    # Valores: tipicamente muito mais altos (valores extremos)
    valores_anomalias = np.random.normal(loc=1500, scale=400, size=n_anomalias)
    valores_anomalias = np.clip(valores_anomalias, 100, None) # garante valor mínimo de R$ 100
    
    # Horários: concentrados na madrugada (entre 00h e 06h)
    horas_anomalias = np.random.normal(loc=3, scale=1.5, size=n_anomalias) % 24
    
    # Distância: compras feitas muito longe do local de residência habitual
    distancia_anomalias = np.random.normal(loc=350, scale=100, size=n_anomalias)
    distancia_anomalias = np.clip(distancia_anomalias, 50, None)
    
    # Novo Dispositivo: probabilidade muito alta para fraudes (75% das vezes é um novo aparelho)
    dispositivo_novo_anomalias = np.random.choice([0, 1], size=n_anomalias, p=[0.25, 0.75])
    
    # Labels
    labels_anomalias = np.ones(n_anomalias, dtype=int)
    
    # --- 3. CONCATENANDO E CRIANDO O DATAFRAME ---
    df_normais = pd.DataFrame({
        'valor': valores_normais,
        'hora_dia': horas_normais,
        'distancia_habitual': distancia_normais,
        'dispositivo_novo': dispositivo_novo_normais,
        'is_anomalia': labels_normais
    })
    
    df_anomalias = pd.DataFrame({
        'valor': valores_anomalias,
        'hora_dia': horas_anomalias,
        'distancia_habitual': distancia_anomalias,
        'dispositivo_novo': dispositivo_novo_anomalias,
        'is_anomalia': labels_anomalias
    })
    
    df_final = pd.concat([df_normais, df_anomalias], ignore_index=True)
    
    # Embaralha os dados para que as fraudes fiquem misturadas
    df_final = df_final.sample(frac=1, random_state=random_state).reset_index(drop=True)
    
    return df_final

if __name__ == "__main__":
    # Garante que a pasta 'dados' existe
    os.makedirs('dados', exist_ok=True)
    
    # Gera os dados
    df = gerar_transacoes(n_transacoes=5000, proporcao_anomalias=0.03)
    
    # Salva em CSV
    caminho_csv = os.path.join('dados', 'transacoes.csv')
    df.to_csv(caminho_csv, index=False)
    print(f"\nSucesso! Dataset salvo em: '{caminho_csv}'")
    print(df.head())
