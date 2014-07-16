# Scraper for Texas 4th Court of Appeals
#CourtID: texapp4
#Court Short Name: TX
#Author: Andrei Chelaru
#Reviewer: mlr
#Date: 2014-07-10


from juriscraper.opinions.united_states.state import tex


class Site(tex.Site):
    def __init__(self):
        super(Site, self).__init__()
        self.court_id = self.__module__
        self.court_name = 'capp_4'
