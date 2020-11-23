import logging

# logging.error('sss','呜呜呜呜errror')
# logging.debug('sss','呜呜呜呜debug')
# logging.info('sss','呜呜呜呜info')
logging.basicConfig(format='%(asctime)s - %(pathname)s[line:%(lineno)d] ''- %(levelname)s: %(message)s',level=logging.WARNING)
logging.debug('debug 信息')
logging.info('info 信息')
logging.warning('warning 信息')
logging.error('error 信息')
logging.critical('critial 信息')