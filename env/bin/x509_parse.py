#!/home/argen/PycharmProjects/Social_Network/env/bin/python
# EASY-INSTALL-ENTRY-SCRIPT: 'x509==0.1','console_scripts','x509_parse.py'
__requires__ = 'x509==0.1'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('x509==0.1', 'console_scripts', 'x509_parse.py')()
    )
