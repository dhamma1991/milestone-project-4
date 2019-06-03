[![Build Status](https://travis-ci.org/dhamma1991/milestone-project-4.svg?branch=master)](https://travis-ci.org/dhamma1991/milestone-project-4)


It was decided to hide some of the default Django 'hints' for when the user is creating an account or changing their password. This was to prevent the form from cluttering up, as the hints, especially for the password, constituted a large proportion of the text content of the forms before the decision to hide the hints was taken. Django seems fairly relaxed about the username or password the user chooses, with authentication that seems pretty standard across the Internet. It was decided therefore to hide the password and username hints using CSS, this being the obvious way to hide them. 

It would probably be more efficient to hide the hints by modifying the forms backend, but with the CSS route only taking a tiny amount of code, this was my preferred option.

Should the user fail the validation when the form is submitted, then hints will still show as before, highlighted in red.

{{ It was decided to not go with client-side validation for the user forms. It would be envisioned that????? }}



Material Icons are used on tasks.html to represent the user's hitpoints, experience, and also as icons representing tasks. 

Within the wireframes for the project, canva elements were used for the icons. It was decided to go with Material Icons during development as these would be easier to implement, are included with Materialize, and are as aesthetically viable as the canva elements.


With the task/done url, there is technically an exploit the user can perform where they can modify the URL to change the amount of xp they gain.

For example, say UserX has a task with id of 6, with a difficulty of Easy. If the user manually enters tasks/done/6/AM (with the 'AM' standing for ambitious), the user will mark the task as done, but gain the 40 xp reward for an Ambitious task completion, as opposed to the usual 10 xp for an Easy task.

However, it should be noted that the user has full control over the difficulty that they set to their tasks, so it doesn't make sense for the user to exploit the url system this way. Therefore, although this exploit exists, it doesn't really effect the functionality of the app.

# # Apps
# # # levelsystem
This app is technically redundant. Originally, I wanted to have the level system contained within its own app with its own models. I wanted to set up a table where I could specify unique xp thresholds, and possibly special rewards upon completing certain level milestones (e.g. perhaps a special popup or congratulations for level 10).

However, in the end, for the first release of the app I found it much easier to just build the level system into the tasks and accounts app.

Since I do intend to continue developing this project I left the levelsystem app in place. This will be built upon for a subsequent release. It will be noted that levelsystem is not included in Django's installed apps.

# Testing

Automated testing was conducted using Django's built-in test framework (TestCase). Although an attempt was made to be as comprehensive as possible with automating testing, it was never a desired outcome to achieve 100% coverage. This was partly due to the app's reliance on external libraries (the built-in components of Django for example would be expected to be well-tested), and also due to my (previous) low familiarity with unit testing. I did not want to over-complicate things for myself by investing too much time learning how to test comprehensively, when that time could be spent on improving the app. My philosophy towards automating testing was therefore to ensure that the core areas of functionality (e.g. the tasks being marked as done/undone, xp gains/loses, the levelling system) were included within testing.

I would consider that my development approach was semi-test driven. I built much of the core functionality of the app without testing, implemented testing maybe 75% of the way through the app's development, and then used the tests written to alert me to any problems with features breaking when new features were added.

I found this approach worked for me. I was able to gain familiarity with Django prior to implementing testing. Then I was able to gain familiarity with testing as I was refining my knowledge of Django.

# # Automated Testing Process

Sanity tests were conducted first, these can be found in levelup/tests.py. Simple assertion tests were used to check that the test framework was functioning correctly.

Building up from there, I tested some of the built-in Django components, starting with the forms. I tested the AddTaskForm and UserCreationForm, checking that objects can be created successfully and that form.is_valid is true and false in cases where it should be true and false. No issues were detected during the tests. The tests themselves can be found within levelup/test_forms.py.

I then moved to testing authentication. I was not expecting any problems here, since I am using the default Django authentication system. I tested that a user with some credentials was able to successfully log on. This test was fine, the test can be found in test_authentication.

I then moved to testing views. Much of the more custom functionality the app possesses can be found within the views, so I focused particularly on these tests during the testing process. These tests can be found in test_views.py.

I first attempted a simple test just checking that the index page can be reached by using self.client.get("/"). At first I got a Value Error stating: Missing staticfiles manifest entry for 'css/style.css'. After some googling I followed the advice in [this stackoverflow thread](Missing staticfiles manifest entry for 'css/style.css') and managed to fix the error by running python manage.py collectstatic. This fixed the error, and the first simple test passed.

I began using Django's test suite in order to conduct tests on views that require a login. I tested that a user can access both the tasks and profile pages, tests which passed without issue. 

{{{ Here's the bit where you found out marking a task as undone when xp is 0 doesnt work correctly }}}
I then conducted a test which proved very useful, and showed me I had a hole in my application.

Expected behaviour is that a user who marks a task as undone loses xp. If the user is higher than level 1, and their xp loss is enough to give them a negative xp amount, they should lose a level. An example of this working would be a level 2 user with 20 xp who marks an ambitious (40xp value) task as undone, should go back to level 1, but have 80 xp. This is because the xp_threshold for a level 1 user is 100. Note that if the user marks the ambitious task as done again, they should go back to the level they were before (in this case level 2) with the same xp as before (in this case, 20 xp).

Through writing a test that tested the expected behaviour outlined above, I found that the expected behaviour does occur provided that the user does NOT have 0 xp when they mark a task as undone. So if the user has 20 xp at level 2, and marks an ambitious task as undone, they will indeed go to level 1 with 80 xp. However, if the user has 0 xp at level 2, and marks the same task as undone, they will not lose a level. In addition, the Django message framework passes through messsages saying that the user has both lost and gained a level (at the same time) This was of course not desired functionality, and I was not aware of this bug until I had conducted the appropriate test.

# Technologies Used

# REFERENCES
Images

Task Checkbox
https://www.canva.com/media/MAAQottVXFI with custom colour modification

Difficulty icons
https://ux.stackexchange.com/questions/55284/what-is-the-best-way-to-show-complexity-or-difficulty-rate

Logo
https://www.canva.com/media/MAAWVMkQET8