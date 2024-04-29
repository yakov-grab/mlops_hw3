from sklearn.preprocessing import StandardScaler
import numpy as np
import os

# Загрузка данных
train_data = np.loadtxt("train/data.csv", delimiter=",")

# Пример предварительной обработки данных
scaler = StandardScaler()
scaled_data = scaler.fit_transform(train_data)

# Сохранение предобработанных данных
os.makedirs("processed_data", exist_ok=True)
np.savetxt("processed_data/train_data_scaled.csv", scaled_data, delimiter=",")
