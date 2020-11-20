# coingeck-python
#### A shitty implementation of the coingecko API in python

This project aims to:
- Provide a simple way to access the CoinGecko API in python
- Exist

## How to use

### connectionTest() - A wrapper for /ping
Just to test if you can connect to the api. Index 0 contains a boolean. True for successful connection. False if failed. In Index 1 is the api response.

### getCoinValue(crypto, fiat) - Find out how much one X is in Y
For example getCoinValue(bitcoin, gbp) will tell you how much one Bitcoin is in GBP. Returns a float of the value
