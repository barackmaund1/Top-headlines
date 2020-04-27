import unittest
from app.models import Article



class ArticleTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the Article class
    '''

    def setUp(self):
        '''
        Set up amethod that will run every test
        '''
        self.new_article=Article("Gizmodo.com","Catie Keck",
        'Travelex Reportedly Paid Ransomware Hackers 285 Bitcoin Worth',
        "Following a ransomware attack against foreign exchange company Travelex earlier this year, the company reportedly paid a hefty, multimillion-dollar sum to hackers in the form of hundreds of bitcoin. Read more...",
        "https://gizmodo.com/travelex-reportedly-paid-ransomware-hackers-285-bitcoin-1842782514",
        'https://i.kinja-img.com/gawker-media/image/upload/c_fill,f_auto,fl_progressive,g_center,h_675,pg_1,q_80,w_1200/y7yn0ztcocikqjpfsy9g.jpg',
        "2020-04-09T21:40:00Z",'Following a ransomware attack against foreign exchange company Travelex earlier this year, the company reportedly paid a hefty, multimillion-dollar sum to hackers in the form of hundreds of bitcoin.\r\nCiting a source familiar with the details of the transactio… [+2026 chars]')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_article,Article))   


if __name__ == '__main__':
    unittest.main()        