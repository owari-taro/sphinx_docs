==========================
utils
==========================
便利関数とかもろもろのめも

-----------------
library管理
-----------------

pipenv
=======
install
----------
installすればPipfileを生成して、記録してくれる。  


.. code-block:: shell
    
    pip isntall pipenv
    #.envを読み込みたくない場合↓
    export PIPENV_DONT_LOAD_ENV=1 
    pipenv install django requests
    #dev用のライブラリ
    pipenv isntall -d pytest pylint
 
.. warning:: 
    
    ver指定してない限りは Pipfileにverは記載されない
    
:: 
    
    pipenv install numpy==1.14



lockファイル生成
------------------
installしたverまで残したいときは

.. code-block:: shell

       #lockファイルの生成.
    pipenv requirements > requirements.lock
    pipenv requirements -dev >requirements_dev.lock
    #ライブラリの依存関係の表示
    pipenv graph
    
環境の再現
-----------
すでに作成済みのPipfileやrequirements.lockなどと同じ環境を再現したい場合は

.. code-block:: shell

    pipenv install 
    pipenv isntall --dev
    #verまで合わせたいとき
    pipenv sync
    pipenv sync --d


poetry
======
pipenvより高速に実行できる.



-----------------------
log
-----------------------
loggingの設定
==================

.. code-block:: 

    import logging
    import sys

    # filename="test.log"を　追加
    logging.basicConfig(level=logging.INFO,
    stream=sys.stdout,
    format="%(asctime)s - %(levelname)s:%(name)s - %(message)s",
    filename="test.log")




---------------
dataclass
---------------
フィールド間の制約などが特にないならクラスを避けてdataclassを使ったほうがきれいに書ける

::

    from dataclasses import dataclass
    @dataclass
    class Product:
        name:str
        price:int

dict変換
============
asdictで変換すれば一発
::
    
    from dataclasses import dataclass, field, asdict


------------------------
正規表現
------------------------



------------------------
日付関数
------------------------

-------------
csv作成
-------------
csvDict
===================
::
    import csv
    writer = csv.DictWriter(ファイル名, fieldnames=field名)
    writer.writeheader()




--------------------------
csv
--------------------------




------------------------
その他
------------------------
リトライ
========
