import os

from dotenv import load_dotenv
from pathlib import Path

from src.fetch_product_data import FetchData
from src.get_detailed_info import DetailedInfo
from src.merge_files import merge_files

load_dotenv()

products_csv = os.getenv('PATH_TO_PRODUCTS')
details_csv = os.getenv('PATH_TO_DETAILS')
merged_csv = os.getenv('PATH_TO_MERGED_FILE')

page_num = 5

url = "https://goldapple.ru/front/api/catalog/products?categoryId=1000000007&cityId=44388ad0-06aa-49b0-bbf9-1704629d1d68&pageNumber="

if __name__ == '__main__':
    full_url = FetchData.get_full_url(url, page_num)  # список ссылок для постраничного вывода

    products = FetchData.fetch_all_data(full_url, Path(products_csv))  # получение общей информации по товарам

    details = DetailedInfo.collect_details(Path(products_csv), Path(details_csv))  # получение детальной информации по товарам

    merged_data = merge_files(Path(products_csv), Path(details_csv), Path(merged_csv))  # файл с объединёнными данными по всем товарам
