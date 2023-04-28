# oidc-python-flask

OpenID Connect Client implementation using Python and Flask

This project is meant to provide a starting point for building a website using python and flask that is secured using OpenID Connect.
Functionality is initially limited to a home page that displays **login**, **logout**, and **profile** links. The profile page will 
display the currently authenticated user's userinfo extracted from their [id_token](https://auth0.com/blog/id-token-access-token-what-is-the-difference/). 

## Requirements

- [Python 3.x](https://www.python.org/)
- [pip](https://pypi.org/project/pip/)
- [venv](https://docs.python.org/3/library/venv.html) or [virtualenv](https://virtualenv.pypa.io/en/stable/)

Depending on your Operating System and envirinment you may need to install these tools yourself. Google is your friend.

Note: For Windows WSL see [this article](https://medium.com/@rhdzmota/python-development-on-the-windows-subsystem-for-linux-wsl-17a0fa1839d)

## Dependencies

- [Flask](https://flask.palletsprojects.com/en/2.3.x/)
- [AuthLib](https://authlib.org/)
- [python-dotenv](https://pypi.org/project/python-dotenv/)
- [requests](https://pypi.org/project/requests/)

Note: Most of the OIDC functionality in this project is provided by AuthLib. 

## Getting Started

If you are using [vscode](https://code.visualstudio.com/) and have the [python extension](https://marketplace.visualstudio.com/items?itemName=ms-python.python)
you should see a **Create Environment...** button if you click on the `requirements.txt` file. See [Creating Environments](https://code.visualstudio.com/docs/python/environments#_creating-environments) for additional help. This method requires [venv](https://docs.python.org/3/library/venv.html).

If you are using a different editor or prefer to do things in a shell you can use the following resources:
- [Python: How To Create, Activate, Deactivate, And Delete Virtual Environments](https://python.land/virtual-environments/virtualenv)
- [How to install Python packages with pip and requirements.txt](https://note.nkmk.me/en/python-pip-install-requirements/)

## Configuration

All configuration for this project is done using a [.env](https://blog.bitsrc.io/a-gentle-introduction-to-env-files-9ad424cc5ff4) file. You can start by renaming
the file `.example.env` to `.env` and then providing the missing values described below. The values that start with `OIDC_` must be acquired from your OpenID Connect provider.

| Variable                 | Description                                                                                                                                |
|--------------------------|--------------------------------------------------------------------------------------------------------------------------------------------|
| SECRET_KEY               | Signing key for authenticating session cookie. Set to a strong random value.                                                               |
| OIDC_SERVER_METADATA_URL | The [OpenID Connect Discovery](https://swagger.io/docs/specification/authentication/openid-connect-discovery/) url for your OIDC Provider. |
| OIDC_CLIENT_ID           | The [Oauth2 Client ID](https://www.oauth.com/oauth2-servers/client-registration/client-id-secret/) from your client.                       |
| OIDC_CLIENT_SECRET       | The [Oauth2 Client Secret](https://www.oauth.com/oauth2-servers/client-registration/client-id-secret/) from your client.                   |
| OIDC_API_BASE_URL        | This is set to `http://localhost:3000` by default, but it **MUST** match the value defined for your client in your OIDC Provider settings. |
| OIDC_CLIENT_KWARGS       | The defaults should work as is for most OIDC Providers. If not you will have to work through the issue with your provider.                 |

Other configuration values may be needed depending on your OpenID Provider. See the AuthLib [documentation](https://docs.authlib.org/en/latest/) for help with other options.

## Development

Once you have finished updating your configuration you can run your website locally by executing `flask run` in your terminal shell.
