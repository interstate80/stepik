#! /usr/bin/python

def myapp(env, start_response):                                                                                      
    data = ''                                                                                                        
    status = '200 OK'                                                                                                
    response_headers = [('Content-type', 'text/plain')]                                                              
    p_data = env['QUERY_STRING']                                                                                     
    for i in p_data.split('&'):                                                                                      
        data += '%s\n' % i                                                                                           
    start_response(status, response_headers)                                                                         
    return [ data ]                                                                                                  