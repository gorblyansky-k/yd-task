from random import randint, choice
import json
from datetime import datetime

class Operator:
    def __init__(self, full_name, city, birth_date, position, experience):
        self.full_name = full_name
        self.city = city
        self.birth_date = birth_date
        self.position = position
        self.experience = experience

class User:
    def __init__(self, full_name, city, birth_date, position, experience):
        self.full_name = full_name
        self.city = city
        self.birth_date = birth_date
        self.position = position
        self.experience = experience

class Chat:
    def __init__(self, operator, user):
        self.operator = operator
        self.user = user
        self.messages = []
        self.is_closed = False
        self.csat = None

    def add_message(self, text): # генератор таймкода и сообщения
        timestamp = datetime.now().strftime("%Y.%m.%d %H:%M:%S")
        self.messages.append((timestamp, text))

operators = [
    Operator("Александр Иванов", "Москва", "1985.03.12", "Специалист ТП", 5),
    Operator("Екатерина Смирнова", "Санкт-Петербург", "1992.07.24", "Старший специалист ТП", 8),
    Operator("Дмитрий Петров", "Новосибирск", "1978.11.05", "Младший специалист ТП", 12),
    Operator("Анна Козлова", "Екатеринбург", "2000.09.18", "Младший специалист ТП", 1),
    Operator("Иван Федоров", "Нижний Новгород", "1989.04.30", "Младший специалист ТП", 6),
    Operator("Мария Лебедева", "Казань", "1995.12.08", "Старший специалист ТП", 7),
    Operator("Алексей Соколов", "Челябинск", "1973.02.15", "Специалист ТП", 8),
    Operator("Ольга Морозова", "Омск", "1987.06.21", "Старший специалист ТП", 2),
    Operator("Сергей Новиков", "Самара", "1998.10.03", "Специалист ТП", 10),
    Operator("Елена Кузнецова", "Ростов-на-Дону", "1982.08.27", "Специалист ТП", 11)
]

users = [
    User("Екатерина Павловна", "Москва", "1995.03.10", "Повар", 12),
    User("Егор Беленов", "Керчь", "1992.11.25", "Учитель", 24),
    User("Кристина Тарасенко", "Евпатория", "1990.01.24", "Космонавт", 10),
    User("Адриан Комаров", "Пермь", "2000.05.05", "Рыбак", 30),
    User("Максим Грач", "Севастополь", "2002.08.09", "Таксист", 5),
    User("Евгений Абонентов", "Симферополь", "1999.01.10", "Танкист", 36),
    User("Анна Соловьёва", "Судак", "1989.12.24", "Шахтёр", 10),
    User("Марина Нечипоренко", "Екатеринбург", "1995.11.15", "Продавец", 4),
    User("Елена Нечитайло", "Ялта", "1998.07.01", "Тренер", 50),
    User("Тарас Панасенко", "Краснодар", "1981.10.10", "Слесарь", 11)
]

messages = [
    "Уточните, пожалуйста, чем я могу вам помочь?",
    "У меня произошла проблема",
    "Спасибо за помощь!",
    "Пришлите, пожалуйста, скриншот ошибки",
    "Секунду",
    "Я жду вашего ответа",
    "Вы не ответили на мой вопрос",
    "Спасибо за понимание"
]

chats = []
for i in range(100): # генерация чатов
    operator = choice(operators)
    user = choice(users)
    chat = Chat(operator, user)

    for m in range(randint(1,5)):
        chat.add_message(choice(messages))

    chat.is_closed = choice([True, False])
    if chat.is_closed == True: # если чат закрыт, csat получит значение
        chat.csat = randint(1, 5)
    chats.append(chat)

# выгрузка всех чатов
def export_all_chats_to_json(chats):
    data = []
    for chat in chats:
        data.append({
            "operator": chat.operator.full_name,
            "user": chat.user.full_name,
            "messages": chat.messages,
            "is_closed": chat.is_closed,
            "csat": chat.csat
            })
    with open("all_chats.json", "w", encoding="utf8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
export_all_chats_to_json(chats)

# выгрузка чатов по выбранному пользователю
def export_chats_by_user(chats, user_name):
    user_chats = [chat for chat in chats if chat.user.full_name == user_name]
    data = []
    for chat in user_chats:
        data.append({
            "operator": chat.operator.full_name,
            "messages": chat.messages,
            "is_closed": chat.is_closed,
            "csat": chat.csat
        })
    with open(f"{user_name}_chats.json", "w", encoding="utf8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
export_chats_by_user(chats, "Евгений Абонентов")

# выгрузка чатов по выбранному оператору
def export_chats_by_operator(chats, operator_name):
    operator_chats = [chat for chat in chats if chat.operator.full_name == operator_name]
    data = []
    for chat in operator_chats:
        data.append({
            "user": chat.user.full_name,
            "messages": chat.messages,
            "is_closed": chat.is_closed,
            "csat": chat.csat
        })
    with open(f"{operator_name}_chats.json", "w", encoding="utf8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
export_chats_by_operator(chats, "Дмитрий Петров")

# выгрузка списка операторов и пользователей
def export_profiles_to_json(operators, users):
    operator_profiles = [{"full_name": operator.full_name,
                          "city": operator.city,
                          "birth_date": operator.birth_date,
                          "position": operator.position,
                          "experience": operator.experience
                          } for operator in operators]
    
    user_profiles = [{"full_name": user.full_name,
                      "city": user.city,
                      "birth_date": user.birth_date,
                      "position": user.position,
                      "experience": user.experience
                      } for user in users]
    
    data = {"operators": operator_profiles, "users": user_profiles}
    with open("profiles.json", "w", encoding="utf8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
export_profiles_to_json(operators, users)
