=======================
django-pytoiiiest
=======================
--------------
conftest
--------------
conftestに、テストの前処理コードなどを書く。conftest.pyの名前を書いておけばimportしなくても同階層のpytestのファイルからimportして使える



-----------------
factoryboy
-----------------
install
===============

::

    pip install pytest-factoryboy

hello world
==========================
factoryboyでテスト用のモデルを生成するコード

.. literalinclude:: ./src/conftest.py
   :language: python



passwordの生成
===================
次のように **postgenerationmethodcall** でpasswordを生成する。
第二引数にdefaultを指定する。
UserFactory(username="HogeTaro",password="Hoge")のように直接指定もできる
`stack-overflow <https://stackoverflow.com/questions/10183664/user-authentication-in-tests-with-django-factory-boy>`__

::

   import factory
   from django.contrib.auth.models import User
   #or
   #from somewhere import CustomUser as User

   class UserFactory(factory.DjangoModelFactory):
      FACTORY_FOR = User

      username = 'UserFactory'
      email = 'test@example.com'
      password = factory.PostGenerationMethodCall('set_password', 'password')


apiテスト
=======================

HTTP request
---------------
django restならAPIClient使う

::

   @pytest.mark.django_db
   def test_create_f1driver_payload():
      client = APIClient()
      url = '/api/create-f1driver/'
      payload = {
         'name': 'Lewis Hamilton',
         'team': 'Mercedes',
         'country': 'England',
         'age': '38',
         'podiums': 412,
         'championships': 7,
      }
      response = client.post(url, payload)
      assert response.status_code == status.HTTP_201_CREATED
      assert F1Driver.objects.count() == 1

https://blog.devgenius.io/testing-django-rest-framework-with-pytest-fb1b7bd8257b



customデータ型の生成
====================
defaultで提供されていない方式でデータを生成したいばあい


pointdata
------------
geometry型は提供されてないので自分で作る必要がある

 `stack overflow <https://www.youtube.com/watch?v=5K69VdIYiNg>`__




