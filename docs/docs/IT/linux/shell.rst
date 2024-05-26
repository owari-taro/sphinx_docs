============================
shell
============================


----------------
shell script
-----------------

引数にデフォルト値をいれたい
=============================
下のようにハイフンに続けて初期値を書く。

.. code-block:: bash
    
    #!/bin/bash
    name=${1-"default1"}
    name2=${2-123}
    echo "$name"
    echo "$name2"



.. code-block:: console

    $ ./default.sh 
        default1
        123

フォルダ内から特定文字列を含むファイルを検索したい
==============================================

::

    #importを含むファイル名だけだしたい  
    find . -type f -name "*.py"|xargs grep -rl import
    #importを含む行だけ表示したい
    find . -type f -name "*.py"|xargs grep -r -h import 

pythonファイル自体はあるがrequirements.txtなどでlibraryが管理されてないコードがレポジトリにあったときに、依存ライブラリを調べるのに使った。

