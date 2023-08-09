import urllib.parse

from webrequests import WebRequest as WR
from simple_loggers import SimpleLogger

from .selectors import SELECTORS


class RequestFailException(Exception):
    pass


class Article(object):
    def __init__(self, url, selector=None):
        self.url = url
        self.logger = SimpleLogger('Article')
        self._soup = None
        self._selector = selector

    @property
    def soup(self):
        if self._soup is None:
            self.logger.debug(f'>>> parse url: {self.url}')
            try:
                self._soup = WR.get_soup(self.url)
            except Exception as e:
                raise RequestFailException(f'failed to get source code for url: {self.url}')
        return self._soup

    @property
    def selector(self):
        if self._selector is None:
            host = urllib.parse.urlparse(self.url).netloc
            selector = SELECTORS.get(host, {})
            if selector:
                self.logger.debug(f'use selector: {selector}')
            title_selector = selector.get('title', 'title')
            article_selector = selector.get('article', 'body')
            self._selector = dict(title=title_selector, article=article_selector)
        return self._selector

    @property
    def title(self):
        title = self.soup.select_one(self.selector['title'])
        title = title.text.strip() if title else ''
        return title

    @property
    def text(self):
        article = self.soup.select_one(self.selector['article'])
        for child in article.children:
            if child.text.strip():
                yield child.text.strip()

    @property
    def full_text(self):
        return '\n'.join(self.text)

    def __repr__(self):
        return f'Article<title={self.title}>'
    
    __str__ = __repr__


if __name__ == '__main__':
    urls = [
        'https://zhuanlan.zhihu.com/p/631360711',
        'https://mp.weixin.qq.com/s/BYMVKbJIHyuOT-NiWbtiWQ',
        'https://blog.csdn.net/qazplm12_3/article/details/117137596',
        'https://www.seqchina.cn/14424.html',
        'https://www.plob.org/article/19031.html',
    ]
    for url in urls:
        article = Article(url)
        print(article)
        print('title:', article.title)
        print('text:', '\n'.join(list(article.text)[:5]))