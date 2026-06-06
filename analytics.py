import pandas as pd
import numpy as np

def generate_mock_data():
    """Generates synthetic supply chain data for testing."""
    np.random.seed(42)
    dates = pd.date_range(start="2026-01-01", periods=200, freq='D')
    
    # Standard normal distribution of shipping costs
    base_costs = np.random.normal(loc=500, scale=50, size=200)
    df = pd.DataFrame({'Date': dates, 'Shipping_Cost': base_costs})
    
    # Inject deliberate anomalies (simulating real-world supply chain shocks)
    df.loc[45, 'Shipping_Cost'] = 1200.0  # Massive spike
    df.loc[120, 'Shipping_Cost'] = 45.0   # Massive drop
    return df

def find_anomalies(df):
    """Uses numpy vectors to calculate Z-scores and isolate anomalies."""
    costs = df['Shipping_Cost'].to_numpy()
    mean = np.mean(costs)
    std = np.std(costs)
    
    # Mathematical calculation of Z-Scores: Z = (X - μ) / σ
    z_scores = (costs - mean) / std
    
    df['Z_Score'] = z_scores
    # Flag anything 3 standard deviations away from the mean
    anomalies = df[np.abs(df['Z_Score']) > 3]
    return anomalies.to_dict(orient='records')

if __name__ == "__main__":
    data = generate_mock_data()
    print("Anomalies Found:\n", find_anomalies(data))