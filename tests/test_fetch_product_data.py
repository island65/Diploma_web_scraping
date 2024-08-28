import unittest

from src.fetch_product_data import FetchData


class TestFetchData(unittest.TestCase):

    def test_get_full_url(self):
        url = 'https://example.com/page/'
        page_num = 5
        expected_result = ['https://example.com/page/1', 'https://example.com/page/2', 'https://example.com/page/3',
                           'https://example.com/page/4', 'https://example.com/page/5']
        self.assertEqual(FetchData.get_full_url(url, page_num), expected_result)

    def test_get_request(self):
        full_url = "https://goldapple.ru/front/api/catalog/products?categoryId=1000000007&cityId=44388ad0-06aa-49b0-bbf9-1704629d1d68&pageNumber=1"

        self.assertIsInstance(FetchData.get_request(full_url), list)

    def test_get_product_common_data(self):
        product = {
            'url': '/19000257262-bois-imperial-refillable-limited-edition',
            'reviews': {'rating': 5},
            'itemId': '19000257262',
            'mainVariantItemId': '19000257262',
            'name': 'Bois imperial refillable limited edition',
            'productType': 'Парфюмерная вода',
            'price': {'actual': {'amount': 100}}}

        data = {'product_url': product['url'],
                'title': product['name'],
                'price': product['price']['actual']['amount'],
                'rating': product.get('reviews', {}).get('rating', None),
                'item_id': product['itemId']}
        self.assertEqual(FetchData.get_product_common_data(product), data)

    def test_save_to_csv(self):
        file_name = 'test.csv'
        products_data = {'product_url': '/19000257262-bois-imperial-refillable-limited-edition', 'title': 'Bois imperial refillable limited edition', 'price': 6881,
                         'rating': 4.2, 'item_id': 19000257262}
        FetchData.save_to_csv(file_name, products_data)
        with open(file_name, mode="r", encoding="utf-8") as csv_file:
            lines = csv_file.readlines()
            self.assertEqual(lines[0].strip(), '/19000257262-bois-imperial-refillable-limited-edition^ Bois imperial refillable limited edition^ 6881^ 4.2^ 19000257262')


if __name__ == '__main__':
    unittest.main()
