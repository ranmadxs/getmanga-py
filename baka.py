#!/usr/bin/env python
# -*- coding: utf-8 -*-
from lxml.html import parse
 
 
def get_today_releases():
    url = 'http://www.mangaupdates.com/releases.html'
    root = parse(url).getroot()
    today_rls = root.xpath("//div/div[2]//tr[position()>=2]")
    releases = []
 
    for rls in today_rls:
        releases.append(dict(
            name=rls.xpath("./td[@class='pad']")[0].text_content(),
            # link=rls.xpath("./td[1]/a")[0].get('href'),  # FIXME: Doesn't work when there is not '/a'
            release=rls.xpath("./td[2]")[0].text_content(),
            group=rls.xpath("./td[3]/a")[0].text_content(),
            group_link=rls.xpath("./td[3]/a")[0].get('href'),  # TODO: Process a release with more than one group
            ))
 
    return releases
 
 
def get_yesterday_releases():
    url = 'http://www.mangaupdates.com/releases.html'
    root = parse(url).getroot()
    ayer_rls = root.xpath("//div/div[3]//tr[position()>=2]")
    releases = []
 
    for rls in ayer_rls:
        releases.append(dict(
            name=rls.xpath("./td[@class='pad']")[0].text_content(),
            # link=rls.xpath("./td[1]/a")[0].get('href'),
            release=rls.xpath("./td[2]")[0].text_content(),
            group=rls.xpath("./td[3]/a")[0].text_content(),
            group_link=rls.xpath("./td[3]/a")[0].get('href'),
            ))
 
    return releases
 
 
if __name__ == '__main__':
    import json
    # print(json.dumps(get_yesterday_releases(), indent=2))
    print(json.dumps(get_today_releases(), indent=2))



