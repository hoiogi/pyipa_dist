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
        <h1>{{adhocBundleName}} Ver.{{adhocShortVersion}} ({{adhocBundleVersion}})</h1>
    </p>
    <p>
        Please
        <a href="itms-services://?action=download-manifest&url={{adhocPlistUrl}}">
            click this link to install
        </a>
    </p>
    <p align=center>
        <br><br><br><br><br><br><br><br><br>
        made by <a href="https://github.com/hoiogi/pyipa_dist">pyipa_dist</a>
    </p>
</body>
</html>
'''

from pyipa import IPAparser
from jinja2 import Template
import os
from urlparse import urljoin

class HTMLMaker(object):
    def __init__(self, ipaFilePath):
        self.__parser = IPAparser(ipaFilePath)
        self.__ipaInfo = self.__parser.parseInfo()

        self.__adhocBundleName = self.__ipaInfo['CFBundleName']
        self.__adhocShortVersion = self.__ipaInfo['CFBundleShortVersionString']
        self.__adhocBundleVersion = self.__ipaInfo['CFBundleVersion']
        self.__ipaFileName = os.path.splitext(ipaFilePath)[0]

    def makeHtml(self, destUrlPath):
        t = Template(HTML_TEMPLATE)
        html = t.render(adhocBundleName=self.__adhocBundleName,
                        adhocShortVersion=self.__adhocShortVersion,
                        adhocBundleVersion=self.__adhocBundleVersion,
                        adhocPlistUrl=urljoin(destUrlPath, self.__ipaFileName + '.plist'),
                        )
        return html