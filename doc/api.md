# RiverID API Documentation

## Description

* Calls are transported across the HTTPS protocol and follow the REST design pattern.
* Calls return a valid JSON response on success or failure.
* All methods support both HTTP GET and POST.
* In the case of HTTP GET, the parameters need to be sent as part of the query string.
* In the case of HTTP POST, the parameters must be form encoded and sent as part of the POST body.
* Append the API method name to the base URL `https://api.example.com/api/`. Replace `api.example.com` with the appropriate host.

## Methods

### changeemail

#### Parameters

* `oldemail` The old email address of the account.
* `newemail` The new email address of the account.
* `password` The account's password.

#### Returns

    {
        "status": "success",
        "oldemail": "user1@example.com",
        "newemail": "user2@example.com"
    }

### changepassword

#### Parameters

* `email` The email address of the account.
* `oldpassword` The old password.
* `newpassword` The new password.

#### Returns

    {
        "status": "success",
        "email": "user@example.com"
    }

### checkpassword

#### Parameters

* `email` The email address of the account.
* `password` The password to check.

#### Returns

    {
        "status": "success",
        "email": "user@example.com",
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

### currentsessions

#### Parameters

* `session` An active session id.

#### Returns

    {
        "email": "user@example.com",
        "sessions": [
            {
                "id": "F98AB1961B8AC364AEE27ABD27D878BFA8FC5585F4387946952DD2E51C9EBC24",
                "created": "2011-01-01T00:00:00Z",
                "ip": "127.0.0.1"
            },
            {
                "id": "66DAC61453552C7C9BF617A0676B0B7E158142F71350859E5ABF1A8B5D6B2124",
                "created": "2011-02-03T01:23:45Z",
                "ip": "127.0.0.2"
            }
        ]
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