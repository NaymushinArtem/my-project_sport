from flask import Flask, request, jsonify

app = Flask(__name__)

# Хранение зарегистрированных участников и соревнований
participants = []
competitions = []

@app.route('/register', methods=['POST'])
def register():
    data = request.json
    participants.append(data)
    return jsonify({"message": "Участник зарегистрирован", "participant": data}), 201

@app.route('/competitions', methods=['POST'])
def create_competition():
    data = request.json
    competitions.append(data)
    return jsonify({"message": "Соревнование создано", "competition": data}), 201

@app.route('/competitions', methods=['GET'])
def get_competitions():
    return jsonify(competitions), 200

@app.route('/participants', methods=['GET'])
def get_participants():
    return jsonify(participants), 200

if __name__ == '__main__':
    app.run(debug=True)

    #Этап 5: Стадия внедрения
Задача 5.1: Подготовка к запуску
Задача 5.2: Обучение пользователей
Задача 5.3: Запуск системы
