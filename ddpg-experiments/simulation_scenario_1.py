# Esse código utiliza a biblioteca stable-baselines3 para criar e treinar um modelo DDPG em um ambiente customizado de IoT.
# ddpg_model.py
import gym
import numpy as np
from stable_baselines3 import DDPG
from stable_baselines3.common.noise import NormalActionNoise
from environment import IoTEnv

# Configuração do ambiente personalizado IoT
env = IoTEnv()

# Definir ruído de ação para DDPG (opcional)
n_actions = env.action_space.shape[-1]
action_noise = NormalActionNoise(mean=np.zeros(n_actions), sigma=0.1 * np.ones(n_actions))

# Criar modelo DDPG
model = DDPG("MlpPolicy", env, action_noise=action_noise, verbose=1)

# Treinar o agente
model.learn(total_timesteps=10000)

# Salvar o modelo treinado
model.save("ddpg_iot_model")
