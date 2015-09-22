#!/usr/bin/python

#!/usr/bin/env python
#coding=utf8

import httplib, urllib


def main():
    httpClient = None
    try:
    #https://api.weibo.com/oauth2/access_token?client_id=YOUR_CLIENT_ID&client_secret=YOUR_CLIENT_SECRET&grant_type=authorization_code&redirect_uri=YOUR_REGISTERED_REDIRECT_URI&code=CODE
        params = urllib.urlencode({'client_id=': 'tom', 'client_secret': 22, 'grant_type':1, "redirect_uri":"none", "code":1})
        headers = {"Content-type": "application/x-www-form-urlencoded", "Accept": "text/plain"}
        httpClient = httplib.HTTPConnection("https://api.weibo.com", 80, timeout=30)
        httpClient.request("POST", "/oauth2/access_token", params, headers) 
        response = httpClient.getresponse()
        print response.status
        print response.reason
        print response.read()
        print response.getheaders()
    except Exception, e:
        print e
    finally:
        if httpClient:
            httpClient.close()


main()
