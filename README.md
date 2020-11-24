# coingecko-python
#### A shitty implementation of the coingecko API in python

This project aims to:
- Provide a simple way to access the CoinGecko API in python
- Exist

## How to use

### connectionTest() - A wrapper for /ping
Just to test if you can connect to the api. Index 0 contains a boolean. True for successful connection. False if failed. In Index 1 is the api response.

### getCoinValue(crypto, fiat) - Find out how much one X is in Y
For example getCoinValue(bitcoin, gbp) will tell you how much one Bitcoin is in GBP. Returns a float of the value

### convertToFiat(crypto, fiat, amount) - Convert from crypto to fiat
Examples:

convertToCrypto(dogecoin, gbp, 50) - Will return how much 50 gbp is in dogecoin
convertToCrypto(litecoin, usd, 1.5) - Will return how much 1.5 usd is in litecoin

### convertToCrypto(crypto, fiat, amount) - Convert from fiat to crypto
Examples:

convertToCrypto(dogecoin, gbp, 50) - Will return how much 50 dogecoin is in gbp
convertToCrypto(litecoin, usd, 1.5) - Will return how much 1.5 litecoin is in usd

### supportedVsCurrencies() - Returns all supported currencies you can convert too

### supportedVsCurrenciesPretty() - Same as supportedVsCurrencies() but with new lines OwO
