## **TESTING**

### Validation

HTML Validation
- Errors found during testing:
    - For the 'add favourites' feature, data is sumitted from a hidden form on the wine modal. The labels for the inputs were only displayed, while the inputs were visually hidden with bootstrap class. This threw up errors as the label cannot be displayed for hidden inputs. Inputs were changed to 'type=hidden' to resolve this.
    - As a modal for each wine is written to the DOM, input and label IDs were duplicated, also causing HTML errors. Once the inputs were changed to 'type=hidden', labels could be removed to resolve this.
    - The remainging warning from the validator only advises that a section lacks a heading, however, this is the empty section used for the flash messages, and a h3 heading is displayed in the child div.
 - [W3C Markup Validator](https://validator.w3.org/) : 
    - [View Results - Home page]()
    - [View Results - Sign Up page]()
    - [View Results - Sign In page]()
    - [View Results - Profile page]()
    - [View Results - Wines page]()
    - [View Results - Add Wine page]()
    - [View Results - Add Review page]()
 
CSS Validation
- No errors found
 - [W3C CSS Validator](https://jigsaw.w3.org/css-validator/) : [View Results]()
 
JS Validation
Javascript validation carried out using [JS hint](https://jshint.com/)
 - home.js
    - Initial verification found some warnings "arrow function syntax (= )' is only available in es6 (use 'esversion 6').(w119)", searching [stackoverflow](https://stackoverflow.com/questions/42866159/arrow-function-syntax-is-only-available-in-es6-use-esversion-6), I found advice to use `/*globals $:false */` as comments at the top of the file to resolve this
    [Errors Screenshot](/workspace/SomethingForTheWeekend/assets/images/readme/jshint-home-errors.jpg)
    - No errors found following this fix.
    [Validated Screenshot](/workspace/SomethingForTheWeekend/assets/images/readme/jshint-home-final.jpg)

PEP8 compliance
Python validation carried out using [PEP8 checker](http://pep8online.com/)
- No errors found.
- [Validated Screenshot]()

 ### User Stories Testing

  - **New Users**

1. As a new user, I want to be able to create a member account
    1. From the home/landing page, the user can either click on 'sign up' link in the nav bar, or else click on the central text over the hero image to be directed to the registration page.
    2. Form validation ensure all the required details are entered.
    3. If no user exists with this username, the account is created for the new member.
2. As a new user, I want to view the wine collection easily
     1. Once the user has created an account, the 'wines' link is clearly visible on the navbar.
     2. On the wines page, the user can explore the collection using the filter and search functions.
3. As a new user, I want to add reviews to existing wines
      1. From the 'view wine' modal, the user can selet the button to add a review to the wine.
      2. If they have not previously added a review for this wine/vintage, the review will be added to the wine.
4. As a new user, I want to add wines to my favourites
      1. From the 'view wine' modal, the user can selet the button to add the wine to their 'favourites'.
      2. If they have not previously added this wine to their favourites, the action will be completed.
5. As a new user, I want to add a new wine to the collection
      1. From any page, the user can click on the navbar link to 'add wine'
      2. Once all required details are submitted and the wine/vintage pair is not already found in the collection, the wine will be added.

 - **Returning Users**

1. As a returning user, I want to be able to log in to my account
    1. From the home page, the user can click on the 'sign in' link on the navbar.
    2. If they click on the central text on the hero image, they will be taken to the 'sign-up' page, where there is also a link to the 'sign-in' page.
    3. Once the user submits their username and password, and the details match the ones in the database, the user will be logged into the session.
2. As a returning user, I want to view the reviews I have made
    1. When the user has signed in, they are taken to their profile page, which displays a list of their reviews on the page.
    2. The user can also see their review for a wine on the modal display for the wine. 
3. As a returning user, I want to edit/remove the reviews I have made
     1. The user can find the review they want to enter on their profile page, or else on the modal display for the wine
     2. Clicking on the 'edit' button takes the user to the 'edit review' page where they caqn make changes to their review text and/or star rating and submit the update.
     3. Clicking on the 'delete' button prompts a confirmation box to ask the user if they are sure they want to remove the review. Clicking ok will remove the review from the database.
4. As a returning user, I want to view the wines in my favourites list
    1. When the user has signed in, they are taken to their profile page, which displays a list of the wines they have added to their favourites list.
    2. The user can click on the 'view' button for each wine to display all the details, or else click on the 'remove' button to remove the wine from their favourites.
5. As a returning user, I want to view the wines I have submitted
    1. When the user has signed in, they are taken to their profile page, which displays a list of the wines they have submitted to the collection.
    2. The user can click on the 'view' button for each wine to display all the details.

 - **Admin Users**
1. As an admin user, I want to be able to removes wines from the website
    1. When the user has signed in as an Admin, they will be able to see a 'delete' button on the modal for each wine.
    2. Once clicked, a popup is displayed to ask for confirmation to delete.
    3. The user can click ok to remove the wine from the database, and it will be no longer visible on the webiste.

### Manual Testing of All Elements

Testing was carried out by myself using Chrome DevTools while writing the code, and once deployed, friends and family helped to test the site on various screen sizes and web browsers.

#### Navbar

  - **Tests**

    1. Check that the 'CellarClub' logo text is visible on all screen sizes, and resized accordingly.
       - **_Verified_**
    2. Check that navbar links are collapsed to hamburger menu for tablet and mobile screens.
       - **_Verified_**
    3. Check that dropdown menu of links is shown when hamburger menu is clicked on mobile and tablet.
       - **_Verified_**
    5. Click on each link to ensure the link goes to the correct page.
       - **_Verified_**

#### Footer

  - **Tests**
    1. Check that footer is visible at the bottom of the page.
        - **_Verified_** 
    2. Check that the 'CellarClub' logo tex, the contact information below, and the the social media icon links are centered and clearly visible on all screen sizes.
        - **_Verified_** 
    3. Check that the social media links open in a new tab.
        - **_Verified_** 
    4. Check that the social media links open to the correct site.
        - **_Verified_** 

  - **Bugs found during testing**
     No issues found.

#### Home Page

  - **Tests**
     1. Navbar and Footer are visible on page
        - **_Verified_**
     2. Hero Image is visible on all screen sizes, and covers the full width and height.
        - **_Verified_**
     3. Text section is visible on all screen sizes, located in the middle of the screen
        - **_Verified_**
    4. Clicking on the text section takes users to the 'sign-up' page
        - **_Verified_**
    5. Only the links for 'sign-up' and 'sign-in' are visible on the navbar
        - **_Verified_**

  - **Bugs found during testing**
     No issues found.

#### Sign up Page

  - **Tests**
     1. Navbar and Footer are visible on page
        - **_Verified_**
     1. Form is centered on the page across all devices
        - **_Verified_**
     3. Sign up form contains elements for 'username', 'password', 'repeat password', 'Date of birth', 'first name' and 'last name'
        - **_Verified_** 
     4. Form validation works for each input field and displays custom message if any field is left blank
        - **_Verified_**  
     5. If user submits a username that already exists, the error "Username already exists" is displayed on the flashed message and registration is not completed
        - **_Verified_**
     6. If user submits a passwords that are not matching, the error "Passwords do not match, please re-check" is displayed on the flashed message and registration is not completed
        - **_Verified_** 
     7.  If user submits a date of birth where their age is less than 18, the error "Sorry, You must be of legal age to join our club" is displayed on the flashed message and registration is not completed 
         - **_Verified_**
     8. If all details are correctly submitted, the user is taken to their profile page and the message "Thanks for joining our club! Browse our wines and add some to your favourites today!" is displayed on the flashed message
        - **_Verified_**
    9. User is logged into session cookie
        - **_Verified_**
    10. The link below the registration button takes the user to the 'sign-in' page if the user already has an account
        - **_Verified_**
    
  - **Bugs found during testing**
    - None

#### Sign in Page

  - **Tests**
     1. Navbar and Footer are visible on page
        - **_Verified_**
     2. Form is centered on the page across all devices
        - **_Verified_**        - 
     3. Sign in form contains elements for 'username' and 'password'
        - **_Verified_**
     4. Form validation works for each input field and displays custom message if any field is left blank
        - **_Verified_**
     5. Form is not submitted if incorrect username or password detils are entered, and the error "Username or password is incorrect, Please try again" is displayed on the flashed message 
        - **_Verified_** 
     6. If all details are correctly submitted, the user is taken to their profile page and the message "Welcome {username}!" is displayed on the flashed message
        - **_Verified_**    
     7. User is logged into session cookie
        - **_Verified_** 
    8. The link below the 'Sign in' button takes the user to the 'sign-up' page if the user does not already have an account
        - **_Verified_** 

  - **Bugs found during testing**
     - None

#### Profile Page

  - **Tests**
     1. Navbar and Footer are visible on page
        - **_Verified_**
     1. Links for "Wines", "Add Wine", "Profile" and "Sign Out" are displayed on Navbar.
        - **_Verified_**
     2. The top part of the page displays centered side by side cards (stacked full width on small screens) displaying "Wines added by {username}" and "{username}'s Favourite Wines". Below these cards another full width card displaying "{username}'s Reviews"
        - **_Verified_**        
     3. "Wines added by {username}" card displays rows with details of wines added to the collection by the user. Card is blank if user has not submitted any wines
        - **_Verified_**
     4. "Wines added by {username}" card: each row shows the wine name and vintage, and view button
        - **_Verified_**
     5. "Wines added by {username}" card: the view button opens the wine modal for the corresponding wine
        - **_Verified_** 
     6. "{username}'s Favourite Wines" card displays rows with details of wines added to the users favourites collection. Card is blank if user has not added any wines to favourites
        - **_Verified_**    
     7. "{username}'s Favourite Wines" card: each row shows the wine name and vintage, view button and 'x' icon button
        - **_Verified_** 
    8. "{username}'s Favourite Wines" card: the view button opens the wine modal for the corresponding wine
        - **_Verified_** 
    9. "{username}'s Favourite Wines" card: the 'x' icon opens an alert to ask for confirmation to remove the wine from the user favourites. On confirmation, the wine no longer appears in the favourites list and the flashed message "Wine has now been removed from your favourites" is displayed.
        - **_Verified_**
     10. "{username}'s Reviews" card: Each row displays the details of each review submitted by the user: wine name, vintage, review, and star rating. Card is blank if user has submitted no reviews
         - **_Verified_**
     11. "{username}'s Reviews" card: Each row displays buttons to "view wine", "delete" and "Edit"
         - **_Verified_** 
     12. "{username}'s Reviews" card: "view wine" button opens the modal for the corresponding wine
         - **_Verified_**    
     13. "{username}'s Reviews" card: "delete" button opens an alert to ask for confirmation to remove the wine from the user favourites. On confirmation, the review is removed from the list, and also from the reviews list on the wine modal. The user is redirected to the wines page and the flashed message "Wine review has successfully been removed" is displayed.
         - **_Verified_** 
      14. "{username}'s Reviews" card: "edit" button redirects the user to the "edit review" page
          - **_Verified_**        

  - **Bugs found during testing**
     - None
     
#### Wine Modal : Profile Page and Wines page.

  - **Tests**
     1. Correct wine name and details corresponding to the "view wine" button section are displayed
        - **_Verified_**
     2. Image is displayed, either of the image url submitted by the user, or if no url submitted, then generic image of wine bottles
        - **_Verified_**        
     3. Link for 'Buy this wine' opens in a new tab, on the correct https://www.wine-searcher.com/ page for the corresponding wine
        - **_Verified_**
     4. Reviews section contains list of reviews showing "Submitted by: {user}", "{review}" and the 1-5 star rating from the user.
        - **_Verified_**
     5. If the user has reviewed this wine, the user will see "delete" and "edit" buttons only on the row with their review.
        - **_Verified_** 
     6. Clicking the "delete" button opens an alert to ask for confirmation to remove the wine from the user favourites. On confirmation, the review is removed from the list, and also from the reviews list on the user profile. The user is redirected to the wines page and the flashed message "Wine review has successfully been removed" is displayed.
        - **_Verified_**    
     7. Clicking the "edit" button redirects the user to the "edit review" page
        - **_Verified_** 
    8. The modal footer section displays buttons for "Add to favourites", "Add review" and "Close"
        - **_Verified_** 
    9. If the wine is not already added to the user favourites, clicking the "Add to favourites" button returns the user to the wines collection page and the flashed message displays "Wine is now added to your favourites list"
        - **_Verified_**
     10. If the wine is already added to the user favourites, clicking the "Add to favourites" button returns the user to the wines collection page and the flashed message displays "This wine was was already added to your favourites list"
         - **_Verified_**
     11. If the user has not already submitted a review for this wine, clicking the "Add review" button redirects the user to the "Add Review" page.
         - **_Verified_** 
     12. If the user has  already submitted a review for this wine, clicking the "Add review" button returns the user to the "wines" collection page and the flashed message displays "You have already reviewed this wine, please edit your review instead" 
         - **_Verified_**    
     13. Clicking the "close button" closes the modal 
         - **_Verified_** 

  - **Bugs found during testing**
     - During testing on the deployed site, when trying to add a wine to the favourites list, the server returned a "HTTP 414 URI Too Long" error. I discovered that the action for the add_favourites form included "wines=wines" which was posting the entire wines collection to the server, which was too long a request. Removing this resolved the error.

#### Wines Page

  - **Tests**
     1. Navbar and Footer are visible on page
        - **_Verified_**
     2. Links for "Wines", "Add Wine", "Profile" and "Sign Out" are displayed on Navbar."
        - **_Verified_**   
     3. A card should be displayed with details for wine in the collection. Cards are displayed full width on mobile, and in 3x3 grid on medium and large screens
        - **_Verified_**    
     4. Card shows a generic wine bottle on the left of each card representing the wine type (red/white/rosé/sparkling)
        - **_Verified_** 
    5. Wine name, grape variety, Country and vintage are displayed on the right of each card.
        - **_Verified_** 
    6. Beneath the wine details, start rating from 1-5 should be displayed as an average of the ratings from all reviews of the wine.
        - **_Verified_**    
     7. Hovering over the card applies a thin burgundy border, heavier shadow and a burgundy outlined "view" button on the card.
        - **_Verified_** 
    8. Clicking anywhwere on the card opens the corresponding wine modal.
        - **_Verified_** 
     9. At the top of the page, "Filter by Wine Type" dropdown and "Search" input are displayed
        - **_Verified_**
     10. "Filter by Wine Type" dropdown shows "Red", "White", "Rose" and "Sparkling" options
         - **_Verified_**
     11. Selecting a filter option and clicking the "filter" button filters the wine cards to the corresponding option (wine bottle colour provides easy verification)
         - **_Verified_** 
     12. If no results found for that filter option, "Sorry! No wines matching your search" is displayed.
         - **_Verified_**    
    13. User enters search term in the search input box and clicks the "search button", all wine cards with any corresponding words are displayed.
         - **_Verified_** 
    14. If no results found for the search option, "Sorry! No wines matching your search" is displayed.
        - **_Verified_**
    15. Clicking the "Reset" button restores all the cards to the page.
        - **_Verified_** 

  - **Bugs found during testing**
     - Cards were displaying in varying heights even though fixed height dimensions were specified for the media types in the CSS file. Removing the bootstrap "row-cols-auto" class from the grid row resolved this.

#### Add Wine Page

  - **Tests**
     1. Navbar and Footer are visible on page
        - **_Verified_**
    2. Links for "Wines", "Add Wine", "Profile" and "Sign Out" are displayed on Navbar
         - **_Verified_**
     1. Form is centered on the page across all devices
        - **_Verified_**
     3. Sign up form contains elements for 'Select Wine Type' drop down, 'Wine Name', 'Grape', 'Vintage', 'Country', 'Region', 'Image URL', 'Review' and 'Rating' inputs.
        - **_Verified_**
     4. Form validation works for each input field and displays custom message if any field is left blank (Region and Image URL fields only are optional)
        - **_Verified_**  
     5. If user submits a wine where the wine name and vintage are matching an existing wine in the collection, user is redirected to the wines collection page and a flashed message displays "Wine/Vintage already exists, please add a review"
        - **_Verified_**
     6. If user submits a wine that is not found in the collection, the wine details are added to the database, user is redirected to the wines collection page and a flashed message displays "Your wine has been added to our collection!"
        - **_Verified_** 
     6. Cancel Button beside the submit button returns users to the wines collection page
        - **_Verified_** 
     
  - **Bugs found during testing**
    - Grape variety input did not have the "required" attribute
    - Country input was limited to 4 character input

#### Add Review Page

  - **Tests**
     1. Navbar and Footer are visible on page
        - **_Verified_**
    2. Links for "Wines", "Add Wine", "Profile" and "Sign Out" are displayed on Navbar
         - **_Verified_**
     1. Form is centered on the page across all devices
        - **_Verified_**
     1. Page header displays "Submit a review for {wine name}, showing the correct wine name    "
        - **_Verified_**
     3. Form contains elements for 'Wine Name', 'Vintage', 'Review' and 'Rating' inputs.
        - **_Verified_**
     3. 'Wine Name' and 'Vintage' inputs are already populated with the corresponding details and are read-only
        - **_Verified_**
     4. Form validation works for each input field and displays custom message if any field is left blank, all fields are required.
        - **_Verified_**  
     5. On form submit, the user is returned to the wines collection page and flashed message displays "Review successfully submitted"
        - **_Verified_**
     6. Cancel Button beside the submit button returns users to the wines collection page
        - **_Verified_** 
     
  - **Bugs found during testing**
    - No bugs found

#### Edit Review Page

  - **Tests**
     1. Navbar and Footer are visible on page
        - **_Verified_**
    2. Links for "Wines", "Add Wine", "Profile" and "Sign Out" are displayed on Navbar
         - **_Verified_**
     1. Form is centered on the page across all devices
        - **_Verified_**
     1. Page header displays "Submit a review for {wine name}, showing the correct wine name    "
        - **_Verified_**
     3. Form contains elements for 'Wine Name', 'Vintage', 'Review' and 'Rating' inputs.
        - **_Verified_**
     3. 'Wine Name' and 'Vintage' inputs are already populated with the corresponding details and are read-only
        - **_Verified_**
     3. Review section and Rating input already populated with the existing review details
        - **_Verified_**
     4. Form validation works for each input field and displays custom message if any field is left blank, all fields are required.
        - **_Verified_**  
     5. On form submit, the user is returned to the wines collection page and flashed message displays "Review successfully submitted"
        - **_Verified_**
     6. Cancel Button beside the submit button returns users to the wines collection page
        - **_Verified_** 
     
  - **Bugs found during testing**
    - No bugs found

#### Admin function

  - **Tests**
     1. When logged in as admin, user can see "Delete" button at the bottom of the wine modal to remove the wine from the collection 
        - **_Verified_**
    2. On click of delete, confirmation alert appears to verify removal
         - **_Verified_**
    3. Once wine is deleted, all reviews for this wine are also deleted, and wine is removed from any user favourites lists
        - **_Verified_**

  - **Bugs found during testing**
    - Wine and reviews were deleted, but wine was not removed from the favourites list as this is part of the users database. Additional code was added to remove the wine from any user favourites.
    
#### Sign Out Function

  - **Tests**
     1. When the user is logged in, "Sign Out" link is accessible from navbar on every page
        - **_Verified_**
    2. On click of "Sign Out", user is removed from session and redirected to the "Sign In" page, flashed message displays "You have been Logged out"
         - **_Verified_**

  - **Bugs found during testing**
    - No bugs found
    
### Lighthouse Testing
Results
 |     Page   | Wireframe | Wireframe |
    | ----------- | ----------- | ----------- |
    |Home page   | [Desktop](https://github.com/annemarie293/cellarClub/blob/master/workspace/CellarClub/static/images/lighthouse/desk-home.png) | [Mobile](https://github.com/annemarie293/cellarClub/blob/master/workspace/CellarClub/static/images/lighthouse/mobile-home.png)|
    |Sign up page   | [Desktop](https://github.com/annemarie293/cellarClub/blob/master/workspace/CellarClub/static/images/lighthouse/desk-sign-up.png) | [Mobile](https://github.com/annemarie293/cellarClub/blob/master/workspace/CellarClub/static/images/lighthouse/mobile-sign-up.png)|
    |Sign in page   | [Desktop](https://github.com/annemarie293/cellarClub/blob/master/workspace/CellarClub/static/images/lighthouse/desk-sign-in.png)  | [Mobile](https://github.com/annemarie293/cellarClub/blob/master/workspace/CellarClub/static/images/lighthouse/mobile-sign-in.png) |
    |Wines page     | [Desktop](https://github.com/annemarie293/cellarClub/blob/master/workspace/CellarClub/static/images/lighthouse/desk-wines.png)    | [Mobile](https://github.com/annemarie293/cellarClub/blob/master/workspace/CellarClub/static/images/lighthouse/mobile-wines.png) |
    |Add wine page  | [Desktop](https://github.com/annemarie293/cellarClub/blob/master/workspace/CellarClub/static/images/lighthouse/desk-add-wine.png)   | [Mobile]https://github.com/annemarie293/cellarClub/blob/master(/workspace/CellarClub/static/images/lighthouse/mobile-add-wine.png) |
    |Add wine page  | [Desktop](https://github.com/annemarie293/cellarClub/blob/master/workspace/CellarClub/static/images/lighthouse/desk-add-wine.png)   | [Mobile](https://github.com/annemarie293/cellarClub/blob/master/workspace/CellarClub/static/images/lighthouse/mobile-add-wine.png) |
    |Add/edit review page   | [Desktop](https://github.com/annemarie293/cellarClub/blob/master/workspace/CellarClub/static/images/lighthouse/desk-add-review.png)| [Mobile](https://github.com/annemarie293/cellarClub/blob/master/workspace/CellarClub/static/images/lighthouse/mobile-add-review.png)|
    |Profile page   | [Desktop](https://github.com/annemarie293/cellarClub/blob/master/workspace/CellarClub/static/images/lighthouse/desk-profile.png)  | [Mobile](https://github.com/annemarie293/cellarClub/blob/master/workspace/CellarClub/static/images/lighthouse/mobile-profile.png)|

#### Performance
Green scores on all pages except mobile wines and mobile home in mid 70s. Some room for improvement with image types and sizes which I did not have time for.
#### Accessibility
All green scores except high 80s for mobile/desk Add Wine page, and high 70s.for mobile/desk Add Review page. Some improvements can be made with better form labelling, and colour contrast changes.
#### Best Practices
All green scores
#### SEO
All green scores
___