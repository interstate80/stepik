#! /usr/bin/python

#from cgi import parse_qs
import urlparse

def myapp(env, start_response):
    data = ''
    status = '200 OK'
    response_headers = [('Content-type', 'text/plain')]
    p_data = env['QUERY_STRING'].split('&')

    start_response(status, response_headers)
    return ['%s' % k for k in p_data]