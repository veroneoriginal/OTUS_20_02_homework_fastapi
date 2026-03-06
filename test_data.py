# test_data.py
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

# Данные для пользователей и проверки ролей
# verone@gmail.com / 1234567

verone = {
    "email": "verone@gmail.com",
    "password": "1234567"
}

answer_verone = {
    # pylint: disable=C0301 (line-too-long)
    "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiI1Iiwicm9sZSI6ImFkbWluIiwiZXhwIjoxNzcyODA4MjMwLCJpYXQiOjE3NzI4MDQ2MzB9.Kr8hdSJOHXf-YqwPgqgATksFTtbt38em8cal9-jy0eI",
    "token_type": "bearer",
    "role": "admin",
}

tomi = {
    "email": "tomas_shelbi@gmail.com",
    "password": "123_67"
}
answer_tomi = {
    # pylint: disable=C0301 (line-too-long)
    "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiI2Iiwicm9sZSI6InVzZXIiLCJleHAiOjE3NzI4MzE1MDEsImlhdCI6MTc3MjgyNzkwMX0.HBjIfjrsmg8GdjT-QiQdhBpB4JLyHYQvCX25j2_urKQ",
    "token_type": "bearer",
    "role": "user"
}

new_user ={
    "email": "new_user@gmail.com",
    "password": "string123"
}

login_new_user = {
    "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiI3Iiwicm9sZSI6InVzZXIiLCJleHAiOjE3NzI4MzIxODMsImlhdCI6MTc3MjgyODU4M30.GT3AiioG94p4_fYsaFP29dnSBpHDaFP6IaWIX8iP8Iw",
    "token_type": "bearer",
    "expires_in": 3600,
    "role": "user"
}