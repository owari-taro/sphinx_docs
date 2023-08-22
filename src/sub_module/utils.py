import sys
#from pathlib import Path
#sys.path.append(Path(__file__))
import requests
from hoge import list
from sub_module.mini_module.mini import mini
#from mini_module.mini import mini
from retry import retry
from functools import wraps



def classpropertymethod(**kwargs1):
    def outer(func):
    
        @wraps(func)
        @retry(**kwargs1)
        def wrapped(*args,**kwargs):
            return func(*args,**kwargs)
        return wrapped
    return outer
    

@classpropertymethod(tries=12)
def fetch_data(url:str):
    """
    | fetch data from url
    | when failed,raise ssome exception

    :param str url: _description_
    :return _type_: _description_
    """    
    print("hogehoge")
 #   raise Exception


#fetch_data("test")



