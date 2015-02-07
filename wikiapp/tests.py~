import unittest
from lxml.html import fromstring, tostring
from pyramid import testing
import HTMLParser
from bs4 import BeautifulSoup

class ViewTests(unittest.TestCase):
    def setUp(self):
        self.config = testing.setUp()

    def tearDown(self):
        testing.tearDown()


    def test_isHTTPURL(self):
        '''
        Method tests the isHTTPURL method in the view class
        '''
        from .views import isHTTPURL
        request = testing.DummyRequest()
        info = isHTTPURL('http://www.java2s.com/Code/Python/String/Comparetwostrings.htm')
        self.assertTrue(info)
        
        
    def test_isWikiURL(self):
        '''
        Method tests the isWikiURL method in the view class
        '''
        from .views import isHTTPURL
        request = testing.DummyRequest()
        info = isHTTPURL('http://en.wikipedia.org/wiki/Dowry')
        self.assertTrue(info)    
       
       
    # Testing the welcome page view callable
    def test_home_view(self):
        from .views import home_view
        request = testing.DummyRequest()
        response = home_view(request)
        self.assertEqual(response['name'], 'Wiki Content Scrapper App')
        
    # Testing the wikiSourceTOCDownloader Method
    def test_wikiSourceTOCDownloader(self):
        '''
        The idea behind this method is to compare the first element in the 
        table of content of the wikipage http://en.wikipedia.org/wiki/Dowry
        with that which is downloaded by wikiSourceTOCDownloader().
        The first element is given by the tag in soup1 variable. The downloaded
        version is stored in the soup2 variable.
        
        The test method basically compares the the <a> tags soup1 and soup2. 
        '''
        from .views import wikiSourceTOCDownloader
        soup1=BeautifulSoup('<a href="#Definition"><span class="tocnumber">1</span> <span class="toctext">Definition</span></a>')
        out=soup1.findAll('a') 
        exp=out[0].text
        info = wikiSourceTOCDownloader('http://en.wikipedia.org/wiki/Dowry')
        h= HTMLParser.HTMLParser().unescape(str(info[0]))
        soup2=BeautifulSoup(h)
        sss= soup2.findAll('a') 
        obtained=sss[0].text
        self.assertEqual(obtained, exp) 
        #self.assertRegexpMatches(obtained,exp)    

        
        
     
        
    
