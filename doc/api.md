# RiverID API Documentation

## Methods

### confirmemail

#### Parameters

* `email` The email address to confirm.
* `token` The secret token sent to the address.

#### Returns

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