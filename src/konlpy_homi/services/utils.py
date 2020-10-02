from functools import wraps

import jpype


def check_options(svc_options:set,input_options:dict):
    input_options_key = set(opt['key'] for opt in input_options)
    un_support_keys = input_options_key - svc_options
    if un_support_keys:
        raise Exception(f"{un_support_keys} options is not supported! (supported options: {svc_options})")

def attachThreadToJVM(func):
    @wraps(func)
    def func_wrapper(*args,**kwargs):
        jpype.attachThreadToJVM()  # XXX: Performance Incresed. (Still don't know yet)
        return func(*args,**kwargs)

    return func_wrapper