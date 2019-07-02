import yandex_translator
import sys

detailed_logging = False
try:
    p_param = sys.argv[1]
    if p_param == '-p':
        detailed_logging = True
except IndexError:
    pass

if detailed_logging:
    print 'DETAILED LOGGING ON!'
yandex_translator.__main__.main(detailed_logging)
