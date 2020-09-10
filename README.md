# Youtube-API-Search
A Django web application to search YouTube API. The web application has a search box where user can input search text and a search button to click afterwards to initiate the search. When the button is clicked and the search query is submitted then it leads the user to a page displaying the results of the search.

## How to Set up
For this repository code to work you will need the following tools/softwares installed __Note__: the __*__ indicates the tool/software is required!.
- *Python 3.6+ (Download [here]())
- *pip (Set up instructions [here]())
- Git (Download [here]())
- virtualenv (Set up instructions [here]())

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

For those that don't have git pre-installed simply click the code button above and click __Download ZIP__. Once the Zip file download is complete, extarct the contents to the home directory (for linux users) or Desktop (for windows users). You should have a directory/folder namesd youtube-api-search-master which you should rename to youtube-api-search.

4. This step is optional but advisable. Set up your virtualenv and activate it by running the following commands
    - #### Linux Users
    ```
    virtualenv venv
    venv\Scripts\activate
    ```

    - #### Windows Users
    ```
    virtualenv venv
    source venv/bin/activate
    ```
Once that is done your next terminal prompt will be prefixed with this __(venv)__. For example,
```C:\Users\christian\Desktop\youtube-api-search>``` 
will become 
```(venv) C:\Users\christian\Desktop\youtube-api-search>```
By the way, the name __venv__ can be changed to a different word/name but we will be using venv in this setup instructions.

5. Upgrade your pip by typing the following command
```
python -m pip install pip --upgrade
```

6. Install all python modules in requirements.txt file by typing the following file
```
pip install -r requirements.txt
```

7. Once all packages have been successfully installed run the following command
```
python manage.py runserver
```
it will output a url looking like this ```http://127.0.0.1:8000```, visit the url to interact with the application

