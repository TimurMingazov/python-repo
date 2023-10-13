users = ['user1', 'user2', 'user3', 'user1', 'user4', 'user2']

# TODO Добавьте словарь и замените в нем нулевые значения статисчикой посещений

visit_users = {"Общее количество": 0, "Уникальные посещения": 0}
full_visit = len(users)
unique_visit = len(set(users))

visit_users["Общее количество"] = full_visit
visit_users["Уникальные посещения"] = unique_visit

print(visit_users)
