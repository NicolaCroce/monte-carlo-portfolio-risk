from typing import Tuple
import numpy as np
import pandas as pd

def run_monte_carlo_simulation(
    mean_returns: pd.Series,
    cov_matrix: pd.DataFrame,
    weights: np.ndarray,
    initial_value: float,
    num_simulations: int,
    horizon_days: int
) -> Tuple[np.ndarray, np.ndarray]:
    """
    Ejecuta una simulación Monte Carlo utilizando la descomposición de Cholesky
    para proyectar el valor y los retornos de un portafolio a un horizonte temporal dado.
    
    Args:
        mean_returns (pd.Series): Retornos medios diarios de los activos.
        cov_matrix (pd.DataFrame): Matriz de covarianza diaria de los activos.
        weights (np.ndarray): Ponderaciones del portafolio (deben sumar 1.0).
        initial_value (float): Valor inicial del portafolio en USD.
        num_simulations (int): Número de caminos estocásticos a simular.
        horizon_days (int): Horizonte temporal de riesgo en días hábiles.
        
    Returns:
        Tuple[np.ndarray, np.ndarray]: 
            - portfolio_values: Valor monetario final del portafolio para cada simulación.
            - portfolio_returns: Retorno porcentual del portafolio en el horizonte para cada simulación.
    """
    num_assets = len(weights)
    
    # 1. Escalado al horizonte temporal (asumiendo independencia temporal i.i.d.)
    # Retorno esperado acumulado a H días y matriz de covarianza escalada a H días
    expected_horizon_return = mean_returns.values * horizon_days
    horizon_cov_matrix = cov_matrix.values * horizon_days
    
    # 2. Descomposición de Cholesky (L * L^T = Cov)
    # Permite transformar choques aleatorios independientes en choques correlacionados
    try:
        chol_matrix = np.linalg.cholesky(horizon_cov_matrix)
    except np.linalg.LinAlgError:
        # En caso numérico de matriz no perfectamente definida positiva, aplicamos regularización leve
        print("[WARN] Matriz no definida positiva exacta. Aplicando regularización...")
        reg_cov = horizon_cov_matrix + np.eye(num_assets) * 1e-8
        chol_matrix = np.linalg.cholesky(reg_cov)
        
    # 3. Generación de números aleatorios estándar normales Z ~ N(0, I)
    # Forma: (num_assets, num_simulations)
    np.random.seed(42)  # Semilla fija para reproducibilidad en auditorías técnicas
    Z = np.random.normal(loc=0.0, scale=1.0, size=(num_assets, num_simulations))
    
    # 4. Construcción de retornos correlacionados para el horizonte
    # X = Drift + (Cholesky * Z)
    correlated_asset_returns = expected_horizon_return[:, np.newaxis] + np.dot(chol_matrix, Z)
    
    # 5. Cálculo del retorno global del portafolio por cada simulación (producto escalar)
    # weights shape: (num_assets,), correlated_asset_returns shape: (num_assets, num_simulations)
    portfolio_returns = np.dot(weights, correlated_asset_returns)
    
    # 6. Conversión a valor monetario final del portafolio
    portfolio_values = initial_value * (1 + portfolio_returns)
    
    print(f"[INFO] Simulación Monte Carlo ejecutada con éxito: {num_simulations:,} caminos simulados a {horizon_days} días.")
    return portfolio_values, portfolio_returns