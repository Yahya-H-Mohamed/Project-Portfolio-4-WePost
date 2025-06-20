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

- Wireframe

![Page Blueprint](images/Screenshot%20(36).png)

- The Post Details page displays the full content of a single post, including its title, body, author, and any associated comments or interactions. Users may be able to comment, like, or interact with the post from this page.
- The My Posts page shows a personalized list of posts created by the currently logged-in user. Users can view, edit, or delete their own posts from this page.
- The All Posts page displays a feed or list of all posts created by users on the platform. Visitors can browse, read, and possibly interact with posts from all users.
- The Sign Up page allows new users to create an account by providing required information such as username, email, and password. Upon successful registration, users can log in and access the platform’s features.
- The Sign In page enables existing users to log into their accounts using their credentials (typically username/email and password). Successful authentication grants access to user-specific and general features of the site.
- The Create Posts page provides a form for users to compose and submit new posts. Users can enter content (such as title, content, category, etc.), and upon submission, the post is added to the platform and visible to others.

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
- I have passed my code through validators with no major errors
- Run and tested my code in the local terminal
- Run and tested my code in the Heroku terminal

As for automated testing, I ran automated tests on the views and forms files.
- test_post_list_view_get: Checks that the home page correctly displays a list of posts.
- test_my_posts_view_redirects_if_not_logged_in: Ensures unauthenticated users are redirected from the "My Posts" page.
- test_my_posts_view_shows_user_posts: Verifies that only the logged-in user's posts are shown on the "My Posts" page.
- test_create_post_view_post_request: Tests that a user can create a new post via the create post form.
- test_post_detail_view: Confirms that the post detail page displays the correct post and its comments.

- test_post_form_is_valid: Checks that the post form is valid with correct data.
- test_post_form_is_invalid_if_title_missing: Ensures the post form is invalid if the title is missing.
- test_comment_form_is_valid: Checks that the comment form is valid with correct data.
- test_comment_form_is_invalid_if_content_missing: Ensures the comment form is invalid if the content is missing.

- Clicking edit button populates form and changes submit button: Simulates clicking the edit button and checks that the comment form is populated, the submit button text changes to "Update", and the form action is set correctly.



## Local Deployment
Steps for local deployment: 
- Fork or Clone this repository

Git clone https://github.com/Yahya-H-Mohamed/Project-Portfolio-4-WePost

- Create a virtual environment

python -m venv venv

- Install dependencies

pip install -r requirements.txt

- Apply migrations

python manage.py migrate

- Collect static files

python manage.py collectstatic

- Run the development server

python manage.py runserver

Steps for Heroku deployment: 
- Create new heroku app

heroku create (app-name)

- Set environment variables on Heroku

heroku config:set SECRET_KEY=<your-secret-key>
heroku config:set ALLOWED_HOSTS=<your-app-name>.herokuapp.com

- Push code to Heroku

git push heroku main

- Run migrations on Heroku

heroku run python manage.py migrate

- Collect static files on Heroku

heroku run python manage.py collectstatic --noinput

- Open deployed app

  heroku open

## Credits
- Reddit for some styling inspiration for the post cards
- Codestar Code Institute project 