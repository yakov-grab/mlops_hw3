from sklearn.metrics import mean_squared_error
import numpy as np
import joblib

# Загрузка тестовых данных
test_data = np.loadtxt("test/data.csv", delimiter=",")

# Загрузка обученной модели
model = joblib.load("trained_model.pkl")

# Предсказание на тестовых данных
X_test = test_data[:, :-1]
y_test = test_data[:, -1]
y_pred = model.predict(X_test)

# Оценка модели
mse = mean_squared_error(y_test, y_pred)
print("Mean Squared Error:", mse)
