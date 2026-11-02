from config import TICKERS, WEIGHTS, INITIAL_PORTFOLIO_VALUE, START_DATE, END_DATE, NUM_SIMULATIONS, TIME_HORIZON_DAYS, CONFIDENCE_LEVEL
from data_loader import fetch_market_data, calculate_portfolio_statistics
from monte_carlo import run_monte_carlo_simulation
from risk_metrics import calculate_risk_metrics
from visualizer import plot_monte_carlo_results

def main():
    print("==================================================")
    print(" INICIO DEL MOTOR DE RIESGO: MONTE CARLO PORTFOLIO")
    print("==================================================")
    
    # 1. Ingesta y preparación de datos
    prices_df = fetch_market_data(TICKERS, START_DATE, END_DATE)
    mean_returns, cov_matrix, log_returns = calculate_portfolio_statistics(prices_df)
    
    # 2. Ejecución de la simulación estocástica (Cholesky)
    portfolio_values, portfolio_returns = run_monte_carlo_simulation(
        mean_returns=mean_returns,
        cov_matrix=cov_matrix,
        weights=WEIGHTS,
        initial_value=INITIAL_PORTFOLIO_VALUE,
        num_simulations=NUM_SIMULATIONS,
        horizon_days=TIME_HORIZON_DAYS
    )
    
    # 3. Cálculo de métricas de riesgo (VaR y CVaR)
    risk_results = calculate_risk_metrics(
        portfolio_values=portfolio_values,
        portfolio_returns=portfolio_returns,
        initial_value=INITIAL_PORTFOLIO_VALUE,
        confidence_level=CONFIDENCE_LEVEL
    )
    
    # 4. Mostrar reporte ejecutivo en consola
    print("\n--------------------------------------------------")
    print(f" REPORTE DE RIESGO DE MERCADO ({TIME_HORIZON_DAYS} DÍAS HÁBILES)")
    print("--------------------------------------------------")
    print(f" Valor Inicial del Portafolio : ${INITIAL_PORTFOLIO_VALUE:,.2f}")
    print(f" Nivel de Confianza           : {risk_results['confidence_level']*100:.1f}%")
    print(f" Value at Risk (VaR %)        : {risk_results['var_pct']*100:.2f}%")
    print(f" Value at Risk (VaR USD)      : ${risk_results['var_monetary']:,.2f}")
    print(f" CVaR / Expected Shortfall (%) : {risk_results['cvar_pct']*100:.2f}%")
    print(f" CVaR / Expected Shortfall ($) : ${risk_results['cvar_monetary']:,.2f}")
    print("--------------------------------------------------")
    
    # 5. Generación de gráficos y exportación de salidas
    plot_monte_carlo_results(
        portfolio_values=portfolio_values,
        initial_value=INITIAL_PORTFOLIO_VALUE,
        metrics=risk_results
    )
    print("[INFO] Proceso finalizado con éxito.")

if __name__ == "__main__":
    main()