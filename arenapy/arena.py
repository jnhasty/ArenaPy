# -*- coding: utf-8 -*

from operator import itemgetter

import requests

API_VERSION = 'v1'
BASE_URL = 'http://are.na/api/%s' % API_VERSION

class ArenaPy(object):
    version = '0.1'

    def __init__(self):
        self.base_url = BASE_URL

    def make_request(self, url_frag):
        '''
        + core request function
        + requires a url fragment
        + returns json data as a dictionary
        '''
        request = requests.get('%s%s' % (self.base_url, url_frag))
        #watch out for bad requests...
        request.raise_for_status()
        return request.json

    ## Basic object requests
    def get_channel(self, channel, options={}):   
        return self.make_request('/channels/%s' % channel) 

    def get_user_channel(self, id, options={}):
        return self.make_request('/channels?user=%s' % id)

    def get_block(self, id, options={}):
        return self.make_request('/blocks/%s' % id)

    def get_blocks_for_channel(self, channel, options={}):
        return self.make_request('/blocks?channel=%s' % channel)

    #######
    ## SORTING, RETRIEVING FUNCTIONS
    #######

    #
    # channel basics
    #
    def get_channel_title(self, channel):
        return channel['title']

    
    #
    # channel channels
    #
    def get_channel_channels(self, channel):
        return channel['channels']

    def get_channel_channels_count(self, channel):
        return len(self.get_channel_channels(channel))

    #
    # channel blocks
    #
    def get_channel_block_count(self, channel):
        return channel['blocks_count']

    def sort_channel_blocks_by_created(self, channel, sort_by = 'desc'):
        '''
        sort a channel's blocks by created timestamp
        sort_by asc or desc, default = desc (newest)
        '''
        if channel.get('blocks'):
            blocks = channel['blocks']
            if sort_by == 'asc':
                blocks = sorted(blocks, key=itemgetter('created_at')) 
            else:
                blocks = sorted(blocks, key=itemgetter('created_at'), reverse=True) 
            channel['blocks'] = blocks
            return channel
        else:
            return None

    def get_channel_images(self, channel):
        if channel.get('blocks'):
            return [block for block in channel['blocks'] if block['block_class'] == 'image']
        else:
            return None

    def get_channel_images_count(self, channel):
        if channel.get('blocks'):
            return len(self.get_channel_images(channel))
        else:
            return None

    def get_channel_media(self, channel):
        if channel.get('blocks'):
            return [block for block in channel['blocks'] if block['block_class'] == 'media']
        else:
            return None

    def get_channel_media_count(self, channel):
        if channel.get('blocks'):
            return len(self.get_channel_media(channel))
        else:
            return None

    def get_channel_text(self, channel):
        if channel.get('blocks'):
            return [block for block in channel['blocks'] if block['block_class'] == 'text']
        else:
            return None

    def get_channel_text_count(self, channel):
        if channel.get('blocks'):
            return len(self.get_channel_text(channel))
        else:
            return None

    def get_channel_links(self, channel):
        if channel.get('blocks'):
            return [block for block in channel['blocks'] if block['block_class'] == 'link']
        else:
            return None

    def get_channel_links(self, channel):
        if channel.get('blocks'):
            return len(self.get_channel_text(channel))
        else:
            return None


    #
    # channel connections
    #
    def get_channel_connections(self, channel):
        '''
        returns all connections in a channel, removes dupes
        '''
        connections = [block['connections'] for block in channel['blocks']]
        flattened = [connection for sublist in connections for connection in sublist]
        seen = set()
        uniques = []
        for f in flattened:
            key = f['channel_id']
            if key not in seen:
                seen.add(key)
                uniques.append(f)
        return uniques

    def get_channel_connections_count(self, channel):
        '''
        returns count of unique connections
        '''
        return len(self.get_channel_connections(channel))
