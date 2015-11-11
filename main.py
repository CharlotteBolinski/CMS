__author__ = 'Lola'

from crawler import Crawler
from pageRank import pageRank

#seeds
url_list = ['http://people.f4.htw-berlin.de/fileadmin/user_upload/Dozenten/WI-Dozenten/Classen/DAWeb/smdocs/d01.html']
url_list.append('http://people.f4.htw-berlin.de/fileadmin/user_upload/Dozenten/WI-Dozenten/Classen/DAWeb/smdocs/d06.html')
url_list.append('http://people.f4.htw-berlin.de/fileadmin/user_upload/Dozenten/WI-Dozenten/Classen/DAWeb/smdocs/d08.html')

crawl = Crawler(url_list)

def activate_crawl():

    if crawl.crawl_complete:
        print('website crawl complete')

    else:
        crawl.downloader()
        crawl.parser()
        crawl.frontier()

        #crawl feedback
        print('link temporary:\t\t', sorted(crawl.link_temporary))
        print('link set:\t\t\t', sorted(crawl.link_set))
        print('page_rank_graph:\t', crawl.page_rank_graph)
        print('not crawled:\t\t',crawl.url_seed)
        print('NEW RUN ++++++++++++++++++++++++++++++++++++++')

        activate_crawl()

activate_crawl()

page_rank = pageRank(crawl.page_rank_graph)
print(page_rank.returnGraph())
print('number_of_sites:\t\t', page_rank.calc_number_of_sites())