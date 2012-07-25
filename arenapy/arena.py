# -*- coding: utf-8 -*

from operator import itemgetter

import requests

API_VERSION = 'v1'
BASE_URL = 'http://are.na/api/%s' % API_VERSION

class ArenaPy(object):
    version = '0.1'

    def __init__(self):
        self.base_url = BASE_URL

    def make_request(self, url_frag, options={}):
        '''
        + core request function
        + requires a url fragment
        + returns json data as a dictionary
        '''
        request = requests.get('%s%s' % (self.base_url, url_frag), params=options)
        #watch out for bad requests...
        request.raise_for_status()
        return request.json
    
    #######
    ## Basic object requests, all return dictionaries
    #######
    def get_channel(self, channel):   
        '''
        + returns a channel dict:
            username, channels, slug, user_id, memberships,
            blocks_count, title, type, created_at, last_block_updated_at,
            updated_at, collaboration, channel_type, avatar, published,
            blocks, open, id, user_url
        
        + no params available
        '''
        return self.make_request('/channels/%s' % channel) 

    def get_blocks_for_channel(self, channel, options={}):
        '''
        + returns a dictionary: blocks, page, per, channel
        
        + optional params are:
            depth: Defaults to public. Passing extended returns the available connections on a block
            page: Specifies the page of results to retrieve.
            per: Specifies the number of channels to retrieve.
        '''
        return self.make_request('/blocks?channel=%s' % channel, options)

    def get_user_channel(self, id, options={}):
        '''
        + returns a dictionary: blocks, page, per, user

        + optional params are:
            page: Specifies the page of results to retrieve.
            per: Specifies the number of channels to retrieve.
        '''
        return self.make_request('/channels?user=%s' % id, options)

    def get_block(self, id, options={}):
        '''
        + returns a block dict:
            provider_url,image_file_size, embed_source_url, updated_at, 
            embed_height, image_remote_url, block_type, id, user_id, 
            image_updated_at, title, comment_count, content, state, 
            image_thumb, provider_name, type, embed_width, username, 
            readable_updated_at, image_content_type, embed_url, description,
            embed_author_url, processing, embed_thumbnail_url, image_original,
            image_file_name, embed_html, embed_author_name, source_url, 
            image_display, user_slug, block_class, created_at, generated_title, 
            remote_source_url, embed_type, link_url, embed_title

        + optional params are:
            depth: Defaults to public. Passing extended returns the available connections on a block
        '''
        return self.make_request('/blocks/%s' % id, options)

    #######
    ## SORTING & ITEM RETRIEVAL FUNCTIONS
    #######

    #
    # channel basics
    #
    def get_channel_title(self, channel):
        return channel.get('title')

    #
    # channel channels
    #
    def get_channel_channels(self, channel):
        return channel.get('channels')

    def get_channel_channels_count(self, channel):
        if self.get_channel_channels(channel):
            return len(self.get_channel_channels(channel))

    #
    # channel blocks
    #
    def get_channel_block_count(self, channel):
        return channel.get('blocks_count')

    def sort_channel_blocks_by_created(self, channel, sort_by = 'desc'):
        '''
        sort a channel's blocks by created timestamp
        sort_by asc or desc, default = desc (newest)
        '''
        blocks = channel.get('blocks')
        if blocks:
            if sort_by == 'asc':
                blocks = sorted(blocks, key=itemgetter('created_at')) 
            else:
                blocks = sorted(blocks, key=itemgetter('created_at'), reverse=True) 
            channel['blocks'] = blocks
            return channel
        else:
            return None

    #
    #  block filtering: all take a list of blocks
    #
    def get_image_blocks(self, blocks_list):
        if blocks_list:
            return [block for block in blocks_list if block['block_class'] == 'image']
        else:
            return None

    def get_image_blocks_count(self, blocks_list):
        if self.get_channel_images(channel):
            return len(self.get_channel_images(channel))
        else:
            return None

    def get_media_blocks(self, blocks_list):
        if blocks_list:
            for b in blocks_list:
                print b
                print '+++++'
            return [block for block in blocks_list if block['block_class'] == 'media']
        else:
            return None

    def get_media_blocks_count(self, blocks_list):
        if self.get_channel_media(channel):
            return len(self.get_channel_media(channel))
        else:
            return None

    def get_text_blocks(self, blocks_list):
        if blocks_list:
            return [block for block in blocks_list if block['block_class'] == 'text']
        else:
            return None

    def get_text_blocks_count(self, blocks_list):
        if self.get_channel_text(channel):
            return len(self.get_channel_text(channel))
        else:
            return None

    def get_links_blocks(self, blocks_list):
        if blocks_list:
            return [block for block in blocks_list if block['block_class'] == 'link']
        else:
        +    return None

    def get_links_blocks_count(self, blocks_list):
        if self.get_channel_text(blocks_list):
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
        if self.get_channel_connections(channel):
            return len(self.get_channel_connections(channel))
        else:
            return None
