import os
import matplotlib.pyplot as plt
import seaborn as sns
from preprocessor import preparar_dados
from models import treinar_isolation_forest, avaliar_modelo

def plotar_resultados(X_test, y_test, predicoes, pasta_saida='outputs'):
    """
    Gera gráficos de dispersão mostrando as anomalias detectadas e salva como imagem.
    """
    os.makedirs(pasta_saida, exist_ok=True)
    
    print("=== GERANDO GRÁFICO DE VISUALIZAÇÃO ===")
    
    # Criamos um DataFrame temporário para o plot (revertendo o escalonamento apenas para visualização realista)
    # Mas como X_test aqui já está padronizado, podemos plotar com as escalas originais dos dados se quisermos.
    # Para simplificar, vamos usar as features normalizadas, mas com títulos claros.
    df_plot = X_test.copy()
    df_plot['Gabarito (Real)'] = y_test.map({0: 'Normal', 1: 'Fraude'})
    df_plot['Predição (Modelo)'] = ['Fraude (Detectada)' if p == 1 else 'Normal' for p in predicoes]
    
    # Define o estilo dos gráficos
    sns.set_theme(style="whitegrid")
    fig, axes = plt.subplots(1, 2, figsize=(16, 6))
    
    # Gráfico 1: O que é real (Gabarito)
    sns.scatterplot(
        data=df_plot,
        x='valor',
        y='distancia_habitual',
        hue='Gabarito (Real)',
        palette={'Normal': '#1f77b4', 'Fraude': '#d62728'},
        alpha=0.7,
        ax=axes[0]
    )
    axes[0].set_title('Transações Reais (Gabarito Original)', fontsize=14, fontweight='bold')
    axes[0].set_xlabel('Valor da Transação (Padronizado)', fontsize=12)
    axes[0].set_ylabel('Distância Habitual (Padronizada)', fontsize=12)
    
    # Gráfico 2: O que o modelo previu
    sns.scatterplot(
        data=df_plot,
        x='valor',
        y='distancia_habitual',
        hue='Predição (Modelo)',
        palette={'Normal': '#1f77b4', 'Fraude (Detectada)': '#ff7f0e'},
        alpha=0.7,
        ax=axes[1]
    )
    axes[1].set_title('Transações Detectadas pelo Isolation Forest', fontsize=14, fontweight='bold')
    axes[1].set_xlabel('Valor da Transação (Padronizado)', fontsize=12)
    axes[1].set_ylabel('Distância Habitual (Padronizada)', fontsize=12)
    
    plt.tight_layout()
    caminho_grafico = os.path.join(pasta_saida, 'deteccao_anomalias.png')
    plt.savefig(caminho_grafico, dpi=300)
    plt.close()
    
    print(f"Gráfico de visualização salvo com sucesso em: '{caminho_grafico}'\n")

def executar_pipeline():
    """
    Executa o pipeline completo de ponta a ponta.
    """
    print("==================================================")
    print(" INICIANDO PIPELINE DE DETECÇÃO DE ANOMALIAS ")
    print("==================================================")
    
    # 1. Carregar e preparar os dados (chama a EDA e normalização)
    X_train, X_test, y_train, y_test = preparar_dados()
    
    # 2. Treinar o modelo de Machine Learning (Isolation Forest)
    modelo = treinar_isolation_forest(X_train, contamination=0.03)
    
    # 3. Avaliar o desempenho com os dados de teste
    predicoes, scores = avaliar_modelo(modelo, X_test, y_test)
    
    # 4. Gerar e salvar gráficos
    plotar_resultados(X_test, y_test, predicoes)
    
    print("==================================================")
    print("       PIPELINE CONCLUÍDO COM SUCESSO!            ")
    print("==================================================")

if __name__ == "__main__":
    executar_pipeline()
