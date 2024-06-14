
### README.md spécifique à l'application `users`

```markdown
# Users Application

## Description

This application handles user registration, authentication, and password recovery for the Lushlyrics website.

## Features

1. **User Registration**: Users can create accounts with username and email validation.
2. **User Authentication**: Users can log in and log out of their accounts.
3. **Password Recovery**: Users can reset their passwords if they forget their credentials.

## Installation

1. Ensure you have Django installed.
2. Add the `users` app to your `INSTALLED_APPS` in `settings.py`.
3. Include the `users` URLs in your project's `urls.py`.

## Usage

### Registration

- URL: `/register/`
- Method: `POST`
- Form: `UserRegisterForm`

### Login

- URL: `/login/`
- Method: `POST`
- Form: `AuthenticationForm`

### Password Reset

- URL: `/password_reset/`
- Method: `POST`
- Form: `CustomPasswordResetForm`

## Templates

### Base Template

The `base_generic.html` file is the base template used across the application to maintain a consistent look and feel. All other templates extend this base template.

- **Location**: `users/templates/base_generic.html`

### Users Templates

- `register.html`: Registration form.
- `login.html`: Login form.
- `password_reset.html`: Password reset form.
- `password_reset_done.html`: Password reset done page.
- `password_reset_confirm.html`: Password reset confirmation page.
- `password_reset_complete.html`: Password reset complete page.

## Logging

Logs are configured for debugging purposes and can be found in the project's root directory.

## Contributing

If you wish to contribute to this application, please fork the repository and submit a pull request.

