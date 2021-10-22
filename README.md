# CellarClub

View the deployed site [here](http://cellar-club.herokuapp.com/ "CellarClub")

## PROJECT INTRODUCTION
Cellar Club is a website desisgned for members of a wine appreciation group. Members can create an account on the site to view the collection of wines, add reviews and ratings to wines in the collection, and also add new wines to the collection. Members can also add the wines to a 'favourites' list for future reference.

![image of home page site mock-ups on various screen sizes](/static/images/mock-ups/mock-screens.png "Mock Up")
![image of wines pagesite mock-ups on various screen sizes](/static/images/mock-ups/mock-screens-wines.png "Mock Up")
___

## **USER EXPERIENCE (UX)**

###  Strategy
 - **User Stories**

New Users

1. As a new user, I want to be able to create a member account
2. As a new user, I want to view the wine collection easily
3. As a new user, I want to add reviews to existing wines
4. As a new user, I want to add wines to my favourites
5. As a new user, I want to add a new wine to the collection

Returning Users

1. As a returning user, I want to be able to log in to my account
2. As a returning user, I want to view the reviews I have made
3. As a returning user, I want to edit/remove the reviews I have made
4. As a returning user, I want to view the wines in my favourites list
5. As a returning user, I want to view the wines I have submitted

Admin Users
1. As an admin user, I want to be able to removes wines from the website

### Design

 - **Colour Scheme**

   - The site is a deisgned with a retro classic feel with mainly black and white colours, while accents are in shades of amber and burgundy.
   
 - **Font**

   - In keeping with the retro feel, 'Corben' from google fonts has been used for this site. The large rounded bubble letters of the 700 weight are used for the logo and headers, while the lighter 400 weight is used for the body


- **Images**

  - All images taken from open source sites, or from free download allowance on subscription sites. The large hero image on the home page was chosen to echo the 'cellar' theme and lead users into the site. The custom background graphic was created as slight background in line with the sites theme, proviving some contrast for the card elements but not distracting or competing. The generic wine bottle images used for the wine cards were chosen to ensure a uniform size and look, while the user can submit an image of the actual wine to be displayed in the pop up modal.

### Wireframes

Wireframes showing the each page across small, medium and large screen sizes.

|     Page   | Wireframe | Wireframe | Wireframe |
| ----------- | ----------- | ----------- | ----------- |
|Sign up page     | [Large](static/images/wireframes/large-sign-up.png) | [Medium](static/images/wireframes/med-sign-up.png)   | [Small](static/images/wireframes/small-sign-up.png)   |
|Sign in page   | [Large](static/images/wireframes/large-sign-in.png) | [Medium](static/images/wireframes/med-sign-in.png)   | [Small](static/images/wireframes/small-sign-in.png)   |
|Home page   |  [Large](static/images/wireframes/large-home.png) | [Medium](static/images/wireframes/med-home.png)   | [Small](static/images/wireframes/small-profile.png)   |
|Wines page  |  [Large](static/images/wireframes/large-wines.png) | [Medium](static/images/wireframes/med-wines.png)   | [Small](static/images/wireframes/small-wines.png)   |
|Wine Modal  | [Large](static/images/wireframes/large-wine-modal.png) | [Medium](static/images/wireframes/med-wine-modal.png) | [Small](static/images/wireframes/small-wine-modal.png)|
|Add wine page   |  [Large](static/images/wireframes/large-add-wine.png) | [Medium](static/images/wireframes/med-add-wine.png)   | [Small](static/images/wireframes/small-add-wine.png)   |
|Add/edit review page   | [Large](static/images/wireframes/large-add-review.png) | [Medium](static/images/wireframes/small-add-review.png)   | [Small](/workspace/CellarClub/static/images/wireframes/small-add-review.png)   |
|Profile page  | [Large](static/images/wireframes/large-profile.png) | [Medium](static/images/wireframes/med-profile.png)   | [Small](static/images/wireframes/small-profile.png)   |

### Database Schema
The Cellar-club database is stored in MongoDB Atlas, made up of 3 collections.

 - Wine_type:

    ![image wine-type collection](static/images/db-schema/wine-type.png "wine_type collection")

    This comprises 4 documents, one for each wine type. Collection is uneditable as these types will not change.

 - Users:
   - Document in the collection:

    ![image users collection](static/images/db-schema/users.png "users collection")

    - This collection holds all the data submitted for each new user.
    - User favourites are stored as dictionary ojects in the "favourites" key array.
    - Value for the "wine_id" key in each of the favourites dictionaries corresponds to the value for the "_id" ObjectID of the favourited wine in the "Wines" collection and can be used to cross reference the collections.
    
 - Wines:
    - Document in the collection:

    ![image wines collection](static/images/db-schema/wines.png "wines collection")

    - This collection holds all the data submitted for each new wine.
    - Wine reviews are stored as dictionaries in the "reviews" key array.
    - Value for the "reviewed_by" key in each of the favourites dictionaries corresponds to the value for the "username" key in the "Users" collection and can be used to cross reference the collections.

______


## **FEATURES**

###  Current Features

  - All pages:
    - Full width header containing navbar links to all pages on the site.
    - Responsive and interactive navbar which collapses to hamburger menu with dropdown menu for smaller screen sizes
    - Navbar only shows 'Sign Up' and 'Sign In' links to new users (or if signed out)
    - Once signed in, navabr shows links to 'Wines', 'Add wine' and 'Profile' pages, as well as a link to sign out of session.
    - Page headings in a yellow banner with the title of the page
    - Footer with contact info and links to social media sites.
  - Home Page:
    - Large full width, viewport height hero image, of a wine cellar, inviting the user to join the club
    - Clicking the central text takes users to the registration page
    - If the user is not yet logged in, the only navbar links displayed are for 'Sign Up' or 'Sign In'
 - Sign Up Page:
    - User is invited to enter their username, pasword, date of birth and full name in the registration form.
    - All fields are required and form validation is in place.
    - There is a second password verification field to ensure the user has typed their password correctly - the form will not sumbit unless passwords are matching.
    - The form will not submit if the user age, as calcuated from the date of birth input field, is under 18. A flashed message at the top of the screen displays a message confirming this.
    - On successfull completion of the form, the user details are added to the "users" collection in MongoDB, and the user profile page is opened.
    - Below the 'Register' submit button, there is a section to direct users who already have an account to the 'sign in' page instead.
 - Sign In Page:
    - User is invited to enter their username and password in the sign in form.
    - If the details match the user details in the 'users' collection, the user is signed in to a new session on the site.
    - If the details do not match, a flashed message ar the top of the screen advises the username/password is incorrect.
    - Below the 'Sign In' submit button, there is a section to direct users who do not already have an account to the 'sign up' page instead.
 - Profile Page:
    - Only accessible to users once signed in. 
    - Top section of the page displays two cards (side by side on med/alrge screens, stacked on small screens)
    - The first card shows a list of wines which have been submitted by the user.
    - Each row in the list shows the wine name and vintage, and a button to view the wine details in the pop up modal.
    - The second card shows a list of wines which have been added to the users 'favourites' array in the "users" collection.
    - Each row in the list shows the wine name and vintage, and a button to view the wine details in the pop up modal, also an "x" icon button to remove the wine from the user favourites,
    - Below this section is a full width card showing a list of all reviews the user has submitted for wines in the site collection.
    - Each row in the list shows the wine name and vintage, then the review text, along with the rating (1-5 stars) the user has awared the wine.
    - Each review also displays a button to edit the review, delete the review, or view the wine in the wine modal.
 - Wines Page:
    - At the top of the page there is a dropdown selector to filter the wines according to wine type: Red, White, Rosé or Sparkling.
    - There is a second input box to search the filter by desired keywords.
    - The details for each wine are displayed in individual cards, full width on small screens or in a 3x3 grid on medium screens and larger.
    - Depending on the wine type, there is an image of a corresponding generic red/white/rosé/sparkling wine bottle on the left of each card. 
    - The right hand side of the card displays the name, vintage year, grape variety and country for the wine.
    - Below the details, there is a 5 star rating display which shows the average rating of the wine calculated from the user reviews.
    - On hover of the card, a thin burgundy border is applied, and a "view" button appears on the card, clicking the card displays the wine modal.
 - Wine Modal Section:
    - The wine modal displays all details for each wine along with the user reviews.
    - The modal header displays the wine name in the site logo font style
    - The modal body displays the wine vintage year, grape variety, country and region (if submitted).
    - A link to purchase the wine through https://www.wine-searcher.com/ is also displayed.
    - If there was an image url included on submission of the wine, this image is dsplayed beside the wine details. If no image was submitted, and image of generic wine bottles is displayed instead.
    - Below the wine details, the user reviews are displayed.
    - Each review shows the username who sumbitted, the review text, and the star rating awarded.
    - If the review was submitted by the current user, they will also see buttons to edit or display their review.
    - The modal footer displays buttons to add the wine to the users favourites, or to adda review to the wine, along with a button to close the modal.
    - An admin user will also see a button to delete the wine. This feature is restricted to admins only, since modifying/deleting the wine following submission would affect other users reviews and favourites lists. Admins can remove the wine if there are any issues.
 - Add Wine Page:
    - Form invites the user to enter details to add a wine to the collection.
    - Required details are wine type (from dropdown selector displaing only red/white/rosé/sparkling), wine name, vintage, grape variety, country, user review and rating (1-5 stars).
    - Optional details are the country region and image url.
    - Multiple wines with the same name can be submitted to the collection, but only one vintage for each wine is allowed.
    - If a user tries to submit an existing wine/vintage paring, the submission is rejected and the user is advised to submit a review instead via a flashed message.
    - Once the wine is submitted, the user is returned to the wines page.
 - Add Review Page:
    - A user can review each wine/vintage pair only once.
    - If a user clicks the 'add review' button and they have already added a review, they cannot access the 'add review' page and are advised to submit a review instead via a flashed message.
    - On the 'add review' page, the wine name and vintage inputs are already populated with the corresponding details and are displayed as read only.
    - The user must add their review to the textarea input, and their rating from 1-5 stars.
    - Once the review is submitted, the user is returned to the wines page.
 - Edit Review Page:
    - The 'edit review' page is displayed identical to the 'add review' page, except the details from the existing review are populated into the 'review' and 'rating' input fields.

 - Site is fully responsive (using bootstrap and CSS) to adapt to all display sizes - mobiles,  tablets and large monitors/laptop screens.


### Potential future features

 - The site could incorporate a shop feature to sell the wines directly to the users.

 ____

 ## **TECHNOLOGIES USED**

 ### Languages

  - [Html5](https://en.wikipedia.org/wiki/HTML5)
  - [CSS3](https://en.wikipedia.org/wiki/CSS)
  - [Javascript](https://www.javascript.com/)
  - [Python](https://www.python.org/)

 ### Frameworks, libraries and tools used

  - [Bootstrap v5.02](https://getbootstrap.com/)
    - Bootstrap was used for navbar, grid layout, form structure, responsive layout, margins, padding etc on all screen sizes.
  - [JQuery](https://jquery.com/)
    - JQuery library used for JS scripts
  - [Jinja templating engine](https://jinja.palletsprojects.com/en/3.0.x/)
    - Used to create html base template, and additional pages, also allows  writing code similar to Python syntax. Then the template is passed data to render the final document.
  - [Flask](https://flask.palletsprojects.com/en/2.0.x/)
    - Framework used to build the webapp (depends on the Jinja template engine and the Werkzeug WSGI toolkit)
  - [Mongo DB Atlas](https://www.mongodb.com/)
    - Used to store and manage the database collections
  - [dnspython](https://www.dnspython.org/)
    - DNS toolkit for Python used for queries
  - [Flask-PyMongo](https://flask-pymongo.readthedocs.io/en/latest/)
    - Tool to  bridge   Flask and PyMongo
  - [Gitpod](https://www.gitpod.io/)
    - Code was written in Gitpod, and version control was managed by commit and push to GitHub.
  - [GitHub](https://github.com/)
    - Used to store the project repository
  - [Heroku](http://www.heroku.com/)
    - Used to deploy the project
  - [Font Awesome](https://fontawesome.com/)
    - Used to display social media icons.
  - [Google Fonts](https://fonts.google.com/)
    - Used to import the Josefin Sans font used throughout the site.
  - [Chrome DevTools](https://developer.chrome.com/docs/devtools/)
    - Used for testing code output, especially to view various display sizes during the site creation.
  - [Balsamiq](https://balsamiq.com/)
    - Wireframes were created using the balsamiq app.
  - [JPEGmini Pro](https://www.jpegmini.com/)
    - Used to reduce file size of images while preserving quality, to improve page loading times.
 - [Image Compressor](https://imagecompressor.com/)
    - Used to reduce file size of images while preserving quality, to improve page loading times.
 - [Canva](http://www.canva.com/r)
    - Graphic design platform used to create the custom background image.
 - [Moqups website mockup generator](https://websitemockupgenerator.com/)
    - Used to generate a mockup of the site on multiple devices

   ___
## **TESTING**
    Full testing documentation found in separate file (TESTING.md(-TESTING.md])
    ___
## **DEPLOYMENT**

#### Deployed using Heroku

- **Instructions**
  1. Open the [repository](https://github.com/annemarie293/CellarClub) in GitHub, then launch in GitPod
  2. Create an env.py file, and ensure it is added to .gitignore file as this will contain sensitive info that should not be pushed to the server.
  3. In env.py add the following
  ```
    import os 
    os.environ.setdefault("IP", "0.0.0.0") 
    os.environ.setdefault("PORT", "5000")
    os.environ.setdefault("SECRET_KEY", " ")
    os.environ.setdefault("MONGO_URI", "mongodb+srv://userannemarie:PASSWORD@myfirstcluster.1ccbb.mongodb.net/DB-NAME?retryWrites=true&w=majority")
    os.environ.setdefault("MONGO_DBNAME", "") 
    ```


    4. Use your own secret key, ideally from a random passoword generator, and add your own Mongo URI, password and DB name from your mongo database
    5. Install Flask, flask-pymongo and dnspython using ```pip3 install``` command
    6. To tell Heroku which dependencies are needed to run your app run:
        ```pip3 freeze --local > requirements.txt``` and 
        ```echo web: python app.py > Procfile``` 
    7. Ensure these files are pushed to git before deploy
    8. Login or create a new account on Heroku.
    9. Create a new app, choosing app name and region
    10. Choose "GitHub" as the deployment method, add your GitHub repo name and click search to connect.
    11. Before clicking "Enable automatic deploys" on the deploy tab, go to "reveal config vars" on the settings tab
    12. Add the below key/value pairs:
    
     |     Key  | Value | 
     | -------- | --------- | 
     |IP    | 0.0.0.0 | 
     |PORT | 5000 | 
     |SECRET_KEY| copy from env.py  | 
     |MONGO_URI | copy from env.py  | 
     |MONGO_DBNAME | copy from env.py   | 

  5. click on "hide config vars"
  6. Return to "deploy" tab and click "Enable automatic deploys"
  7. Then click "Deploy Branch" to deploy your app.

#### Forking the Repository

- **Instructions**
  1. Open the [repository](https://github.com/annemarie293/CellarClub) in GitHub
  2. Click on the “fork” button at the top right hand side of the page, just below the navbar.
  3. A copy of the original repository will be created to your own GitHub account.


#### Cloning the Repository

- **Instructions**
  1. Open the [repository](https://github.com/annemarie293/CellarClub)
  2. Click on the “code” button to the left of the green “Gitpod” button.
  3. To clone the repository using HTTPS, under "Clone with HTTPS", click the clipboard icon. 
  4. To clone the repository using an SSH key, including a certificate issued by your organization's SSH certificate authority, click Use SSH, then click the clipboard icon . 
  5. To clone a repository using GitHub CLI, click Use GitHub CLI, then click the clipboard icon.
  6. Open Git Bash.
  7. Change the current working directory to the location where you want the cloned directory.
  8. Type `git clone`, and then paste the URL you copied earlier.

`$ git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY`

  9. Press Enter to create your local clone.

```
$ git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY
> Cloning into `Spoon-Knife`...
> remote: Counting objects: 10, done.
> remote: Compressing objects: 100% (8/8), done.
> remove: Total 10 (delta 1), reused 10 (delta 1)
> Unpacking objects: 100% (10/10), done.
```
 
  10. For more detailed info on this process please click [here](https://docs.github.com/en/github/creating-cloning-and-archiving-repositories/cloning-a-repository)

___

## **CODE**

#### Credits

All code written by myself using lessons from the Code Institute back end development module as a kicking off point, with the exception of:
 
- [Flash Alert CSS](Source: https://www.w3schools.com/howto/tryit.asp?filename=tryhow_js_alert)

 

#### Content
  - The text content for this site was all written by myself, Anne Marie Murphy.

#### Media
- **The photos used in this site were freely obtained from below image sites:**

- [Home Page image](https://www.shutterstock.com/image-photo/collection-wines-store-elite-alcohol-bottles-1316148788)
- [Image for generic wine bottles](https://www.shutterstock.com/image-vector/set-wine-bottles-isolated-on-transparent-574585954)
- [Image for generic champagne bottles](https://www.shutterstock.com/image-vector/vector-realistic-illustration-champagne-bottles-on-1959046075)
- **Image urls submitted by users and displayed in the wine modal section may not be from free image sites**

#### Acknowledgements

   - I received inspiration for this project from our course material, and help with issues from the below resources:
     - [W3schools](https://www.w3schools.com/)
     - [Stackoverlfow](https://stackoverflow.com/)
     - [CSS-Tricks](https://css-tricks.com/)
     - [Mozilla developer](https://developer.mozilla.org/en-US/) 
     - Code Institute slack channel

   - Thanks also to my mentor Rahul Lakhanpal for all his help and support throughout this project. 