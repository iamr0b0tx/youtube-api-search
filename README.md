# Youtube-API-Search
A Django web application to search YouTube API. The web application has a search box where user can input search text and a search button to click afterwards to initiate the search. When the button is clicked and the search query is submitted then it leads the user to a page displaying the results of the search.

## How to Set up
For this repository code to work you will need the following tools/softwares installed __Note__: the __*__ indicates the tool/software is required!.
- *Python 3.6+ (Download [here](https://www.python.org/downloads/), instructions [here](https://realpython.com/installing-python/))
- *pip (Set up instructions [here](https://www.liquidweb.com/kb/install-pip-windows/) or [here](https://packaging.python.org/tutorials/installing-packages/#ensure-you-can-run-pip-from-the-command-line))
- Git (Download [here](https://git-scm.com/downloads))
- virtualenv (Set up instructions [here](https://packaging.python.org/tutorials/installing-packages/#creating-virtual-environments))

### Prerequisites
You can check [here](https://developers.google.com/youtube/v3/guides/auth/server-side-web-apps) for more info on this section

#### Enable APIs for your project
Any application that calls Google APIs needs to enable those APIs in the API Console.

To enable an API for your project:

1. Open the API Library in the Google API Console.
2. If prompted, select a project, or create a new one.
3. Use the Library page to find and enable the YouTube Data API. Find any other APIs that your application will use and enable those, too.

#### Create authorization credentials
Any application that uses OAuth 2.0 to access Google APIs must have authorization credentials that identify the application to Google's OAuth 2.0 server. The following steps explain how to create credentials for your project. Your applications can then use the credentials to access APIs that you have enabled for that project.

1. Go to the Credentials page.
2. Click Create credentials > OAuth client ID.
3. Select the Web application application type.
4. Fill in the form and click Create. Applications must specify authorized redirect URIs. The redirect URIs are the endpoints to which the OAuth 2.0 server can send responses.
For testing, you can specify URIs that refer to the local machine, such as http://127.0.0.1:8000/oauth2callback. With that in mind, please note that all of the examples in this document use http://localhost:8000/oauth2callback as the redirect URI.

We recommend that you design your app's auth endpoints so that your application does not expose authorization codes to other resources on the page.

After creating your credentials, download the client_secret.json file from the API Console. Securely store the file in a location that only your application can access. In this case will be your project folder __youtube-api-search__.

### Set up steps
1. Open your CLI (Terminal for linux users and Command prompt for windows users)
2. Navigate to your home/Desktop directory for linux/windows users
    - #### Linux Users
    ```
    cd ~
    ```

    - #### Windows Users
    ```
    cd %userprofile%/Desktop
    ```

3. If you have Git installed simply type the following commands (for both windows and linux users)
```
git clone https://github.com/iamr0b0tx/youtube-api-search
cd youtube-api-search
```

For those that don't have git pre-installed simply click the code button above and click __Download ZIP__. Once the Zip file download is complete, extract the contents to the home directory (for linux users) or Desktop (for windows users). You should have a directory/folder namesd youtube-api-search-master which you should rename to youtube-api-search.

4. Make sure to transfer your client_secret.json file to your youtube-api-search folder. Also amke sure the client_secret.json file has that exact name, client_secret.json.

5. This step is optional but advised. Set up your virtualenv and activate it by running the following commands
    - #### Windiws Users
    ```
    virtualenv venv
    venv\Scripts\activate
    ```

    - #### Linux Users
    ```
    virtualenv venv
    source venv/bin/activate
    ```
Once that is done your next terminal prompt will be prefixed with this __(venv)__. For example,
```C:\Users\christian\Desktop\youtube-api-search>``` 
will become 
```(venv) C:\Users\christian\Desktop\youtube-api-search>```
By the way, the name __venv__ can be changed to a different word/name but we will be using venv in this setup instructions.

6. Upgrade your pip by typing the following command
```
python -m pip install pip --upgrade
```

7. Install all python modules in requirements.txt file by typing the following file
```
pip install -r requirements.txt
```

8. Once all packages have been successfully installed run the following command
```
python manage.py runserver
```
it will output a url looking like this ```http://127.0.0.1:8000```, visit the url to interact with the application


## References
1. [Using OAuth 2.0 for Web Server Applications](https://developers.google.com/youtube/v3/guides/auth/server-side-web-apps)
2. [Python 3 Installation & Setup Guide](https://realpython.com/installing-python/)
3. [How to Install PIP on Windows](https://www.liquidweb.com/kb/install-pip-windows/)
4. [Installing Packages (in python)](https://packaging.python.org/tutorials/installing-packages/)