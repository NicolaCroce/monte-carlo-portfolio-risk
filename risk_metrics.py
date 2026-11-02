from typing import Dict
import numpy as np

def calculate_risk_metrics(
    portfolio_values: np.ndarray,
    portfolio_returns: np.ndarray,
    initial_value: float,
    confidence_level: float
) -> Dict[str, float]:
    """
    Calcula el Value at Risk (VaR) y el Conditional Value at Risk (CVaR / Expected Shortfall)
    a partir de los resultados de la simulación Monte Carlo.
    
    Args:
        portfolio_values (np.ndarray): Valores monetarios finales simulados del portafolio.
        portfolio_returns (np.ndarray): Retornos porcentuales simulados del portafolio.
        initial_value (float): Valor inicial del portafolio.
        confidence_level (float): Nivel de confianza (ej. 0.95 para 95%).
        
    Returns:
        Dict[str, float]: Diccionario con las métricas de riesgo en porcentaje y dólares.
    """
    # 1. Cálculo del PnL monetario (Ganancia/Pérdida absoluta)
    pnl_monetary = portfolio_values - initial_value
    
    # 2. Determinación del percentil crítico (alpha) según el nivel de confianza
    # Ejemplo: Para un 95% de confianza, alpha es 0.05 (la cola izquierda de pérdidas)
    alpha = 1.0 - confidence_level
    
    # Percentiles para los retornos y el PnL
    var_return = np.percentile(portfolio_returns, alpha * 100)
    var_monetary = np.percentile(pnl_monetary, alpha * 100)
    
    # Expresamos el VaR como una pérdida positiva (magnitud del riesgo)
    var_loss_pct = -var_return
    var_loss_monetary = -var_monetary
    
    # 3. Cálculo del CVaR (Expected Shortfall)
    # Es la pérdida promedio en el peor (1 - confidence_level)% de los escenarios (riesgo de cola)
    tail_losses_returns = portfolio_returns[portfolio_returns <= var_return]
    tail_losses_monetary = pnl_monetary[pnl_monetary <= var_monetary]
    
    cvar_return = np.mean(tail_losses_returns) if len(tail_losses_returns) > 0 else var_return
    cvar_monetary = np.mean(tail_losses_monetary) if len(tail_losses_monetary) > 0 else var_monetary
    
    cvar_loss_pct = -cvar_return
    cvar_loss_monetary = -cvar_monetary
    
    # 4. Consolidar resultados en un diccionario estructurado
    metrics = {
        "confidence_level": confidence_level,
        "var_pct": var_loss_pct,
        "var_monetary": var_loss_monetary,
        "cvar_pct": cvar_loss_pct,
        "cvar_monetary": cvar_loss_monetary
    }
    
    print(f"[INFO] Métricas de riesgo calculadas con éxito (VaR {confidence_level*100:.0f}% y CVaR).")
    return metrics