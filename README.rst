
pyipa_dist: a lib for creates plist and html from IPA file
-----------------------------------------------------------

This is a library to easily creates plist and html from IPA file for Adhoc distribution, and also a command line utility to do that

Install
_______

.. code:: sh

    $ pip install pyipa_dist

Usage
-----
::

    Usage:
        pyipa_dist [-d --destUrlPath=<DestinationUrl>] IPA [FILE_OUT_DIR]
        pyipa_dist (-h | --help)
        pyipa_dist --version

    Options:
        -d --destUrlPath=<DestinationUrl> Path is the output files(html, plist, ipa) location in distribution server.
                                          (eg. "https://qa.ncsoft.com/QADeploy/CredentialSDK/20151210/")
        -h --help               Show this screen.
        --version               Show version.



Contribute
__________
- Fork the project on github to start making your changes
- Send pull requests with your bug fixes or features
- Submit and create issues on github
