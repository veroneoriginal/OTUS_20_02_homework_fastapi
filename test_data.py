# Данные, чтобы все проверить через отправку запроса в Swagger

# Высокий риск (ожидаем 1)
predict_data = {
    "Pregnancies": 2,
    "Glucose": 140,
    "BMI": 35.5,
    "Age": 32
}

# Низкий риск (ожидаем 0)
predict_data_1 = {
    "Pregnancies": 0,
    "Glucose": 85,
    "BMI": 22.5,
    "Age": 25
}

# Пограничное значение
predict_data_2 = {
    "Pregnancies": 2,
    "Glucose": 140,
    "BMI": 30.0,
    "Age": 35
}
