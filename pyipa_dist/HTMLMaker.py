# -*- coding: utf-8 -*-

HTML_TEMPLATE='''
<!DOCTYPE html>
<html>
<head>
    <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
    <meta name="viewport" content="width=device-width, user-scalable=no" />
    <title>Distribution page for {{adhocTitle}}</title>
</head>
<body>
    <p>
        <h1>{{adhocTitle}} {{adhocShortVersion}}</h1>
    </p>
    <p>
        Please
        <a href="itms-services://?action=download-manifest&url={{adhocPlistUrl}}">
            click this link to install
        </a>
    </p>
</body>
</html>
'''

from pyipa import IPAparser
from jinja2 import Template

class HTMLMaker(object):
    def __init__(self, ipaFilePath):
        self.__parser = IPAparser(ipaFilePath)
        self.__ipaInfo = self.__parser.parseInfo()
        self.__adhocShortVersion = self.__ipaInfo["CFBundleShortVersionString"]

    def makeHtml(self, parameters):
        t = Template(HTML_TEMPLATE)
        html = t.render(adhocTitle=parameters["adhoc_title"],
                        adhocPlistUrl=parameters["adhoc_plist_url"],
                        adhocShortVersion=self.__adhocShortVersion)
        return html