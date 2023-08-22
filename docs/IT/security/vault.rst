=============
vaultメモ
=============


-------------
インストール
-------------
公式ページのコマンドをペイスト



------------
hello world
------------




::

    $ vault kv put secret/mypassword password=p@SSw0rd
        ===== Secret Path =====
        secret/data/mypassword

        ======= Metadata =======
        Key                Value
        ---                -----
        created_time       2023-03-10T01:21:50.735352723Z
        custom_metadata    <nil>
        deletion_time      n/a
        destroyed          false
        version            1
    
    $ vault kv get secret/mypassword
    
        ===== Secret Path =====
        secret/data/mypassword

        ======= Metadata =======
        Key                Value
        ---                -----
        created_time       2023-03-10T01:21:50.735352723Z
        custom_metadata    <nil>
        deletion_time      n/a
        destroyed          false
        version            1

        ====== Data ======
        Key         Value
        ---         -----
        password    p@SSw0rd
