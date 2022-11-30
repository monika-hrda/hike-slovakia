# Hike Slovakia
_“To walk in nature is to witness a thousand miracles.” - Mary Davis_

The app was built as my fourth milestone project for Diploma in Full Stack Software Development with Code Institute. 

Hike Slovakia is a multi-page eCommerce web application for both visitors of and people living in Slovakia who wish to explore the country and its beautiful hiking destinations. The website offers its users a chance to book onto guided hikes in the region.

![Hike Slovakia](docs/readme-img/am-i-responsive.png)

You can view the live website [here](https://hike-slovakia.herokuapp.com/ "Hike Slovakia"). 


***
## User Experience (UX)

### Site Goals

#### Site Owner's Goals

* Letting people know about 'Hike Slovakia'.
* Motivating people to explore Slovakia and its hiking trails.
* Making profit from providing guiding services.
* Benefitting from an automated booking system. 
* Creating opportunity to scale the business.

#### Site User's Goals

* Exploring Slovakia using the services of an experienced guide.
* Finding information about all scheduled hikes, selecting & booking any with ease.
* Learning about hiking trails & destinations in Slovakia.

### User Stories

As a guest / not logged in user, I want to be able to:
* easily understand what the purpose of the website is.
* navigate the website easily, so that I can find any relevant content.
* find more information about the company, so that I can understand more about what they are doing.
* view an offering of all guided hikes posted on the website.
* find general details of any guided hike, as well as find out what dates they are scheduled on.
* contact the business owner / administrator, so that I can ask any specific questions and get more information.
* view the website clearly on multiple devices, including my mobile device, so that I can achieve my other goals on the go.
* register on the website so that I can book / pay for a hike I am interested in.

As a registered / logged in user, in addition to the above, I want to be able to:
* log into my account so that I can use the website’s services.
* select the number of people I am booking a selected hike for.
* start the booking process of the scheduled hike I am interested in.
* securely pay for the scheduled hike I choose to book.
* receive a confirmation email after I successfully book my hike.
* view my profile - including my personal information as well as a list of hike bookings I made in the past.
* update my personal information.
* log out.

As an admin, I want to be able to:
* add a new hike offering, so that I can expand my services offering.
* update and delete any existing hike offering, so that I can stay flexible in my offerings in accordance with my business needs.
* schedule a new hike.
* access the Django admin portal easily.

### Planned Features

* Navigation menu on all pages - changes contents depending on user status
* Home page with information on the site purpose
* User authentication (register, login, logout)
* List of guided hikes / hike offerings
* Guided hike detail page
* Hike booking / payment
* Admin interface
* 404 & 500 error pages
* Responsive design

### Wireframes

<details><summary>Home page</summary>

![home page wireframe](docs/wireframes/home.png)
</details>

<details><summary>Hike Offerings page</summary>

![classes page wireframe](docs/wireframes/hike-offerings.png)
</details>

<details><summary>Hike Detail page</summary>

![classes page wireframe](docs/wireframes/hike-detail.png)
</details>

<details><summary>Hike Detail page - logged in user only</summary>

![classes page wireframe](docs/wireframes/hike-detail-logged-in.png)
</details>

<details><summary>Hike Detail page - admin user only</summary>

![classes page wireframe](docs/wireframes/hike-detail-admin.png)
</details>

<details><summary>Review Booking page - logged in user only</summary>

![classes page wireframe](docs/wireframes/review-booking.png)
</details>

<details><summary>Checkout page - logged in user only</summary>

![classes page wireframe](docs/wireframes/checkout.png)
</details>

<details><summary>Booking Confirmation page - logged in user only</summary>

![classes page wireframe](docs/wireframes/booking-confirmation.png)
</details>

<details><summary>Profile page</summary>

![profile page wireframe](docs/wireframes/profile.png)
</details>

<details><summary>Add a hike page - admin user only</summary>

![profile page wireframe](docs/wireframes/add-hike.png)
</details>

<details><summary>Register page</summary>

![register page wireframe](docs/wireframes/register.png)
</details>

<details><summary>Login page</summary>

![login page wireframe](docs/wireframes/login.png)
</details>

<details><summary>404 page</summary>

![404 page wireframe](docs/wireframes/404.png)
</details>


### Design

* Clean design lets images of the Slovak nature do the talking.

***
## Notes on Development Process

* I have decided to not follow the example e-commerce project Boutique Ado to the dot, and instead of selling products, I am selling services which are date-dependent. Boutique Ado being my introduction to Django, by not following its format, the learning curve has proven quite steep. Towards the end of the MVP development, I've started to feel like I am getting the grasp on Django, at long last! I can see many areas where I can improve the existing codebase and I am now quite excited to continue the development of this app, as well as other apps in the future.

* Trello Board has been used since the beginning of development to track progress, capture ideas, and make notes (screenshot from early on in the process)
![trello board](docs/readme-img/trello-board.jpg)

* Changes to design - layout of the website & pages was designed in advance, and wireframes were followed during development, except for some minor changes; the only major one being adding a list of past bookings to a user's profile page.

***
## Database Design

![database schema](docs/readme-img/database-schema.png)

The above schema shows only the tables created by me (except the auth_user one, I am however manipulating its data in my code). 

Project Hike Slovakia currently contains 5 Django apps, and 5 custom models.

***
## Features

### Existing Features

* **Home Page (Logged out and Logged in):**
  - The Home Page features a beautiful backdrop of natural scenery from Slovakia, with a Navigation Bar at the top of the page. 
  - The Nav Bar will add access to features such as a Profile Page for logged in Users and a Hike Management page for the Site Admin.
  - A success modal will appear on the right hand side of the screen to inform the site viewer or admin that they are loggin in.
  - In the centre of the screen, a button displaying "Explore Hikes" intices users to check out the hikes on offer in the Hikes list page.

* **Hike List (Logged out and Logged in):**
  - The Hike List Page displays cards with information on different hiking experiences, with up front information including difficulty and price.
  - This list can be expaned by accessing the Hike Management page as an admin.
  - Each card can be clicked on to take the user to the Hike detail page of that specific article, where they can access further information of what is involved in the Hike that they selected.

* **Hike Detail:**
  - In the Hike Detail View, the same title, price and difficulty are displayed as on the cards from the list page, but here the site user can access further information about what the hike involves.
  - Users are able to select scheduled dates of the hike from the drop down, to find out availability.
  - Only future dates show here. 
  - If the site user is signed in, they can choose number of hikers that intend to go on the trip, and continue with the booking process.
  - The hike is then booked by clicking on the "Book Hike for x people" button, where x changes automatically based on the number of hikers inputted.

* **Only Future Dates of Hikes Display in the dropdown selection for users**

* **Sign Up:**
  - The sign up page is rendered using Django's Allauth package, and it takes the following information from the user in order to register for an account:
    - Email
    - Email again (confirmation)
    - Username
    - Password
    - Password again (confirmation)

  - If the form is filled in correctly, the user is sent a confiration email with a confirmation link. After clicking on confirm link, the user is signed in and redirected back to the home page, where the navigation will allow access to a profile page, and ability to make bookings is enabled.

* **Sign In:**
  - Again, using the Django Allauth package, the Login page takes the user's email or username and their password in order to grant access to their account. 
  - As per above, the user is redirected to the homepage when successfully logged in.

* **Forgot Password:**
  - The Forget Password page also comes with the Django Allauth package, and will request the user's email in order to reset the password.
  - If the email address exists on file, an email is sent to that address with instructions to reset their password once the "Reset my password" button is clicked. 
  - There is also a "Back to login" button to allow the user to quickly return to the login page.

* **Profile Page:**
  - The Profile page, which is accessible once the user is logged in, displays the user's information on file, as well as the user's previous hike booking history to the right hand side.
  - The User can update their first name, last name, email and phone number in the inputs on the page, and this is saved when the "Update Information" button is clicked.
  - A success modal will appear on the right hand side of the screen to inform the user that the information has been successfully updated.
  - Email is a required / validated field, and phone number allows only numeric characters (but is not required).
  - User can navigate to an individual booking success page of a past booking by clicking on booking number of selected hike.

* **Hike Management - Add New Hike:**
  - This is a site admin-only accessible page, where the site owner can add a new hike.
  - The form takes all the information required to give the necessary details to the Hike List view and, of course, the Hike Detail view.
  - The hike is added with the "Add" button, and the "Cancel" button redirects back to the Hikes List Page.

* **Hike Management - Edit Hike:**
  - This is a site admin-only accessible page, where the site owner can update existing hike.
  - The form takes all the information required to give the necessary details to the Hike List view and, of course, the Hike Detail view.
  - The hike is updated with the "Edit" button, and the "Cancel" button redirects back to the Hike's Detail Page.

* **Hike Management - Delete Hike:**
  - There is a "Delete" button on each Hike's Detail Page, with which the site owner can delete the existing hike.
  - Defensive Programming - on click of the "Delete" button, the admin is prompted to re-confirm the choice to delete the hike.

* **Review Booking / Basket:**
  - Upon selecting a hike (and date) to book, user is redirected to this page to review their booking.
  - They can choose to edit their selection and they are redirected back to the individual hike page.
  - Or they can continue to checkout page.

* **Checkout:**
  - User can see the amount they are about to pay.
  - Stripe picks up any invalid card numbers and returns appropriate error messages.
  - Upon entering valid payment card information, the user is given a success modal and redirected to successful booking page.

* **Successful Booking:**
  - User can see details of the hike they just purchased.

* **Confirmation Email:**
  - Upon successful booking, user is sent a confirmation email with details of their booking.

* **Contact Us:**
  - Users can fill in a contact form to get in touch with the Hike Slovakia company. 
  - Admin is able to review the sent messages in the Admin portion of the site.

* **404, 403 and 500 Error Pages**

### Features Left to Implement in the Future

* As the company grows, they will expect higher demand on their services, so more automation will be developed than is presented here in the MVP.
* Details on number of people booked on each individual hike & date will be accessible to the admin of the site / site owner.
* The company is outsourcing their clients in case there is a higher demand on a particular date, but in the future this will be taken care of by developing mechanisms to alert the company when the numbers on a particular hike are getting higher than expected. 

***
## Technologies Used

### Languages Used

* HTML5
* CSS3
* JavaScript
* Python3

### Frameworks, Libraries & Programs Used

* [Django](https://www.djangoproject.com/) - open-source, Python-based web framework that follows the model–template–views architectural pattern
* Django AllAuth - to provide enhanced user account management functionality
* [Heroku](https://heroku.com/) - to deploy the live site
* Heroku PostgreSQL - to host the database
* [WhiteNoise](http://whitenoise.evans.io/en/stable/django.html) - mainly for serving static files
* [Cloudinary](https://cloudinary.com/) - to upload, store, manage, and deliver images
* [Bootstrap](https://getbootstrap.com/docs/4.6/getting-started/introduction/) - framework for building responsive, mobile-first sites
* [Font Awesome](https://fontawesome.com/) - to add icons to the site
* [pip](https://pip.pypa.io/en/stable/) - to install dependencies for the site
* [Git](https://git-scm.com/) - version control
* [GitHub](https://github.com/) - to store the code for this project
* [GitPod](https://www.gitpod.io/) - virtual IDE used to build this site
* [jQuery](https://jquery.com/) - JavaScript library
* [Google DevTools](https://developer.chrome.com/docs/devtools/) - invaluable during development
* [Trello](https://www.trello.com/) - to project manage, Kanban-style
* [Balsamiq](https://balsamiq.com/wireframes/) - to create wireframes
* [DbVisualizer](https://www.dbvis.com/) - to visualize database data
* [https://imagecompressor.com/](https://imagecompressor.com/) - to compress image files
* [https://favicon.io/](https://favicon.io/favicon-converter/) - to generate favicon
* [amiresponsive](https://ui.dev/amiresponsive?url=https://yoga-hub.herokuapp.com/home)

***
## Testing

Find a separate document for the [testing section here](https://github.com/monika-hrda/hike-slovakia/blob/main/TESTING.md). This is due to its size.

***
## Deployment

### Requirements for Deployment

* Heroku account
* Stripe account
* Cloudinary account
* GitHub account, Gitpod

### Heroku Deployment

This project was deployed on Heroku following these steps:

#### Requirements.txt and Procfile

Create these files using these steps in (GitPod) terminal:

1. Type `pip3 freeze -–local > requirements.txt` to create a requirements file (it keeps track of the Python / Django dependencies that we've installed for our project)
2. Type `echo web: python3 run.py > Procfile` to create Procfile (a Heroku-specific type of file that tells Heroku how to run our project, what command to use to start the app)
3. Delete any additional empty lines after the line `web: gunicorn hike_slovakia.wsgi:application`
4. Push these two files into your depository

#### Create Heroku App

1. Log in to Heroku and 'Create New App' from the dashboard
2. Choose an app name (each app name has to be unique)
3. Select the region based on your location
4. Click 'Create App'
5. Add config vars to Heroku - go to Heroku Settings tab, click on Reveal Config Vars, and add environment variables described below in key/value pairs

#### Create Database

1. Select the app from the list in Heroku
2. Go to Heroku 'Resources' tab and in the add-ons section search for Postgres
3. Select Heroku Postgres
4. Select 'Submit Order Form'
5. In the Heroku Settings tab, within the config vars section, the DATABASE_URL will appear and can be used to connect to the remote database
6. Migrations can be ran locally against the remote database if we set up the DATABASE_URL variable in our local environment.
7. In order to automate the process of migrating, we can add this line into Procfile (on line 1): `release: python manage.py makemigrations && python manage.py migrate`

#### Environment Variables

Create an env.py file within the Django app and configure the project via the following various environment variables.
(Please note - as this file contains sensitive information, it needs to be added to the .gitignore file to not be pushed to GitHub!)

It will look similar to this:

```
import os

os.environ["SECRET_KEY"] = "unique secret key"
os.environ["DEVELOPMENT"] = 'True'
os.environ["CLOUDINARY_URL"] = 'cloudinary_url'

```

Add these environment variables:

* SECRET_KEY - there are websites online that will help you generate random Django secret keys

* DEVELOPMENT - if set, it will put the project into debug mode

* EMAIL_HOST_USER - your email address used to send emails out

* EMAIL_HOST_PASS - used to authenticate to the SMTP server

* STRIPE_PUBLIC_KEY, STRIPE_SECRET_KEY, STRIPE_WH_SECRET - Stripe payments variables (you will need to set up a Stripe account)

* CLOUDINARY_URL - to upload images to Cloudinary (you will need to set up a Cloudinary account)

Add these variables to Heroku's Config Vars as well (do not add the DEVELOPMENT one, so that Heroku runs in production mode)

#### Deploying our App to Heroku

1. Navigate to the Deploy tab in Heroku and connect your app to GitHub.
2. Deploy the branch manually.
3. Check the build log for errors.
4. Once Heroku completed the build process, you will see a 'Your App Was Successfully Deployed' message and a link to the live site.
5. You can also choose to enable Automatic deploys. 

#### Alternative Heroku deployment via CLI

0. In your CLI install Heroku by typing `npm install -g heroku`
1. Login to Heroku by typing `heroku login -i`
2. Get your app name from Heroku by typing command `heroku apps`
3. Set the Heroku remote (replace the <app_name> with your actual app name): `heroku git:remote -a <app_name>`
4. Add and commit changes to your code (commands `git add .` & `git commit -m "Deploy to Heroku via CLI"`)
5. Push to GitHub `git push origin main`
6. Push to Heroku `git push heroku main`
7. Your Heroku app will be built and you will see your deployed app's URL

### Forking the Repository

This project can be forked following these steps: 

1. Log in to GitHub and locate this project (you are most likely here). 
2. Locate the Fork button at the top right corner of the page and click on it. 
3. A copy of the original repository is now in your GitHub account

### Local Clone

1. Navigate to this GitHub repository (you are most likely here)
2. Click on the Code dropdown
3. Copy the URL of the repository in the HTTPS tab
4. Use your IDE of choice to open its terminal
5. Change the current working directory to the location where you want the cloned directory
6. Type `git clone` and then paste the previously copied URL
7. Press enter to create your local clone
8. Create the above described env.py file with your own values
9. Install the project requirements by using the command `pip3 install -r requirements.txt`
10. Run the program

***
## Credits

### Code

* project is based on and developed from [Code Institute](https://codeinstitute.net/)'s walkthrough Boutique Ado
* Django documentation has been researched extensively
* code for modal from [W3Schools](https://www.w3schools.com/howto/howto_css_modals.asp)
* gte lookup for filtering by future date on [Stack Overflow](https://stackoverflow.com/questions/45947222/django-queryset-with-datetime-need-to-get-all-future-dated-entries)

### Media

* background immage on home page from [Pixabay](https://pixabay.com/)
* default hike image from [Pxhere](https://pxhere.com/)
* all other images of Slovak nature currently used on hikes' pages were taken by Monika Hrda
* gif image used as a loading "spinner" found on [Icons8](https://icons8.com/preloaders/)

### Acknowledgements

A big thank you to fellow Slackers from Code Institute's Slack channel for their support, advice, encouragement, and friendship.