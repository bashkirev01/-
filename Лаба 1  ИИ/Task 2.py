# TODO Найдите количество книг, которое можно разместить на дискете
weight = 1.44
pages = 100
strokes = 50
symbols_ = 25
for_one_symbol = 4

#вес накопителя в байтах
weight_bites = 1.44 * 1024 * 1024

#кол-во байт для одной книги
for_one_boook = pages * strokes * symbols_ * for_one_symbol
books = int(weight_bites // for_one_boook)

print("Количество книг, помещающихся на дискету:", books)
