#!/usr/bin/env python

import re
import yaml
import urllib
import urllib2

class WikiError(Exception):
    pass

class Wiki:
    
    def __init__(self, lang):
        self.lang = lang
    
    def __fetch(self, url):
        request = urllib2.Request(url)
        request.add_header('User-Agent', 'Mozilla/5.0')
        
        try:
            result = urllib2.urlopen(request)
        except urllib2.HTTPError, e:
            raise WikipediaError(e.code)
        except urllib2.URLError, e:
            raise WikipediaError(e.reason)
        
        return result
    
    def article(self, url):
        content = self.__fetch(url).read()
        
        if content.upper().startswith('#REDIRECT'):
            match = re.match('(?i)#REDIRECT \[\[([^\[\]]+)\]\]', content)
            
            if not match == None:
                return self.article(match.group(1))
            
            raise WikiError('Can\'t found redirect article.')
        
        return content
    
