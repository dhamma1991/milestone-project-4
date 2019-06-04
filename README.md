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