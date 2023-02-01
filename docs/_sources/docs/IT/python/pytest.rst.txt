=====================
pytest-tips
=====================


-------------
fixture
-------------
test実行前のsetup部分をテストコードとは独立させて、テスト関数で再利用できるようにする仕組み。
例えば次のようにdatabaseをsetupするときに使う。このようにするとtest自体のboiltplateなコードが消えて
テストしているaction自体が見やすい。



::

    @pytest.fixture(scope="session")
    def init_db():
      with TempotaryDirectory()n as db_dir:
        db_path=Path(db_dir)
        db_=cards.CardsDb(db_path)
        yield db_
        db_.close()

    

一覧確認
=========================
既存のfixtureの一覧を見たい場合


::
  
    pytest --fixtures -v
scope
================
* defaultはfunction
* 時間のかかるもので複数回実行する必要がないものはmoduleやsessionにすることで実行回数を減らせる。
*  ユニットテストでは実行速度も需要なので遅い場合はfixtureで調整することも選択肢。特にgeodjangoなどは処理速度が遅いので注意!
  
  例えば下記のようにmoduleにすると同じmoduleないで使った場合は再実行されない。
  :: 

長さ
================
* 名前である程度何が行われているかわかるようにす
* dbに複数objを登録するときなどは、fixtureをcallする側で値を設定するような方式にしたほうが
  テストを読んだときにわかりやすい
  