import numpy as np
from sklearn.ensemble import IsolationForest
from sklearn.metrics import classification_report, confusion_matrix, roc_auc_score, average_precision_score

def treinar_isolation_forest(X_train, contamination=0.03, random_state=42):
    """
    Treina o modelo Isolation Forest no conjunto de treino.
    Note que o modelo é NÃO SUPERVISIONADO, ou seja, não passamos o y_train no fit!
    
    Parâmetros:
    - X_train: features de treino padronizadas.
    - contamination: proporção esperada de anomalias no dataset.
    """
    print("=== TREINANDO ISOLATION FOREST ===")
    model = IsolationForest(contamination=contamination, random_state=random_state, n_estimators=100)
    model.fit(X_train)
    print("Modelo treinado com sucesso!\n")
    return model

def avaliar_modelo(model, X_test, y_test):
    """
    Avalia o modelo utilizando o conjunto de teste e exibe métricas detalhadas.
    """
    print("=== AVALIAÇÃO DO MODELO ===")
    
    # O Isolation Forest retorna -1 para anomalias e 1 para registros normais
    pred_brutas = model.predict(X_test)
    
    # Precisamos mapear para nosso padrão: 1 para anomalia (fraude) e 0 para normal
    pred_mapeadas = np.where(pred_brutas == -1, 1, 0)
    
    # Também podemos obter os scores de anomalia (quanto menor/mais negativo, mais anômalo)
    # Convertemos para escala positiva onde valores maiores significam maior chance de anomalia
    scores = -model.decision_function(X_test)
    
    # 1. Matriz de Confusão
    print("Matriz de Confusão:")
    cm = confusion_matrix(y_test, pred_mapeadas)
    print(f" Verdadeiros Negativos (Legítimas corretas): {cm[0][0]}")
    print(f" Falsos Positivos (Legítimas marcadas como fraude): {cm[0][1]}")
    print(f" Falsos Negativos (Fraudes não detectadas): {cm[1][0]}")
    print(f" Verdadeiros Positivos (Fraudes detectadas): {cm[1][1]}")
    
    # 2. Relatório de Classificação (Precisão, Recall, F1)
    print("\nRelatório de Classificação:")
    print(classification_report(y_test, pred_mapeadas, target_names=['Normal', 'Anomalia']))
    
    # 3. Métricas de Curvas (ROC-AUC e Average Precision para dados desbalanceados)
    auc_roc = roc_auc_score(y_test, scores)
    auc_pr = average_precision_score(y_test, scores)
    
    print(f"Área sob a Curva ROC (AUC-ROC): {auc_roc:.4f}")
    print(f"Área sob a Curva Precisão-Recall (AUC-PR): {auc_pr:.4f}")
    print("============================\n")
    
    return pred_mapeadas, scores

if __name__ == "__main__":
    # Importação tardia para evitar loops de importação
    from preprocessor import preparar_dados
    
    # 1. Carrega e prepara os dados
    X_train, X_test, y_train, y_test = preparar_dados()
    
    # 2. Treina o Isolation Forest (sabemos que a contaminação é de 3%)
    modelo_if = treinar_isolation_forest(X_train, contamination=0.03)
    
    # 3. Avalia o modelo
    avaliar_modelo(modelo_if, X_test, y_test)
