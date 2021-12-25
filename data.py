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
comment3= {
    "Text" : "You could say that again!",
    "Name": "Jenna",
    "Username": "jennnnn",
    "Picture":"charlie_profile_picture.png",
    "DateTime" : datetime(2021, 8, 5, 23, 5, 0)
}

post1 = {
    "post_id":1,
    "Text":"I can't wait to go to the park today",
    "Name":"Melba",
    "Username":"melba",
    "Likes":['charlie','jenna'],
    "Comments":[comment1,comment2],
    "DateTime": datetime(2021,7,1,17,0,0),
    "Picture": "melba_profile.png"
}
post2 = {
    "post_id":2,
    "Text":"I could really go for a treat right now",
    "Name":"Melba",
    "Username":"melba",
    "Likes":['Melba'],
    "Comments":[comment3],
    "DateTime": datetime(2021,8,4,17,2,5),
    "Picture": "melba_profile.png"
}

test_posts = {
    1 : post1,
    2 : post2
}

melba_posts = {
    1:post1
    2:post2
}

jenna_posts = {

}

charlie_posts = {

}

melba{
    "Name": "Melba",
    "Bio":"My name is Melba. I'm a miniature golden-doodle.  My favorite place in the world is Discovery Park in Seattle, Washington.",
    "Username": :"melba",
    "Picture": "melba_profile.png",
    "Birthday":datetime(2013, 2, 14),
    "Posts": melba_posts
}

charlie{
    "Name": "Charlie",
    "Bio": "Hi, I'm Charlie!  I'm a standard poodle and I love to nap.",
    "Username": "chucky",
    "Picture": "charlie_profile_picture.jpg",
    "Birthday": datetime(2018, 1, 2),
    "Posts": charlie_posts
}

jenna{
    "Name": "Jenna",
    "Bio": "Hello, I'm Jenna. I'm a young pup with big aspirations",
    "Username": "jennnnn",
    "Picture": "charlie_profile_picture.jpg",
    "Birthday": datetime(2021,5,6),
    "Posts" : jenna_posts
}

dogs{
    "melba":melba,
    "chucky": charlie,
    "jennnnn": jenna
    }
