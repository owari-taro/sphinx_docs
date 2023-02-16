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


6章 having句の力
===================

6-1
-----------------
1. 
* 教科書の回答

::
    
    postgres=#  select seq,SUMs^Ceq) over (order by seq range between 1 following and 1 following) as nex_seq from sample_se
    qtbl;
    postgres=# select case when count(*)<>max(seq) then '歯抜けあり' else '歯抜けあり'end as gap from sample_seqtbl;
        gap
    ------------
    歯抜けあり
    (1 row)


   
* having使わずにウィンドウ関数で実行した場合の回答

::
     
    postgres=# select * from sample_seqtbl;
    id | seq | name
    ----+-----+------
    1 |   1 | test
    2 |   2 | test
    3 |   4 | test
    4 |   5 | test
    5 |   6 | test
    6 |   7 | test
    (6 rows)

    postgres=# select seq ,case when nex_seq=seq+1 then '歯抜けなし' else '歯抜けあり' end 
    as message from ( select seq,SUM(seq) over (order by seq range between 1 following and 1 following) as nex_seq from sample_seqtbl)A;
    seq |  message
    -----+------------
    1 | 歯抜けなし
    2 | 歯抜けあり
    4 | 歯抜けなし
    5 | 歯抜けなし
    6 | 歯抜けなし
    7 | 歯抜けあり
    (6 rows)


6-2
--------------
各departmentのmaxが締め切りより早いといことをhaving内で指定

::

    postgres=# select * from sample_student;
    id | department |         submitted_at
    ----+------------+-------------------------------
    9 | a          |
    10 | a          | 2023-03-03 00:00:00+00
    11 | b          | 2023-02-02 07:39:08.980201+00
    12 | b          | 2023-02-02 07:39:08.981886+00
    13 | c          | 2023-03-03 00:00:00+00
    14 | c          | 2023-02-02 07:39:08.985113+00
    (6 rows)

    postgres=# select department from sample_student group by department 
    having count(*)=count(submitted_at) and max(submitted_at)<now();
    department
    ------------
    b
    (1 row)

    postgres=#


    6-3
    --------

    ::

        select S.name,sum(case when S.item in (select name from sample_item) then 1 else 0 end) as item, 
          count(I.name)  from sample_shop S inner join sample_item I on S.item=I.name group by S.name;



