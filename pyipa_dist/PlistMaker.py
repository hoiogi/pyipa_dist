# -*- coding: utf-8 -*-

PLIST_TEMPLATE='''
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>items</key>
	<array>
		<dict>
			<key>assets</key>
			<array>
				<dict>
					<key>kind</key>
					<string>software-package</string>
					<key>url</key>
					<string>{{ipaUrl}}</string>
				</dict>
			</array>
			<key>metadata</key>
			<dict>
				<key>title</key>
				<string>{{adhocBundleName}} Ver.{{adhocBundleVersion}}</string>
				<key>bundle-version</key>
				<string>{{adhocBundleVersion}}</string>
				<key>kind</key>
				<string>software</string>
				<key>bundle-identifier</key>
				<string>{{adhocBundleIdentifier}}</string>
			</dict>
		</dict>
	</array>
</dict>
</plist>
'''

from pyipa import IPAparser
from jinja2 import Template
from urlparse import urljoin
import os

class PlistMaker(object):
    def __init__(self, ipaFilePath):
        self.__parser = IPAparser(ipaFilePath)
        self.__ipaInfo = self.__parser.parseInfo()

        self.__adhocShortVersion = self.__ipaInfo['CFBundleShortVersionString']
        self.__adhocBundleIdentifier = self.__ipaInfo['CFBundleIdentifier']
        self.__adhocBundleName = self.__ipaInfo['CFBundleName']
        self.__ipaFileName = os.path.splitext(ipaFilePath)[0]

    def makePlist(self, destUrlPath):
        t = Template(PLIST_TEMPLATE)
        plist = t.render(ipaUrl=urljoin(destUrlPath, self.__ipaFileName + '.ipa'),
                         adhocBundleVersion=self.__adhocShortVersion,
                         adhocBundleIdentifier=self.__adhocBundleIdentifier,
                         adhocBundleName=self.__adhocBundleName)
        return plist
