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
                "id": "Jl70Vs0UDoABLkkfZGWFKOeVioI0bag07hWVk40lGwQL8mdemca0VjwS9Jbzz0BJ",
                "created": "2011-07-25T12:38:57.881095"
            },
            {
                "id": "LyF6J3Dn4A5wS9MDKRzB9eAZZqihDol6KSGQVifxYwgrEpQ7KSnXDmNSDW4efLUa",
                "created": "2011-07-25T12:40:02.476250"
            }
        ]
    }

### registered

#### Parameters

* `email` The email address to look up.

#### Returns

    {
        "email": "user@example.com",
        "registered": true
    }

### requestpassword

#### Parameters

* `email` The email address of the account.

### Returns

    {
        "status": "success",
        "email": "user@example.com"
    }

### setpassword

#### Parameters

* `email` The email address of the account.
* `token` The token mailed to the email address.
* `password` The new password of the account.

#### Returns

    {
        "status": "success",
        "email": "user@example.com"
    }

### signin

#### Parameters

* `email` The email address of the account.
* `password` The password associated with the email address.

#### Returns

    {
        "status": "success",
        "email": "user@example.com",
        "session_id": "tMFynC1zRYIne0gKjtvSem6yb9usGzIz1xzgeb15YJiKsj0b92gw09b5ueNyhsrW",
        "session_start": "2011-07-25T12:41:59.814633"
    }

### signout

#### Parameters

* `email` The email address of the account.
* `session_id` The session identifier.

#### Returns

    {
        "status: "success",
        "email": "user@example.com",
        "session_id": "tMFynC1zRYIne0gKjtvSem6yb9usGzIz1xzgeb15YJiKsj0b92gw09b5ueNyhsrW",
        "session_stop": "2011-07-25T13:34:24.184900"
    }