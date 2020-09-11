import os, json
from datetime import datetime

# google api client modules
import google.oauth2.credentials
import google_auth_oauthlib.flow
import googleapiclient.discovery

# django dependencies
from django.shortcuts import render, HttpResponseRedirect, reverse
from django.utils import dateparse

SCOPES = ["https://www.googleapis.com/auth/youtube.force-ssl"]

# Disable OAuthlib's HTTPS verification when running locally.
# *DO NOT* leave this option enabled in production.
os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

API_SERVICE_NAME = "youtube"
API_VERSION  = "v3"
CLIENT_SECRETS_FILE = "client_secret.json"

# the session variables
state = credentials_dictionary = credentials_dictionary = authenticated = None

# utility functions
def search_youtube_api(query : str) -> dict:
    ''' data from youtube api '''
    global authenticated, credentials, credentials_dictionary

    if not authenticated:
        return HttpResponseRedirect(reverse(index))

    # Load credentials from the session.
    credentials = google.oauth2.credentials.Credentials(**credentials_dictionary)

    youtube = googleapiclient.discovery.build(
        API_SERVICE_NAME, API_VERSION, credentials=credentials
    )

    # Save credentials back to session in case access token was refreshed.
    # ACTION ITEM: In a production app, you likely want to save these
    #              credentials in a persistent database instead.
    credentials_dictionary = credentials_to_dict(credentials)

    # all reponse gathered
    result = {"items":[]}
    page_token = ""

    # number of iterations to gather limit amout of result
    for _ in range(200//50):
        request = youtube.search().list(
            part="snippet",
            maxResults=50,
            pageToken=page_token,
            order="date",
            q=query,
            type="video"
        )

        # search results json
        search_result_response = request.execute()

        # get videos from response check if items are available
        videos = search_result_response.get('items')
        if videos is None:
            break

        # gather all video ids (this double search is expensive as it cost twice as much quota)
        video_ids = ",".join([
                item["id"]["videoId"] for item in videos
            ]
        )
        
        # check if next_page_token is present and get it for the next result page on api
        page_token = search_result_response.get('nextPageToken')
        if page_token is None:
            break

        # the video details and stats
        request = youtube.videos().list(
            part="snippet,statistics",
            id=video_ids
        )

        # video details fetched from api
        video_details_response = request.execute()

        # update all the response
        result['items'].extend(video_details_response["items"])

    return result
    
def credentials_to_dict(credentials : object) -> dict:
    return {
        'token': credentials.token,
        'refresh_token': credentials.refresh_token,
        'token_uri': credentials.token_uri,
        'client_id': credentials.client_id,
        'client_secret': credentials.client_secret,
        'scopes': credentials.scopes
    }


# the endpoints/views for the urls.py
def authorize(request):
    ''' authorize the google user '''
    global state

    # Create flow instance to manage the OAuth 2.0 Authorization Grant Flow steps.
    flow = google_auth_oauthlib.flow.Flow.from_client_secrets_file(
        CLIENT_SECRETS_FILE, scopes=SCOPES
    )

    # The URI created here must exactly match one of the authorized redirect URIs
    # for the OAuth 2.0 client, which you configured in the API Console. If this
    # value doesn't match an authorized URI, you will get a 'redirect_uri_mismatch'
    # error.
    flow.redirect_uri = request.build_absolute_uri(location=reverse(oauth2callback))

    # Store the state so the callback can verify the auth server response.
    authorization_url, state = flow.authorization_url(
        # Enable offline access so that you can refresh an access token without
        # re-prompting the user for permission. Recommended for web server apps.
        access_type='offline',
        # Enable incremental authorization. Recommended as a best practice.
        include_granted_scopes='true'
    )

    return HttpResponseRedirect(authorization_url)

def index(request):
    ''' returns the index page (in this case no index page exists so it redirects to the serach page) '''

    global credentials_dictionary, authenticated

    if credentials_dictionary is None:
        return HttpResponseRedirect(reverse(authorize))

    authenticated = True
    return HttpResponseRedirect(reverse(search))

def oauth2callback(request):
    global credentials, credentials_dictionary
    # Get credentials and create an API client
    flow = google_auth_oauthlib.flow.Flow.from_client_secrets_file(
        CLIENT_SECRETS_FILE, 
        SCOPES,
    )

    flow.redirect_uri = request.build_absolute_uri(location=reverse(oauth2callback))
    
    # authorization_response = f"{request.build_absolute_uri()}&redirect_uri="
    authorization_response = request.build_absolute_uri()

    flow.fetch_token(authorization_response=authorization_response)

    credentials = flow.credentials
    credentials_dictionary = credentials_to_dict(credentials)

    return HttpResponseRedirect(reverse(index))

# Create your views here.
def search(request):
    ''' returns the html search page with an input field to receive query from user '''
    global authenticated

    if not authenticated:
        return HttpResponseRedirect(reverse(index))

    return render(request, "search.html")

# Create your views here.
def search_result(request):
    ''' returns the search result from searching youtube api as html response '''

    global authenticated

    if not authenticated:
        return HttpResponseRedirect(reverse(index))

    # initialize context dictionary
    context = {
        "search_query": "",
        "result": []
    }

    # search api only on get request
    if request.method == "GET":
        # update the search query value
        context["search_query"] = search_query = request.GET.get("search_query", "")

        try:
            # call the api
            result = search_youtube_api(search_query)

            context["result"] = [
                {
                    "title": item["snippet"]["title"],
                    "channel_name": item["snippet"]["channelTitle"],
                    "number_of_views": item["statistics"]["viewCount"],
                    "description": item["snippet"]["description"],
                    "upload_date": dateparse.parse_datetime(item["snippet"]["publishedAt"]),
                    "video_id": item["id"],
                    "thumbnail_url": item["snippet"]["thumbnails"]["high"]["url"]

                } for item in result['items']
            ]

            print(len(context['result']), "results found")

        except Exception as e:
            print(e)
            
    return render(request, "search_result.html", context)