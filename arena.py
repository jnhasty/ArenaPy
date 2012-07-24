# -*- coding: utf-8 -*

import requests

API_VERSION = 'v1'
BASE_URL = 'http://are.na/api/%s' % API_VERSION
API_CALLBACK = '?callback=?&depth=extended'

class ArenaPy(object):
    version = '0.1'

    def __init__(self):
        self.base_url = BASE_URL
        self.api_callback = API_CALLBACK

    def make_request(self, url_frag):
        request = requests.get('%s%s' % (self.base_url, url_frag))
        return request.json

    def get_channel(self, identifier, options={}):
        return self.make_request('/channels/%s' % identifier) 

    def get_users_channels(self, id, options={}):
        return self.make_request('/channels?user=%s' % id)

    def get_block(self, id, options={}):
        return self.make_request('/blocks/%s' % id)

    def get_blocks(self, identifier, options={}):
        return self.make_request('/blocks?channel=%s' % identifier)
