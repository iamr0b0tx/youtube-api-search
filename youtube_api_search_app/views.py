from django.shortcuts import render, HttpResponseRedirect, reverse

# Create your views here.
def index(request):
    ''' returns the index page (in this case no index page exists so it redirects to the serach page) '''
    return HttpResponseRedirect(reverse(search))

# Create your views here.
def search(request):
    ''' returns the html search page with an input field to receive query from user '''
    return render(request, "search.html")

# Create your views here.
def search_result(request):
    ''' returns the search result from searching youtube api as html response '''

    # initialize context dictionary
    context = {
        "search_query": "",
        "result": []
    }

    # search api only on get request
    if request.method == "GET":
        # update the search query value
        context["search_query"] = search_query = request.GET.get("search_query", "")

        result = {
            "kind": "youtube#searchListResponse",
            "etag": "S0cfPzkhGWdqtFBqE9JZNOG2paI",
            "nextPageToken": "CDIQAA",
            "regionCode": "NG",
            "pageInfo": {
                "totalResults": 1000000,
                "resultsPerPage": 50
            },
            "items": [
                {
                "kind": "youtube#searchResult",
                "etag": "2vU7vNbwPPcQwpOON4_5g8NEdmk",
                "id": {
                    "kind": "youtube#video",
                    "videoId": "vuSMk6jtUdw"
                },
                "snippet": {
                    "publishedAt": "2020-09-11T06:39:00Z",
                    "channelId": "UCG8jk5TBxSVuHK-0Jv8JwQw",
                    "title": "11.9.20 מצב הים ותחזית בוקר שישי Israel Surf Report",
                    "description": "עדכוני מצב הים וסרטוני גלישה - מוזמנים לעקוב \u200f\u200e\u200fVideos of surfing from israel - SUBSCRIBE \u200fhttp://www.youtube.com/c/SurfingIsrael4K?sub_confirmation=1 ...",
                    "thumbnails": {
                    "default": {
                        "url": "https://i.ytimg.com/vi/vuSMk6jtUdw/default.jpg",
                        "width": 120,
                        "height": 90
                    },
                    "medium": {
                        "url": "https://i.ytimg.com/vi/vuSMk6jtUdw/mqdefault.jpg",
                        "width": 320,
                        "height": 180
                    },
                    "high": {
                        "url": "https://i.ytimg.com/vi/vuSMk6jtUdw/hqdefault.jpg",
                        "width": 480,
                        "height": 360
                    }
                    },
                    "channelTitle": "Surfing Israel 4K",
                    "liveBroadcastContent": "none",
                    "publishTime": "2020-09-11T06:39:00Z"
                }
                },
                {
                "kind": "youtube#searchResult",
                "etag": "uNOzagARYe7txA5dXCR2xf7gHcM",
                "id": {
                    "kind": "youtube#video",
                    "videoId": "wBXTqtZ1p30"
                },
                "snippet": {
                    "publishedAt": "2020-09-10T16:05:42Z",
                    "channelId": "UCXTZALB1hZ4H-vcr-zPi38Q",
                    "title": "Surfing and Diving in Fiji with Kieran Anderson",
                    "description": "Kieran Anderson shows off the beautiful waters and underwater reefs of Fiji from his last trip! Check out the views as he takes us along his surfing and diving ...",
                    "thumbnails": {
                    "default": {
                        "url": "https://i.ytimg.com/vi/wBXTqtZ1p30/default.jpg",
                        "width": 120,
                        "height": 90
                    },
                    "medium": {
                        "url": "https://i.ytimg.com/vi/wBXTqtZ1p30/mqdefault.jpg",
                        "width": 320,
                        "height": 180
                    },
                    "high": {
                        "url": "https://i.ytimg.com/vi/wBXTqtZ1p30/hqdefault.jpg",
                        "width": 480,
                        "height": 360
                    }
                    },
                    "channelTitle": "Salt Life",
                    "liveBroadcastContent": "none",
                    "publishTime": "2020-09-10T16:05:42Z"
                }
                },
                {
                "kind": "youtube#searchResult",
                "etag": "FYuTqSzYLI2l5grE73RBc8IH9zA",
                "id": {
                    "kind": "youtube#video",
                    "videoId": "1zaYcBtNUO4"
                },
                "snippet": {
                    "publishedAt": "2020-09-10T15:50:55Z",
                    "channelId": "UCznv7Vf9nBdJYvBagFdAHWw",
                    "title": "Kelly Slater — The Surfing Legend on Routine, Favorite Books, and Setbacks | The Tim Ferriss Show",
                    "description": "Kelly Slater — The Surfing Legend on Routine, Rickson Gracie, Favorite Books, and Overcoming Setbacks | Brought to you by Dry Farm Wines ...",
                    "thumbnails": {
                    "default": {
                        "url": "https://i.ytimg.com/vi/1zaYcBtNUO4/default.jpg",
                        "width": 120,
                        "height": 90
                    },
                    "medium": {
                        "url": "https://i.ytimg.com/vi/1zaYcBtNUO4/mqdefault.jpg",
                        "width": 320,
                        "height": 180
                    },
                    "high": {
                        "url": "https://i.ytimg.com/vi/1zaYcBtNUO4/hqdefault.jpg",
                        "width": 480,
                        "height": 360
                    }
                    },
                    "channelTitle": "Tim Ferriss",
                    "liveBroadcastContent": "none",
                    "publishTime": "2020-09-10T15:50:55Z"
                }
                },
                {
                "kind": "youtube#searchResult",
                "etag": "JJNV5xPSq3X7Ehcy3u4D-lVKNB8",
                "id": {
                    "kind": "youtube#video",
                    "videoId": "Q-fnDbYLbL8"
                },
                "snippet": {
                    "publishedAt": "2020-09-10T15:00:11Z",
                    "channelId": "UC_wCbFZHCh9amfaXXI4yq_g",
                    "title": "Riding Gnarly Trails in Canada&#39;s top Surf Town",
                    "description": "I love surfing, but I'm not sure that there is much better than surfing and riding on the same day! Click here to support my channel and help me to do more edits ...",
                    "thumbnails": {
                    "default": {
                        "url": "https://i.ytimg.com/vi/Q-fnDbYLbL8/default.jpg",
                        "width": 120,
                        "height": 90
                    },
                    "medium": {
                        "url": "https://i.ytimg.com/vi/Q-fnDbYLbL8/mqdefault.jpg",
                        "width": 320,
                        "height": 180
                    },
                    "high": {
                        "url": "https://i.ytimg.com/vi/Q-fnDbYLbL8/hqdefault.jpg",
                        "width": 480,
                        "height": 360
                    }
                    },
                    "channelTitle": "Rémy Métailler",
                    "liveBroadcastContent": "none",
                    "publishTime": "2020-09-10T15:00:11Z"
                }
                },
                {
                "kind": "youtube#searchResult",
                "etag": "9hcr2QWlHmP31iCHa5EhCgsHTAE",
                "id": {
                    "kind": "youtube#video",
                    "videoId": "3bSlPzyuDfM"
                },
                "snippet": {
                    "publishedAt": "2020-09-10T09:33:44Z",
                    "channelId": "UC_gUM8rL-Lrg6O3adPW9K1g",
                    "title": "4 year old Brazilian surfing Prodigy stuns the world with his smooth moves | WION News",
                    "description": "4 year old Brazilian surfing Prodigy stuns the world with his smooth moves A 4-year-old Brazilian boy has carved his way through the sea at a very young age as ...",
                    "thumbnails": {
                    "default": {
                        "url": "https://i.ytimg.com/vi/3bSlPzyuDfM/default.jpg",
                        "width": 120,
                        "height": 90
                    },
                    "medium": {
                        "url": "https://i.ytimg.com/vi/3bSlPzyuDfM/mqdefault.jpg",
                        "width": 320,
                        "height": 180
                    },
                    "high": {
                        "url": "https://i.ytimg.com/vi/3bSlPzyuDfM/hqdefault.jpg",
                        "width": 480,
                        "height": 360
                    }
                    },
                    "channelTitle": "WION",
                    "liveBroadcastContent": "none",
                    "publishTime": "2020-09-10T09:33:44Z"
                }
                },
                {
                "kind": "youtube#searchResult",
                "etag": "JJPn6wZZMD1DbwYLCNCjwhDShoU",
                "id": {
                    "kind": "youtube#video",
                    "videoId": "5XBL1mgeRpw"
                },
                "snippet": {
                    "publishedAt": "2020-09-10T07:53:23Z",
                    "channelId": "UCG8jk5TBxSVuHK-0Jv8JwQw",
                    "title": "10.9.20 גולשים חמישי בוקר Surfing Israel",
                    "description": "עדכוני מצב הים וסרטוני גלישה - מוזמנים לעקוב \u200f\u200e\u200fVideos of surfing from israel - SUBSCRIBE \u200fhttp://www.youtube.com/c/SurfingIsrael4K?sub_confirmation=1 ...",
                    "thumbnails": {
                    "default": {
                        "url": "https://i.ytimg.com/vi/5XBL1mgeRpw/default.jpg",
                        "width": 120,
                        "height": 90
                    },
                    "medium": {
                        "url": "https://i.ytimg.com/vi/5XBL1mgeRpw/mqdefault.jpg",
                        "width": 320,
                        "height": 180
                    },
                    "high": {
                        "url": "https://i.ytimg.com/vi/5XBL1mgeRpw/hqdefault.jpg",
                        "width": 480,
                        "height": 360
                    }
                    },
                    "channelTitle": "Surfing Israel 4K",
                    "liveBroadcastContent": "none",
                    "publishTime": "2020-09-10T07:53:23Z"
                }
                },
                {
                "kind": "youtube#searchResult",
                "etag": "7_XozcVC9qt95FjDLd_j3Nw3Vbk",
                "id": {
                    "kind": "youtube#video",
                    "videoId": "bZgk68YFhS0"
                },
                "snippet": {
                    "publishedAt": "2020-09-10T06:14:48Z",
                    "channelId": "UCG8jk5TBxSVuHK-0Jv8JwQw",
                    "title": "10.9.20 סוול חדש נכנס - מצב הים בוקר חמישי גלים Israel Surf Report",
                    "description": "עדכוני מצב הים וסרטוני גלישה - מוזמנים לעקוב \u200f\u200e\u200fVideos of surfing from israel - SUBSCRIBE \u200fhttp://www.youtube.com/c/SurfingIsrael4K?sub_confirmation=1 ...",
                    "thumbnails": {
                    "default": {
                        "url": "https://i.ytimg.com/vi/bZgk68YFhS0/default.jpg",
                        "width": 120,
                        "height": 90
                    },
                    "medium": {
                        "url": "https://i.ytimg.com/vi/bZgk68YFhS0/mqdefault.jpg",
                        "width": 320,
                        "height": 180
                    },
                    "high": {
                        "url": "https://i.ytimg.com/vi/bZgk68YFhS0/hqdefault.jpg",
                        "width": 480,
                        "height": 360
                    }
                    },
                    "channelTitle": "Surfing Israel 4K",
                    "liveBroadcastContent": "none",
                    "publishTime": "2020-09-10T06:14:48Z"
                }
                },
                {
                "kind": "youtube#searchResult",
                "etag": "G-4GO-UV0Kr_CHKd5lDPwqly318",
                "id": {
                    "kind": "youtube#video",
                    "videoId": "CQ50lLNO0Uw"
                },
                "snippet": {
                    "publishedAt": "2020-09-10T04:52:59Z",
                    "channelId": "UCx84l7oNMRuJ_GTRioq4Byg",
                    "title": "POV SURF RAW: RIVER SURFING IN BEND Oregon (BEST RIVER WAVE) SURFING IN THE MIDDLE OF OREGON - gopro",
                    "description": "Join me on my Surf Trip up north for empty and unusual waves, in this video I surf the RIVER WAVE in BEND OREGON and have a blast chatting with some local ...",
                    "thumbnails": {
                    "default": {
                        "url": "https://i.ytimg.com/vi/CQ50lLNO0Uw/default.jpg",
                        "width": 120,
                        "height": 90
                    },
                    "medium": {
                        "url": "https://i.ytimg.com/vi/CQ50lLNO0Uw/mqdefault.jpg",
                        "width": 320,
                        "height": 180
                    },
                    "high": {
                        "url": "https://i.ytimg.com/vi/CQ50lLNO0Uw/hqdefault.jpg",
                        "width": 480,
                        "height": 360
                    }
                    },
                    "channelTitle": "Loren Bird",
                    "liveBroadcastContent": "none",
                    "publishTime": "2020-09-10T04:52:59Z"
                }
                },
                {
                "kind": "youtube#searchResult",
                "etag": "7-fNzzK3xnZQozSrssdXp2mcQ48",
                "id": {
                    "kind": "youtube#video",
                    "videoId": "RwaJPrkLhOQ"
                },
                "snippet": {
                    "publishedAt": "2020-09-10T04:52:27Z",
                    "channelId": "UCBwN7WtBF-LQxvdisAk9lIQ",
                    "title": "Uncrowded Waves At One Of Indo&#39;s Funnest Points - Ujung Bocur - Surfing Sumatra, September 2020",
                    "description": "Ujung Bocur is undoubtedly one of Indonesia's funnest point breaks. Offering long rippable walls and the occasional barrel section, most surfers really like the ...",
                    "thumbnails": {
                    "default": {
                        "url": "https://i.ytimg.com/vi/RwaJPrkLhOQ/default.jpg",
                        "width": 120,
                        "height": 90
                    },
                    "medium": {
                        "url": "https://i.ytimg.com/vi/RwaJPrkLhOQ/mqdefault.jpg",
                        "width": 320,
                        "height": 180
                    },
                    "high": {
                        "url": "https://i.ytimg.com/vi/RwaJPrkLhOQ/hqdefault.jpg",
                        "width": 480,
                        "height": 360
                    }
                    },
                    "channelTitle": "Always Left - Indo Surf Content",
                    "liveBroadcastContent": "none",
                    "publishTime": "2020-09-10T04:52:27Z"
                }
                },
                {
                "kind": "youtube#searchResult",
                "etag": "eNv6773nZ5jXY2Ol7LgAQGBwNIQ",
                "id": {
                    "kind": "youtube#video",
                    "videoId": "3wbhLs0QxG4"
                },
                "snippet": {
                    "publishedAt": "2020-09-10T01:07:23Z",
                    "channelId": "UCn7s1bTIbscwY0w65U7WFAw",
                    "title": "Surfing. Fails, Bails, Carnage &amp; Wipeouts From The Gold Coast 2020",
                    "description": "Surfing. Fails, Bails, Carnage & Wipeouts From The Gold Coast 2020. All the ugly fun stuff so far this year Music: We Move Like Giants ...",
                    "thumbnails": {
                    "default": {
                        "url": "https://i.ytimg.com/vi/3wbhLs0QxG4/default.jpg",
                        "width": 120,
                        "height": 90
                    },
                    "medium": {
                        "url": "https://i.ytimg.com/vi/3wbhLs0QxG4/mqdefault.jpg",
                        "width": 320,
                        "height": 180
                    },
                    "high": {
                        "url": "https://i.ytimg.com/vi/3wbhLs0QxG4/hqdefault.jpg",
                        "width": 480,
                        "height": 360
                    }
                    },
                    "channelTitle": "surfonmars",
                    "liveBroadcastContent": "none",
                    "publishTime": "2020-09-10T01:07:23Z"
                }
                },
                {
                "kind": "youtube#searchResult",
                "etag": "V5R-B63gYu_e05GKFAuKfWHJN5U",
                "id": {
                    "kind": "youtube#video",
                    "videoId": "1ciKjgb-yo8"
                },
                "snippet": {
                    "publishedAt": "2020-09-09T20:41:49Z",
                    "channelId": "UCVSNOxehfALut52NbkfRBaA",
                    "title": "Surfer in Spain Arrested for Breaching Quarantine",
                    "description": "A woman was arrested while surfing in northern Spain, Monday, September 7, because she was not self-isolating with a positive coronavirus test, according to ...",
                    "thumbnails": {
                    "default": {
                        "url": "https://i.ytimg.com/vi/1ciKjgb-yo8/default.jpg",
                        "width": 120,
                        "height": 90
                    },
                    "medium": {
                        "url": "https://i.ytimg.com/vi/1ciKjgb-yo8/mqdefault.jpg",
                        "width": 320,
                        "height": 180
                    },
                    "high": {
                        "url": "https://i.ytimg.com/vi/1ciKjgb-yo8/hqdefault.jpg",
                        "width": 480,
                        "height": 360
                    }
                    },
                    "channelTitle": "VOA News",
                    "liveBroadcastContent": "none",
                    "publishTime": "2020-09-09T20:41:49Z"
                }
                },
                {
                "kind": "youtube#searchResult",
                "etag": "5MlHyLOAc8_nc0KHqgLsp8M56Yw",
                "id": {
                    "kind": "youtube#video",
                    "videoId": "9YMS2P_ZHSc"
                },
                "snippet": {
                    "publishedAt": "2020-09-09T18:10:40Z",
                    "channelId": "UCsopuR4Uw3TSA1VPY0MyAfQ",
                    "title": "VLOG! Surfing, Favorite Books, Hiking &amp; More",
                    "description": "NEW VIDEO! My computer breaking, learning to surf, current books & more! #fableticsambassador Become a Fabletics VIP Member + get 2 leggings for $24: ...",
                    "thumbnails": {
                    "default": {
                        "url": "https://i.ytimg.com/vi/9YMS2P_ZHSc/default.jpg",
                        "width": 120,
                        "height": 90
                    },
                    "medium": {
                        "url": "https://i.ytimg.com/vi/9YMS2P_ZHSc/mqdefault.jpg",
                        "width": 320,
                        "height": 180
                    },
                    "high": {
                        "url": "https://i.ytimg.com/vi/9YMS2P_ZHSc/hqdefault.jpg",
                        "width": 480,
                        "height": 360
                    }
                    },
                    "channelTitle": "Claudia Sulewski",
                    "liveBroadcastContent": "none",
                    "publishTime": "2020-09-09T18:10:40Z"
                }
                },
                {
                "kind": "youtube#searchResult",
                "etag": "guWIPpB06Fn5d8HVX4p3MFaO73U",
                "id": {
                    "kind": "youtube#video",
                    "videoId": "_qbPlSXat4w"
                },
                "snippet": {
                    "publishedAt": "2020-09-09T18:00:06Z",
                    "channelId": "UC_F4Iy5korq2mEWZDQhG07w",
                    "title": "SURFING CALIFORNIA&#39;S HEAT WAVE! || EPIC NEWPORT BEACH! Cali pt.3",
                    "description": "THANK YOU CALIFORNIA WE LOVE YOU! Some really fun waves in Newport and good times with everyone in YEWWWport. Buy a sticker rep the Brand.",
                    "thumbnails": {
                    "default": {
                        "url": "https://i.ytimg.com/vi/_qbPlSXat4w/default.jpg",
                        "width": 120,
                        "height": 90
                    },
                    "medium": {
                        "url": "https://i.ytimg.com/vi/_qbPlSXat4w/mqdefault.jpg",
                        "width": 320,
                        "height": 180
                    },
                    "high": {
                        "url": "https://i.ytimg.com/vi/_qbPlSXat4w/hqdefault.jpg",
                        "width": 480,
                        "height": 360
                    }
                    },
                    "channelTitle": "Koa Rothman",
                    "liveBroadcastContent": "none",
                    "publishTime": "2020-09-09T18:00:06Z"
                }
                },
                {
                "kind": "youtube#searchResult",
                "etag": "78-MJmEy-Jhax_r92_3LpkI4gQc",
                "id": {
                    "kind": "youtube#video",
                    "videoId": "X5aQl2cRl5g"
                },
                "snippet": {
                    "publishedAt": "2020-09-09T15:49:27Z",
                    "channelId": "UC86dbj-lbDks_hZ5gRKL49Q",
                    "title": "Spanish woman arrested for breaching quarantine to go surfing | AFP",
                    "description": "A woman who went surfing when she should have been self-isolating after testing positive for Covid-19 is arrested on a beach in San Sebastian in northern ...",
                    "thumbnails": {
                    "default": {
                        "url": "https://i.ytimg.com/vi/X5aQl2cRl5g/default.jpg",
                        "width": 120,
                        "height": 90
                    },
                    "medium": {
                        "url": "https://i.ytimg.com/vi/X5aQl2cRl5g/mqdefault.jpg",
                        "width": 320,
                        "height": 180
                    },
                    "high": {
                        "url": "https://i.ytimg.com/vi/X5aQl2cRl5g/hqdefault.jpg",
                        "width": 480,
                        "height": 360
                    }
                    },
                    "channelTitle": "AFP News Agency",
                    "liveBroadcastContent": "none",
                    "publishTime": "2020-09-09T15:49:27Z"
                }
                },
                {
                "kind": "youtube#searchResult",
                "etag": "-9xzYLd7HOTidNBHf1oLsyZTNpU",
                "id": {
                    "kind": "youtube#video",
                    "videoId": "a7WRVYEuIOE"
                },
                "snippet": {
                    "publishedAt": "2020-09-09T15:10:12Z",
                    "channelId": "UCIzXayRP7-P0ANpq-nD-h5g",
                    "title": "Surfer killed in shark attack on Australia&#39;s Gold Coast",
                    "description": "This is the horrific moment an estate agent is killed by a great white shark as other surfers try to save his life by dragging him to shore. Nick Slater, 46, was ...",
                    "thumbnails": {
                    "default": {
                        "url": "https://i.ytimg.com/vi/a7WRVYEuIOE/default.jpg",
                        "width": 120,
                        "height": 90
                    },
                    "medium": {
                        "url": "https://i.ytimg.com/vi/a7WRVYEuIOE/mqdefault.jpg",
                        "width": 320,
                        "height": 180
                    },
                    "high": {
                        "url": "https://i.ytimg.com/vi/a7WRVYEuIOE/hqdefault.jpg",
                        "width": 480,
                        "height": 360
                    }
                    },
                    "channelTitle": "The Sun",
                    "liveBroadcastContent": "none",
                    "publishTime": "2020-09-09T15:10:12Z"
                }
                },
                {
                "kind": "youtube#searchResult",
                "etag": "h_sJpdylquSpWKcBnyZCIYlzQB0",
                "id": {
                    "kind": "youtube#video",
                    "videoId": "pZsMLKXEDwc"
                },
                "snippet": {
                    "publishedAt": "2020-09-09T11:30:24Z",
                    "channelId": "UCUhpu5MJQ_bjPkXO00jyxsw",
                    "title": "Clip: An Qi Is Suddenly In Danger! | Summer Surf Shop EP09  | 夏日冲浪店 | iQIYI",
                    "description": "【Summer Surf Shop】is trending on iQIYI with multiple subtitles. Watch more episodes for FREE & ONLY on iQIYI App or Website! App: https://bit.ly/iqapps ...",
                    "thumbnails": {
                    "default": {
                        "url": "https://i.ytimg.com/vi/pZsMLKXEDwc/default.jpg",
                        "width": 120,
                        "height": 90
                    },
                    "medium": {
                        "url": "https://i.ytimg.com/vi/pZsMLKXEDwc/mqdefault.jpg",
                        "width": 320,
                        "height": 180
                    },
                    "high": {
                        "url": "https://i.ytimg.com/vi/pZsMLKXEDwc/hqdefault.jpg",
                        "width": 480,
                        "height": 360
                    }
                    },
                    "channelTitle": "iQIYI 爱奇艺",
                    "liveBroadcastContent": "none",
                    "publishTime": "2020-09-09T11:30:24Z"
                }
                },
                {
                "kind": "youtube#searchResult",
                "etag": "mH2Fx9RviazcowfKcSVbOZJ-Myk",
                "id": {
                    "kind": "youtube#video",
                    "videoId": "X7ySp3y_eNQ"
                },
                "snippet": {
                    "publishedAt": "2020-09-09T11:00:12Z",
                    "channelId": "UCzcQOTuXYGuCvTekySb_CeQ",
                    "title": "Cleaned Up Uluwatu - 6 September 2020",
                    "description": "After a slightly off day for the SE trade wind (see previous video), the following day was business as usual, with a healthy offshore breeze grooming the swell into ...",
                    "thumbnails": {
                    "default": {
                        "url": "https://i.ytimg.com/vi/X7ySp3y_eNQ/default.jpg",
                        "width": 120,
                        "height": 90
                    },
                    "medium": {
                        "url": "https://i.ytimg.com/vi/X7ySp3y_eNQ/mqdefault.jpg",
                        "width": 320,
                        "height": 180
                    },
                    "high": {
                        "url": "https://i.ytimg.com/vi/X7ySp3y_eNQ/hqdefault.jpg",
                        "width": 480,
                        "height": 360
                    }
                    },
                    "channelTitle": "Surfers of Bali",
                    "liveBroadcastContent": "none",
                    "publishTime": "2020-09-09T11:00:12Z"
                }
                },
                {
                "kind": "youtube#searchResult",
                "etag": "Ba6p3LnHeGNl_Fcv0HLuKe5Ll5E",
                "id": {
                    "kind": "youtube#video",
                    "videoId": "e5G0Ng3NIPo"
                },
                "snippet": {
                    "publishedAt": "2020-09-09T10:00:23Z",
                    "channelId": "UCNrMcPXlCYFoH-MEtVnKMxA",
                    "title": "Foil Surfing on Flat Water | Hydrofoil pumping in Serre-Ponçon 🌲🏄\u200d♂️🌲",
                    "description": "RIDER◅ Philippe CANERI ▻FOILBOARD◅ HORUE Website: http://www.horue.fr Instagram: https://www.instagram.com/horue/ ▻SPECIAL THANKS◅ Serre ...",
                    "thumbnails": {
                    "default": {
                        "url": "https://i.ytimg.com/vi/e5G0Ng3NIPo/default.jpg",
                        "width": 120,
                        "height": 90
                    },
                    "medium": {
                        "url": "https://i.ytimg.com/vi/e5G0Ng3NIPo/mqdefault.jpg",
                        "width": 320,
                        "height": 180
                    },
                    "high": {
                        "url": "https://i.ytimg.com/vi/e5G0Ng3NIPo/hqdefault.jpg",
                        "width": 480,
                        "height": 360
                    }
                    },
                    "channelTitle": "Horue Movie",
                    "liveBroadcastContent": "none",
                    "publishTime": "2020-09-09T10:00:23Z"
                }
                },
                {
                "kind": "youtube#searchResult",
                "etag": "5uPlQmrQUNN99_gZH5k4WkyFZQY",
                "id": {
                    "kind": "youtube#video",
                    "videoId": "qiuv1NbdvNQ"
                },
                "snippet": {
                    "publishedAt": "2020-09-09T05:34:02Z",
                    "channelId": "UCG8jk5TBxSVuHK-0Jv8JwQw",
                    "title": "9.9.20 מצב הים בוקר רביעי Israel Surf Report",
                    "description": "עדכוני מצב הים וסרטוני גלישה - מוזמנים לעקוב \u200f\u200e\u200fVideos of surfing from israel - SUBSCRIBE \u200fhttp://www.youtube.com/c/SurfingIsrael4K?sub_confirmation=1 ...",
                    "thumbnails": {
                    "default": {
                        "url": "https://i.ytimg.com/vi/qiuv1NbdvNQ/default.jpg",
                        "width": 120,
                        "height": 90
                    },
                    "medium": {
                        "url": "https://i.ytimg.com/vi/qiuv1NbdvNQ/mqdefault.jpg",
                        "width": 320,
                        "height": 180
                    },
                    "high": {
                        "url": "https://i.ytimg.com/vi/qiuv1NbdvNQ/hqdefault.jpg",
                        "width": 480,
                        "height": 360
                    }
                    },
                    "channelTitle": "Surfing Israel 4K",
                    "liveBroadcastContent": "none",
                    "publishTime": "2020-09-09T05:34:02Z"
                }
                },
                {
                "kind": "youtube#searchResult",
                "etag": "VgxLy_4Qv_dNeVORcKwZN7lv8e0",
                "id": {
                    "kind": "youtube#video",
                    "videoId": "YtbLxNxIcS4"
                },
                "snippet": {
                    "publishedAt": "2020-09-09T00:57:19Z",
                    "channelId": "UCn7s1bTIbscwY0w65U7WFAw",
                    "title": "Surfing A Gnarly Nth Coast Slab 2012 PLUS, Pumping South Straddie,  May 2009.",
                    "description": "Surfing A Gnarly Nth Coast Slab April 2012 PLUS, Pumping South Straddie, May 2009. with Mick Fanning, Josh Fuller Brenno, Samba Mann, Hazza Twins, Luke ...",
                    "thumbnails": {
                    "default": {
                        "url": "https://i.ytimg.com/vi/YtbLxNxIcS4/default.jpg",
                        "width": 120,
                        "height": 90
                    },
                    "medium": {
                        "url": "https://i.ytimg.com/vi/YtbLxNxIcS4/mqdefault.jpg",
                        "width": 320,
                        "height": 180
                    },
                    "high": {
                        "url": "https://i.ytimg.com/vi/YtbLxNxIcS4/hqdefault.jpg",
                        "width": 480,
                        "height": 360
                    }
                    },
                    "channelTitle": "surfonmars",
                    "liveBroadcastContent": "none",
                    "publishTime": "2020-09-09T00:57:19Z"
                }
                },
                {
                "kind": "youtube#searchResult",
                "etag": "8dBeIh0WVJTRCUkVof5BxF5Hux8",
                "id": {
                    "kind": "youtube#video",
                    "videoId": "tSvjOBed31E"
                },
                "snippet": {
                    "publishedAt": "2020-09-08T21:42:14Z",
                    "channelId": "UCVgO39Bk5sMo66-6o6Spn6Q",
                    "title": "Surfer dies after shark attack at Gold Coast beach | ABC News",
                    "description": "A man has died after being attacked by a shark while he was surfing at Coolangatta on the southern end of the Gold Coast. Queensland Ambulance Service was ...",
                    "thumbnails": {
                    "default": {
                        "url": "https://i.ytimg.com/vi/tSvjOBed31E/default.jpg",
                        "width": 120,
                        "height": 90
                    },
                    "medium": {
                        "url": "https://i.ytimg.com/vi/tSvjOBed31E/mqdefault.jpg",
                        "width": 320,
                        "height": 180
                    },
                    "high": {
                        "url": "https://i.ytimg.com/vi/tSvjOBed31E/hqdefault.jpg",
                        "width": 480,
                        "height": 360
                    }
                    },
                    "channelTitle": "ABC News (Australia)",
                    "liveBroadcastContent": "none",
                    "publishTime": "2020-09-08T21:42:14Z"
                }
                },
                {
                "kind": "youtube#searchResult",
                "etag": "L1H0MBKDnOkCQHRm9UcMzt8cln8",
                "id": {
                    "kind": "youtube#video",
                    "videoId": "aaiJ4TzcjeI"
                },
                "snippet": {
                    "publishedAt": "2020-09-08T17:33:57Z",
                    "channelId": "UCpXwMqnXfJzazKS5fJ8nrVw",
                    "title": "shiey - poem to a pigeon (Train Surfing Video)",
                    "description": "SPOTIFY/APPLE/SOUNDCLOUD: https://www.smarturl.it/shiey-safety Edited & produced by shiey. Filmed by: GIFGAS ...",
                    "thumbnails": {
                    "default": {
                        "url": "https://i.ytimg.com/vi/aaiJ4TzcjeI/default.jpg",
                        "width": 120,
                        "height": 90
                    },
                    "medium": {
                        "url": "https://i.ytimg.com/vi/aaiJ4TzcjeI/mqdefault.jpg",
                        "width": 320,
                        "height": 180
                    },
                    "high": {
                        "url": "https://i.ytimg.com/vi/aaiJ4TzcjeI/hqdefault.jpg",
                        "width": 480,
                        "height": 360
                    }
                    },
                    "channelTitle": "shiey",
                    "liveBroadcastContent": "none",
                    "publishTime": "2020-09-08T17:33:57Z"
                }
                },
                {
                "kind": "youtube#searchResult",
                "etag": "S8pv5rhU4U4RfqMS653L-AZvjDM",
                "id": {
                    "kind": "youtube#video",
                    "videoId": "6A2f_u7kwsc"
                },
                "snippet": {
                    "publishedAt": "2020-09-08T15:49:17Z",
                    "channelId": "UC0uzP4XsyVMGr7NwBUYv4mA",
                    "title": "SURFING 101 (part three) | learn how to surf",
                    "description": "Hey everyone! This is the very long awaited 3rd part of my SURFING 101 series where I give you my tips for learning to surf as a beginner. I hope you enjoy!",
                    "thumbnails": {
                    "default": {
                        "url": "https://i.ytimg.com/vi/6A2f_u7kwsc/default.jpg",
                        "width": 120,
                        "height": 90
                    },
                    "medium": {
                        "url": "https://i.ytimg.com/vi/6A2f_u7kwsc/mqdefault.jpg",
                        "width": 320,
                        "height": 180
                    },
                    "high": {
                        "url": "https://i.ytimg.com/vi/6A2f_u7kwsc/hqdefault.jpg",
                        "width": 480,
                        "height": 360
                    }
                    },
                    "channelTitle": "Eryn Krouse",
                    "liveBroadcastContent": "none",
                    "publishTime": "2020-09-08T15:49:17Z"
                }
                },
                {
                "kind": "youtube#searchResult",
                "etag": "YqNh-NXCX1c16uaoqAoG-lvVBS8",
                "id": {
                    "kind": "youtube#video",
                    "videoId": "NeRkQu54blY"
                },
                "snippet": {
                    "publishedAt": "2020-09-08T14:00:07Z",
                    "channelId": "UC2U95oR1h306i7Uh3DT0lVw",
                    "title": "Surfing record size citywave USA - the world&#39;s biggest stationary wave",
                    "description": "First footage of the 50ft. (16m) wide wave at Lakeside Surf in Chelan, WA, USA. More info: www.citywaveusa.com.",
                    "thumbnails": {
                    "default": {
                        "url": "https://i.ytimg.com/vi/NeRkQu54blY/default.jpg",
                        "width": 120,
                        "height": 90
                    },
                    "medium": {
                        "url": "https://i.ytimg.com/vi/NeRkQu54blY/mqdefault.jpg",
                        "width": 320,
                        "height": 180
                    },
                    "high": {
                        "url": "https://i.ytimg.com/vi/NeRkQu54blY/hqdefault.jpg",
                        "width": 480,
                        "height": 360
                    }
                    },
                    "channelTitle": "Citywave - The Ultimate Surf Pool",
                    "liveBroadcastContent": "none",
                    "publishTime": "2020-09-08T14:00:07Z"
                }
                },
                {
                "kind": "youtube#searchResult",
                "etag": "0xrmgFMkdbV1vFMOX4ndT7VKPZ4",
                "id": {
                    "kind": "youtube#video",
                    "videoId": "abMX-OM7j2c"
                },
                "snippet": {
                    "publishedAt": "2020-09-08T04:04:45Z",
                    "channelId": "UC5aeU5hk31cLzq_sAExLVWg",
                    "title": "Spain: Woman arrested for surfing after testing positive for coronavirus in San Sebastian",
                    "description": "Subscribe to our channel! rupt.ly/subscribe Mandatory credit: JaviZone A woman who had reportedly tested positive for COVID-19 and had to be isolated at her ...",
                    "thumbnails": {
                    "default": {
                        "url": "https://i.ytimg.com/vi/abMX-OM7j2c/default.jpg",
                        "width": 120,
                        "height": 90
                    },
                    "medium": {
                        "url": "https://i.ytimg.com/vi/abMX-OM7j2c/mqdefault.jpg",
                        "width": 320,
                        "height": 180
                    },
                    "high": {
                        "url": "https://i.ytimg.com/vi/abMX-OM7j2c/hqdefault.jpg",
                        "width": 480,
                        "height": 360
                    }
                    },
                    "channelTitle": "Ruptly",
                    "liveBroadcastContent": "none",
                    "publishTime": "2020-09-08T04:04:45Z"
                }
                },
                {
                "kind": "youtube#searchResult",
                "etag": "SlcmfQSnczZ7SYTqZZjKeONJzLU",
                "id": {
                    "kind": "youtube#video",
                    "videoId": "3CnbGF0Pv2c"
                },
                "snippet": {
                    "publishedAt": "2020-09-07T13:00:10Z",
                    "channelId": "UCwU_XmppMy9R9k4YJET7R6w",
                    "title": "Amazing NEW SURFING P.O.V.  |  GoPro MAX",
                    "description": "I just found my NEW FAVORITE Perspective for POV (point of view) SURF SHOTS! All it takes is a little free time to get creative... and you never know what you'll ...",
                    "thumbnails": {
                    "default": {
                        "url": "https://i.ytimg.com/vi/3CnbGF0Pv2c/default.jpg",
                        "width": 120,
                        "height": 90
                    },
                    "medium": {
                        "url": "https://i.ytimg.com/vi/3CnbGF0Pv2c/mqdefault.jpg",
                        "width": 320,
                        "height": 180
                    },
                    "high": {
                        "url": "https://i.ytimg.com/vi/3CnbGF0Pv2c/hqdefault.jpg",
                        "width": 480,
                        "height": 360
                    }
                    },
                    "channelTitle": "Brett Barley",
                    "liveBroadcastContent": "none",
                    "publishTime": "2020-09-07T13:00:10Z"
                }
                },
                {
                "kind": "youtube#searchResult",
                "etag": "DtyeKUeL5A2A9OEJRWrbJroY-1g",
                "id": {
                    "kind": "youtube#video",
                    "videoId": "YztlZnme5j0"
                },
                "snippet": {
                    "publishedAt": "2020-09-07T10:00:07Z",
                    "channelId": "UCmzxts0YGES5tN-oJ9abTQg",
                    "title": "WINCHING OUR FRIENDS POOL SURFING AND FOILING + MORE! // 20@20 Episode 15",
                    "description": "It was Otis's first day ever windsurfing Ho'okipa, I had fun showing him how to do it without getting destroyed. Then we Wing Foiled at Kuau Bay before riding soft ...",
                    "thumbnails": {
                    "default": {
                        "url": "https://i.ytimg.com/vi/YztlZnme5j0/default.jpg",
                        "width": 120,
                        "height": 90
                    },
                    "medium": {
                        "url": "https://i.ytimg.com/vi/YztlZnme5j0/mqdefault.jpg",
                        "width": 320,
                        "height": 180
                    },
                    "high": {
                        "url": "https://i.ytimg.com/vi/YztlZnme5j0/hqdefault.jpg",
                        "width": 480,
                        "height": 360
                    }
                    },
                    "channelTitle": "Kai Lenny",
                    "liveBroadcastContent": "none",
                    "publishTime": "2020-09-07T10:00:07Z"
                }
                },
                {
                "kind": "youtube#searchResult",
                "etag": "FNUkjICcFN9SsbdbM5kMecR2ejc",
                "id": {
                    "kind": "youtube#video",
                    "videoId": "-Pg7xCw4EXI"
                },
                "snippet": {
                    "publishedAt": "2020-09-07T04:24:12Z",
                    "channelId": "UCG8jk5TBxSVuHK-0Jv8JwQw",
                    "title": "7.9.20 גלים צינורות מצב הים בוקר שני Israel Surf Report",
                    "description": "עדכוני מצב הים וסרטוני גלישה - מוזמנים לעקוב \u200f\u200e\u200fVideos of surfing from israel - SUBSCRIBE \u200fhttp://www.youtube.com/c/SurfingIsrael4K?sub_confirmation=1 ...",
                    "thumbnails": {
                    "default": {
                        "url": "https://i.ytimg.com/vi/-Pg7xCw4EXI/default.jpg",
                        "width": 120,
                        "height": 90
                    },
                    "medium": {
                        "url": "https://i.ytimg.com/vi/-Pg7xCw4EXI/mqdefault.jpg",
                        "width": 320,
                        "height": 180
                    },
                    "high": {
                        "url": "https://i.ytimg.com/vi/-Pg7xCw4EXI/hqdefault.jpg",
                        "width": 480,
                        "height": 360
                    }
                    },
                    "channelTitle": "Surfing Israel 4K",
                    "liveBroadcastContent": "none",
                    "publishTime": "2020-09-07T04:24:12Z"
                }
                },
                {
                "kind": "youtube#searchResult",
                "etag": "qBYdQMpfp0kicn1GV86Vs2LOM40",
                "id": {
                    "kind": "youtube#video",
                    "videoId": "VD204YHh3go"
                },
                "snippet": {
                    "publishedAt": "2020-09-07T02:26:26Z",
                    "channelId": "UCKjU3KzdbJE1EFcHVqXC3_g",
                    "title": "Surfing towards change in North Preston, N.S.",
                    "description": "In one of Canada's historic Black communities, North Preston, N.S., people are reaching for surfboards to make the community's beaches more inclusive.",
                    "thumbnails": {
                    "default": {
                        "url": "https://i.ytimg.com/vi/VD204YHh3go/default.jpg",
                        "width": 120,
                        "height": 90
                    },
                    "medium": {
                        "url": "https://i.ytimg.com/vi/VD204YHh3go/mqdefault.jpg",
                        "width": 320,
                        "height": 180
                    },
                    "high": {
                        "url": "https://i.ytimg.com/vi/VD204YHh3go/hqdefault.jpg",
                        "width": 480,
                        "height": 360
                    }
                    },
                    "channelTitle": "CBC News: The National",
                    "liveBroadcastContent": "none",
                    "publishTime": "2020-09-07T02:26:26Z"
                }
                },
                {
                "kind": "youtube#searchResult",
                "etag": "saz7L7GpW3_ArGZn4Y8gcJBq-Ws",
                "id": {
                    "kind": "youtube#video",
                    "videoId": "yekouNcSm4A"
                },
                "snippet": {
                    "publishedAt": "2020-09-07T01:34:43Z",
                    "channelId": "UCOtHosOqPe9d6vLy-8LfHzQ",
                    "title": "Best Surfing Videos of the Week [#031]",
                    "description": "15 Surfing Videos of the Week selected by NobodySurf. Watch the full edit version of each video on the playlist below. Subscribe to NobodySurf channel for ...",
                    "thumbnails": {
                    "default": {
                        "url": "https://i.ytimg.com/vi/yekouNcSm4A/default.jpg",
                        "width": 120,
                        "height": 90
                    },
                    "medium": {
                        "url": "https://i.ytimg.com/vi/yekouNcSm4A/mqdefault.jpg",
                        "width": 320,
                        "height": 180
                    },
                    "high": {
                        "url": "https://i.ytimg.com/vi/yekouNcSm4A/hqdefault.jpg",
                        "width": 480,
                        "height": 360
                    }
                    },
                    "channelTitle": "NobodySurf : Surfing Videos",
                    "liveBroadcastContent": "none",
                    "publishTime": "2020-09-07T01:34:43Z"
                }
                },
                {
                "kind": "youtube#searchResult",
                "etag": "qgA9U6SIv4-Uu3ia_37lqWDdsCo",
                "id": {
                    "kind": "youtube#video",
                    "videoId": "v7VH6X793ho"
                },
                "snippet": {
                    "publishedAt": "2020-09-06T23:55:10Z",
                    "channelId": "UCLdPicN16eAKPKir8EY1UXQ",
                    "title": "The Ultimate Surf Skate Practice Routine For Surfing",
                    "description": "Surf-skating is a hugely beneficial tool we can use to better our surfing performance. How many opportunities do you really get to practice that manoeuvre you've ...",
                    "thumbnails": {
                    "default": {
                        "url": "https://i.ytimg.com/vi/v7VH6X793ho/default.jpg",
                        "width": 120,
                        "height": 90
                    },
                    "medium": {
                        "url": "https://i.ytimg.com/vi/v7VH6X793ho/mqdefault.jpg",
                        "width": 320,
                        "height": 180
                    },
                    "high": {
                        "url": "https://i.ytimg.com/vi/v7VH6X793ho/hqdefault.jpg",
                        "width": 480,
                        "height": 360
                    }
                    },
                    "channelTitle": "Kale Brock",
                    "liveBroadcastContent": "none",
                    "publishTime": "2020-09-06T23:55:10Z"
                }
                },
                {
                "kind": "youtube#searchResult",
                "etag": "rtalm4u3s5ZzpuSUSV9psFYP2kE",
                "id": {
                    "kind": "youtube#video",
                    "videoId": "LBITMCIoEks"
                },
                "snippet": {
                    "publishedAt": "2020-09-06T10:49:22Z",
                    "channelId": "UCG8jk5TBxSVuHK-0Jv8JwQw",
                    "title": "6.9.20 איזה בוקר מושלם היה לנו ! גולשים גלים 12:00 Surfing Israel",
                    "description": "עדכוני מצב הים וסרטוני גלישה - מוזמנים לעקוב \u200f\u200e\u200fVideos of surfing from israel - SUBSCRIBE \u200fhttp://www.youtube.com/c/SurfingIsrael4K?sub_confirmation=1 ...",
                    "thumbnails": {
                    "default": {
                        "url": "https://i.ytimg.com/vi/LBITMCIoEks/default.jpg",
                        "width": 120,
                        "height": 90
                    },
                    "medium": {
                        "url": "https://i.ytimg.com/vi/LBITMCIoEks/mqdefault.jpg",
                        "width": 320,
                        "height": 180
                    },
                    "high": {
                        "url": "https://i.ytimg.com/vi/LBITMCIoEks/hqdefault.jpg",
                        "width": 480,
                        "height": 360
                    }
                    },
                    "channelTitle": "Surfing Israel 4K",
                    "liveBroadcastContent": "none",
                    "publishTime": "2020-09-06T10:49:22Z"
                }
                },
                {
                "kind": "youtube#searchResult",
                "etag": "gHbyJiSjOUGYCogbzqgxPNQYDRk",
                "id": {
                    "kind": "youtube#video",
                    "videoId": "BqNRJukQzhE"
                },
                "snippet": {
                    "publishedAt": "2020-09-06T05:26:23Z",
                    "channelId": "UCkqcY4CAuBFNFho6JgygCnA",
                    "title": "Jocko on Surfing and What It Does for Him - Jocko Willink",
                    "description": "Join the conversation on Twitter/Instagram: @jockowillink @echocharles Excerpt from JOCKOPODCAST 26.",
                    "thumbnails": {
                    "default": {
                        "url": "https://i.ytimg.com/vi/BqNRJukQzhE/default.jpg",
                        "width": 120,
                        "height": 90
                    },
                    "medium": {
                        "url": "https://i.ytimg.com/vi/BqNRJukQzhE/mqdefault.jpg",
                        "width": 320,
                        "height": 180
                    },
                    "high": {
                        "url": "https://i.ytimg.com/vi/BqNRJukQzhE/hqdefault.jpg",
                        "width": 480,
                        "height": 360
                    }
                    },
                    "channelTitle": "Jocko Podcast",
                    "liveBroadcastContent": "none",
                    "publishTime": "2020-09-06T05:26:23Z"
                }
                },
                {
                "kind": "youtube#searchResult",
                "etag": "1zUzbB027vRft6B9ddPYA3TtAvo",
                "id": {
                    "kind": "youtube#video",
                    "videoId": "6z2lVg_SVh8"
                },
                "snippet": {
                    "publishedAt": "2020-09-06T05:17:41Z",
                    "channelId": "UCG8jk5TBxSVuHK-0Jv8JwQw",
                    "title": "6.9.20 בוקר סוול מושלם ! רוצו לים Surfing Israel Perfect Morning",
                    "description": "עדכוני מצב הים וסרטוני גלישה - מוזמנים לעקוב \u200f\u200e\u200fVideos of surfing from israel - SUBSCRIBE \u200fhttp://www.youtube.com/c/SurfingIsrael4K?sub_confirmation=1 ...",
                    "thumbnails": {
                    "default": {
                        "url": "https://i.ytimg.com/vi/6z2lVg_SVh8/default.jpg",
                        "width": 120,
                        "height": 90
                    },
                    "medium": {
                        "url": "https://i.ytimg.com/vi/6z2lVg_SVh8/mqdefault.jpg",
                        "width": 320,
                        "height": 180
                    },
                    "high": {
                        "url": "https://i.ytimg.com/vi/6z2lVg_SVh8/hqdefault.jpg",
                        "width": 480,
                        "height": 360
                    }
                    },
                    "channelTitle": "Surfing Israel 4K",
                    "liveBroadcastContent": "none",
                    "publishTime": "2020-09-06T05:17:41Z"
                }
                },
                {
                "kind": "youtube#searchResult",
                "etag": "24FfarypNKz7vfV8lggZyRFrhHY",
                "id": {
                    "kind": "youtube#video",
                    "videoId": "n4VJc38S2yk"
                },
                "snippet": {
                    "publishedAt": "2020-09-05T01:28:12Z",
                    "channelId": "UCsG5dkqFUHZO6eY9uOzQqow",
                    "title": "Dane And Jordy Ride Civilian Boards From Local Surf Shop | Deleted Scene Stab in the Dark All Stars",
                    "description": "What if it wasn't the vast chasm of dedication and skill that separated us from the world's best surfers, but instead the superior foam beneath their feet? If you've ...",
                    "thumbnails": {
                    "default": {
                        "url": "https://i.ytimg.com/vi/n4VJc38S2yk/default.jpg",
                        "width": 120,
                        "height": 90
                    },
                    "medium": {
                        "url": "https://i.ytimg.com/vi/n4VJc38S2yk/mqdefault.jpg",
                        "width": 320,
                        "height": 180
                    },
                    "high": {
                        "url": "https://i.ytimg.com/vi/n4VJc38S2yk/hqdefault.jpg",
                        "width": 480,
                        "height": 360
                    }
                    },
                    "channelTitle": "Stab: We like to surf",
                    "liveBroadcastContent": "none",
                    "publishTime": "2020-09-05T01:28:12Z"
                }
                },
                {
                "kind": "youtube#searchResult",
                "etag": "eeQROlBTRvnzqiY6IWI71rtuXt4",
                "id": {
                    "kind": "youtube#video",
                    "videoId": "LYqnbd-XItY"
                },
                "snippet": {
                    "publishedAt": "2020-09-04T19:29:40Z",
                    "channelId": "UCFdhu2ZZ7GBbGliV8tZ0UJw",
                    "title": "POV Raw SURF - CRYSTAL WATER",
                    "description": "Crystal water during winter on my island in the Indian Ocean : Réunion Island. We had the clearest water ever last week, so nice! Love. Surf is everything to me!",
                    "thumbnails": {
                    "default": {
                        "url": "https://i.ytimg.com/vi/LYqnbd-XItY/default.jpg",
                        "width": 120,
                        "height": 90
                    },
                    "medium": {
                        "url": "https://i.ytimg.com/vi/LYqnbd-XItY/mqdefault.jpg",
                        "width": 320,
                        "height": 180
                    },
                    "high": {
                        "url": "https://i.ytimg.com/vi/LYqnbd-XItY/hqdefault.jpg",
                        "width": 480,
                        "height": 360
                    }
                    },
                    "channelTitle": "Kai Noa",
                    "liveBroadcastContent": "none",
                    "publishTime": "2020-09-04T19:29:40Z"
                }
                },
                {
                "kind": "youtube#searchResult",
                "etag": "3OGJf5i0z0lj0jsIFknBOgvInVs",
                "id": {
                    "kind": "youtube#video",
                    "videoId": "YZDzEHFed6I"
                },
                "snippet": {
                    "publishedAt": "2020-09-04T14:37:03Z",
                    "channelId": "UCeYue9Nbodzg3T1Nt88E3fg",
                    "title": "Surfing Hurricane Douglas",
                    "description": "Mason Ho surfs a rare Hawaiian hurricane swell on Oahu. Hurricane Douglas. Filming: Rory Pringle Surfers: Mason Ho & Kai Pattison Jams: Jimi Hendrix.",
                    "thumbnails": {
                    "default": {
                        "url": "https://i.ytimg.com/vi/YZDzEHFed6I/default.jpg",
                        "width": 120,
                        "height": 90
                    },
                    "medium": {
                        "url": "https://i.ytimg.com/vi/YZDzEHFed6I/mqdefault.jpg",
                        "width": 320,
                        "height": 180
                    },
                    "high": {
                        "url": "https://i.ytimg.com/vi/YZDzEHFed6I/hqdefault.jpg",
                        "width": 480,
                        "height": 360
                    }
                    },
                    "channelTitle": "Ho & Pringle Productions",
                    "liveBroadcastContent": "none",
                    "publishTime": "2020-09-04T14:37:03Z"
                }
                },
                {
                "kind": "youtube#searchResult",
                "etag": "_vWja9Morw_UEcPwL9YAFf2nGI0",
                "id": {
                    "kind": "youtube#video",
                    "videoId": "zVoawta0w3M"
                },
                "snippet": {
                    "publishedAt": "2020-09-04T14:09:20Z",
                    "channelId": "UCGZ7Y3-CHCf29ma0JD0tmgw",
                    "title": "『北国にファンウェーブがやってきた』2020/9/4 #SURFING",
                    "description": "波乗り珍道中 #北海道サーフィン #蝦夷地.",
                    "thumbnails": {
                    "default": {
                        "url": "https://i.ytimg.com/vi/zVoawta0w3M/default.jpg",
                        "width": 120,
                        "height": 90
                    },
                    "medium": {
                        "url": "https://i.ytimg.com/vi/zVoawta0w3M/mqdefault.jpg",
                        "width": 320,
                        "height": 180
                    },
                    "high": {
                        "url": "https://i.ytimg.com/vi/zVoawta0w3M/hqdefault.jpg",
                        "width": 480,
                        "height": 360
                    }
                    },
                    "channelTitle": "波乗り珍道中",
                    "liveBroadcastContent": "none",
                    "publishTime": "2020-09-04T14:09:20Z"
                }
                },
                {
                "kind": "youtube#searchResult",
                "etag": "0oFZa9-aeVj5YyxwnK3qHWNMHS4",
                "id": {
                    "kind": "youtube#video",
                    "videoId": "V0hUXHNE4hE"
                },
                "snippet": {
                    "publishedAt": "2020-09-03T17:30:01Z",
                    "channelId": "UChuLeaTGRcfzo0UjL-2qSbQ",
                    "title": "SURFING RETURNS TO EUROPE WITH THE WSL COUNTDOWN!!! | SURF BREAKS",
                    "description": "Competitive surfing returns to Europe with the return of the WSL Countdown! Cruise as we check in with the 2019 World Champs! Vibe out with the legend Coco ...",
                    "thumbnails": {
                    "default": {
                        "url": "https://i.ytimg.com/vi/V0hUXHNE4hE/default.jpg",
                        "width": 120,
                        "height": 90
                    },
                    "medium": {
                        "url": "https://i.ytimg.com/vi/V0hUXHNE4hE/mqdefault.jpg",
                        "width": 320,
                        "height": 180
                    },
                    "high": {
                        "url": "https://i.ytimg.com/vi/V0hUXHNE4hE/hqdefault.jpg",
                        "width": 480,
                        "height": 360
                    }
                    },
                    "channelTitle": "World Surf League",
                    "liveBroadcastContent": "none",
                    "publishTime": "2020-09-03T17:30:01Z"
                }
                },
                {
                "kind": "youtube#searchResult",
                "etag": "mKRB8BQqh98XIGbxOuYe3WZGYiU",
                "id": {
                    "kind": "youtube#video",
                    "videoId": "WJIB7lLm1AQ"
                },
                "snippet": {
                    "publishedAt": "2020-09-03T16:00:07Z",
                    "channelId": "UC8ZzfqsNPVFzOEJp3Llovmw",
                    "title": "SUMMER VIBES☀️🌊 in NAZARE, foil, skate🛹 &amp; big waves surfing🏄🏼\u200d♂️, Ep29",
                    "description": "Skate, foil et surf de grosses vagues en plein été à Nazare Abonnes toi à ma chaine pour ne pas manquer la prochaine vidéo ✅ https://bit.ly/2NGnw3M ...",
                    "thumbnails": {
                    "default": {
                        "url": "https://i.ytimg.com/vi/WJIB7lLm1AQ/default.jpg",
                        "width": 120,
                        "height": 90
                    },
                    "medium": {
                        "url": "https://i.ytimg.com/vi/WJIB7lLm1AQ/mqdefault.jpg",
                        "width": 320,
                        "height": 180
                    },
                    "high": {
                        "url": "https://i.ytimg.com/vi/WJIB7lLm1AQ/hqdefault.jpg",
                        "width": 480,
                        "height": 360
                    }
                    },
                    "channelTitle": "Justine Dupont",
                    "liveBroadcastContent": "none",
                    "publishTime": "2020-09-03T16:00:07Z"
                }
                },
                {
                "kind": "youtube#searchResult",
                "etag": "KeI196d916Dt7bnsd9faLIeM6mE",
                "id": {
                    "kind": "youtube#video",
                    "videoId": "ByjjlBvdMkQ"
                },
                "snippet": {
                    "publishedAt": "2020-09-03T11:30:03Z",
                    "channelId": "UCjNea6tkE7f0WHR50iNPf5A",
                    "title": "Lion Family 🍒 Surfing Champion | Cartoon for Babies",
                    "description": "Little Lion likes surfing. Bedtime Stories for Kids #lionfamily #kidscartoon #mouse.",
                    "thumbnails": {
                    "default": {
                        "url": "https://i.ytimg.com/vi/ByjjlBvdMkQ/default.jpg",
                        "width": 120,
                        "height": 90
                    },
                    "medium": {
                        "url": "https://i.ytimg.com/vi/ByjjlBvdMkQ/mqdefault.jpg",
                        "width": 320,
                        "height": 180
                    },
                    "high": {
                        "url": "https://i.ytimg.com/vi/ByjjlBvdMkQ/hqdefault.jpg",
                        "width": 480,
                        "height": 360
                    }
                    },
                    "channelTitle": "Lion Family English",
                    "liveBroadcastContent": "none",
                    "publishTime": "2020-09-03T11:30:03Z"
                }
                },
                {
                "kind": "youtube#searchResult",
                "etag": "osqFmgHtNkBDWlYE2WGC1pUlgc8",
                "id": {
                    "kind": "youtube#video",
                    "videoId": "AkDq377IkXg"
                },
                "snippet": {
                    "publishedAt": "2020-09-03T11:00:02Z",
                    "channelId": "UCzcQOTuXYGuCvTekySb_CeQ",
                    "title": "Bali Surf Journal - August 2020",
                    "description": "We didn't get any really big swells in August and it was uncharacteristically small for a few days towards the end of the month. Despite this, it was still a fruitful ...",
                    "thumbnails": {
                    "default": {
                        "url": "https://i.ytimg.com/vi/AkDq377IkXg/default.jpg",
                        "width": 120,
                        "height": 90
                    },
                    "medium": {
                        "url": "https://i.ytimg.com/vi/AkDq377IkXg/mqdefault.jpg",
                        "width": 320,
                        "height": 180
                    },
                    "high": {
                        "url": "https://i.ytimg.com/vi/AkDq377IkXg/hqdefault.jpg",
                        "width": 480,
                        "height": 360
                    }
                    },
                    "channelTitle": "Surfers of Bali",
                    "liveBroadcastContent": "none",
                    "publishTime": "2020-09-03T11:00:02Z"
                }
                },
                {
                "kind": "youtube#searchResult",
                "etag": "Q_JmQGNfTR_E_9jWfuLPIBuTotA",
                "id": {
                    "kind": "youtube#video",
                    "videoId": "DHdBNGHXIUw"
                },
                "snippet": {
                    "publishedAt": "2020-09-02T18:00:02Z",
                    "channelId": "UC_F4Iy5korq2mEWZDQhG07w",
                    "title": "CHAOS AT LOWER TRESTLES! || WHAT KOA EATS TO SURF ALL DAY! Cali pt.2",
                    "description": "Get your This is Livin' Merch! https://koarothman.com/ California part 2 was a great time! We head to the Quiksilver store to grab a bunch of clothing and wetsuits.",
                    "thumbnails": {
                    "default": {
                        "url": "https://i.ytimg.com/vi/DHdBNGHXIUw/default.jpg",
                        "width": 120,
                        "height": 90
                    },
                    "medium": {
                        "url": "https://i.ytimg.com/vi/DHdBNGHXIUw/mqdefault.jpg",
                        "width": 320,
                        "height": 180
                    },
                    "high": {
                        "url": "https://i.ytimg.com/vi/DHdBNGHXIUw/hqdefault.jpg",
                        "width": 480,
                        "height": 360
                    }
                    },
                    "channelTitle": "Koa Rothman",
                    "liveBroadcastContent": "none",
                    "publishTime": "2020-09-02T18:00:02Z"
                }
                },
                {
                "kind": "youtube#searchResult",
                "etag": "fj7ChdKyXl7Erpstd_NAwCsJnx4",
                "id": {
                    "kind": "youtube#video",
                    "videoId": "ImoUkJRDheM"
                },
                "snippet": {
                    "publishedAt": "2020-09-02T14:18:17Z",
                    "channelId": "UC873OURVczg_utAk8dXx_Uw",
                    "title": "Surfing My Homemade Electric Surfboard - PART 2",
                    "description": "The electric surfboard did not catch fire. Ha, you doubters! I have new stronger and better motors on the way right now! Look forward for PART 3! This project ...",
                    "thumbnails": {
                    "default": {
                        "url": "https://i.ytimg.com/vi/ImoUkJRDheM/default.jpg",
                        "width": 120,
                        "height": 90
                    },
                    "medium": {
                        "url": "https://i.ytimg.com/vi/ImoUkJRDheM/mqdefault.jpg",
                        "width": 320,
                        "height": 180
                    },
                    "high": {
                        "url": "https://i.ytimg.com/vi/ImoUkJRDheM/hqdefault.jpg",
                        "width": 480,
                        "height": 360
                    }
                    },
                    "channelTitle": "RCLifeOn",
                    "liveBroadcastContent": "none",
                    "publishTime": "2020-09-02T14:18:17Z"
                }
                },
                {
                "kind": "youtube#searchResult",
                "etag": "Lt9zXu6DeUjdAcsZiG2JRAWC0go",
                "id": {
                    "kind": "youtube#video",
                    "videoId": "azSoYakQqEc"
                },
                "snippet": {
                    "publishedAt": "2020-09-02T03:48:10Z",
                    "channelId": "UCSsrubE-H29qSN1cGGNUXQQ",
                    "title": "Coastline Magazine visited Surf Lakes&#39; 5 Waves R&amp;D site in Yeppoon",
                    "description": "Check out the latest from “The Coastline Magazine”. Hear of the wonder of the development of Surf Lakes' 5 Waves technology on an old beef cattle farm, and ...",
                    "thumbnails": {
                    "default": {
                        "url": "https://i.ytimg.com/vi/azSoYakQqEc/default.jpg",
                        "width": 120,
                        "height": 90
                    },
                    "medium": {
                        "url": "https://i.ytimg.com/vi/azSoYakQqEc/mqdefault.jpg",
                        "width": 320,
                        "height": 180
                    },
                    "high": {
                        "url": "https://i.ytimg.com/vi/azSoYakQqEc/hqdefault.jpg",
                        "width": 480,
                        "height": 360
                    }
                    },
                    "channelTitle": "Surf Lakes",
                    "liveBroadcastContent": "none",
                    "publishTime": "2020-09-02T03:48:10Z"
                }
                },
                {
                "kind": "youtube#searchResult",
                "etag": "OzQ6HSbS-E0mSUqqR2js7jj4fzk",
                "id": {
                    "kind": "youtube#video",
                    "videoId": "W4dZ5sHMZzM"
                },
                "snippet": {
                    "publishedAt": "2020-09-02T01:18:07Z",
                    "channelId": "UC3sF0ruoSi5lmyXKorXa-oA",
                    "title": "밥상으로 서핑을 탈 수 있을까? l Surfing on a table",
                    "description": "korean#crazy#surfing What happened when my wife didn't buy me a surfing board.",
                    "thumbnails": {
                    "default": {
                        "url": "https://i.ytimg.com/vi/W4dZ5sHMZzM/default.jpg",
                        "width": 120,
                        "height": 90
                    },
                    "medium": {
                        "url": "https://i.ytimg.com/vi/W4dZ5sHMZzM/mqdefault.jpg",
                        "width": 320,
                        "height": 180
                    },
                    "high": {
                        "url": "https://i.ytimg.com/vi/W4dZ5sHMZzM/hqdefault.jpg",
                        "width": 480,
                        "height": 360
                    }
                    },
                    "channelTitle": "유세유니 대단해",
                    "liveBroadcastContent": "none",
                    "publishTime": "2020-09-02T01:18:07Z"
                }
                },
                {
                "kind": "youtube#searchResult",
                "etag": "PVGf1YGo_3AM5WL4nRql2341F_U",
                "id": {
                    "kind": "youtube#video",
                    "videoId": "k2DQMNGQXf0"
                },
                "snippet": {
                    "publishedAt": "2020-08-31T17:17:00Z",
                    "channelId": "UCr3Lrf7n3h3XGjkxTOSRMCA",
                    "title": "I Tried Surfing Storm Waves in Belgium",
                    "description": "I wasn't going to film a video this week. But when my brother sent me a text message that there were going to be 2m waves in Belgium (the shittiest country to ...",
                    "thumbnails": {
                    "default": {
                        "url": "https://i.ytimg.com/vi/k2DQMNGQXf0/default.jpg",
                        "width": 120,
                        "height": 90
                    },
                    "medium": {
                        "url": "https://i.ytimg.com/vi/k2DQMNGQXf0/mqdefault.jpg",
                        "width": 320,
                        "height": 180
                    },
                    "high": {
                        "url": "https://i.ytimg.com/vi/k2DQMNGQXf0/hqdefault.jpg",
                        "width": 480,
                        "height": 360
                    }
                    },
                    "channelTitle": "Average Rob",
                    "liveBroadcastContent": "none",
                    "publishTime": "2020-08-31T17:17:00Z"
                }
                },
                {
                "kind": "youtube#searchResult",
                "etag": "b2ARK_34qtguiUmh7IOez7TZFUg",
                "id": {
                    "kind": "youtube#video",
                    "videoId": "N8stgAxd_Rc"
                },
                "snippet": {
                    "publishedAt": "2020-08-31T16:59:43Z",
                    "channelId": "UCd5dgfpboQbApKvN4P3FWVw",
                    "title": "Jackson Dorian &amp; Sky Brown surfing Palm Springs!",
                    "description": "Super fun day at The Palm Springs Surf Club thanks so much to Kalani Robb and Cheyne Magnusson for having us. Fun day surfing with @skybrown and ...",
                    "thumbnails": {
                    "default": {
                        "url": "https://i.ytimg.com/vi/N8stgAxd_Rc/default.jpg",
                        "width": 120,
                        "height": 90
                    },
                    "medium": {
                        "url": "https://i.ytimg.com/vi/N8stgAxd_Rc/mqdefault.jpg",
                        "width": 320,
                        "height": 180
                    },
                    "high": {
                        "url": "https://i.ytimg.com/vi/N8stgAxd_Rc/hqdefault.jpg",
                        "width": 480,
                        "height": 360
                    }
                    },
                    "channelTitle": "Jackson Dorian",
                    "liveBroadcastContent": "none",
                    "publishTime": "2020-08-31T16:59:43Z"
                }
                },
                {
                "kind": "youtube#searchResult",
                "etag": "xS_E7rraXnQO23c2luhw0puG8kk",
                "id": {
                    "kind": "youtube#video",
                    "videoId": "ZdTqWFOnT6E"
                },
                "snippet": {
                    "publishedAt": "2020-08-31T08:24:11Z",
                    "channelId": "UCgbuI1Xv-HS3UKKmkeKM3qw",
                    "title": "SAIL FOR SURF",
                    "description": "Sail for surf is the story of Collin Martins, a french chef with only one goal in mind: surfing. The virus was born at the age of 3 when his parents put him on a ...",
                    "thumbnails": {
                    "default": {
                        "url": "https://i.ytimg.com/vi/ZdTqWFOnT6E/default.jpg",
                        "width": 120,
                        "height": 90
                    },
                    "medium": {
                        "url": "https://i.ytimg.com/vi/ZdTqWFOnT6E/mqdefault.jpg",
                        "width": 320,
                        "height": 180
                    },
                    "high": {
                        "url": "https://i.ytimg.com/vi/ZdTqWFOnT6E/hqdefault.jpg",
                        "width": 480,
                        "height": 360
                    }
                    },
                    "channelTitle": "Picture Organic Clothing",
                    "liveBroadcastContent": "none",
                    "publishTime": "2020-08-31T08:24:11Z"
                }
                },
                {
                "kind": "youtube#searchResult",
                "etag": "jVH058B47oRlUoSnkyf8-OPh7-E",
                "id": {
                    "kind": "youtube#video",
                    "videoId": "Viyj1A4Lnik"
                },
                "snippet": {
                    "publishedAt": "2020-08-30T16:31:01Z",
                    "channelId": "UCIJ0lLcABPdYGp7pRMGccAQ",
                    "title": "Surf&#39;s Up! | People Are Awesome Vs. FailArmy",
                    "description": "We're back with another round of People Are Awesome Vs. FailArmy, where we celebrate all the lessons learned on the way to awesome! Featured clips include ...",
                    "thumbnails": {
                    "default": {
                        "url": "https://i.ytimg.com/vi/Viyj1A4Lnik/default.jpg",
                        "width": 120,
                        "height": 90
                    },
                    "medium": {
                        "url": "https://i.ytimg.com/vi/Viyj1A4Lnik/mqdefault.jpg",
                        "width": 320,
                        "height": 180
                    },
                    "high": {
                        "url": "https://i.ytimg.com/vi/Viyj1A4Lnik/hqdefault.jpg",
                        "width": 480,
                        "height": 360
                    }
                    },
                    "channelTitle": "People are Awesome",
                    "liveBroadcastContent": "none",
                    "publishTime": "2020-08-30T16:31:01Z"
                }
                }
            ]
        }

        context["result"] = [
            {
                "title": item[search_query]["title"],
                "channel_name": item[search_query]["channelTitle"],
                "number_of_views": item[search_query]["channelTitle"],
                "description": item[search_query]["description"],
                "upload_date": item[search_query]["publishTime"],
                "thumbnail_url": item[search_query]["thumbnails"]["high"]["url"]

            } for item in result['items']
        ]


    return render(request, "search_result.html", context)