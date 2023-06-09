====================
decorator
====================


------------------
引数付きdecorator
------------------
多重化
===========
デコレータをデコレートしたい場合の実装方法。
あまり使う機会はない。decoratorをそのまま使うとsphinxでdocstringが無効かされてしまうというときに使った。


::
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
        raise Exception


    fetch_data("test")
