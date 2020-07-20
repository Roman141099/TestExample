while True:
    confPath = str(input('Provide name of configuration file : \n'))
    textPath = str(input('Provide name of text file : \n'))
    uniqueS = {}
    try:
        with open('Output', 'w', encoding='UTF-8') as outPut, \
                open(confPath, 'r', encoding='UTF-8') as fileConfig, \
                open(textPath, 'r', encoding='UTF-8') as fileText:
            for line in fileConfig:
                # Разбиение строки на массив из 2-х элементов, разделенных '='
                splitted = line.split('=')
                # Добавление в словарь ключа и значения, 0 и 1 индекса массива соответственно
                uniqueS[splitted[0]] = splitted[1].strip()
            sampleText = ''.join([line for line in fileText])
            for k, v in uniqueS.items():
                sampleText = sampleText.replace(k, v)
            outPut.write(sampleText)
    except FileNotFoundError as e:
        print(e)
        continue
    else:
        print('OK')
