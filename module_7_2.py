

def custom_write(file_name, strings): # file_name - название файла для записи, strings - список строк для записи.
    file = open(file_name, 'a', encoding = 'utf-8')
    strings_positions = {}
    numder_line = 0

    for string in strings:
        number_byte = file.tell()
        file.write(f'{string}\n')
        numder_line += 1
        strings_positions[numder_line, number_byte] = string
    file.close()

    return strings_positions

info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]

result = custom_write('test.txt', info)
for elem in result.items():
  print(elem)