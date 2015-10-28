__author__ = 'Sophie-Charlotte'

#imports---------------------------------------------------------------
#standard lib to read and download urls
import urllib.request
from bs4 import BeautifulSoup

#set up----------------------------------------------------------------

#seeds
url_list = ['http://people.f4.htw-berlin.de/fileadmin/user_upload/Dozenten/WI-Dozenten/Classen/DAWeb/smdocs/d01.html']
url_list.append('http://people.f4.htw-berlin.de/fileadmin/user_upload/Dozenten/WI-Dozenten/Classen/DAWeb/smdocs/d06.html')
url_list.append('http://people.f4.htw-berlin.de/fileadmin/user_upload/Dozenten/WI-Dozenten/Classen/DAWeb/smdocs/d08.html')

url_seed = []
link_set = set()

#check if crawl is complete
crawl_complete = False

#main method----------------------------------------------------------------
def main():

    global url_seed
    global crawl_complete

    #rekursive call until there are no urls left to crawl/ the crawl content list is empty
    if crawl_complete:
        print('website crawl complete')
    else:

        #connect all methods
        content_list = downloader(url_seed)
        link_temporary = parser(content_list)
        url_seed = frontier(link_temporary)

        #call main method recursively
        main()

#Downloader-------------------------------------------------------------
#needs known protocol (http/https/ftp...)
#gets data from the frontier
#sends downloaded data to the parser

#Download the url (Fetch Chain)

def downloader(url_seed):

    content_list = []

    #just true on first run, frontier submitted no data
    if not url_seed:
        url_seed = url_list

    #saves url contents in a content_list
    #maybe save everything in one file?
    for url in url_seed:
        content_list.append(urllib.request.urlopen(url).read())

    return content_list


#Parser-----------------------------------------------------------------
#analyses documents
#extraction of links or other information
#structure of the document has to be known!
#sends extracted data to the frontier

#write the document into the file system,
#clear cash, request new url over frontier

def parser(content_list):

    #resetted every time the function is called
    linktags_on_sites = []
    link_temporary = []

    #search content for a tags and the contained link
    for content in content_list:
        #Beautiful Soup object
        soup = BeautifulSoup(content)

        #returns list of a-tags and their content
        linktags_on_sites.append(soup.find_all('a'))

    for linktags_one_site in linktags_on_sites:
        #returns content of hrefs just if link is not already in the set

        for link in linktags_one_site:
            link_temporary.append(link.get('href'))


    return link_temporary

#Frontier---------------------------------------------------------------
#saves crawled urls and urls to be crawled
#sends urls to be crawled to the downloader
#challenge: Use the right data structure to crawl!!

#check if url should be crawled (Candidate Chain)

#ensures that all linked sites are visited and that just once
#...write results in an array and check if entry already exists

def frontier(link_temporary):

    not_crawled = []

    #read global set
    global link_set
    global crawl_complete

    #initialization for first run
    if not link_set:
        link_set = set(link_temporary)

        #add all links from first seed to not_crawled list
        for link in link_temporary:
            not_crawled.append('http://people.f4.htw-berlin.de/fileadmin/user_upload/Dozenten/WI-Dozenten/Classen/DAWeb/smdocs/'+link)

        #add the seed adresses to the set --- remove this for loop to delete seed links from crawl
        for first_seed_adress in url_list:

            #split seed url
            splitted_url = first_seed_adress.split('/')

            #returns last element of the splitted seed url
            url = splitted_url[-1]

            link_set.add(url)
        #---------------------------

    else:
        #compare links in temporary array with set of links (unique link list)
       for link in link_temporary:
           if link not in link_set:
                #print(link)
                not_crawled.append('http://people.f4.htw-berlin.de/fileadmin/user_upload/Dozenten/WI-Dozenten/Classen/DAWeb/smdocs/'+link)
                link_set.add(link)

       #check if crawl is complete, stops recursion if so
       if not not_crawled:
           crawl_complete = True

    #crawl feedback
    print(sorted(link_set))
    print(not_crawled)

    return not_crawled


#Start Program----------------------------------------------------------
main()