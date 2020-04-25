class Top_headlines:
    '''
    Top_headlines class to define Top_headlines Objects
    '''
    def __init__(self,source,author,title,description,url,urlToImage,publishedAt,content):
        self.source = source
        self.author = author
        self.title = title
        self.description = description
        self.url = url
        self.urlToImage= urlToImage
        self.publishedAt = publishedAt
        self.content=content