list_players = ["Маша", "Петя", "Саша", "Оля", "Кирилл", "Коля"]

# TODO Разделите участников на две команды
count_of_players = len(list_players) #Всего игроков
count_half_players = count_of_players // 2 #Число половины игроков

first_half_players = list_players[:count_half_players] #Первая половина игроков
second_half_players = list_players[count_half_players:] #Вторая половина игроков
print(first_half_players)
print(second_half_players)
