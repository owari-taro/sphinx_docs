====================
postgres
====================




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
