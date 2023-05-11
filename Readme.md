# NightOwl
The Night Owl project can be divided into several modules, each with its own set of features and functionalities. 

Here are the different modules of the Night Owl project:
## User Authentication Module: 
This module is responsible for user registration, login, and authentication. 
It allows users to create an account, log in securely, and access their profile and settings.

## Location-based Search Module: 
This module enables users to search for cafes, pubs, and restaurants in their nearby area based on their pincode or location. 
It utilizes location data and Google Maps API to provide accurate and relevant search results.

## Rating and Review Module: 
This module allows users to rate and review the cafes, pubs, and restaurants they visit. 
It enables users to share their experiences, opinions, and feedback with other users, and helps them make informed decisions about where to go for their next late-night outing.

## Picture Upload Module: 
This module enables users to upload pictures of the food and atmosphere of the cafes, pubs, and restaurants they visit. 
It allows other users to get a visual idea of what to expect and helps them choose the best place to visit for their next late-night hangout.

## Admin Dashboard Module: 
This module is responsible for managing the website's content, users, and settings. 
It enables the website administrator to monitor user activities, moderate user-generated content, and customize the website's appearance and functionality.

## Notification Module: 
This module enables users to receive notifications about new places, ratings, reviews, and pictures. 
It keeps users informed and engaged, and encourages them to participate more actively in the Night Owl community.

Overall, these modules work together to provide users with a seamless and enjoyable experience while using the Night Owl website. They enable users to discover new places, share their experiences, and connect with other night owls who share their passion for late-night hangouts.

# To run it locally
## Prerequisites
- Pyhton 3.8 or later


## Steps
1. Install the dependencies
```zsh
python -m pip install -r requirements.txt
```
2. Run `migrate` command to create the db
```zsh
python manage.py migrate
```
3. Run the local server
```zsh
python manage.py runserver
```

Open http://localhost:8000 to see the home page

Open http://localhost:8000/admin to login to the admin site

## To create a superuser
```zsh
python manage.py createsuperuser
```



<!-- 

Model View Template
MVT

Model View Controller
MVC

Users
----––––---------------
id   | name | password






def login():
    if user_password == password:
        return name
    else:
        return 'Username/password is wrong'

url.py
    include
    path

request
HttpResponse
render
Template
jinja2

writing jinga template


admin site
creating Model
extending django user
migration
list_display
jinja for loop







# Views

## User
- register
- login
- forgot password


## Establishment Search
- search


## Establishment
- restaurant/1
- pub/1
- cafe/1


## Review
- **/review
- upload/


## Admin
- dashboard
- establishment/[CUD]
- user/[UD]
- review/[D]
- phogto/[D] 

-->
