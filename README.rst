Multicrypt - A utility to split your Bitcoin seed into shares
=============================================================

::

  Licence: MIT Licence
  Author: Ron Reiter
  Language: Python 3
  Homepage: https://github.com/ronreiter/multicrypt


.. image:: https://github.com/ronreiter/multicrypt/blob/master/icons/multicrypt.png?raw=true
    :target: https://travis-ci.org/ronreiter/multicrypt
    :height: 128px
    :alt: Build Status


Getting started
===============

Multicrypt is a Python 3 GUI application written using the Qt library.
Multicrypt is a utility that uses Shamir's secret sharing scheme 
to split a deterministic wallet seed into several seeds in such a way 
that not all seeds are required to recover the seed.

.. image:: https://github.com/ronreiter/multicrypt/blob/master/screenshot.png?raw=true
  

Usage Instructions
==================

1. Open your wallet in Electrum and go to Wallet -> Seed. Copy and paste the seed into this application.
2. Adjust 'Hashes Required' according to the number of hashes you wish to require in order for you to be able to recover your seed.
3. Adjust 'Hashes to Generate' according to the number of hashes you wish to distribute.
4. Click on 'Encrypt'. You may verify that the secret shares are reversible using 'Decrypt'.
5. Distribute the secret shares to people you trust. Do not store all shares together digitally in one location.

Currently only Electrum deterministic wallets are supported.

Running the development version
===============================

To run multicrypt, create a Python 3 virtualenv, install all requirements, and run multicrypt.py.

::

    git clone git://github.com/ronreiter/multicrypt.git
    cd multicrypt
    mkvirtualenv multicrypt -p `which python3`
    pip install -r requirements.txt
    python multicrypt.py


Creating Binaries
=================

There is no way to create binaries yet. Please feel free to assist by sending me a pull request. 
