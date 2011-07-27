# RiverID API Documentation

## Description

* All calls are transported across the HTTP protocol and follow the REST design pattern.
* All methods return a valid JSON response.
* All methods support both HTTP GET and POST.
* In the case of HTTP GET, the parameters need to be sent as part of the query string.
* In the case of HTTP POST, the parameters must be form encoded and sent as part of the POST body.
* Append the API method name to the base URL `https://api.example.com/api/`. Replace `api.example.com` with the appropriate host.

## Errors

### Handling

* On success, the boolean `success` will equal `true`, on error it will equal `false`.
* If `success` equals `false`, an `error` will be provided explaining the error.

### Success Example

    {
        "success": true,
        "request_parameters": {
            "email": "user@example.com"
        }
    }

### Failure Example

    {
        "success": false,
        "error": "Some message explaining the error.",
        "request_parameters": {
            "email": "user@example.com"
        }
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

* `valid` Boolean indicating if the password is valid for the email account.

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

* `registered` Boolean indicating if the email address is registered.

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

* `session_id` 64-character alphanumeric unique session identifier.
* `session_start` The exact start date (including microseconds) in ISO format.

### signout

#### Parameters

* `email` The email address of the account.
* `session_id` The session identifier.

#### Returns

* `session_stop` The exact stop date (including microseconds) in ISO format.