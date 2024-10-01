# simulation_scenario_1.py
import pandas as pd
import numpy as np

# Simular dados de dispositivos IoT com diferentes potências
def simulate_data(num_devices=5, power_levels=[2, 5, 10, 15]):
    data = []
    for power in power_levels:
        for device in range(1, num_devices + 1):
            sent = np.random.randint(100, 150)
            received = np.random.randint(80, sent)
            success_rate = received / sent
            consumption = power * np.random.uniform(0.5, 1.0)
            data.append([power, device, sent, received, success_rate, consumption])
    
    columns = ['Power (mW)', 'Device ID', 'Sent', 'Received', 'Success Rate', 'Consumption (mJ)']
    df = pd.DataFrame(data, columns=columns)
    return df

# Gerar simulação e salvar em CSV
df = simulate_data()
df.to_csv('simulated_scenario_1.csv', index=False)
print("Simulação salva como 'simulated_scenario_1.csv'")
