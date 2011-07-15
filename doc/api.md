# RiverID API Documentation

## Description

* Calls are transported across the HTTPS protocol and follow the REST design pattern.
* Calls return a valid JSON response on success or failure.
* All methods support both HTTP GET and POST.
* In the case of HTTP GET, the parameters need to be sent as part of the query string.
* In the case of HTTP POST, the parameters must be form encoded and sent as part of the POST body.
* Append the API method name to the base URL `https://api.example.com/api/`. Replace `api.example.com` with the appropriate host.

## Methods

### checkpassword

#### Parameters

* `email` The email address of the account.
* `password` The password to check.

#### Returns

    {
        "status": "success",
        "valid": true
    }

### confirmemail

#### Parameters

* `email` The email address to confirm.
* `token` The secret token sent to the address.

#### Returns

    {
        "status": "success",
        "email": "user@example.com"
    }

### recoverpassword

#### Parameters

* `email` The email address of the account to recover.

### Returns

    {
        "status": "success",
        "email": "user@example.com"
    }

### register

#### Parameters

* `email` The email address associated with the new account.
* `password` The initial password of the new account.

#### Returns

    {
        "status": "success",
        "email": "user@example.com"
    }

### signin

#### Parameters

* `email` The email address of the user signing in.
* `password` The password associated with the email address.

#### Returns

    {
        "status": "success",
        "email": "user@example.com",
        "session": "2C7C5F47B6CFBE2FB3BE931C9FB2CC05638D26A00D85E747BF7DB2900154D58D"
    }

### signout

#### Parameters

* `session` The session identifier.

#### Returns

    {
        "status: "success"
    }