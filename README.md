# Hike Slovakia
_“To walk in nature is to witness a thousand miracles.” - Mary Davis_

The app was built as my fourth milestone project for Diploma in Full Stack Software Development with Code Institute. 

Hike Slovakia is a multi-page eCommerce web application for both visitors of and people living in Slovakia who wish to explore the country and its beautiful hiking destinations. The website offers its users a chance to book onto guided hikes in the region.

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

* Home page
![home page wireframe](docs/wireframes/home.png)

* Hike Offerings page
![classes page wireframe](docs/wireframes/hike-offerings.png)

* Hike Detail page
![classes page wireframe](docs/wireframes/hike-detail.png)

* Hike Detail page - logged in user only
![classes page wireframe](docs/wireframes/hike-detail-logged-in.png)

* Hike Detail page - admin user only
![classes page wireframe](docs/wireframes/hike-detail-admin.png)

* Review Booking page - logged in user only
![classes page wireframe](docs/wireframes/review-booking.png)

* Booking Confirmation page - logged in user only
![classes page wireframe](docs/wireframes/booking-confirmation.png)

* Checkout page - logged in user only
![classes page wireframe](docs/wireframes/checkout.png)

* Profile page
![profile page wireframe](docs/wireframes/profile.png)

* Add a hike page - admin user only
![profile page wireframe](docs/wireframes/add-hike.png)

* Register page
![register page wireframe](docs/wireframes/register.png)

* Login page
![login page wireframe](docs/wireframes/login.png)

* 404 page
![404 page wireframe](docs/wireframes/404.png)

### Design

* #### Colour Scheme

* #### Typography

* #### Imagery

***
## Notes on Development Process

* Trello Board has been used since the beginning of development to track progress, capture ideas, and make notes (screenshot from early on in the process)
![trello board](docs/readme-img/trello-board.jpg)

* Changes to design - layout of the website & pages was designed in advance, and wireframes were followed during deveopment, except for some minor changes; the only major one being adding a list of past bookings to a user's profile page.

***
## Database Design

***
## Features

### Existing Features

### Features Left to Implement in the Future

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

### Validator Testing

### User Stories Testing

### Continuous Testing - Issues and Resolutions to issues found during testing

During the development process, the application was continuously tested and bugs and issues that were found were resolved. A few examples:

* When a user redirected to a checkout view manually (without selecting a hike to book first), a 500 internal server error was raised. This was happening due to the view initially incorrectly checking whether a local storage existed. (Which it did since we were initialising it there.) The bug was fixed by checking for existence of a hike_id in the local storage instead, and now if it does not exist, the user will be brought back to all_hikes view to select a hike to book.

* After implementing a confirmation email sending after a successful purchase, the checkout process started failing with 500 error. Logging details into console revealed a bug in code - customer's email was being populated with the user, rather than the user's email. The fix was rather straightforward and payment process works ok now. 

### Known Bugs and Issues

***
## Deployment

***
## Credits

### Code

* project is based on and developed from [Code Institute](https://codeinstitute.net/)'s walkthrough Boutique Ado
* code for modal from [W3Schools](https://www.w3schools.com/howto/howto_css_modals.asp)

### Content

### Media

* background immage on home page from [Pixabay](https://pixabay.com/)
* default hike image from [Pxhere](https://pxhere.com/)
* all other images of Slovak nature currently used on hikes pages were taken by Monika Hrda
* gif image used as a loading "spinner" found on [Icons8](https://icons8.com/preloaders/)

### Acknowledgements

A big thank you to fellow Slackers from Code Institute's Slack channel for their support, advice, encouragement, and friendship.