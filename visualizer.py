import os
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

def plot_monte_carlo_results(
    portfolio_values: np.ndarray,
    initial_value: float,
    metrics: dict,
    output_dir: str = "outputs"
) -> None:
    """
    Genera y guarda un gráfico ejecutivo de la distribución de valores del portafolio
    simulados por Monte Carlo, destacando los umbrales de VaR y CVaR.
    """
    # Asegurar que la carpeta de salidas exista
    os.makedirs(output_dir, exist_ok=True)
    
    # Configuración de estilo visual corporativo
    sns.set_theme(style="whitegrid")
    plt.figure(figsize=(12, 7))
    
    # Histograma de densidades de los valores finales
    sns.histplot(
        portfolio_values, 
        bins=100, 
        kde=True, 
        color="royalblue", 
        stat="density", 
        alpha=0.6,
        label="Simulaciones Monte Carlo"
    )
    
    # Líneas de referencia para el valor inicial, VaR y CVaR
    var_val = initial_value - metrics["var_monetary"]
    cvar_val = initial_value - metrics["cvar_monetary"]
    conf_pct = int(metrics["confidence_level"] * 100)
    
    plt.axvline(initial_value, color="black", linestyle="--", linewidth=1.5, label=f"Valor Inicial (${initial_value:,.2f})")
    plt.axvline(var_val, color="darkorange", linestyle="-.", linewidth=2, label=f"VaR {conf_pct}% (${metrics['var_monetary']:,.2f})")
    plt.axvline(cvar_val, color="firebrick", linestyle="-", linewidth=2.5, label=f"CVaR / Expected Shortfall (${metrics['cvar_monetary']:,.2f})")
    
    # Títulos y etiquetas corporativas
    plt.title(f"Simulación Monte Carlo: Distribución de Riesgo de Portafolio (Horizonte a 10 Días)", fontsize=14, fontweight="bold", pad=15)
    plt.xlabel("Valor Final del Portafolio ($ USD)", fontsize=11, labelpad=10)
    plt.ylabel("Densidad de Probabilidad", fontsize=11, labelpad=10)
    plt.legend(loc="upper left", frameon=True, facecolor="white", framealpha=0.9, fontsize=10)
    
    # Guardar la figura
    output_path = os.path.join(output_dir, "monte_carlo_var_cvar.png")
    plt.tight_layout()
    plt.savefig(output_path, dpi=300)
    plt.close()
    
    print(f"[INFO] Gráfico de riesgo guardado con éxito en: {output_path}")