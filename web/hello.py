#! /usr/bin/python

#from cgi import parse_qs
import urlparse

def myapp(env, start_response):
    data = ''
    status = '200 OK'
    response_headers = [('Content-type', 'text/plain')]
    p_data = urlparse.parse_qs(env['QUERY_STRING'])
    # for i, v in p_data.items():
    #     v = str(v).replace('\']','')
    #     v = v.replace('[\'','')
    #     data += '%s=%s\n' % (i,v)
    start_response(status, response_headers)
    return ['%s=%s<br>' % (k, p_data[k][0]) for k in p_data]