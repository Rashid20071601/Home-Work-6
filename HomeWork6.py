# 1
immutable_var = 1, 2, 3, 'str', True, [5, 8, 'string', False]
print(immutable_var)

# 2
# immutable_var[0] = 0
# Изменить значение элемента кортежа не выходит, потому что кортеж неизменяемый тип данных, но я могу изменить список внутри кортежа, т.к. Кортеж поддерживает в себе изменяемы типы данных

# 3
mutable_list = [5, 8, 'string', False]
print(mutable_list)
mutable_list[2] = 'Rashid'
print(mutable_list)