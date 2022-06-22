import requests
from bs4 import BeautifulSoup


class A101:
    def __init__(self):

        self.home_page_url = 'https://www.aktuel-katalogu.com/kategori/a101-aktuel'

        html = requests.get(self.home_page_url).content
        self.soup = BeautifulSoup(html, 'html.parser')

    @staticmethod
    def content_page_loader(url):
        html = requests.get(url).content
        soup = BeautifulSoup(html, 'html.parser')

        list1 = soup.find('div', {'class': 'post-single-content box mark-links'}).findAll('p')

        content1 = list1[1].text.split('.')
        content2 = list1[2].text.split('.')
        result = ''

        for item in content1:
            result += item + '.' + '\n'

        for item in content2:
            result += item + '.' + '\n'

        return result

    def home_page_returner(self):
        list1 = self.soup.find_all('a', {'id': 'featured-thumbnail'}, limit=3)

        link = []
        title = []

        for item in list1:
            link.append(item.get('href'))
            title.append(item.get('title'))

        return link, title

    @staticmethod
    def write_the_file(text):
        with open('a101.txt', 'w', encoding='utf-8') as file:
            file.write(text)


class BIM:
    def __init__(self):

        self.home_page_url = 'https://www.aktuel-katalogu.com/kategori/bim-aktuel'

        html = requests.get(self.home_page_url).content
        self.soup = BeautifulSoup(html, 'html.parser')

    @staticmethod
    def content_page_loader(url):
        html = requests.get(url).content
        soup = BeautifulSoup(html, 'html.parser')

        list1 = soup.find('div', {'class': 'post-single-content box mark-links'}).findAll('p')

        content1 = list1[1].text.split('.')
        content2 = list1[2].text.split('.')
        result = ''

        for item in content1:
            result += item + '.' + '\n'

        for item in content2:
            result += item + '.' + '\n'

        return result

    def home_page_returner(self):
        list1 = self.soup.find_all('a', {'id': 'featured-thumbnail'}, limit=3)

        link = []
        title = []

        for item in list1:
            link.append(item.get('href'))
            title.append(item.get('title'))

        return link, title

    @staticmethod
    def write_the_file(text):
        with open('bim.txt', 'w', encoding='utf-8') as file:
            file.write(text)


class SOK:
    def __init__(self):

        self.home_page_url = 'https://www.aktuel-katalogu.com/kategori/sok-aktuel'

        html = requests.get(self.home_page_url).content
        self.soup = BeautifulSoup(html, 'html.parser')

    @staticmethod
    def content_page_loader(url):
        html = requests.get(url).content
        soup = BeautifulSoup(html, 'html.parser')

        list1 = soup.find('div', {'class': 'post-single-content box mark-links'}).findAll('p')

        content1 = list1[1].text.split('.')
        content2 = list1[2].text.split('.')
        result = ''

        for item in content1:
            result += item + '.' + '\n'

        for item in content2:
            result += item + '.' + '\n'

        return result

    def home_page_returner(self):
        list1 = self.soup.find_all('a', {'id': 'featured-thumbnail'}, limit=3)

        link = []
        title = []

        for item in list1:
            link.append(item.get('href'))
            title.append(item.get('title'))

        return link, title

    @staticmethod
    def write_the_file(text):
        with open('sok.txt', 'w', encoding='utf-8') as file:
            file.write(text)
