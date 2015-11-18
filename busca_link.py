# -*- coding: utf-8 -*-
"""
Created on Wed Nov 18 10:18:46 2015

@author: papacheco
"""

import requests
import re
try:
    from urllib.parse import urljoin
except ImportError:
    from urlparse import urljoin

# regex
email_re = re.compile(r'([\w\.,]+@[\w\.,]+\.\w+)')
link_re = re.compile(r'href="(.*?)"')


def crawl(url):

    result = set()

    req = requests.get(url)

    # Verifica se está ok
    if(req.status_code != 200):
        return []

    # Busca links
    links = link_re.findall(req.text)

    print("\nFound {} links".format(len(links)))

    # Busca por emails
    for link in links:

        # Obtem uma URL absoluta para um link
        link = urljoin(url, link)

        # Busca todos os links da pagina
        result.update(email_re.findall(req.text))

    return result

if __name__ == '__main__':
    emails = crawl('http://www.qualquerst.com.br/')

    print("\nScrapped e-mail addresses:")
    for email in emails:
        print(email)
    print("\n")