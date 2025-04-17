import pytest

from src.article import Article

@pytest.fixture
def one_article():
    Article.articles = dict()
    return Article.insert('test', 'test')


@pytest.fixture
def two_article():
    Article.articles = dict()
    Article.insert('test', 'test')
    assert Article.insert('test', 'test')

def test_insert(one_article):
    """ Тест для проверки, что количество статей равно еденице"""
    assert len(one_article.articles) == 1


def test_article_id(one_article):
    """ Тест на проверку увеличения ID статьи"""
    assert one_article.article_id == 1


def test_increase_id(two_article):
    """ Тест на проверку увеличения ID статьи"""
    assert two_article.article_id == 2


def test_increase_article_count(two_article):
    """ Тест на увеличение списка статей"""
    assert len(Article.articles) == 2