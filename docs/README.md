# multicrypt

Multicrypt is a utility that uses Shamir's secret sharing scheme to split a deterministic wallet seed into 
several seeds in such a way that not all seeds are required to recover the seed.

Multicrypt is a Python 3 GUI application written using the Qt library.
 
![Multicrypt](https://github.com/ronreiter/multicrypt/blob/master/screenshot.png?raw=true "Multicrypt")

Downloads
=========

* Mac Version - [Multicrypt-osx-0.0.1.dmg](https://github.com/ronreiter/multicrypt/raw/master/dist/Multicrypt-osx-0.0.1.dmg)
* Windows Version - Unavailable
* Linux Version - Unavailable
* Source - Click [here](https://github.com/ronreiter/multicrypt) for further instructions

Usage Instructions
==================

1. Open your wallet in Electrum and go to Wallet -> Seed. Copy and paste the seed into this application.
2. Adjust 'Shares Required' according to the number of shares you wish to require in order for you to be able to recover your seed.
3. Adjust 'Shares to Generate' according to the number of shares you wish to distribute.
4. Click on 'Encrypt'. You may verify that the secret shares are reversible using 'Decrypt'.
5. Distribute the secret shares to people you trust. Do not store all shares together digitally in one location.

Currently only Electrum deterministic wallets are supported.

Download Electrum from here: [https://electrum.org](https://electrum.org)

### Support

If you have any issue with Multicrypt, please open an issue [here](https://github.com/ronreiter/multicrypt/issues).
