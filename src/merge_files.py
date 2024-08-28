import pandas as pd


def merge_files(csv_file1, csv_file2, merged_csv):
    """Функция записывает csv-файлы в 2 датасета, объединяет, нормализует данные и записывает в csv-файл"""
    df1 = pd.read_csv(csv_file1, header=None, delimiter='^', escapechar='\\')
    df2 = pd.read_csv(csv_file2, header=None, delimiter='^', escapechar='\\')
    result = pd.merge(df1, df2, left_on=4, right_on=0)
    result.columns = ['product_url', 'title', 'price', 'rating', 'id', 'id1', 'description', 'instruction', 'country']
    result.drop_duplicates(subset='id1', keep='first')

    result.to_csv(
        merged_csv,
        sep='^',
        columns=['id', 'product_url', 'title', 'price', 'rating', 'description', 'instruction', 'country'],
        index=False)
