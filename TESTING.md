Go back to [README.md](https://github.com/monika-hrda/hike-slovakia/blob/main/README.md)

## Testing

* Validator Testing
* Page quality measurement / Performance
* User Stories Testing
* Manual Testing
* Error Testing
* Continuous Testing

### Validator Testing

#### HTML

All pages were checked using [W3C Markup Validation Service](https://validator.w3.org/).

The HTML code was validated using the page URI.

There was one warning and two info messages found, which have been corrected. See below.
![HTML validation](docs/testing/html-validation-errors.png)

![HTML validation](docs/testing/html-validation-pass.png)

All pages are passing all checks.

#### CSS

The CSS file was checked using [W3C CSS Markup Validation Service](https://jigsaw.w3.org/css-validator/).

It was tested both via URI and direct input. No errors were found.
![CSS validation](docs/testing/css-validation-pass.png)

#### JavaScript

[JSHint](https://jshint.com/) was used to validate JavaScript code. 

"One undefined variable" was raised for 'Stripe', which now got corrected to 'stripe'. Also, 3 semicolons were found to be missing :)

However, changing 'Stripe' to 'stripe' broke Stripe's functionality, so it's been changed back to its original state.

The project's JavaScript code is now passing this validator.

#### Python

The [PEP8 online](http://pep8online.com/) validator website is currently not functional, so the Python code was checked by a PEP8 validator directly in my Gitpod Workspace. 

All errors (mostly 'Line too long') have been corrected, except the usual issue with Django adding the `objects`, `DoesNotExist` properties to all model classes, which the IDE is not aware of (e.g. `Class 'xyz' has no 'objects' member` and `Class 'zyx' has no 'DoesNotExist' member`). These are just warnings from pylint.
Same goes for `Instance of 'OneToOneField' has no 'username' member`. 

All classes have been given docstrings.

### User Stories Testing

### Continuous Testing - Issues and Resolutions to issues found during testing

During the development process, the application was continuously tested and bugs and issues that were found were resolved. A few examples:

* When a user redirected to a checkout view manually (without selecting a hike to book first), a 500 internal server error was raised. This was happening due to the view initially incorrectly checking whether a local storage existed. (Which it did since we were initialising it there.) The bug was fixed by checking for existence of a hike_id in the local storage instead, and now if it does not exist, the user will be brought back to all_hikes view to select a hike to book.

* After implementing a confirmation email sending after a successful purchase, the checkout process started failing with 500 error. Logging details into console revealed a bug in code - customer's email was being populated with the user, rather than the user's email. The fix was rather straightforward and payment process works ok now. 

### Known Bugs and Issues
