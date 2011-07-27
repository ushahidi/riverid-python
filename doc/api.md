# RiverID API Documentation

## Overview

* All calls are transported across the HTTP protocol and follow the REST design pattern.
* All methods return a valid JSON response.
* All methods support both HTTP GET and POST.
* In the case of HTTP GET, the parameters need to be sent as part of the query string.
* In the case of HTTP POST, the parameters must be form encoded and sent as part of the POST body.
* Append the API method name to the base URL `http://api.example.com/api/`. Replace `api.example.com` with the appropriate host.

## Responses

* On success, the boolean `success` will equal `true`; on error it will equal `false`.
* If `success` equals `true` and the method returns a value, `response` will equal the returned value.
* If `success` equals `true` and the method does not return a value, `response` will equal `null`.
* If `success` equals `false`, an `error` will be provided explaining the error.

## Examples

### Curl

    $ curl http://api.example.com/api/requestpassword?email=user@example.com
    {"status": true, "request": {"email": "user@example.com"}, "method": "requestpassword", "response": null}

### Success JSON

    {
        "status": true,
        "request": {
            "email": "user@example.com"
        },
        "method": "requestpassword",
        "response": null
    }

### Failure JSON

    {
        "status": false,
        "request": {
            "email": "user@example"
        },
        "method": "requestpassword",
        "error": "Please provide a valid email address."
    }

## Methods

### changeemail

#### Parameters

* `oldemail` The old email address of the account.
* `newemail` The new email address of the account.
* `password` The account's password.

### changepassword

#### Parameters

* `email` The email address of the account.
* `oldpassword` The old password.
* `newpassword` The new password.

### checkpassword

#### Parameters

* `email` The email address of the account.
* `password` The password to check.

#### Returns

* `boolean` Indicator of whether the password is valid for the email account.

### confirmemail

#### Parameters

* `email` The email address to confirm.
* `token` The secret token sent to the address.

### currentsessions

#### Parameters

* `session` An active session id.

#### Returns

    {
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

* `boolean` Indicator of whether the email address is associated with an account.

### requestpassword

#### Parameters

* `email` The email address of the account.

### setpassword

#### Parameters

* `email` The email address of the account.
* `token` The token mailed to the email address.
* `password` The new password of the account.

### signin

#### Parameters

* `email` The email address of the account.
* `password` The password associated with the email address.

#### Returns

* `string` The 64-character alphanumeric unique session identifier.

### signout

#### Parameters

* `email` The email address of the account.
* `session_id` The session identifier.
