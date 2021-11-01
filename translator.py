from googletrans import Translator
import json


def Translat(fileJson, src='ru', dest='uk'):
    translator = Translator()

    with open(fileJson, encoding='utf-8') as file:
        data = json.load(file)

    for prodId in data:
        product = data[prodId]
        print(f'Обработка {prodId}')

        try:
            product['ОписаниеUA'] = translator.translate(
                product['Описание'], dest, src).text
            product['ИмяUA'] = translator.translate(
                product['Имя'], dest, src).text
            product['ОсобенностиUA'] = translator.translate(
                product['Особенности'], dest, src).text

        except Exception as ex:
            print(ex)
        finally:
            data[prodId] = product

    with open(fileJson, 'w', encoding='utf-8') as file:
        json.dump(data, file, indent=4, ensure_ascii=False)

    pass


if __name__ == '__main__':
    Translat('all_content — копия.json')
