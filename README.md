# SpellSmith

Add a Blurb about the site here, what does it do, why did you build it?

SpellSmith is an innovative online platform designed to help fantasy role-playing game DC20 players create their own magical spells. This interactive tool allows users to explore and understand various spells from the system, create their own and share their creations with the community. 

I built this website as a way to create and share creations among the DC20 community and to allow them to easily share their own creations, and act as a central reposity of up to date homebrew creations. Making cloud based applications for boardgames and tabletoip games is an area im very much intrested in going into in my career.

Whether you're a seasoned Dungeon Master looking for new spells for your campaigns, a player referring to one of the spells or a homebrewer looking to create new spells for the growing DC20 system. SpellSmith offers a unique resource for exploring the world of fantasy spells.

![A picture of the Spellsmith Homepage](assets/documentation/spelllistview.png)

[View SpellSmith on Heroku here](https://spellsmith-9d992f394814.herokuapp.com/)

---

## CONTENTS

* [User Experience](#user-experience-ux)
  * [User Stories](#user-stories)

* [Design](#design)
  * [Colour Scheme](#colour-scheme)
  * [Typography](#typography)
  * [Imagery](#imagery)
  * [Wireframes](#wireframes)

* [Features](#features)
  * [General Features on Each Page](#general-features-on-each-page)
  * [Future Implementations](#future-implementations)
  * [Accessibility](#accessibility)

* [Technologies Used](#technologies-used)
  * [Languages Used](#languages-used)
  * [Frameworks, Libraries & Programs Used](#frameworks-libraries--programs-used)

* [Deployment & Local Development](#deployment--local-development)
  * [Deployment](#deployment)
  * [Local Development](#local-development)
    * [How to Fork](#how-to-fork)
    * [How to Clone](#how-to-clone)

* [Testing](#testing)

* [Credits](#credits)
  * [Code Used](#code-used)
  * [Content](#content)
  * [Media](#media)
  * [Acknowledgments](#acknowledgments)

---

## User Experience (UX)

DC20 is a fantasy roleplaying stsem currently being developed by the Dungeon Coach, a prominet conetnt creator in the TTRPG space, SpellSmith is a online repository of fan created spells, sharing ideas in the community. Users create a spell using the 'Create a Spell' page and can then update the spells they have created.

Key Features
  * Comprehensive Spell Database: Explore a wide range of spells across different schools of magic, including Conjuration, Destruction, Illusion, and Protection.
  * Detailed Spell Descriptions: Each spell comes with a vivid description, explaining its effects, usage, and potential outcomes.
  * Visual Representation: Spells are presented in the same format as the DC20 spellbook for a consistent experence.
  * User authentication: Powered by AllAuth, Users can create accounts, recover their accounts and use the account validation to edit or delete their homebrew spells. 

### User Stories

[User Stores for development can be found here:](https://github.com/users/LaurieAnderson92/projects/5/views/1)

#### Client Goals
* To be able to view the site on a range of device sizes.
* To make it easy for potential contributors to access and add to the repository.
* To allow people to join the DC20 community on discord
#### Viewer Goals
* I want to view spells that the community has created
* I want to be able to find more information about DC20
#### Contributor Goals
* I want to be able to easily make spells
* I want to be able to share the spells I make with the community via a link so others can see them.

## Design
### Colour Scheme

![Colour Palette of Seasalt, Cosmic latte, Steel pink, Purple and Eerie black](assets/documentation/colourpalette.png)

#### F7F7F7 | Seasalt 
* I used Seasalt as a offwhite colour as the background for the page, as #FFFFFF has a very sterile and clinical feel to it, and this muted white makes the other is softer and draws the eye to the Steel Pink or Purple

#### ba55d3 | Cosmic Latte
* Cosmic Lattee was picked as it is the closest colour that resembled parchment but still has a soft colour for a nice contrast with the default text colour and the colour when the text is highlighted

#### fcf5e5 | Steel Pink 
* Steel pink is the same as Purple, but a few shades lighter with more green. I picked this colour as the highlighted text for the nav bar and the footer to better contast with the dark background

#### 222222 | Purple
* Purple was picked as the key accent colour as it is the same shade of purple that DC20 uses, and so creates a association between SpellSmith and DC20 in the vewers mind.

#### 800080 | Eerie Black
* Eerie black is a off black, and was chosen for the same reason as Seasalt, to mimic graphite or ink on parchment rather than the dark black associated with computer text.

These colours also work for users with achromatic vision as can be demonstrated [here](https://coolors.co/f7f7f7-fcf5e5-ba55d3-800080-222222)

### Typography

I chose to use the Merienda font from [Google Fonts](https://fonts.google.com/) to look like writing within a spellbook. Merienda has soft shapes, is slightly condensed, and has a rhythm which is an invitation to read short pieces of text.

![alt text](assets/documentation/merienda_font.png)


### Wireframes

![A wireframe of the home page](assets/documentation/wireframe.png)

### ERD

![A diagram of the one model SpellSmith uses](assets/documentation/erd.png)

| Field |Description|
|-------|-----------|
|creator|This is a FK for the django's User model, one to many relationship (one user can create many spells) If the user is deleted, the spells remain. This isn't populated on the Create a Spell form|
|name|This is the name of the spell, Max Character 255, required|
|excerpt|This is a flavourful description of the spell that appears on the list view and the detail view|
|school|this is a interger field, min 0 max 11, they corrolate to the SCHOOL array of tuples that list a school, every spell has a school and this list canot be added to by users for gameplay reasons. on the form is is adropdown select button|
|ap_cost|This is a interger field, min 1 max 4 and denotes how many action points it takes to cast the spell, required|
|mp_cost|This is a interger field, min 0 max 9 and denotes how many mana points it takes to cast the spell, of 0 then the spell is specififed as a cantrip in the spell detail, required|
|range|This is a text field, usually the range is either 'Self' or 10 Spaces but there are edge cases in the published spells, so free text seemed best, required|
|duration|This is a text field, usually the distance is either 'X Spaces' but there are edge cases in the published spells, so free text seemed best, required|
|concentration|This is Boolean field, if ticked then the requirement will appear on the spell.|
|description|This is a big text field where the details of the spell need to go, This field needs to be unique to prevent duplicates, required|
|ap_enhancements|This is a Big text field, Currently spells either have ap enhancements or mp enhancements, but I wanted to leave the posability for both to be present, or neither for flexability in homebre creation|
|mp_enhancements|This is a Big text field, Currently spells either have ap enhancements or mp enhancements, but I wanted to leave the posability for both to be present, or neither for flexability in homebre creation|

## Features

👩🏻‍💻 View an example of a completed user experience section [here](https://github.com/kera-cudmore/TheQuizArms#Features)

This section can be used to explain what pages your site is made up of.

### General features on each page

If there is a feature that appears on all pages of your site, include it here. Examples of what to include would the the navigation, a footer and a favicon.

I then like to add a screenshot of each page of the site here, i use [amiresponsive](https://ui.dev/amiresponsive) which allows me to grab an image of the site as it would be displayed on mobile, tablet and desktop, this helps to show the responsiveness of the site.

### Future Implementations

What features would you like to implement in the future on your site? Would you like to add more pages, or create login functionality? Add these plans here.

### Accessibility

Be an amazing developer and get used to thinking about accessibility in all of your projects!

This is the place to make a note of anything you have done with accessibility in mind. Some examples include:

Have you used icons and added aria-labels to enable screen readers to understand these?
Have you ensured your site meets the minimum contrast requirements?
Have you chosen fonts that are dyslexia/accessible friendly?

Code Institute have an amazing channel for all things accessibility (a11y-accessibility) I would highly recommend joining this channel as it contains a wealth of information about accessibility and what we can do as developers to be more inclusive.

## Technologies Used

👩🏻‍💻 View an example of a completed Technologies Used section [here](https://github.com/kera-cudmore/Bully-Book-Club#Technologies-Used)

### Languages Used

Make a note here of all the languages used in creating your project. For the first project this will most likely just be HTML & CSS.

### Frameworks, Libraries & Programs Used

Add any frameworks, libraries or programs used while creating your project.

Make sure to include things like git, GitHub, the program used to make your wireframes, any programs used to compress your images, did you use a CSS framework like Bootstrap? If so add it here (add the version used).

A great tip for this section is to include them as you use them, that way you won't forget what you ended up using when you get to the end of your project.

## Deployment & Local Development

👩🏻‍💻 View an example of a completed Deployment & Local Development section [here](https://github.com/kera-cudmore/TheQuizArms#Deployment)

### Deployment

Include instructions here on how to deploy your project. For your first project you will most likely be using GitHub Pages.

### Local Development

The local development section gives instructions on how someone else could make a copy of your project to play with on their local machine. This section will get more complex in the later projects, and can be a great reference to yourself if you forget how to do this.

#### How to Fork

Place instructions on how to fork your project here.

#### How to Clone

Place instructions on how to clone your project here.

## Testing

Start as you mean to go on - and get used to writing a TESTING.md file from the very first project!

Testing requirements aren't massive for your first project, however if you start using a TESTING.md file from your first project you will thank yourself later when completing your later projects, which will contain much more information.
  
Use this part of the README to link to your TESTING.md file - you can view the example TESTING.md file [here](milestone1-testing.md)

## Credits

👩🏻‍💻 View an example of a completed Credits section [here](https://github.com/kera-cudmore/BookWorm#Credits)

The Credits section is where you can credit all the people and sources you used throughout your project.

### Code Used

If you have used some code in your project that you didn't write, this is the place to make note of it. Credit the author of the code and if possible a link to where you found the code. You could also add in a brief description of what the code does, or what you are using it for here.

### Content

Who wrote the content for the website? Was it yourself - or have you made the site for someone and they specified what the site was to say? This is the best place to put this information.

###  Media

If you have used any media on your site (images, audio, video etc) you can credit them here. I like to link back to the source where I found the media, and include where on the site the image is used.
  
###  Acknowledgments

If someone helped you out during your project, you can acknowledge them here! For example someone may have taken the time to help you on slack with a problem. Pop a little thank you here with a note of what they helped you with (I like to try and link back to their GitHub or Linked In account too). This is also a great place to thank your mentor and tutor support if you used them.