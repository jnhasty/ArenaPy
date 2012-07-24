ARENAPY
===========

A simple client interface for Are.na written in python! 

Requires requests (https://github.com/kennethreitz/requests) to handle http interactions.

Typical Usage:

    from arena import ArenaPy    
    arena_connect = ArenaPy()
    user_channel_json = arena_connect.get_users_channels('nick-hasty')
    
user_channel_json will be a unicode json string. 

see arena.py for available methods.
