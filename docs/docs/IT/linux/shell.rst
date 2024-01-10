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

