# TODO Найдите количество книг, которое можно разместить на дискете
volume_disk = 1.44 #Объем диска Мб
count_of_page = 100 #Количество страниц в книге
count_of_lines = 50 #Число строк на странице
count_of_symb = 25 #Количество символов в строке
weight_symb = 4 #Вес 1 символа в байтах

weight_book_b = count_of_symb*count_of_lines*count_of_page*weight_symb #Вес книги в б
weight_book_mb = weight_book_b/(1024*1024) #Вес книги в Мб

count_of_book = int(volume_disk // weight_book_mb) #Записываем кол-во в целочисленном значении
print("Количество книг, помещающихся на дискету:", count_of_book)
