# Project-Portfolio-4-WePost

Welcome to WePost! A Django community/blog social media application where people can engage in discussion. You can sign up for free and share your opinion online for all users to see and interact with.

[Click here to open WePost](https://wepost-project-7798d87be756.herokuapp.com/)


## Planning/Agile
- When I came up with the idea to build a sort-of- Reddit style community app. I first came up with a rough statement for this project. "This will be a community/social media site similar to Reddit. Users will be able to create accounts, make posts and comment on other users and edit or delete their own account information as well as their posts and comments. There will be a general posts page where you will see a hub of every users posts, a page where you can view all of your own posts and a page where you can view all your own posts and a page where you can view and edit your account."

- From this I was able to break of parts of the statement to form Epics. For example, General Posts Page, Account System, ect...

- With these epics I was able to create several user stories:
- - As a user, I can view all posts on a general page, so I can choose one to view
- - As a user, I can view all of my own posts on a page, so I can choose one to view
- - As a user, I can comment on other peoples posts, so I can share my thoughts
- - As a user, I can edit or delete my posts and comments, so others cannot see them
- - As a user, I can create posts so I can start a discussion with other users

- With these as a guideline I went about implementing each user story, however due to running out of time, I was unable to completely finish the edit and delete functionality of the posts, so I had to scale my project down slightly to fit the deadline.

## How To Use
- Users who are not logged in still have access to the app content and can read posts
- Users who are new to the site are able to freely create and account with a secure username and password
- Users who are logged into an account have quick and easy accesss to a filtered page of their posts
- Users with an account have access to additonal features such as creating their own posts
- Registered users are also able to leave comments on other peoples blog posts
- Comment owners can freely change or delete comments they leave on other peoples posts
- Users can Sign out by clicking the sign up link
- Users with admin control are able to delete users, posts and comments.

## Packages and Technologies
- asgiref==3.8.1
- crispy-bootstrap5==0.7
- dj-database-url==0.5.0
- Django==4.2.19
- django-allauth==0.57.2
- django-crispy-forms==2.3
- django-summernote==0.8.20.0
- gunicorn==20.1.0
- oauthlib==3.2.2
- psycopg2==2.9.10
- PyJWT==2.10.1
- python3-openid==3.2.0
- requests-oauthlib==2.0.0
- sqlparse==0.5.3
- whitenoise==5.3.0
- python-3.10.9
- bootstrap
- HTML
- CSS
- JS

## Testing
The tests I have carried out on this project are:
- I have verified that the blog post detail page is rendered correctly with unit testing
- I have verified that the form codes behave as expected when valid and invalid data is submitted using unit testing
- I have entered different inputs for all scenarios to ensure I have caught all potential input errors
- I have passed my code through validators with no major errors
- Run and tested my code in the local terminal
- Run and tested my code in the Heroku terminal

## Local Deployment
- Steps for deployment: 
- - Fork or Clone this repository
- - Create a virtual environment
- - Install all of the packages required
- - Migrate databases
- - Run command python3 manage.py runserver
- - Open application in localhost browser

## Credits
- Reddit for some styling inspiration for the post cards
- Codestar Code Institute project 