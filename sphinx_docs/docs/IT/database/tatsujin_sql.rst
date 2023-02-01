============================
達人に学ぶsql徹底指南書
============================

----------------
練習問題
----------------
4章
=============
dbごとでのnullに関する挙動の違いを確かめる。
ここではpostgresqlを使用
4-1
------
* order by ではNullは最後。descをつけると逆転してnullが一番上に来る、

::

   #sort     
    postgres=# select * from sample_person
    order by address;
    id | name  |    address     
    ----+-------+----------------
    5 | sato  | ishikawa
    1 | test  | tokyo_shinjuku
    2 | taro  | yodobashi
    3 | soba  | 
    4 | aiueo | 
    (5 rows)

    postgres=# select * from sample_person
    order by address desc ;
    id | name  |    address     
    ----+-------+----------------
    3 | soba  | 
    4 | aiueo | 
    2 | taro  | yodobashi
    1 | test  | tokyo_shinjuku
    5 | sato  | ishikawa
    (5 rows)



4-2
-----
* 彼文字列との連結は通常通り
* nullと文字列を連結するとnullになる
  
:: 

    
    postgres=# select 'abc'||''  as str;
    str 
    -----
    abc
    (1 row)

    postgres=# select 'abc'||NULL  as str;
    str 
    -----
    
    (1 row)
