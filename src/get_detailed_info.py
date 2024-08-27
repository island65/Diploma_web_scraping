import os
import re
import requests


class DetailedInfo:
    """Класс для получения детальной информации о товаре"""

    def __init__(self, item_url):
        """Ссылка страницу с детальной информацией о товаре"""
        self.item_url = item_url

    @classmethod
    def get_item_id(cls, csv_file):
        """Возвращает id товара из csv файла"""
        with (open(csv_file, 'r', encoding='utf-8') as file):
            lines = file.readlines()
            item_id_list = []
            for line in lines:
                item_id = re.search(r"\d+", line).group()
                item_id_list.append(item_id)
        return item_id_list

    @classmethod
    def get_item_url(cls, item_id_list):
        """Возвращает список ссылок на страницы с детальной информацией о товаре"""
        item_url_list = []
        for line in item_id_list:
            item_id = re.search(r"\d+", line).group()
            item_url = f"https://goldapple.ru/front/api/catalog/product-card/base?itemId={item_id}&cityId=0c5b2444-70a0-4932-980c-b4dc0d3f02b5&customerGroupId=0"
            item_url_list.append(item_url)
        return item_url_list

    @classmethod
    def get_request_for_detailed_info(cls, item_url):
        """Метод для запроса с сайта информации о каждом товаре -> список словарей"""

        payload = {}
        headers = {
            'Accept': 'application/json, text/plain, */*',
            'Sec-Fetch-Site': 'same-origin',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
            'Sec-Fetch-Mode': 'cors',
            'Host': 'goldapple.ru',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.5 Safari/605.1.15',
            'Connection': 'keep-alive',
            'Sec-Fetch-Dest': 'empty',
            'Cookie': '_ga_QE5MQ8XJJK=GS1.1.1723649086.19.1.1723654967.0.0.0; MCS_SESSID=ad61c82f984e6a594eb0ee7edf6d65bd; section_data_ids=%7B%22geolocation%22%3A1723654962%2C%22adult_goods%22%3A1723654963%2C%22cart%22%3A1723654964%7D; _ym_visorc=b; advcake_track_url=%3D202408120ymAeEGQaUN0jMIWLbPgFjuDVQE5BZagoC%2BIV5mFI5U5yVaZAwzmd91Ri9DogAZHmJ04Pgfwy2Ppsl5ZbJiKrTJp%2FcJHC%2BPZ6Wig2bNx1TXdzIBompqWae4z3464E9lmNzGVq06TYfl2Pk02gJkf9m9%2BUq%2BUTIgqT6NhAAIb0zQ2LSn2obe6Z%2BlgPdTZXvFm6WKrSrAGraUeXbtiLNiSvIxW8P%2B1%2FWWaL80QRWu95juULdl%2FxKiRaVfSkdcNSTJjYjecT%2BtdmfdfoOSBGCFesvAzlvSo511p2E5uvwQO54yPahVsYT8nlMiOxr6pmWDvTpV50DG9nuRiKLiZtxRXE04qlNTrU8lhjjyfFrUhNTCBhoJk%2Fj%2Bb0NV8LOREDst%2FDURQ81YkKrp8XgzdjoryUgqFw2WVkjC%2BDDBI3uBsVbNFkNDHG98IvLmtmwbe24JO7jrDN5jKnc8PZD4SCwWgnbFh9GtUFP1vFpoMRQRTW70aVvSl%2BBLd4brDygo5SHqzSedanv9LGw%2FHaD22UoCa9gP2jeX4hq8byKvuwyE5A7OMXlvRP2JscpZFdTbjiS4D1YEbXwTfzMHWKdivqT7VHgRAhuMNmgJSzmVDTJ4nSi9D4iVNnnMXSCRY%2FfA%2FBTdcmVNLElCiwf0uPzHUAjC9uqGRVgVuLxvLuLkcz%2BIbshC8Akjod0bBwqo%3D; _ga=GA1.1.800260019.1723102720; _gcl_au=1.1.2081473348.1723102720; _gid=GA1.2.1529193665.1723552270; tmr_lvid=fdaef488e743b23b37f6c9f4bee62c2a; tmr_lvidTS=1723102720410; client-store-code=default; ga-lang=ru; tmr_detect=1%7C1723654962838; digi-analytics-sessionId=CtUtb7Jm2FaLVw039IXgr; isAddressConfirmed=true; ga-plp-simple-layout=true; ngenix_jscv_2198e54375cc=cookie_expires=1723655276&bot_profile_check=true&cookie_signature=TKhJZM6d39QdqdaP4D9ZrKLjuMk%3D; domain_sid=9JU1lbYZMOeAacVbpiuWQ%3A1723641140261; _ym_isad=1; _ym_d=1723102720; _ym_uid=1723102720830207345; advcake_session_id=25976154-7d16-78a9-b91a-e2c7e8c8d0db; advcake_track_id=68c0abf5-4d5f-c45e-41ae-fde176ab2af1; directCrm-session=%7B%22deviceGuid%22%3A%22eeea756f-7b83-49b2-a06b-42668ad32380%22%7D; mindboxDeviceUUID=eeea756f-7b83-49b2-a06b-42668ad32380; ga-device-id=WacqeEOwc9CmIeDzjfOGy',
            'traceparent': '00-bb457ead60b7ccf258efa3422e822917-90811b42f8d8a52d-01',
            'x-app-version': '1.47.0',
            'x-gast': '36923682.452567786,36923682.452567786'
        }

        response = requests.request("GET", item_url, headers=headers, data=payload)
        detailed_data = response.json().get("data").get("productDescription")

        return detailed_data

    @classmethod
    def get_description(cls, detailed_data):
        """Метод для получения данных с описанием товара """
        for item in detailed_data:
            for key, value in item.items():
                if value == 'описание':
                    description = item.get("content")
                    description = re.sub(r'[\n<p><br>]', '', description).strip()
                    return description

    @classmethod
    def get_usage(cls, detailed_data):
        """Метод для получения данных с инструкцией по применению"""
        for item in detailed_data:
            for key, value in item.items():
                if value == 'применение':
                    usage = item.get("content")
                    usage = re.sub(r'[\n<p><br>]', '', usage).strip()
                    return usage

    @classmethod
    def get_country(cls, detailed_data):
        """Метод для получения данных о стране-производителе"""
        for item in detailed_data:
            for key, value in item.items():
                if value == 'о бренде':
                    if item.get('subtitle') != '':
                        country = item.get('subtitle')
                        return country
                    else:
                        for dict_item in detailed_data:
                            if 'Дополнительная информация' in dict_item.values():
                                country = re.search(r'страна происхождения<br>(.*?)<br>',
                                                    dict_item['content']).group(1)
                                return country

    @classmethod
    def details_dict(cls, description, usage, country):
        details = {"description": description,
                   "usage": usage,
                   "country": country}
        return details

    @classmethod
    def save_to_csv(cls, file_name, details_data):
        with open(file_name, mode="a", newline="", encoding="utf-8") as csv_file:
            csv_file.write(
                f"Описание продукта: {details_data['description']}; Инструкция по применению: {details_data['usage']}; Страна-производитель: {details_data['country']}\n")

    @classmethod
    def collect_details(cls, csv_products, csv_details):
        item_id_list = cls.get_item_id(csv_products)
        item_url_list = cls.get_item_url(item_id_list)
        for url in item_url_list:
            response = cls.get_request_for_detailed_info(url)
            detailed_data = cls.details_dict(cls.get_description(response), cls.get_usage(response),
                                             cls.get_country(response))
            cls.save_to_csv(csv_details, detailed_data)
