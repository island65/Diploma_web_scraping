import unittest

from src.get_detailed_info import DetailedInfo


class TestGetDetailedInfo(unittest.TestCase):
    detailed_data = [{'attributes': [{'key': 'тип продукта', 'value': 'диффузоры'},
                                     {'key': 'объём', 'value': '100 мл'}],
                      'content': 'Это описание товара',
                      'subtitle': 'артикул: 19000152495',
                      'text': 'описание',
                      'title': 'IMMERSE FOG',
                      'type': 'Description',
                      'value': 'Description_0'},
                     {'content': 'Это инструкция по применению',
                      'subtitle': '',
                      'text': 'применение',
                      'title': '',
                      'type': 'Text',
                      'value': 'Text_1'},
                     {'content': '',
                      'links': [{'title': 'смотреть каталог бренда', 'url': '/brands/immerse'}],
                      'subtitle': 'Россия',
                      'text': 'о бренде',
                      'title': 'IMMERSE',
                      'type': 'Brand',
                      'value': 'Brand_3'},
                     {'content': 'страна происхождения<br>Россия<br><br>изготовитель:<br>ИП Маркин '
                                 'А.О.<br>Российская Федерация, 109444, МОСКВА Г, УЛ ФЕРГАНСКАЯ, '
                                 'дом 15, корп. 1, кв. 325<br>order@immerse.store<br><br>',
                      'subtitle': '',
                      'text': 'Дополнительная информация',
                      'title': '',
                      'type': 'Text',
                      'value': 'Text_4'}]

    def test_get_item_id(self):
        line = "/19000257262-bois-imperial-refillable-limited-edition"
        self.assertEqual(DetailedInfo.get_item_id(line), "19000257262")

    def test_get_item_url(self):
        item_id = "19000257262"
        self.assertEqual(DetailedInfo.get_item_url(item_id), f"https://goldapple.ru/front/api/catalog/product-card/base?itemId={item_id}&cityId=0c5b2444-70a0-4932-980c-b4dc0d3f02b5&customerGroupId=0")

    def test_get_request_for_detailed_info(self):
        item_url = "https://goldapple.ru/front/api/catalog/product-card/base?itemId=19000257262&cityId=0c5b2444-70a0-4932-980c-b4dc0d3f02b5&customerGroupId=0"

        self.assertIsInstance(DetailedInfo.get_request_for_detailed_info(item_url), list)

    def test_get_description(self):
        detailed_data = self.detailed_data
        self.assertEqual(DetailedInfo.get_description(detailed_data), "Это описание товара")

    def test_get_usage(self):
        detailed_data = self.detailed_data
        self.assertEqual(DetailedInfo.get_usage(detailed_data), "Это инструкция по применению")

    def test_get_country(self):
        detailed_data = self.detailed_data
        self.assertEqual(DetailedInfo.get_country(detailed_data), "Россия")

    def test_details_dict(self):
        item_id = "19000257262"
        description = "Это описание товара"
        usage = "Это инструкция по применению"
        country = "Россия"
        details = DetailedInfo.details_dict(item_id, description, usage, country)
        self.assertIsInstance(details, dict)
        self.assertEqual(details["id"], item_id)
        self.assertEqual(details["description"], description)
        self.assertEqual(details["usage"], usage)
        self.assertEqual(details["country"], country)

    def test_save_to_csv(self):
        file_name = "test_details.csv"
        details_data = {"id": "19000257262", "description": "Описание товара", "usage": "Инструкция по применению", "country": "Страна-производитель"}
        DetailedInfo.save_to_csv(file_name, details_data)
        with open(file_name, "r", encoding="utf-8") as file:
            lines = file.readlines()
            self.assertEqual(lines[0].strip(), f"{details_data['id']}^ {details_data['description']}^ {details_data['usage']}^ {details_data['country']}")


if __name__ == "__main__":
    unittest.main()
