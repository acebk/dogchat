from datetime import datetime

comment1 = {
    "Text" : "what time are you going?",
    "Name": "Charlie",
    "Username": "chucky",
    "Picture":"charlie_profile_picture.png",
    "DateTime" : datetime(2021, 7, 1, 18, 0, 0)
}
comment2 = {
    "Text" : "See you there!!!",
    "Name": "Jenna",
    "Username": "jennnnn",
    "Picture":"charlie_profile_picture.png",
    "DateTime" : datetime(2021, 7, 1, 23, 5, 0)
}

post1 = {
    "Text":"I can't wait to go to the park today",
    "Name":"Melba",
    "Username":"melba",
    "Likes":['charlie','jenna'],
    "Comments":[comment1,comment2],
    "DateTime": datetime(2021,7,1,17,0,0),
    "Picture": "melba_profile.png"
}
post2 = {
    "Text":"I could really go for a treat right now",
    "Name":"Melba",
    "Username":"melba",
    "Likes":[],
    "Comments":[],
    "DateTime": datetime(2021,8,4,17,2,5),
    "Picture": "melba_profile.png"
}

test_posts= [post1,post2]
