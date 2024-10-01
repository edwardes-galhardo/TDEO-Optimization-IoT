# environment.py
import gym
import numpy as np
import pandas as pd

class IoTEnv(gym.Env):
    def __init__(self):
        super(IoTEnv, self).__init__()
        self.action_space = gym.spaces.Discrete(4)  # 4 níveis de potência: 2, 5, 10, 15 mW
        self.observation_space = gym.spaces.Box(low=0, high=1, shape=(5,), dtype=np.float32)  # Supondo 5 métricas
        
        # Carregar os dados simulados
        self.data = pd.read_csv('simulated_scenario_1.csv')
        self.current_step = 0
    
    def reset(self):
        self.current_step = np.random.randint(0, len(self.data))
        return self._next_observation()
    
    def _next_observation(self):
        obs = self.data.iloc[self.current_step][['Success Rate', 'Consumption (mJ)']].values
        return np.array(obs, dtype=np.float32)

    def step(self, action):
        current_power = [2, 5, 10, 15][action]
        metrics = self.data.iloc[self.current_step]
        success_rate = metrics['Success Rate']
        consumption = metrics['Consumption (mJ)']
        
        # Recompensa: equilíbrio entre taxa de sucesso e consumo
        reward = success_rate - (consumption / current_power)
        done = self.current_step >= len(self.data) - 1
        self.current_step += 1
        
        return self._next_observation(), reward, done, {}

    def render(self, mode='human'):
        pass
