class Article:
    """Класс для хранения статьи"""
    article_id: int
    title: str  # заголовок
    content: str  # содержимое статьи

    articles = dict()  # атрибут на уровне класса для хранения всех статей

    def __init__(self, title: str, content: str):
        """Конструктор для статьи """
        self.article_id = self.get_new_id()
        self.title = title
        self.content = content


    def get_new_id(self) -> int:
        """Метод дл получения ID следующей статьи"""
        if len(self.articles) > 0:
            return max(self.articles.keys()) + 1  # проверяем, если в словарь добавился тайтл, то добавляем ему 1 ед ID
        return 1  # возвращаем ID 1ого тайтла


    @classmethod
    def insert(cls, title: str, content: str):
        """ Метод для создания и добавления статьи"""
        new_article = cls(title, content)
        cls.articles[new_article.article_id] = new_article
        # через [] обращаемся к словарю, создается новая статься,
        # создается новый ID
        return new_article

    @classmethod
    def search(cls, article_id):
        """ Метод для поиска статьи по ID"""
        return cls.articles[article_id]

if __name__ == '__main__':
    new_article_1 = Article.insert('test1', 'test1')
    print(new_article_1.article_id)  # вывоз 1ого тайтла

    new_article_2 = Article.insert('test2', 'test2')
    print(new_article_2.article_id)  # вывоз 1ого тайтла
