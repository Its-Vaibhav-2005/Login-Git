# Flask GitHub OAuth App

This repository provides a practical example of integrating **GitHub OAuth authentication** into a Flask web application using the `Flask-Dance` library. With this setup, users can:

- **Log in** securely using their GitHub accounts.
- **View** their profile information, including details like username, avatar, and bio.
- **Access** and explore their repositories directly from the application.

The implementation showcases how to handle OAuth flows, manage user sessions, and interact with the GitHub API to fetch and display relevant data. This can serve as a foundational guide for developers looking to add GitHub authentication and repository management features to their Flask projects.

---

## Features

- **GitHub OAuth Login:** Allows users to log in securely using their GitHub accounts through GitHub's OAuth 2.0 protocol.
- **Session Management:** Efficiently stores and manages user session data, including the GitHub username and profile information.
- **Fetch Repositories:** Retrieves and displays a list of the authenticated user's GitHub repositories.
- **Dynamic Pages:** Generates and renders personalized content dynamically after the user has logged in.
- **Flask-Dance Integration:** Simplifies the setup and integration of OAuth with GitHub, making the development process smoother.

---

## How It Works

1. **Login:** Users visit the login page and authenticate using their GitHub credentials.
2. **Fetch Data:** Once logged in, the app retrieves the user's profile details and list of repositories from GitHub.
3. **View Information:** Authenticated users can then view their profile information and explore their repositories on the main page.
4. **Session Management:** The app manages sessions to keep user information available throughout their visit.
5. **Logout:** Users can log out at any time to clear their session and end the authenticated state.

---

## File Structure

The project is organized into the following files and directories:

- **`app.py`**: This is the main application file. It contains the code that handles various routes and integrates GitHub OAuth authentication.

- **`templates/`**: This directory contains the HTML templates used for rendering different pages of the application.
  - **`login.html`**: The login page that prompts users to authenticate using their GitHub credentials.
  - **`index.html`**: The main page where authenticated users can view their profile information and explore their repositories.

Here's a visual representation of the file structure:

```
project-root/
│
├── app.py
│
└── templates/
    ├── login.html
    └── index.html
```

This structure helps keep the code organized and makes it easier to manage and understand the different components of the application.

---

## Environment Variables
The app uses `os.environ` for environment-specific settings.  
- **`OAUTHLIB_INSECURE_TRANSPORT`**: Allows HTTP communication for local testing.
- Replace the placeholders for `client_id` and `client_secret` with values from your GitHub OAuth app.

---

## Prerequisites
- A GitHub account.
- A GitHub OAuth App with `client_id` and `client_secret`.
- Python installed with Flask and Flask-Dance libraries.

---

## Usage
1. Register a GitHub OAuth app at the [GitHub Developer Portal](https://github.com/settings/developers).
2. Replace the `client_id` and `client_secret` in `app.py` with your app credentials.
3. Run the Flask app locally and access it through your browser.

---

## Key Routes
- **`/log-in`**: Initiates the login process with GitHub OAuth.
- **`/log-out`**: Clears the user session and logs out.
- **`/login-req`**: Displays the login page.
- **`/callback`**: Handles the callback after GitHub authorization.
- **`/` or `/main`**: Displays the main page with user profile and repositories.

---

## Contact
For questions or feedback, please reach out via [GitHub](https://github.com/Its-Vaibhav-2005/) or [Email](vaibhav.test.api@gmail.com).
