====================
postgres
====================
------------------------
role
------------------------


.. glossary:: 

    role
        aiueo

    group
        他のロールを含むロール。

role作成
==================

::

    docker compose up -d 
    psql -h localhost -U postgres


untilをつけると期限付きのroleが作れる。

::

    create role test with password 'dummy';
    create role tmp_test with password 'dummy' 
    valid until '2023-12-24 00:00:00';

特定databaseの権限付与
=========================

::

    create datasbse {db-name}
    GRANT ALL PRIVILEGES ON DATABASE {database-name} to {role-name};

        


一覧表示
===================
::

    psall -U postgres -h localhost
    \du
    
     Role name |                         Attributes                         | Member of 
    -----------+------------------------------------------------------------+-----------
    dummy     |                                                            | {test}
    postgres  | Superuser, Create role, Create DB, Replication, Bypass RLS | {}
    test      |                                                            | {}

    

--------
view
--------

viewの作成
=======================


::

    create view hogehogeview as {select 文}    


view削除
=======================

::
    drop view {view_name}

viewの権限付与
================

::

    grant select on {view_name} to {role}


viewの定義確認
=======================

::

     SELECT definition FROM pg_views WHERE viewname = 'foobar';
