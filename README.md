## CoinFort - NFT SCAM Predictor
Our team provides an API for NFT validation using machine learning algorithms. Our service classify NFTs whether it refers to SCAM or not.
Also we have NFTs address validation. These methods will help you to be safe when buying NFTs.

[Some info about our product and team.](https://docs.google.com/presentation/d/1c37upNhv2XQjR1a2YZlRpqz48NyfdsdsUxV7KOokhbw)

## Testing

Our [Gitbook](https://coinfort.gitbook.io/coinfort/) tells you about our API. There you can here instructions about testing API.

You can get API key [here](https://k5b4tz7itoa.typeform.com/to/rhY1DMSm).

Request example :

```
curl -X POST https://joz8jzbkxi.execute-api.eu-central-1.amazonaws.com/Prod/solana/v0/mainnet/token/check \
    -H 'x-api-key: <API_KEY>' \
    -d 2hQZuDm1y4HPiphKnEgJNsGWa4B4M5VhMdAbXNPABgfw
```
Respone example :

```
{
    "result": "SUSPECTED_MALICIOUS", 
    "malicious_type": "PHISHING",
    "token_address": "2hQZuDm1y4HPiphKnEgJNsGWa4B4M5VhMdAbXNPABgfw"
}
```
