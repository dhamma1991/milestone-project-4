# Milestone Project 4 – LevelUp - A Gamified Productivity Task Manager App Built with Django

[![Build Status](https://travis-ci.org/dhamma1991/milestone-project-4.svg?branch=master)](https://travis-ci.org/dhamma1991/milestone-project-4)

## Table Of Contents

[1. Introduction](#1-introduction)

----------

[2. UX](#2-ux)

[2.1. Wireframes](#21-wireframes)

----------

[3. Features](#3-features)

[3.1. Authentication System](#31-authentication-system)

[3.2. User Profile System](#32-user-profile-system)

[3.3. Tasks](#33-tasks)

[3.4. Add and Edit Task Forms](#34-add-and-edit-task-forms)

[3.5. Integration with Stripe](#35-integration-with-stripe)

----------

[4. Features Left to Implement](#4-features-left-to-implement)

----------

[5. How Existing Features Fulfil User Requirements](#5-how-existing-features-fulfil-user-requirements)

----------

[6. Technologies Used](#6-technologies-used)

----------

[7. Testing](#7-Testing)

[7.1. Code Validation](#71-code-validation)

[7.2. Manual Testing](#72-manual-testing)

[7.3. Other Manual Testing](#73-other-manual-testing)

[7.4. Automated Testing](#74-automated-testing)

[7.5. Browser and Responsiveness Testing](#75-browser-and-responsiveness-testing)

[7.6. Known Issues](#76-known-issues)

----------

[8. Deployment](#8-deployment)

----------

[9. Credits](#9-credits)

[9.1. Images](#91-images)

[9.2. Acknowledgements](#92-acknowledgements)

--------------------
## 1. Introduction
This project is a ‘gamifed’ productivity task manager app called LevelUp. The purpose of this app is to serve as a task manager that a user can use to track completion of daily tasks in their personal life that they wish to perform. The ‘gamified’ element is borrowed from RPG-type games, allowing the user to gain experience points within the app through completing their real-life tasks. Upon gaining enough experience points, the user gains levels within the app, with higher levels becoming progressively harder to obtain. Failing to complete tasks on a daily basis leads to the user losing ‘hitpoints’, and once the user reaches 0 hitpoints they lose a level.

LevelUp borrows many concepts from real-world apps such as [Habitica](https://habitica.com/) and [LifeRPG](https://www.reddit.com/r/LifeRPG/). I have been a personal user of Habitica for many years, and LevelUp could be considered to be a minimal, stripped-down version of Habitica without the fantasy-RPG elements.
## 2. UX
LevelUp is aimed at productivity-minded people. The expected type of user would be someone who has used more than one productivity app, perhaps including other task managers and scheduler apps. The expected type of user is expected to be someone high-achieving (or someone who aims to become high-achieving) in their personal goals, or simply someone who wants to try a novel way of motivating themselves to do daily tasks. 

The typical user will need to be able to:

1. Have access to an easy to use authentication system that enables the personalised functionality of the app.

2. An easy way to add tasks.

3. See a clearly organised and easy to decipher task page.

4. ‘At a glance’ overview of the user’s current stats (hitpoints and experience points).

5. Information explaining the mechanics of the app to the user. This could be in the form of a dedicated tutorial page for the app, tooltips scattered throughout the app, or a combination of both.

### 2.1. Wireframes
Prior to work beginning on the app, wireframes were created to aid the design process and provide direction during actual coding. These can be found in the "wireframes" folder in the root directory of the project.

The wireframes are not a complete picture of how the app in its finished form looks. I do find wireframes very helpful in establishing the colour scheme and overall aesthetics of the app, as well as providing the general structure and layout of pages. However, often during development I find that features need to be added which were not foreseen, or layouts tweaked in order to accommodate content in practicality. The wireframes serve as a ‘launch pad’ for the app. In addition, some pages do not feature an overly complex layout, in which case they have no wireframe. In other cases, I can picture the design in my head without concrete sketches.

Along with designs for the visual layout of the app itself, within the wireframes directory you may find sketches of the schemas for the various models.
## 3. Features
As previously mentioned in the [introduction](#1-introduction), LevelUp is a gamified productivity task manager app. The features included in the current release of the app are:
### 3.1. Authentication System 
The user is able to create an account with a unique username. Within the app, the user is able to update their details and add a profile picture. There is functioning password reset functionality, so that a user who chooses to reset their password will get a password reset email sent to their inbox.

### 3.2. User Profile System
This profile system uses a one-to-one relationship with Django’s built in model User in order to add functionality that is required by LevelUp, in particular the hitpoints and experience system. 

Hitpoints range from 0 to 100. If users fail to complete tasks by the end of the day (currently 0:00 UTC), then the difficulty of the task determines how many hitpoints they will lose, with more difficult tasks causing the user to lose more hitpoints. If the user reaches 0 hitpoints, they will lose a level (with the exception of if they are level 1; level 0 or below do not exist on the app). Once a user gains a new level, any lost hitpoints will be regained.

**Note**: It may be hard to see the task refresh and hitpoint loss functionality in action, as by its nature it only becomes apparent after a login has occurred after the reset time of 0:00 UTC. A user has been created on the heroku deployment with the username of **User123** and password of **password123**. This user has some uncompleted tasks, and anyone wishing to view the hitpoint loss functionality at work can log in as this user.

Experience is gained through completing tasks. The amount of experience gained depends on the difficulty of the tasks, with more difficult tasks granting more experience. At every level, users must reach a certain experience threshold in order to gain the next level. The experience threshold gradually gets higher as the user gains levels, with the experience threshold for level 1 being 100, level 2 being 200, level 3 being 300 and so on. Once the user reaches a new level, their experience is reset to 0 and their hitpoints are restored to 100.

### 3.3. Tasks
The tasks page contains daily tasks that the user creates that the user can mark as done. At a specified point in time (currently 0:00 UTC) the user’s tasks ‘refresh’, and are marked as not done ready for the start of a new day. Any tasks not done mean the user loses hitpoints. 

It should be noted that the task refresh system is only active on the days that the user is. For example, if the user does not log in to the app for 3 days, this does not mean that they lose 3 days’ worth of hitpoints. This was implemented to ensure that the user is not punished too much if they are unable or unwilling to log in to the app for a sustained period of time.

### 3.4. Add and Edit Task Forms
Users are able to use forms within the app to both add and edit tasks. Users can give tasks a name, some optional tasks notes, and a difficulty. The task difficulty can be picked by the user from 4 options; easy, medium, hard and ambitious, representing 10, 20, 30, and 40 xp gain and hp loss respectively. Tasks can be edited at any time and the difficulty adjusted with no limitations or penalties.

### 3.5. Integration with Stripe
Stripe payment processing is used to facilitate payment processing within the app. This integration is fairly basic, and consists of the user being able to donate a pre-defined amount (5 USD) to the developers of the app as a thank you for their hard work. Users who donate have their username added to a thank you list that is displayed on donate.html.

## 4. Features Left to Implement
Some features are left open to the idea of implementation but were not featured in this release.
### Customised days when tasks have to be completed
Currently, each task the user creates must be completed every day. This does not allow the user to specify certain days that the task does not need to be completed. For example, a user may want to go to the gym 4 days a week. They could set their gym daily task to only be active on 4 out of the 7 days of the week, and on the other days, the task is inactive and does not cause the user to lose hitpoints if it has not been marked as done.

I’m not sure how this functionality could be implemented at present, but it would certainly involve the Python module datetime.date. This would allow days of the week to be used in the program. The task could perhaps run a check during each sync-time (when the app checks for non-completed dailies), seeing if there are any tasks that do not need to be completed on the next coming day. A new Boolean field in the tasks model would also probably be necessary, indicating whether or not a task is required to be completed on a given day.

### A mechanic for hitpoint recovery other than levelling up
Currently, a user on less than 100 hitpoints has no way to recover their hitpoints other than by gaining enough experience to gain a level. With the increases in the experience threshold required by users in order to gain higher levels, this has the potential to make the app overly difficulty to make progress in without some system way of being able to regain hitpoints without levelling up.

A potential solution to this would be to implement a system of ‘gold’, as found in Habitica. The user could use this in-app currency to purchase ‘healing potions’ (again to borrow from Habitica) which would allow the user to recover Hitpoints.

Implementing such a system would, at the minimum, require an overhaul of the front-end to provide a visual indicator of the amount of in-game currency the user has, as well as somewhere that they can buy and use the healing mechanic. In addition, there would need to be modifications to the Profile model, associating these healing mechanic items with the user’s profile. New views would need to be written handing how the hitpoints are gained.
### Email authentication
Currently, the user signs in to the app using the username they created when they signed up. I personally dislike this system; usernames, which may be app specific, may be much easier to forget than email addresses. I would suspect most internet users possess maybe 2 or 3 personal emails at most, and the majority will possess only one email address that they use frequently.

Currently, the app is able to help users who have forgotten their username through them clicking the ‘Forgot Username or Password?’ link on the login page. The password reset email sent contains the username associated with the email. However, an email login system is still the preferred option in my mind and I consider it to be more user friendly 
### Keep the scroll of the page when a user marks a task as done/not done
Currently, when a user marks a task as done or not done, the tasks page will reload, but with the scroll set to the top of the page. A user with many tasks, who marks a task as done or not done which is towards the bottom of the list, will then lose their scroll position within the page and have to scroll back down to view the task that they just marked as done/not done when the page reloads.

It would be fairly easy to implement a way of keeping the scroll on a task when the user toggles that task’s done status, without adding any further dependencies; give each task a unique html id, pass that through to the toggle_done_status view, and then get the view to pass it through to the template, with some JavaScript ready to scroll that task id into view.

However, one current obstacle to this otherwise easy implementation is the way that the Django messages currently work on the app; they appear at the top of the page, indicating user experience and level change. If the user was automatically scrolled back down to a particular task, those messages would not be immediately apparent to the user.

What would have to be implemented is perhaps message popups that appear regardless of where the scroll is on the tasks page. The page could then be freely scrolled to whichever task the user last toggled as done/not done, without the user losing out on the message contents.
### A way to ‘pause’ the app
In the current release of LevelUp, there is no way the user can ‘pause’ the app, and prevent uncompleted daily tasks from causing hitpoint loss. Tying the user in to completing their daily tasks every single day without fail may be neither practical nor possible, and there may be some days where the user is either unable or unwilling to engage with the app.

Ideally, the user should not be penalised within the app for taking time off of the app. A way to prevent uncompleted tasks causing hitpoint loss should therefore be implemented in a future release. 
### Delete task confirmation
Currently, a task is deleted as soon as a user clicks the ‘Delete Task’ button on the task detail pages. It would probably be better practice to have the user go to a delete confirmation page first, this would guard against misclicks or mistakes.
### Custom donation amount
Currently, LevelUp only accepts donations of 5 USD from users. This feature could be expanded to accommodate a donation of any amount, and could also be tailored to match the user’s own currency. Further configuration of Stripe would be necessary in order for this to be implanted.
## 5. How Existing Features Fulfil User Requirements
This section details how the features implemented in the current release of the project meet the requirements of users discussed in the UX section.
### See a clearly organised and easy to decipher task page.
The user is able to see their list of tasks on tasks.html, reachable from the main nav. Each task is contained within a Materialize ‘card’, which adds some styling to distinguish each task from the next. The difficulty for each task is represented by an icon of some bars, with more bars being filled for more difficulty tasks. The icons provide a visual indicator of the difficulty of the task without cluttering up each task card with too much text. In addition, it is clear to see which tasks the user has currently completed, with a ‘tick’ icon used to represent a task as being done.
### An easy way to add tasks
There is a link to the add task form positioned in a prominent place above the task list. The add task form contains instructions and guidance on how to add a task and how to pick a task difficulty. 
### ‘At a glance’ overview of the user’s current stats (hitpoints and experience points)
These are positioned towards the top of the tasks page in a prominent location. Colourful Material icons are used to represent hitpoints (red) and experience (yellow), and these aid in making these elements stand out from the rest of the page. 
### Information explaining the mechanics of the app to the user
The core philosophy behind the app is explained in the ‘About’ section of the app, reachable from the main nav as well as the ‘Get Started’ link which shows on index.html. In addition, there is text towards the top of both the tasks page and the add task page which explain those areas of functionality to the user.
## 6. Technologies Used
Here can be found a list of the main packages, languages, frameworks and services that constitute LevelUp.
### [HTML5](https://www.w3.org/standards/webdesign/htmlcss)
The project's markup uses HTML5 and makes as much use of HTML5 semantics as possible using W3C standards.
### [CSS3](https://www.w3.org/standards/webdesign/htmlcss)
The markup is styled using CSS3.
### [SASS Pre-Processing](https://sass-lang.com/)
SASS pre-processing (using SCSS syntax) is used to render the project’s style.css file, making the process of creating CSS easier.
### [Materialize 1.0.0](https://materializecss.com/)
Materialize is a front-end framework based on Google’s philosophy of “material design”. Materialize is used throughout the app in order to simplify the process of generating the visual look and feel of the project.
### [Material Icons](https://material.io/tools/icons/?style=baseline)
Included as part of the Materialize framework. Provides a useful set of icons that can be used to represent actions and items.
### [JavaScript](https://developer.mozilla.org/en-US/docs/Web/JavaScript)
The project does not rely heavily on JavaScript, although there is some JavaScript scattered throughout the project. Its primary purpose is to enable the use of jQuery, but there are some examples of pure JavaScript found within the app (e.g. the copyright date script found at the bottom of base.html).
### [jQuery 3.2.1](https://jquery.com)
jQuery is utilised by the project for a number of areas of functionality:

1. Materialize depends on jQuery for its JavaScript components (e.g. the sidenav).
2. The library chain_fade.js, used for the text fade in effect on index.html
3. The custom written script that hides Django messages when the user clicks on the close button, using the slideUp animation.
### [Django 2.0](https://docs.djangoproject.com/en/2.0/)
Django is the main engine that powers LevelUp, providing user authentication, templating system and administration among other tasks.
### [Amazon S3](https://aws.amazon.com/s3/)
Amazon’s object storage service is used to store user-uploaded profile pictures.
### [Boto 3 1.9.146](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html)
The SDK provided by Amazon for Python. Used by LevelUp to configure S3.
### [Django Crispy Forms 1.7.2](https://django-crispy-forms.readthedocs.io/en/latest/)
Used to simplify the process of rendering Django forms.
### [Crispy Forms Materialize 0.2](https://pypi.org/project/crispy-forms-materialize/)
Allows compatibility between the Materialize framework and Django Crispy Forms.
### [Django Database URL](https://github.com/kennethreitz/dj-database-url)
Allows Django to parse database URLs.
### [Pillow](https://pillow.readthedocs.io/en/stable/)
Pillow is a PIL fork that allows Python to be used to manipulate image files.
### [Psycopg2](https://pypi.org/project/psycopg2/)
Allows Python to communicate with LevelUp’s production postgreSQL database.
### [Whitenoise 4.1.2](http://whitenoise.evans.io/en/stable/)
Used to integrate the app’s static files, which eases the process of deploying the app on Heroku.
### [Stripe](https://stripe.com/)
Stripe is a payment processor, used by LevelUp to facilitate users being able to donate.
### [Git](https://git-scm.com/)
Used for version control
### [GitHub](https://github.com/)
Used as the online hosting service for the git repository.
###[Travis CI](https://travis-ci.org/)
Continuous Integration is probably more useful when working in a team. However, I find that being able to essentially push and test code in one command is useful. In addition, I like the ‘build passing’ seal of approval that Travis provides upon successful passing of all automated tests.
### [Heroku](https://dashboard.heroku.com/login)
Used to deploy the app on the web.
### [Heroku Postgres](https://www.heroku.com/postgres)
Postgres is used to manage the database. Heroku Postgres provides a way to manage the database on Heroku.
### [Real Favicon Generator](https://realfavicongenerator.net/)
This tool was used to construct favicons for the project. How favicons are rendered is different depending on the browser or platform used, and this tool simplifies the process by providing the appropriate markup and icon for each platform.
### [BeFunky](https://www.befunky.com/)
Used for adjustment of the app’s images.
Used for adjustment of the app’s images.
## 7. Testing
### 7.1. Code Validation
The W3C code validators for [HTML](https://validator.w3.org/) and [CSS](https://jigsaw.w3.org/css-validator/) were used to check markup validity.

For the HTML validator, there were a few errors and warnings that I was able to fix. One error of note was found on password-reset.html. The markup I had written personally was fine. However, the use of {{ form | crispy }} led to a div with a class of “row” being outputted to the page without a closing div tag. I was able to fix this by just manually adding a closing div tag after the {{ form | crispy }} within the template.

I suspect this issue is to do with the fact I am using a package called crispy-forms-materialize. This package is only version 0.2, so this stray div may just be an oversight of the package’s author.

In regards the style.css file compiled by SASS, this was found to be error free.
### 7.2. Manual Testing
Manual testing was conducted by both myself (the developer) and other testers who have no development experience. In the case of one of these other testers, I was able to sit with them and observe and record their interactions with the app. All the manual testing is documented in this section.
#### User Stories Testing
The typical user actions identified in the [UX section](#2-ux) were tested by myself to ensure that they can be undertaken. Each of these actions is discussed in turn.

**1. Have access to an easy to use authentication system that enables the personalised functionality of the app.**

Upon landing on the homepage, I am able to find the link to create a new account in the nav without difficulty. I enter in some details to create a new account, and upon submitting the form I am taken to the login page. I am able to login to my account using the account details I just provided.

I then logout of my account, go back to the login page, and pretend I have forgotten my password. I click the forgot password link and I am taken to the password reset form. I enter in my email and go to check my emails. I have received a password reset email. I open the email and follow the link it provides, which takes me to a new password form. I enter a new password and I am taken once again to the login page. I login with my new password and I am able to access the app with my new credentials.

**2. An easy way to add tasks.**

After logging in to the app with the new account that I previously created above, I can see that I currently have no tasks. I click the ‘Add Task’ link and I am taken to a form. I am able to read the text that accompanies the form, and decide that the task I will add is ‘Write in journal’ which has a task difficulty of medium. I enter in those details and click ‘Save’. I am taken back to the tasks page, and can see that my previously empty task list now contains the task I just created.

At this point I realised however that the app does not give any feedback or message when a task is added. This is probably fine when the user has zero or just a few tasks, as a new task being added to their task list will be obvious, and in any case the new task is added to the top of their task list. However, I decided it would be better if the app gave specific indication when a new task is created .

I decided to fix this by getting Django to pass a message.success through upon the successful creation of a new task through modifying the create_task view. The message will indicate to the user that a task was created successfully.

Once the fix was added, I tested it by returning to the add task form and adding a new task. When I submitted the add task form, I can see a ‘Task created!’ message at the top of the tasks page, along with the created task appearing in my task list.

**3. See a clearly organised and easy to decipher task page.**
Continuing on from the tests above, I can see the two tasks I have added in my task list. Each task looks separate from the other through the use of Materialize’s card styles. The interface for each task looks straight forward enough, although I realise that the icon representing task difficulty might be at first confusing to users. There is a tooltip that appears over the icon if the user hovers over it, and I test this tooltip appears on hover, which it does.

**4. ‘At a glance’ overview of the user’s current stats (hitpoints and experience points).**

Further continuing on from the testing scenario above, I can see some information at the top of the tasks page. I see my username, my current level, as well as my hitpoints and current experience.

Both the hitpoints and experience use abbreviations (‘hp’ for hitpoints and ‘xp’ for experience). These abbreviations are commonly found in RPG-type games. However, I realise that a person using the app who is unfamiliar with these types of games may not know what ‘hp’ and ‘xp’ stand for.

I decided to add tooltips for both the hp and xp indicators. This is an easy addition, and I opt to just add title attributes to the containing divs for both the hp and xp indicators. Once this is done, I test the tooltips appear when I hover over the indicators, which they do.

**5. Information explaining the mechanics of the app to the user. This could be in the form of a dedicated tutorial page for the app, tooltips scattered throughout the app, or a combination of both.**

Information regarding the app’s mechanics are spread throughout the app. In particular, the content on about.html, reachable from either the ‘About’ link in the main nav and footer or the ‘Get Started’ link on index.html, contains an article of text on the purpose of the app and the philosophy behind it.

I test to ensure the about.html page is reachable, and I also check that the instruction text on the tasks page and the add task page makes sense.

### 7.3. Other Manual Testing
Apart from testing the app personally, I also made use of other people to test the app, most of whom were not developers. Feedback from these users was positive, with all agreeing that the site works well. With one of these tests I was able to sit with the person and observe and record them using the app. We can call this person User X.

Upon landing on the home page, User X followed the ‘Get Started’ link that goes to the About page. They skimmed the text content, and then went to create an account. User X was able to create an account and then sign in without any difficulty. 

I asked User X to create a new task. They managed to do this, and then they were able to mark the task as done. User X gained 20 experience, as the task they had created had a difficulty of medium. This is expected behaviour.

Lastly, I asked User X to update the profile picture for their account, although I did not tell them how to do this. User X was able to quickly work out that the Profile page can be access from the dropdown menu that appears below the user’s name when they click on it. On the Profile page, the user was able to update their profile picture image without difficulty. This concluded the testing with User X

User X commented that they liked the overall design of the app, and thought it looked sleek and modern. 

### 7.4. Automated Testing
Automated testing was conducted using Django's built-in test framework (TestCase). Although an attempt was made to be as comprehensive as possible with automating testing, it was never a desired outcome to achieve 100% coverage. This was partly due to the app's reliance on external libraries (the built-in components of Django for example would be expected to be well-tested), and also due to my (previous) low familiarity with unit testing. I did not want to over-complicate things for myself by investing too much time learning how to test comprehensively, when that time could be spent on improving the app. My philosophy towards automating testing was therefore to ensure that the core areas of functionality (e.g. the tasks being marked as done/undone, xp gains/loses, the levelling system) were included within testing.

I would consider that my development approach was semi-test driven. I built much of the core functionality of the app without testing, implemented testing maybe 75% of the way through the app's development, and then used the tests written to alert me to any problems with features breaking when new features were added.

I found this approach worked for me. I was able to gain familiarity with Django prior to implementing testing. Then I was able to gain familiarity with testing as I was refining my knowledge of Django.
#### Automated Testing Process
Sanity tests were conducted first, these can be found in levelup/tests.py. Simple assertion tests were used to check that the test framework was functioning correctly.

Building up from there, I tested some of the built-in Django components, starting with the forms. I tested the AddTaskForm and UserCreationForm, checking that objects can be created successfully and that form.is_valid is true and false in cases where it should be true and false. No issues were detected during the tests. The tests themselves can be found within levelup/test_forms.py.

I then moved to testing authentication. I was not expecting any problems here, since I am using the default Django authentication system. I tested that a user with some credentials was able to successfully log on. This test was fine, the test can be found in test_authentication.

I then moved to testing views. Much of the more custom functionality the app possesses can be found within the views, so I focused particularly on these tests during the testing process. These tests can be found in test_views.py.

I first attempted a simple test just checking that the index page can be reached by using self.client.get("/"). At first I got a Value Error stating: Missing staticfiles manifest entry for 'css/style.css'. After some googling I followed the advice in [this stackoverflow thread](https://stackoverflow.com/questions/44160666/valueerror-missing-staticfiles-manifest-entry-for-favicon-ico) and managed to fix the error by running python manage.py collectstatic. This fixed the error, and the first simple test passed.

I began using Django's test suite in order to conduct tests on views that require a login. I tested that a user can access both the tasks and profile pages, tests which passed without issue. 

Additional testing involved ensuring the functionality involved within the views toggle_done_status and get_tasks (two large and important views) function correctly. It was here that I conducted tests which proved very useful, and showed me I had holes in my application.

In one case, expected behaviour is that a user who marks a task as undone loses xp. If the user is higher than level 1, and their xp loss is enough to give them a negative xp amount, they should lose a level. An example of this working would be a level 2 user with 20 xp who marks an ambitious (40xp value) task as undone, should go back to level 1, but have 80 xp. This is because the xp_threshold for a level 1 user is 100. Note that if the user marks the ambitious task as done again, they should go back to the level they were before (in this case level 2) with the same xp as before (in this case, 20 xp).

Through writing a test that tested the expected behaviour outlined above, I found that the expected behaviour does occur provided that the user does NOT have 0 xp when they mark a task as undone. So if the user has 20 xp at level 2, and marks an ambitious task as undone, they will indeed go to level 1 with 80 xp. However, if the user has 0 xp at level 2, and marks the same task as undone, they will not lose a level. In addition, the Django message framework passed through messages saying that the user had both lost and gained a level (at the same time) This was of course not desired functionality, and I was not aware of this bug until I had conducted the appropriate test.

In order to pass this test I had to make modifications to the toggle_done_status view, mainly by ensuring that the ‘leftover’ variable used within the view is calculated correctly.

I continued to write more tests, with the end number of tests for the current release of the app numbering 32. All tests currently pass.
### 7.5. Browser and Responsiveness Testing
The app was primarily tested on Google Chrome version 74.0.3729.169 on a Windows PC with a default maximised screen size of 1936px. 

In addition to Google Chrome's developer tools where mobile devices can be simulated, an iPhone 7 running iOS v11.3 was used to test the app with its native Safari browser. The website was also tested on Firefox v66.0.3, Safari v12.1.1 (on a MacBook Pro 15-inch Retina) and Edge v42.17134.1.0.

The app was developed mobile first. I tend to always work on projects with the browser set to simulate a mobile device. I build the app from there, and when it looks right on the smaller viewports I make any changes it needs to work on the larger viewports.

No issues were detected on any of the tested browsers in terms of either layout or functionality, with the exception of a minor issue with the Safari browser; this related to the position of the close button for Django messages, which was in the wrong place, overlapping with the nav element. Some slight adjustment of the css was required in order to fix this issue.

In addition to modern browser testing, the app was tested on IE version 11.0.9600.19130. On this browser, none of the charts were rendered. After some searching, I found that DC.js is tested in IE but that [mine wasn’t the only issue] https://stackoverflow.com/questions/50047687/dc-js-im-facing-issues-rendering-the-dc-js-dashboards-in-ie-11) and that issues relating to DC.js working with IE [have been documented](https://github.com/dc-js/dc.js/issues/1334).

Due to IE being a legacy browser, and with Windows 10 (and Edge) becoming more and more common, I adopted to not support IE in any of its incarnations. To this effect, a user trying to view the app on IE will see a page similar to the no-js functionality, asking them to upgrade their browser.
### 7.6. Known Issues
There are several issues with the app that were not tackled in the current release, mainly because of the time it would have taken to implement fixes.
#### User email is not unique
The default Django User model utilised in the app does not require the user to sign up with a unique email, just a unique username. This has the potential to cause problems for the password reset functionality; if more than one username is associated with the same email address, two emails will be send to that email address when that email is used in the password reset process, with the ability to reset both user accounts from the same email.

This could cause a user confusion if a malicious user, or simply someone who made a mistake, entered someone else’s email during the sign-up process and then triggered the password reset process. The person with legitimate access to that email would then get two password reset emails.

Although this would look bad, it doesn’t really pose a security concern for the app; an attacker trying to steal someone’s LevelUp account would still need access to that user’s email address in order to get access to their LevelUp account.
### No custom task refresh time
Currently, the app will check for tasks that are not done, apply any hitpoint loss, and set all tasks to not done ready for a new day, at 0:00 UTC. The user currently has no way of customising this, which makes internationalization of the app less than optimal; a user in San Francisco, for example, would find their daily tasks refresh at either 5pm or 6pm (depending on daylight saving), which is probably not an ideal time for a user to start their daily tasks.

A way around this would be to allow the user to submit their current time zone, and then either program the app to refresh their tasks based on what their midnight is, or allow them to set their own custom time which is convenient for them. Both solutions would require an overhaul of the get_tasks view as it stands currently, and with this functionality envisioned to require far more code than the current implementation, it would probably require a dedicated view. The User or Profile models would also have to be adjusted to accommodate the user’s selected time zone.
## 8. Deployment
The project is deployed on Heroku, available [here](https://levelup-productivity.herokuapp.com/). The deployment process was (thankfully) mostly headache free. Upon creating the heroku deployment, the first thing that was done was setting the environment variables, which are mostly the same values as the variables used in development. 

Two variables that had to be added to Heroku that were not present in development are the DISABLE_COLLECTSTATIC variable, which I found was necessary in order to avoid issues with static files, and the DATABASE_URL variable, which links to the Heroku Postgres database. LevelUp makes use of a separate, SQLite database in development, with the Heroku Postgres used in production only.  In addition, a variable called DEVELOPMENT, which exists in the development environment and activates Django’s debug mode, is not set in Heroku, where debug mode is not desirable.

Anyone wishing to run the app locally would need to account for the following env variables:

#### DEVELOPMENT
Normally set to ‘1’ (when in development). This just enables Django’s debug mode.
#### DJANGO_SECRET_KEY
Anyone wishing to run LevelUp locally will have to generate a Django secret key and assign the value to this variable.
#### EMAIL_USER and EMAIL_PASSWORD
The password reset functionality makes use of a gmail account I created for the app. Anyone wishing to run the app locally and make use of the password reset functionality would need to configure an email account to work with the app.
#### STRIPE_SEC_KEY
This is used by Stripe in order to facilitate the donations system on the app. A local deployment would need to set up a Stripe account and configure the app to that account.
#### AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY and AWS_STORAGE_BUCKET_NAME
These variables are used in order to order to configure AWS to work with the app. AWS is primarily used for S3, which is where user uploaded images are stored. A local deployment will either have to modify settings.py in order to accommodate a different file storage system, or use a different AWS account in order to serve the files. 
## 9. Credits
### 9.1. Images
#### Task Checkbox
https://www.canva.com/media/MAAQottVXFI with custom colour modification
#### Difficulty Icons
https://ux.stackexchange.com/questions/55284/what-is-the-best-way-to-show-complexity-or-difficulty-rate
#### LevelUp Logo
https://www.canva.com/media/MAAWVMkQET8
### 9.2. Acknowledgements
I received inspiration for this project mainly from [Habitica] https://habitica.com/).
#### Code Acknowledgements
Other developer’s code that I have reused is indicated within the code itself by comments.









