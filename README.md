# **STAR MATCH**

## TABLE OF CONTENT 
* [Introduction](#introduction)    
* [UX](#ux)
    * [UX design work](#ux-design-work)
    * [Colour scheme](#colour-scheme)
    * [Typography](#typography)
* [Development cycle](#development-cycle)
* [Features](#features)
    * [Grid sytem](#grid-system)
    * [Control buttons and counter](#control-buttons-and-counter)    
    * [Footer](#footer)
* [Technologies used](#technologies-used)
* [Javascript game logic](#javascript-game-logic)
* [Testing](#testing)
    * [UX testing](#ux-testing)
    * [validators](#validators)
    * [Chrome DevTools](#chrome-devtools)
    * [Jasmine unit testing](#jasmine-unit-testing)
    * [Game testing](#game-testing)
    * [Responsive design](#responsive-design)
    * [Button and link testing](#button-and-link-testing)    
    * [Issues encountered during development](#issues-encountered-during-development)

* [Deployment](#deployment)
* [Future improvments](#future-improvements)
* [Credits](#credits)

## INTRODUCTION 

![Responsive image for game](assets/doc/responsive.png)

This site has was created as a product listing site with the intention of providing a service for artist to showcase 
their art work to potential buyers and other ethusiasts. 

The site would permit the registered users to upload and manage their items while also creating a profile page. Thus providing 
the user with the power of creating, updating and modifying their items by using a database system.

## UX 

By visiting this site as a user I want to:
* be able to easily understand what the site is about inorder to see if it is of interest to me. 
* have a user friendly register/login process inorder to start using the site.  
* be able to upload my items information with ease inorder for buyers to view them.
* be provided with an option to upload my personal information so potential buyers can see who I am.
* be able to edit and delete all uploaded information if any changes need to be made.

By visiting this site as a buyer I want to:

* be able to easily understand what the site is about inorder to see if it is of interest to me. 
* have information about the item being sold in one place for convenience of use.
* have the ability to view items by search criteria inorder to narrow down item list to specific requirements.

By visiting this site as the site owner:

* be able to edit and delete any loaded information for content control purposes.
* have full access to all uploaded information in one convenient place if any modifications is required.

### UX design work 

A wireframe was constructed using balsamique wireframes. It can be found [here](assets/doc/wireframe.pdf).

The site was designed to have an artistic atmosphere by by making use of hero image reflecting an artist studio with 
suitable banner text. 

Also the site implemented several features to make registration, login, adding items and profiles as user friendly and 
intuitive as possible. 

A search bar was then provided inbetween hero image and items list as it would provide filter options all the items listed
below.

The items section was placed next and consisted of using a card display divided into image and desciption sections providing
an all nessary info about the item in one place. 

An item list was situated on the right for devices having a screen size large or higher to provide a scroll function to specific
item names.

The profile page consisted of the seller profile information followed by all items the seller has listed in one convenient place.
This was thought to improve UX since it would be a be able to showcase all works by the user to potential buyers.

For the site owner a control center page ws included to allow for centralised place where all CRUD functions could be performed.

All features are described in detail [below](#features).

### Colour Scheme 

Several colour schemes were tested and the following palette was finally adopted since it was thought to fit into the overall site theme well.

![Image of colour scheme](static/doc/colours.png)

![Image of header](static/doc/header-colour.png)

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
2. Database design and creation using mongodb.
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
17. Final project review and adjustments.


## FEATURES

The site consists of a two page design. The first page consists of the game which is made up of a logo, rules link, 
card grid system, control buttons, counter and footer. Three modals have also been included and described below.

![Image of main page](assets/doc/mainpage.png)

The second page consists of a tile grid system which can be clicked on to show character facts. A home button was also included
below the tiles. 

![Image of character page](assets/doc/characterpage.png)

### Grid system

![Image of card grid system](assets/doc/grid.png)

The card grid system forms the main part of the site whereby the user can click on tiles to select a pair of cards for comparison.
The design also includes a hover effect to assist the user is knowing which card will be selected.

### Control buttons and counter

![Image of control buttons](assets/doc/control.png)

2 control buttons were included. The restart button permits the user to reset the game whilst the sound button
removes/adds sound effects.

A counter was included to provide the user with a running count of every turn made.

### Modals

Two modals were included for the main game. The first one permits the user to choose a difficulty level
which would change the size of card grid system. The second modal activated when the game was complete and contained:
* stats on the number of turns required to complete the game
* Star Wars character fact obtained from https://swapi.dev API 
* a button to play again.

![Image of modals](assets/doc/level.png)

A modal was included for the character facts section to show info on the clicked character.

![Image of character modal](assets/doc/facts.png)


### footer

A footer was added which incoporated social links to:
* official Star Wars facebook site
* official Star Wars twitter site
* official Star Wars Istagram site

## TECHNOLOGIES USED

* HTML5
* css 
* javacript (ES6)
* Jquery to simplify DOM manipulation
* official W3C validator to check HTML syntax
* css official validator(jigsaw) to check css syntax
* JSHint to check javacript syntax 
* Jasmine testing framework for unit testing
* Chrome developers tools for analysing scripts and debugging
* Bootstrap 4 for page layout purposes and responsive design aspects
* balsamiq wireframes application to create the site design
* Chrome extension 'responsive viewer' to aid in reponsive design 

## JAVASCRIPT GAME LOGIC

The code logic behind the main game was as follow:
* Determine grid size my selecting difficulty level which would hide or expose div elements which specific classes.
* Provide the attribute of '.card' and '.character' (e.g ".yoda") to the class of all card elements using a for loop for the
'.character' class.
The '.card' class would be situated below '.character' class in css to make it the dominant class.
* Select two cards. 
* For each card selected the class attribute of '.card' would be removed using removeClass method, which would expose the '.character' class.
* A Comparison of the remaining class attribute of the two selected cards is then performed.
* If the remaining class attribute for two cards are the same then the off click method (.off("click")) would be applied and match count increased by 1.
* If the remaining class attribute are not the same the class attribute of ".card" would be added back which would hide the character class.
* sequence continues until all '.character' classes are exposed which is identified by using match count and grid size. 

## TESTING 

This section provides details of testing performed during development. The following table highlights the different stages when testing were carried out:

| Test                | Stage Performed                                  | Tool used                                     |
|---------------------|:-------------------------------------------------|:----------------------------------------------|
|Syntax errors        |Once During mid development and on completion     |W3C validator, css validator(jigsaw), jshint   |
|Debugging            |During the whole project                          |Chrome Devtools                                |
|Reponsive design     |During the whole project                          |Chrome Devtools and reposnsive viewer extension|
|Unit testing         |One check when main game functions were completed |Jasmine Framework                              |
|User game testing    |As from when main game module was completed       |n/a                                            |
|Browser compatibility|On project completion                             |Manual testing on browsers and parrotqa.com    |                    
|Button/link testing  |During development and project completion         |Manual testing                                 |


### UX testing

The goals set out in the UX section were accomplished as follows:

1. User goal: *play a game to improve my congnitive function*<br>
Although difficult to measure, memory match games have scientifically been shown to be an effective brain training tool, especially
improving:
* concentration
* shorterm memory
* attention to detail 
* finding similarities and differences in objects

2. User goal: *be able to navigate through the site with minimal difficulty inorder to play the game.*</br>
The site design used straight forward user friendly step-by-step guides to help assist the player navigate
the options with ease. This was further achieved by the use of hide/show jquery methods which manipulated modals and text changes.
For example once the user selected "click here to play' the grid system would appear together with a 
modal allowing the user to select difficulty level. Also the text "click here to play" changes to "match the cards" indicating that the game has started.
This was further tested by allowing test users to play the game with minimum prompting.

3. User goal: *be provided with options so I can adapt to my personal preference.*</br>
This was primarily achieved by providing a [level select](#modals) option which would change the card grid size from easy (2x4) to hard (4x4). This would permit 
the user to change difficulty level depending on personal requirements. For example, the user could select hard to experience more of a challenge.
Another option included was the [sound on/off](#control-buttons-and-counter) button.

4. User goal: *have feedback on how well i am performing so as I can track any improvements in memory*</br>
This was achieved by using a [counter](#control-buttons-and-counter) indicating how many turns had been taken which could be used as a
baseline for improvement during future game attempts.

5. User goal: *play a brain training game whilst having a fun experience*</br>
This was achieved by using a Star Wars themed design which made the game more visually appealing.

6. User goal: *be exposed to general Star Wars character facts so I can further my star wars knowledge*</br>
This was achieved by consuming a Star Wars API provided by [swapi.dev](https://swapi.dev). This would provide a random character
fact highlighting the characters name, height, weight, and hair-colour when the game finished. The second page
also allowed the user to click on specific Star wars characters included in the game to obtain facts.
These features are described [above](#modals).

The above user goals were further tested by obtaining feedback from testers. The feedback was positive all on aspects.

### Validators

Code syntax were checked for errors with the following validators:
* official W3C validator located [here](https://validator.w3.org/)
* css official validator(jigsaw) located [here](https://jigsaw.w3.org/css-validator/)
* JSHint located [here](https://jshint.com/)


Errors were corrected and final test results are given below:

| Test                           | Expected result                | Results            |                                 
|:-------------------------------|:-------------------------------|:-------------------|
|W3C validator                   |No errors or warnings to show   |Passed              |
|css official validator(jigsaw)  |No errors found                 |Passed              |                            
|JSHint located                  |Congratulations. No error found |Warnings present    |

![Image of html validator](assets/doc/html_validator.png)
![Image of html validator](assets/doc/css_validator.png)

The Jshint test results had the warning " 'let' is available in ES6 (use 'esversion: 6') or Mozilla JS extensions (use moz)." was due to
syntax used for defining variables.

### Chrome DevTools

Chrome DevTools were used extensively during development phase to assist in:
* page layout issues 
* checking errors
* debugging
* verifying correct output using console  

### Jasmine unit testing

Once the main game functions were completed, Jasmine framework was used to ensure functions were defined and output were correct. 
Tests were successful as detailed below. 
The scriptSpec.js file is located in the spec folder.

| Test                           | Expected result                                     | Results  |                                 
|:-------------------------------|:----------------------------------------------------|:---------|
|expect(gameArray).toBeDefined() |Should exist                                         |Passed    |
|gameArray("easy")               |"yoda","yoda","vader","vader","luke","luke","r2","r2"|Passed    |                            
|expect(matchCheck).toBeDefined()|Should exist                                         |Passed    |
|matchCheck(["yoda","yoda"])     |should return total turns 1                          |Passed    |
|matchCheck(["yoda","yoda"])     |should return total match 1                          |Passed    |
|expect(game).toBeDefined()      |Should exist"                                        |Passed    |
|expect(click).toBe(0)           |should be equal to 0                                 |Passed    |

![Image of jasmiine testing](assets/doc/jasmine.png)
![Image of jasmine testing](assets/doc/jasmine2.png)

### Game testing

The game was tested with friends and relatives to check for bugs and to obtain general feedback. This was performed when main game 
module was complete upto project completion. 

Issues encountered and rectified are given [below](#issues-encountered-during-development)

### Responsive design

The site was viewed on different device sizes to check for correct reponsive design. This was done using primarily
Chrome DevTools with different emulated devices(moto G4, iphone 6/7/8, ipad, ipad pro). The responsive viewer chrome 
extension was also used covering the following screen resolutions:

|Screen resolution| Device                        |
|:----------------|:------------------------------|
|1280 X 800       |large screen                   |
|1024 X 800       |medium screen                  |
|414 X 736        |iPhone 8 Plus, 7 Plus, 6S Plus |
|375 X 667        |iPhone 8, 7, 6S, 6             |
|414 X 896        |iPhone XR, XS Max              |
|375 X 812        |iPhone XS, X                   |
|412 X 846        |Galaxy S9 Plus, S8 Plus        |
|360 X 740        |Galaxy S9, Note 8, S8          |
|323 X 786        |Pixel 3, 3 XL                  |

![reponsive design Image](assets/doc/responsive_two.png)

A final check was done using the website http://ami.responsivedesign.is/. 

Issues encountered and rectified are given [below](#issues-encountered-during-development)

### Browser compatibility

The site was tested on Google Chrome, FireFox, Internet Explorer, Safari and Opera. An automated test was also perfomed using 
a cross browser checker using the website https://www.parrotqa.com catering for chrome, safari and FireFox.

![reponsive design Image](assets/doc/browser.png)

Issues encountered and rectified are given [below](#issues-encountered-during-development)

### Button and link testing

The following gives test results for button and link testing.

|Page            | Action taken                           |Expected result                                          | Results |                                 
|:---------------|----------------------------------------|:--------------------------------------------------------|:--------|
|index.html      |click on "click here to play"           |Card grid system and level select modal to appear        |Passed   |
|index.html      |click on "play" with no level selected  |"Choose you difficulty level" to flash                   |Passed   |                           
|index.html      |click on "play" with level selected     |level modal game to disappear                            |Passed   |
|index.html      |click on card                           |star wars character to appear                            |Passed   |
|index.html      |click on restart button                 |level modal to appear                                    |Passed   |
|index.html      |click on sound button                   |sound icon to change and audio to off                    |Passed   |
|index.html      |click on facebook icon                  |Facebook star wars page to open up in new window         |Passed   |                     
|index.html      |click on twitter icon                   |Twitter star wars page to open up in new window          |Passed   |         
|index.html      |click on Insagram icon                  |Instagram star wars page to open up in new window        |Passed   |  
|index.html      |click on character facts                |Page directs to character.html page                      |Passed   | 
|character.html  |click on home button                    |Return back to index.html page                           |Passed   |
|character.html  |click on card                           |character  modal to appear with image and facts          |Passed   |                           
|character.html  |click on modal close button             |Character facts modal game to disappear                  |Passed   |
|character.html  |click on facebook icon                  |Facebook star wars page to open up in new window         |Passed   |                     
|character.html  |click on twitter icon                   |Twitter star wars page to open up in new window          |Passed   |         
|character.html  |click on Insagram icon                  |Instagram star wars page to open up in new window        |Passed   |
|index.html      |click on non-existent link              |Page directs to 404.html page                            |Passed   |
|index.html      |click on rules link                     |Wikepedia page to open in new window                     |Passed   |

### Issues Encountered during development

During testing phase the following issues were indentified and corrected.

1. Once a specific card was exposed it could be selected again causing the card game logic to breakdown. This was 
resolved by adding the condition ```(($(this).attr("class")).length)>=6)``` in the click function. 

2. The Star Wars character funfact at the end of the game would not show up if a status other than 200 was obtained.
To cater for this issue a defensive design was implemented by including an else if statement in the getData function so that if a status other than 200 was obtained
a default character fact would appear. Character chosen was Luke Skywalker. This was further tested by providing an incorrect URL to the getdata function 
and checking the output.</br>
For the character-info.html page 'data unavailable' would appear in the fields.</br> 
![Image of unavailable data](assets/doc/data.png)

3. On the level select modal the play button could be pressed without a level being selected. To fix this bug
a condition was added, ```if($("input[type=radio][name=level]:checked").length===1)```, to activate the play button only when a level was selected and the "choose your difficulty level" text 
was made to blink so as to prompt the user.

4. After completing the game and pressing the restart button, two modals would superimpose on each other. This bug was fixed
by hiding the 'gameEnd' module if the restart button is pressed.

5. Each star wars character had its own character class which produced alot of repetition for only a change in image URL. To avoid having
to repeat each character class, consuming large amount of css lines, a solution was found whereby the background-image URL was added 
with Javacsript once the card was selected. This provided a more efficient style sheet.

6. Once the main game was completed and testing peformed it was noticed that the play again button was hidden on the game end modal.
This was adjusted by increasing modal height from 270px to 310px.</br>
![Image of play button](assets/doc/error.png)

7. When the game was completed and the fun facts would appear it would briefly show the previous character info. This issue
was addressed by adding a loading bar gif when ever the fun facts function was called and no repsonse from the API had been obtained yet.

8. While checking for browser compatibility it was found that the footer was not fixed to the bottom on IE browser. This issues was corrected 
by changing ```flex: 1``` to ```flex-grow: 1```.</br>
![Image of IE](assets/doc/error1.png)

9. Another issue noticed while performing browser compatibility test was the scroll function did not work on IE and was abrupt on safari.
After consulting documentation from [W3schools](https://www.w3schools.com/howto/howto_css_smooth_scroll.asp#section2) it was observed that
the scroll function was not supported on these browsers. A modification was attempted using the animate function however this also produced
abrupt screen movement. Consequently, the Choice was made to revert back to the original code. 

10. While testing for reponsiveness using chrome dev tools it was noticed that the text below logo would change lines on smaller devices.
This issue was addressed by changing font size.</br>
![Image of error](assets/doc/error2.png)

11. After final project review it was decided to add instructions on how to play the game. This was achieved by adding a link to  the header which directs to a wikepdia [page](https://en.wikipedia.org/wiki/Matching_game) containing generic rules on how to play. 

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
