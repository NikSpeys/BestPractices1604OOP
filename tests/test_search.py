import pytest
from src.article import Article

@pytest.fixture
def list_article():
    Article.articles = dict()
    Article.insert('test1', 'test1')  # Наполняем хранилище статьями
    Article.insert('test2', 'test2')
    Article.insert('test3', 'test3')
    Article.insert('test4', 'test4')
    Article.insert('test5', 'test5')


def test_searching_3(list_article):
    """ Тестирование поиска статьи по ID"""
    searchable_article = Article.search(3)  # 3 - это поисковой номер статьи, в контенте это 'test3'
    return searchable_article == 'test3'


def test_searching_4(list_article):
    """ Тестирование поиска статьи по ID"""
    searchable_article = Article.search(4)  # 3 - это поисковой номер статьи, в контенте это 'test3'
    return searchable_article == 'test4'


