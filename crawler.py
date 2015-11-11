__author__ = 'Sophie-Charlotte'

import urllib.request
from bs4 import BeautifulSoup

class Crawler(object):

    url_seed = []
    url_seed_filenames = []

    link_set = set()

    crawl_complete = False
    page_rank_graph = {}

    content = []
    link_temporary = []
    not_crawled = []

    def __init__(self, url_list):
        self.url_seed = url_list

#Downloader-------------------------------------------------------------
    def downloader(self):

        content_list = []
        self.url_seed_filenames = []


        for url in self.url_seed:
            content_list.append(urllib.request.urlopen(url).read())

            splitted_url = url.split('/')
            page_rank_index = splitted_url[-1]

            self.url_seed_filenames.append(page_rank_index)
            self.page_rank_graph[page_rank_index] = []

        print(content_list)
        self.content = content_list

#Parser-----------------------------------------------------------------
    def parser(self):

        linktags_on_sites = []
        link_temporary = []

        for content in self.content:
            soup = BeautifulSoup(content)
            linktags_on_sites.append(soup.find_all('a'))


        for index, linktags_one_site in enumerate(linktags_on_sites):

            link_graph = []

            for link in linktags_one_site:
                link_temporary.append(link.get('href'))
                link_graph.append(link.get('href'))

            self.page_rank_graph[self.url_seed_filenames[index]] += link_graph

        self.link_temporary = link_temporary


#Frontier---------------------------------------------------------------
    def frontier(self):

        not_crawled = []

        if not self.link_set:
            self.link_set = set(self.link_temporary)

            for link in self.link_temporary:
                not_crawled.append('http://people.f4.htw-berlin.de/fileadmin/user_upload/Dozenten/WI-Dozenten/Classen/DAWeb/smdocs/'+link)


            for first_seed_adress in self.url_seed:
                splitted_url = first_seed_adress.split('/')
                url = splitted_url[-1]

                self.link_set.add(url)

        else:

            for link in self.link_temporary:
                if link not in self.link_set:
                    not_crawled.append('http://people.f4.htw-berlin.de/fileadmin/user_upload/Dozenten/WI-Dozenten/Classen/DAWeb/smdocs/'+link)
                    self.link_set.add(link)

            if not not_crawled:
                self.crawl_complete = True


        self.url_seed = not_crawled