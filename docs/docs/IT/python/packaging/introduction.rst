============================
introduction
============================

----------------------------
hello world
----------------------------
unknown!!
================
空のpyproject.tomlを作ればbuildはできる。がunknwonだらけで何のパッケージかが分からない状態

.. code-block:: shell

    >python -m venv venv
    >source venv/bin/activate
    >touch pyproject.toml
    >pyproject-build
    >unzip -l dist/UNKNOWN-0.0.0-py3-none-any.whl 
    
    Archive:  dist/UNKNOWN-0.0.0-py3-none-any.whl
    Length      Date    Time    Name
    ---------  ---------- -----   ----
        52  2023-10-13 13:50   UNKNOWN-0.0.0.dist-info/METADATA
        92  2023-10-13 13:50   UNKNOWN-0.0.0.dist-info/WHEEL
            1  2023-10-13 13:50   UNKNOWN-0.0.0.dist-info/top_level.txt
        295  2023-10-13 13:50   UNKNOWN-0.0.0.dist-info/RECORD
    ---------                     -------

名前付け
========================
setup.cfg

::

    