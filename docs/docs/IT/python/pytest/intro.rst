=====================
pytest-tips
=====================

--------------
install
--------------

.. code-block:: shell

   pip install pytest
   #django使ってるならこっち
   pip install pytest-django


-------------
設定ファイル
-------------

pytest.ini
==========

.. code-block:: shell

    [pytest]
    python_files=test*.py
    markers=
        slow: test consuming lots of time
        smoke:  subset of tests you are handling with
    addopts=
        --strict-markers
  

-------------
fixture
-------------
test実行前のsetup部分をテストコードとは独立させて、テスト関数で再利用できるようにする仕組み。
例えば次のようにdatabaseをsetupするときに使う。このようにするとtest自体のboiltplateなコードが消えて
テストしているaction自体が見やすい。

.. code-block:: python
  
    import pytest
    @pytest.fixture()
    def some_data():
      return 41
    
    def test_some_data(some_data):
        assert some_data==41



yieldの後はテスト終了後の後処理を記述する

.. code-block:: python

    @pytest.fixture(scope="session")
    def init_db():
      with TempotaryDirectory()n as db_dir:
        db_path=Path(db_dir)
        db_=cards.CardsDb(db_path)
        yield db_
        db_.close()

    def test_db(init_db):
        assert init_db.count()==0
        init_db.add(cards.Card("test"))
        assert init_db.count()==1


**conftest.py** にfixtureを記述することでimportなしで使用できる。

aws
======================
| awsを使ったモジュールをテストしたい場合はmotoが便利（ただしs3など一部のサービスに限られる）
| 例えば下記のようにbucketを作るfixtureが書ける。

.. code-block:: python
    
    import pytest
    from moto import mock_s3
    import boto3
    from typing import Callable
    @pytest.fixture(scope="function")
    def create_dummy_bucket():
        """
        """    
        def _create(bucket_name:str):
            client = boto3.client("s3", region_name="us-east-1")
            return  client.create_bucket(Bucket=bucket_name)
        with mock_s3():
            yield _create



.. code-block:: python

  def test_upload(create_dummy_bucket):
      create_dummy_bucket("test")
      upload("test","test.txt")




一覧確認
=========================
既存のfixtureの一覧を見たい場合


::
  
    pytest --fixtures -v

================
* defaultはfunction
* 時間のかかるもので複数回実行する必要がないものはmoduleやsessionにすることで実行回数を減らせる。
*  ユニットテストでは実行速度も需要なので遅い場合はfixtureで調整することも選択肢。特にgeodjangoなどは処理速度が遅いので注意!
  
  例えば下記のようにmoduleにすると同じmoduleないで使った場合は再実行されない。



.
=============
* 名前である程度何が行われているかわかるようにす
* dbに複数objを登録するときなどは、fixtureをcallする側で値を設定するような方式にしたほうが
  テストを読んだときにわかりやすい
  


