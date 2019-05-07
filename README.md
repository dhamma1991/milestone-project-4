[![Build Status](https://travis-ci.org/dhamma1991/milestone-project-4.svg?branch=master)](https://travis-ci.org/dhamma1991/milestone-project-4)


It was decided to hide some of the default Django 'hints' for when the user is creating an account or changing their password. This was to prevent the form from cluttering up, as the hints, especially for the password, constituted a large proportion of the text content of the forms before the decision to hide the hints was taken. Django seems fairly relaxed about the username or password the user chooses, with authentication that seems pretty standard across the Internet. It was decided therefore to hide the password and username hints using CSS, this being the obvious way to hide them. 

It would probably be more efficient to hide the hints by modifying the forms backend, but with the CSS route only taking a tiny amount of code, this was my preferred option.

Should the user fail the validation when the form is submitted, then hints will still show as before, highlighted in red.

{{ It was decided to not go with client-side validation for the user forms. It would be envisioned that????? }}



Material Icons are used on tasks.html to represent the user's hitpoints, experience, and also as icons representing tasks. 

Within the wireframes for the project, canva elements were used for the icons. It was decided to go with Material Icons during development as these would be easier to implement, are included with Materialize, and are as aesthetically viable as the canva elements.

# Technologies Used
Django
[link here]

Materialize 1.0.0
https://materializecss.com/

jQuery 3.2.1
[link here]

chain-fade
https://www.jqueryscript.net/animation/Sequential-Entrance-Animations-chain-fade.html

# REFERENCES
Images

Task Checkbox
https://www.canva.com/media/MAAQottVXFI with custom colour modification