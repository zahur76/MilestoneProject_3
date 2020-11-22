# **Artist For Life**

![Responsive image for site](static/doc/responsive2.png)

## TABLE OF CONTENT 
* [Introduction](#introduction)    
* [UX](#ux)
    * [UX design work](#ux-design-work)
    * [Colour scheme](#colour-scheme)
    * [Typography](#typography)
* [Development cycle](#development-cycle)
* [Features](#features)
    * [Navbar](#navbar)
    * [Modals](#modals)
    * [search bar and pagination](#search-bar-and-pagination) 
    * [Profile page](#profile-page)
    * [Control center](#control-center)
    * [Side navigation](#side-navigation)
    * [Sold feature](#sold-feature)
    * [Flash messages](#flash-messages)
    * [Footer](#footer)
* [Technologies used](#technologies-used)
* [Images](#images)
* [Data schema](#data-schema)
    * [CRUD operations](#crud-operations)
    * [CRUD authorisation](#crud-authorisation)    
* [Testing](#testing)
    * [UX testing](#ux-testing)
    * [validators](#validators)
    * [Chrome DevTools](#chrome-devtools)    
    * [Site testing](#site-testing)
    * [Responsive design](#responsive-design)
    * [Browser compatibility](#browser-compatibility)
    * [Button and link testing](#button-and-link-testing) 
    * [Crud operation testing](#crud-operation-testing)    
    * [Issues encountered during development](#issues-encountered-during-development)

* [Deployment](#deployment)
* [Future improvments](#future-improvements)
* [Credits](#credits)

## INTRODUCTION 

This site has was created as a product listing site with the intention of providing a service for artist to showcase 
their art work to potential buyers and other ethusiasts in the Mauritian market. 

The site would permit the registered users to upload and manage their items while also creating a profile page. Thus providing 
the user with the power of creating, updating and modifying their items by using a database system. 

The live site can be found [here](http://artist-for-life.herokuapp.com/).

## UX 

By visiting this site as a user I want to:
* be able to easily understand what the site is about inorder to see if it is of interest to me. 
* have a user friendly register/login process inorder to start using the site.  
* be able to upload my item information with ease inorder for buyers to view them.
* be provided with an option to upload my personal information so potential buyers can see who I am.
* be able to edit and delete all uploaded information if any changes need to be made.
* be able to tag an item as sold so as the buyers can see how in demand my works are.

By visiting this site as a buyer I want to:

* have information about the item being sold in one place for convenience of use.
* have the ability to view items by search criteria inorder to narrow down item list to specific requirements.

By using this site as the site owner:

* be able to edit and delete any loaded information for content control purposes.
* have full access to all uploaded information in one convenient place for CRUD operations.

### UX design work 

The following provides an overview of the site layout and logic behind design choices.

A wireframe was constructed using balsamique wireframes. It can be found [here](assets/doc/wireframe.pdf).

The site was designed to have an artistic atmosphere by by making use of hero image reflecting an artist studio with 
suitable banner text. 

Modals were the preferred chose for login and registration since was more visually appealing.

Also the site implemented several features to make registration, login, adding items and profiles as user friendly and 
intuitive as possible. 

Flash messages were included so as to enable the user obtain feedback on whether actions had been completed. The messages
were made to disappear after 5's since the messages were of temporary nature.

A search bar was then provided inbetween hero image and items list as it would provide filter options all listed item. This
was situated above the items list.

The items section was placed next and consisted of using a card display divided into image and desciption sections providing
all the nessary info about the item in one place. 

An item list was situated on the right for devices having a screen size large or higher to provide a scroll function to specific
item names.

The profile page consisted of the seller profile information followed by all items the seller has listed in one convenient place.
This was thought to improve UX since it would be a be able to showcase all works by the user to potential buyers.

For the site owner a control center page ws included to allow for centralised place where all CRUD functions could be performed.

All features are described in detail [below](#features).

### Colour Scheme 

Several colour schemes were tested and the following palette was finally adopted since it was thought to fit into the overall site theme.

![Image of colour scheme](static/doc/colours.png)

![Image of header](static/doc/header-colour.png)

All button were also designed to have an identical colour scheme for easy identification.

### Typography

Font were obtained from [google font](https://fonts.google.com/) and consisted of the following:
- 'Fredericka the Great ws used for logo, login/registration header and flash messages.
- 'Parisienne' used all page headers
- 'Lora' was used for flash messages
- 'Source Serif Pro' used for banner text
- Roboto

## DEVELOPMENT CYCLE

The main development cycle is listed below:

1. Site design work making use of sketch pad and balsamique.
2. Database design (field definition) and creation using mongodb.
3. Coding of base html page with header, footer and navbar.
4. Programming of item page.
5. Coding of registration and login modal in base html page.
6. Coding of logout function.
7. Coding of profile page.
8. Coding of add/edit/delete items funcitons.
9. Coding of add/edit/delete profile funcitons.
10. Coding of control center functions.
11. Coding of add/edit/delete categories funcitons.
12. Mid Project Review.
13. Implementation of pagination for items page.
14. Implementation of search bar on items page with pagination.
15. Restructuring of profile page.
16. Restructuring of registration modal to allow for email and phone input.
17. Modifications to add/edit items page due to modification above.
16. Creation of about modal.
17. Coding of sold fucntion.
18. Final project testing and adjustments.

## FEATURES

This section gives details of the features included and their function.

### Navbar

A standard navbar was used which was obtained from materialize to allow navigation between the
different pages and was made to collapse on medium and down devices.

![Navbar](static/doc/navbar.png)

### Modals

During site design it was decided to use modals for registration and login instead of having seperate pages. This was 
thought to improve the overall site experience since login could be done from the main page. Modals could be 
interchanged with a click here button and would reopen if data submitted did not meet the login/registration criteria. 

![Image of login modal](static/doc/login.png)

![Image of register modal](static/doc/register.png)

A third modal was also used for the about section.

### Search bar and pagination

Search bar and pagination features were included in the site. These functions were not originally planned and were  
were included after mid project review since it was thought to be good practice for such a site where item quantity 
could be significant. The inclusion was thought to improve UX. The search criteria used were:
1. seller name
2. category
3. description

These criterion were suitable enought to narrow down the item list significantly whilst offering the user broad search requirements.

![Search bar](static/doc/search.png)

### Item cards

The item was displayed on cards and divided into two areas, one for item image and the other for item description.
All information on the item was located in one place for convenience and the image could be enlarged by clicking 
on them by making use of materialize media box.

![Item card](static/doc/item.png)

The card also had a link to the profile page of the seller if the buyer wished to obtain further information. Edit and
delete item buttons were also included on the card to provide conevenient place for the item owner to make modifications.

### Profile page

A user profile page was included which permitted the user to upload a profile pic and provide a description about themselves
so a buyer could obtain more details about the person. This feature was made to be optional.

This page also provided the profile user and buyer with and centralised page where all the profile users items would be listed in a 
convenient way. 

The items could be modified and deleted at will by the profile user instead of having to search for each individual item 
on the main page hence improving the user interface.

![Profile page](static/doc/profile.png)

### Control center

A control center page was included for only for the admin. This page listed all registered users, items and categories for the admin
to have access to in one convenient place. This page was used for control purposes were all modifications could be made instead of having 
to search for each individual user and items. 

![Control center](static/doc/control.png)

### Side navigation

A side navigation menu was added on large screen and higher devices. This permitted the user to scroll to items by
name and was added to improve user experience.

![Side navigation menu](static/doc/menu.png)

### Sold feature

The profile page also included a sold feature whereby the item could be listed as sold instead of deleting them and could be used
as a marketing tool indicating that the seller items were in demand.

Once the item sold feature was activated the item would be removed from items list on the main page.

![Sold](static/doc/sold.png)

### Flash messages

Flash messages were used when ever a CRUD operation was performed. This would provide confirmation to the user
that the operation had been completed and the database had been updated.

![flash message](static/doc/flash.png)

### footer

A basic footer was provided with a link to wikipedia containing a list of art museums.

## TECHNOLOGIES USED

* HTML5
* css 
* javacript (ES6)
* python 
* flask for the web framework
* mongodb to store data 
* Jquery to simplify DOM manipulation
* pylint, flake8, PEP8 for python syntax
* official W3C validator to check HTML syntax
* css official validator(jigsaw) to check css syntax
* JSHint to check javacript syntax 
* Chrome developers tools for analysing scripts and debugging
* Materilize 1.0.0 for :
    1. page layout purposes and responsive design aspects
    2. Forms 
    3. Modals
    4. Scrollspy
    5. Materialized media box
    6. Navbar
    7. Footer
* balsamiq wireframes application to create the site design
* Chrome extension 'responsive viewer' to aid in reponsive design 

## Images 

A important part of the website design process was the means by which the user would provide images to the site. 
From the outset it was decided to allow the user to upload images instead of the user providing a URL. This was thought to 
improve the overall site experience since it would be much more convenient for the user. 

A tutorial on how to upload images into mongodb database was sought and is located [here](https://www.youtube.com/watch?v=DsgAuceHha4)

Mongodb BSON documents allowed the storage of images and was capped at 16mb. This was thought to be sufficient for the
intended use. A helper text when uploading images was added stating a lower limit of 10mb. 

Images which were deleted had there correspoding fs.files and fs.chunks removed for house cleaning purposes since the database was 
of limited size.

## Data schema 

Mongodb was used for database storage since this type of non relational database was well suited for storing user and
item details which contained information of different formats. Information could be displayed faster since a query doesn’t 
have to view several tables in order to deliver an answer, this was well suited for the items collections.

Also flexible schema offered by mongodb was thought to be advantageous in the likely event that new fields would need to be
added in the future. This was hightlighted by the introduction of the sold feature into the items collection.

The main database contained 4 collections:

| Collections         |   Fields                                                           |
|:--------------------|:-------------------------------------------------------------------|
|User                 |  Username, Password, contact number, email                         |                                     |    
|Profile              |  Username, profile image, fullname, profile description            |
|Items                |  Category, image, name, description, price, username, sold         |             
|Categories           |  Category name                                                     |            

The user collection was used for registration and login purposes. The contact number and email fields were
added to this collection instead of the items collection since it would only have to be entered once and would remain
constant for that user. This would also prevent the user from having to add contact info with each item upload and prevent 
multi contact info for the same user.

The username would be used as seller name.

The profile collection was used to provide additional information on the seller and was purposely given its own 
collection since it was an option and could be independantly edited without affecting other collections. 

The items collections consisted of all the required information about the item being sold for a buyer to see. 

Categories collections consisted of seven main painting categories and was made to be independant.

The user, profile and items collections had a matching field of 'username' which was used as a common reference. This was
done to links documents where common information about a user needed to displayed. One such page which made use of this 
reference was the profile page.

![Collections](static/doc/collections.png)

### CRUD operations

CRUD operations were essential for the running of the site and were provided for the following features:

| Feature             |   Create   |   Read    |  Update  |  Delete  |  Mongodb collection | 
|:--------------------|:-----------|:----------|:---------|:---------|:--------------------|
|User registration    |  &#9745;   |           |  &#9745; |          | Users               |   
|User login           |            |  &#9745;  |          |          | Users               |
|User items           |  &#9745;   |  &#9745;  |  &#9745; |  &#9745; | Items               |             
|User Profile         |  &#9745;   |  &#9745;  |  &#9745; |  &#9745; | Profile             |            
|Item sold            |  &#9745;   |  &#9745;  |  &#9745; |          | Items               |
|Category             |  &#9745;   |  &#9745;  |  &#9745; |  &#9745; | Category            |

The update operation for the registration feature was for the contact information fields only. 

### CRUD authorisation

A user would have authorisation to update and delete any information uploaded by themselves except for the their username,
and password.

The admin would have authorisation to update and delete all uploaded user information present in the database.
This was done so as the admin has control on what information was being displayed on the site.

## TESTING 

This section provides details of testing performed during development. The following table highlights the different stages when testing were carried out:

| Test                | Stage Performed                                  | Tool used                                     |
|---------------------|:-------------------------------------------------|:----------------------------------------------|
|Syntax errors        |Once During mid development and on completion     |W3C validator, css validator(jigsaw), jshint   |
|Debugging            |During the whole project                          |Chrome Devtools                                |
|Reponsive design     |During the whole project                          |Chrome Devtools and reposnsive viewer extension|
|Site testing         |As from when main site was completed              |By myself and relatives                        |
|Browser compatibility|On project completion                             |Manual testing on browsers                     |                    
|Button/link testing  |During development and project completion         |Manual testing                                 |

### UX testing

The goals set out in the UX section were accomplished as follows:

1. User goal: *be able to easily understand what the site is about inorder to see if it is of interest to me*<br>
The site design was thought to achieve this goal and an about section was included to this effect.

2. User goal: *have a user friendly register/login process inorder to start using the site*</br>
The site made use of easy to use straight forward registration and login modals which made the both processes very easy. 

3. User goal: *be able to upload my item information with ease inorder for buyers to view them*</br>
This was achieved by using an add item form page which contained all the necessary information required for uploading in 
one easy to use form.

![Add item](static/doc/add-item.png)

4. User goal: *be provided with an option to upload my personal information so potential buyers can see who I am*</br>
This was achieved by having using a profile page which is described [above](#profile-page).

5. User goal: *be able to edit and delete all uploaded information if any changes need to be made*</br>
This was achieved by using the CRUD functions detailed [above](#crud-operations).

6. User goal: *be able to tag an item as sold so as the buyers can see how in demand my works are*</br>
This was achieved by using the sold item feature detailed [above](#sold-feature).

7. Buyer goal: *have information about the item being sold in one place for convenience of use*</br>
This was achieved by using the items cards detailed [above](#item-cards).

8. Buyer goal: *have the ability to view items by search criteria inorder to narrow down item list to specific requirements*</br>
This was achieved by using the search bar detailed [above](#search-bar-and-pagination).

9. Site owner: *be able to edit and delete any loaded information for content control purposes.*</br>
This was achieved by allowing full CRUD operations to the admin as detailed [above](#crud-authorisation).

10. Site owner: *have full access to all uploaded information in one convenient place for CRUD operations*</br>
This was achieved by using the the [control center](#control-center) and tested by myself.

The above user goals were further tested by obtaining feedback from an artist. The feedback was positive all on aspects.

### Validators

Code syntax were checked for errors with the following validators:
* official W3C validator located [here](https://validator.w3.org/)
* css official validator(jigsaw) located [here](https://jigsaw.w3.org/css-validator/)
* JSHint located [here](https://jshint.com/)
* Pylint for python code validation

Errors were corrected and final test results are given below:

| Test                                 | Expected result                | Results            |                                 
|:-------------------------------------|:-------------------------------|:-------------------|
|W3C validator                         |No errors or warnings to show   |Passed              | 
|css official validator(jigsaw)        |No errors found                 |Passed              |                            
|JSHint located                        |Congratulations. No error found |Warnings present    |
|Python validator(pylint, Flake8, PEP8)|No errors                       |Passed              |

For the W3C validator all errors due to jinja templates were filtered out.
The error 'Doctype must be declared first' was also ignored and was due to the use of base.html template.

The Jshint test results had the warning " 'let' is available in ES6 (use 'esversion: 6') or Mozilla JS extensions (use moz)." was due to
syntax used for defining variables.

### Chrome DevTools

Chrome DevTools were used extensively during development phase to assist in:
* page layout issues 
* checking errors
* debugging
* verifying correct output using console  

### Site testing

The site was tested by myself and once the main site was completed it was further tested by having an artist 
register and use the site. The feedback obtained was positive.

### Responsive design

The site was viewed on different device sizes to check for correct reponsive design. This was done using primarily
Chrome DevTools with different emulated devices(moto G4, iphone 6/7/8, ipad, ipad pro). The responsive viewer chrome 
extension was also used. Resolutions covered are as follows:

|Screen resolution| Device                        |
|:----------------|:------------------------------|
|1280 X 800       |large screen                   |
|1024 X 800       |medium screen                  |
|768 X 1024       |ipad                           |
|414 X 736        |iPhone 8 Plus, 7 Plus, 6S Plus |
|375 X 667        |iPhone 8, 7, 6S, 6             |
|414 X 896        |iPhone XR, XS Max              |
|375 X 812        |iPhone XS, X                   |
|412 X 846        |Galaxy S9 Plus, S8 Plus        |
|360 X 740        |Galaxy S9, Note 8, S8          |
|323 X 786        |Pixel 3, 3 XL                  |

![reponsive design Image](static/doc/responsive.png)

A final check was done using the website http://ami.responsivedesign.is/. 

### Browser compatibility

The site was tested on Google Chrome, FireFox, Internet Explorer, Safari and Opera.

### Button and link testing

The following gives test results for button and link testing not related to CRUD operations.

|links/button                            |Expected result                                         | Results |                                 
|:---------------------------------------|:-------------------------------------------------------|:--------|
|Register                                |Register modal to open                                  |Passed   |
|Submit on Register modal(correct data)  |Flash message "You have been registered"                |Passed   |                                           
|Submit on Register modal(incorrect data)|Flash message error mesage and modal to reopen          |Passed   |
|Submit on Login modal(correct data)     |Flash message "You have been logged in"                 |Passed   |
|Submit on Login modal(incorrect data)   |Flash error message and modal to reopen                 |Passed   |
|here text on modals                     |Login/Register Modals to switch over                    |Passed   |
|Logout                                  |Flash message "You have been logged out"                |Passed   |
|About                                   |About Modal to open up                                  |Passed   |
|Register on about modal                 |About modal to close and register modal to open         |Passed   |
|Artist for life logo                    |Main index html page to load                            |Passed   |
|Artist for life logo                    |Main index html page to load                            |Passed   |
|Control center                          |Control center html  page to load                       |Passed   |
|Profile                                 |Profile html page to load                               |Passed   |
|Add item                                |Add item html form page to load                         |Passed   |
|Edit item                               |Edit item html form page to load                        |Passed   |
|Create profile                          |Add profile html form page to load                      |Passed   |
|Edit profile                            |Edit profile html form page to load                     |Passed   |
|Edit Contact details                    |Edit contact html form to load                          |Passed   |
|Mark as sold                            |Sold banner text to appear on item                      |Passed   |
|Mark as available                       |Sold banner text to be removed from item                |Passed   |
|Seller profile                          |Profle page to load for that user                       |Passed   |
|chevron arrows                          |Loading of next or previous page                        |Passed   |
|pagination numbers                      |Loading of selected page                                |Passed   |
|search button                           |Search page to load with relevant search results        |Passed   |
|Reset search                            |Main item page to load                                  |Passed   |
|Palette icon                            |Wikepedia page to open in seperate page                 |Passed   |
|click to call                           |Phone request to be made with correct number            |Passed   |
|click to mail                           |Email request activated with correct email              |Passed   |

### Crud operation testing

The following table summarises CRUD operation testing

|Button            | Location              |Expected result                                                     | Results |                                 
|:-----------------|:----------------------|:-------------------------------------------------------------------|:--------|
|Submit            | Registration modal    |user information to be added to users collection in mongodb         |Passed   |
|Add item          | Add item form page    |Item information to be added to items collection in mongodb         |Passed   |
|Add profile       | Add profile form page |Profile information to be added to profiles collection in mongodb   |Passed   |
|Confirm           | Edit item form page   |Item information to be updated in items collection in mongodb       |Passed   |
|Confirm           | Edit profile form page|Item information to be updated in profiles collection in mongodb    |Passed   |
|Delete            | items main page       |Item information to be removed from items collectionsin mongodb     |Passed   |
|Delete            | Profile main page     |Item/profile to be removed from items/profile collection in mongodb |Passed   |
|confirm           | Edit contact form page|Contact details to be updated in users collection in mongodb        |Passed   |
|confirm           | Edit contact form page|Contact details to be updated in users collection in mongodb        |Passed   |
|Add category      | Control center page   |New category to be added to categories collection in mongodb        |Passed   |
|Confirm           | Edit category page    |Category to be updated in categories collection in mongodb          |Passed   |
|Mark as sold      | Profile html page     |Sold field to be updated to "true" in items collection              |Passed   |
|Mark as available | Profile html page     |Sold field to be updated to "false" in items collection             |Passed   |

During item deletion/editing it was checked to see that image data was removed/updated from fs.files and fs.chunks also.

A further test was performed whereby all items and profiles were deleeted to check whether no data remained in fs.files and
fs.chunks. This test was successful.

### Issues Encountered during development

During testing phase the following issues were indentified and corrected.

1. If a jinja template contained two similar loops from the same query then only the first would be activated. This issue
was resolved by adding ```list``` to the mongodb query. For example ```items = list(mongo.db.items.find({"username": username}))```.

2. If editing of item or profile was performed then the user would have to reselect an image since a image preselect value could 
not be added to the edit form. The solution adopted was to remove the ```required``` attribute for the image file and then add a condition 
in the backend to detect if the user had indeed uplaoded a new image. If it was the case then the new file would be updated in the
collection database, if not then the old image would be kept.

3. When items were deleted the image data, fs.files and fs.chunks, would still remain in the monogdb database. This was thought to 
be ineffective since such data would take up space in the size restricted mongodb database. Such data would also never be reused.
A solution was found to remove these files when item and profile deletion were performed by using the objectid and filename as 
reference. The ObjectId was a common reference between the items/profiles collection and fs.files and was used to clear data from 
fs.files collection. The filename was a common reference between fs.files and fs.chunks and was used to clear data from the fs.chunks collection.

4. Initially the contact info was part of the add item form page. After mid project review this was thought not to be logical
since these fields would remain constant for the user and would have to be added each time the user uploaded an item. The solution
adopted was to have the contact details added to the user collection as from registration which made more sense. These field could
then be queried and used accordingly when required without user input. 

5. The scrollspy function initially made use of username as reference to scroll to the item. However, since the username was not unique 
indentify for uploaded items, this caused issue when items having same username where clicked on. The solution adopted was to use ```item._id``` 
as reference since it was unique.

6. In the initial testing phase items having images with same filename were uploaded. When these items were deleted this caused
errors due to the existance of duplicate filenames. Research was performed a solution found 
[here](https://www.geeksforgeeks.org/generating-random-ids-using-uuid-python/).The solution made use of python library UUID 
(Univrsal Unique Identifier) which would allow uploaded files to  be assigned a unique filename.

7. When sign-in and registration were performed and incorrect username/password or existing username/password were used the modals
would close with the corresponding flash error message with no reopenning of modals. This was thought to be poor UX and was 
corrected with javascript which would trigger the repoenning of modals if the above conditions occurred.

![Code](static/doc/modal-code.png)

8. After mid project review it was observed that such a site would have large amounts of items uploaded and pagination would 
be essential for proper UX. Research was performed and flask-paginate [module](https://pythonhosted.org/Flask-paginate/) document was 
consulted for pagination. However, after several attempts the module did not yeild the required results. The documentation was 
then studied and pagination was done using python programming to produce the desired results. The pagination was also extended to the 
search page.

# DEPLOYMENT

Gitpod was used as an online IDE and then pushed to GITHUB for [hosting](https://zahur76.github.io/MilestoneProject_2/).

To deploy the project on github pages the following steps were used:
1. Login to Github and select the the MilestoneProject_2 repository.
2. Press the setting button on the top menu bar located on the right-hand side.</br>
![image of github menu bar](assets/doc/github.png)

3. Scroll down to the Github pages section and select Master branch from the dropdown menu and press save.</br>
![image of github pages section](assets/doc/githubpages.png)

4. Once completed an active link is published for the repository. 

To run code locally the following steps should be performed:
1. On GitHub, navigate to the main page of the repository.
2. Above the list of files, click  Code and copy URL.</br>
![image of github pages section](assets/doc/clone.png)
3. Open Git Bash.
4. Change the current working directory to the location where you want the cloned directory.
5. Type git clone, and then paste the URL you copied earlier.</br>
    $ git clone https://github.com/zahur76/MilestoneProject_2
6. Press Enter to create your local clone.

## FUTURE IMPROVEMENTS

Add a countdown timer option to add another level of difficulty to the game. The user would be able to specify both
a difficulty level and a time limit inorder to complete the game.

## CREDITS

### Content

* [wikepedia](https://en.wikipedia.org/wiki/Matching_game) was used as source for rules.
* Star Wars character facts obtained from open source [swapi](https://swapi.dev/).
* dev.to was consulted to assist in footer [placement](https://dev.to/amjadmh73/the-best-way-to-keep-the-footer-at-the-bottom-of-your-web-page-32ek).

### Media

* The following fonts were used from [google font](https://fonts.google.com/):
    - Roboto
    - Orbitron 
    - Press Start 2P
* Sound clips were obtained from [101 soundboard](https://www.101soundboards.com/).
* Card images were purchased from [mintParcel](https://www.mintparcel.com).
* Logo obtained from [flaming text](https://flamingtext.com/).
* Icons for home, social media and galactic senate were obtained from [font awesome](https://www.fontawesome.com).
* Loading gif was obtained from [icons8](https://icons8.com/).

### Acknowledgment

* I would like to thank zara meerun, sofia meerun and behlal meerun for testing the game and also my mentor 
Allen Thomas Varghese for his input during the mentor sessions.
