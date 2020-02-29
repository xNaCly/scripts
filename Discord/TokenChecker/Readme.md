# Tokenchecker for Discord
## Checks if a token is valid and if so returns a JSON-object containing information about the token's user
### What you need to do:
  - installing python
  
### How it works:
  - will ask you for a Token
  - will send a request to the discord api
  - will print out the response as a JSON-object:
  ```JSON
  {
    "id": "678261196507578371",
    "username": "xnacly",
    "avatar": null,
    "discriminator": "2371",
    "email": null,
    "verified": false,
    "locale": "en-US",
    "mfa_enabled": false,
    "phone": null,
    "flags": 0
  }
  ```
### What is a token?
  - why even use this if you dont know? anyways [here.](https://discordapp.com/developers/docs/topics/oauth2#bots) & [here v2](https://discordapp.com/developers/docs/reference#authentication)
