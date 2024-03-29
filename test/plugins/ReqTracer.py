import logging
import os

from nose2.events import Plugin

class ReqTracer(Plugin):
    configSection = 'req-tracer'

    def afterSummaryReport(self, event):
        with open('RequirementResult.txt', 'w') as myFile:
            for key, item in Requirements.items():
                myFile.write(key+ ' '+str(item.func_name)+'\n')

class RequirementTrace(object):
    req_text = ""
    def __init__(self, text):
        self.req_text = text
        self.func_name = []

Requirements = {}

def requirements(req_list):
    def wrapper(func):
        def add_req_and_call(*args, **kwargs):
            for req in req_list:
                if req not in Requirements.keys():
                    raise Exception('Requirement {0} not defined'.format(req))
                Requirements[req].func_name.append(func.__name__)
            return func(*args, **kwargs)

        return add_req_and_call

    return wrapper

with open('RequirementTags.txt') as f:
    for line in f.readlines():
        if '#00' in line:
            req_id, desc = line.split(' ', 1)
            Requirements[req_id] = RequirementTrace(desc)
