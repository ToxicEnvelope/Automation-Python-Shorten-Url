#!/usr/bin/env python
import requests

"""
    [Description]
    main
    - This is the start of our program
"""
def main():

    ENTRY = 'graph.facebook.com/v3.2/nytimes'
    BASE_API = '/feed?access_token='
    TOKEN = 'EAAFrXmPkrJABAFzF6cSHvEP8IZBo9kZAMVXQqbatxPZAZAwGsk6V8Drh1k3bhjc6lVglfsuKdnXwB2xXcpp0dE3D8dCVkTZCtJpNDgz9qTz1uTavJv9P4RmtkV0PK87nPKPYJSgbYbHZCvMdIiuMLXhkDEun0ngevJpo5ZAL6mnYX5AuEZCZAeCXiPWvhq9dflbAZD'
    BASE_URL = 'https://{0}{1}{2}'.format(ENTRY, BASE_API, TOKEN)

    ids = {}
    jsonObj = get_json(BASE_URL)
    idcntr = 0

    while not len(ids).__eq__(500):

        data = jsonObj['data']
        if data == None:
            break

        paging = jsonObj['paging']
        if paging == None:
            break

        nxtpage = paging['next']

        for datum in data:
            idcntr += 1
            id = datum['id']
            ids[id] = idcntr
        jsonObj = get_json(nxtpage)

"""
    [Description]
    get_json
    - This method return a json object given a url
    :param -> url : str - URL to be requested
    :return ->  json object as string
"""
def get_json(url):
    res = requests.get(url)
    if not res.status_code.__eq__(200):
        jsonObj = res.json()
        print('[Error] STATUS CODE {0}\n[STACK] {1}'.format(res.status_code, jsonObj))
        return None
    jsonObj = res.json()
    print('[Info] STATUS CODE {0}\n[STACK] {1}'.format(res.status_code, jsonObj))
    return jsonObj


if __name__ == "__main__":
    main()
