__author__ = 'Lola'

class pageRank(object):

    teleportation = 0.05
    distance = 0.95
    delta = 0.04

    number_of_sites = 0

    page_rank_graph_back = {}

    def __init__(self, page_rank_graph):
        self.page_rank_graph = page_rank_graph

    def returnGraph(self):
        return self.page_rank_graph

    def calc_number_of_sites(self):
        #Berechne Anzahl von keys in page_rank_graph
        return len(self.page_rank_graph)

    def back_graph(self):
        #for loop page_rank_graph
        #suche in den arrays des dictionaries nach keys des Dictionaries suchen
        #und so back graph erstellen

