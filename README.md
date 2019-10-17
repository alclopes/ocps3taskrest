<div id = 'top' />

# Project

* This project was started in Python == 3.4 and Django == 1.8 while attending Udemy.
* After this course the project was expanded with new libraries, features, controls and migrated to newer versions of Python (3.7) and Django (2.2.4). 

* [Next Steps](#nextsteps)
* [Activities Completed](#done)
* [List of Tables and Project Features](#services)
* [Best Practices / Attentions](#atention)
* [Know the project](#see)


<div id = 'nextsteps' />

## Next Steps - Plan

### Deploy - Puppet + Docker + Git + Travis + AWS (IAAS Cloud)
* Awaiting

### Deploy - Puppet + Docker + Git + Travis + Heroku 
* Docker (Container Virtualization) running the application locally with the exact configuration of the production environment)
* Awaiting

### Deploy - Puppet + Git + Travis + Heroku
* Puppet / Ansible (machine provisioning server preparation scripts, machine provisioning).
* Awaiting

### shopping cart
Add ways to pay the enrollment in the course.
* Awaiting

[Back to top](#top)

<div id = 'done' />

## Completed Activities - Done

### 191017c - Fix words Internationalization 
* Fix some portuguese words not translated.
* DONE - by Andre Carvalho

### 191017a - Fix Menu Forum - Links
* Remove left menu Forum if page is showing details forum.
* DONE - by Andre Carvalho

### 191017b - Fix Counter Forum - Filter More Recently
* Fix counter Forum to Filter More Recently - Counter is counting if you only see the register.
* DONE - by Andre Carvalho

### Fix Redix - Heroku
* Update Redix config to Heroku
* DONE - by Andre Carvalho

### Deploy - Git + Travis + Heroku
* Travis (task manager) using for testing automation to start deploy
* DONE - by Andre Carvalho

### Importing Partner Course Data
* Use JSON to import partner's course data to application
* DONE - by Andre Carvalho

### Fix Tests
* DONE - by Andre Carvalho

### README Translation
* Provide README in English and Portuguese
* DONE - by Andre Carvalho

### API / Rest Framework
* Provide APIs for service use
    * Users End Point: "http://127.0.0.1:8000/users/v1" => Admin Access Only
    * Categories End Point: "http://127.0.0.1:8000/categories/v1/" => Open Access.
    * Courses End Point: "http://127.0.0.1:8000/v1/courses/v1/" => Access if logged in
    * Teacher End Point: "http://127.0.0.1:8000/v1/teacher/v1/" => Access if logged in
* DONE - by Andre Carvalho

### Deploy - Heroku (Cloud PAAS)
* DONE - by Andre Carvalho

### GitHub Inclusion
* DONE - by Andre Carvalho
  
### Adding Static to S3 AWS (Cloud IAAS)
* DONE - by Andre Carvalho

### Migration to Python and Django Current Versions
* DONE - by Andre Carvalho

### Data Load Script in Tables Using OCR
* DONE - by Andre Carvalho
* Need to migrate to Heroku - postgres

### Incrementing Course Views
* The course was done in threadView (allows the same user in the same session to increment several times)
* Now made for user session-based CourseView, increments based on new session only
* DONE - by Andre Carvalho

### Material Inclusion Requirement
* Adding material via admin can only contain an attachment type or embedded text.
* Previously the admin module accepted an attachment and text embedded in the same material.
and when accessing this material, the system ignored the attachment showing only the embedded text.
* DONE - by Andre Carvalho

### Fix Insert the course by WebApp
* DONE - by Andre Carvalho

### Translation using Google for Portuguese and Spanish
* DONE - by Andre Carvalho

### Correcting and Configuring Emailing Parameters Using Decouple
* DONE - by Andre Carvalho
* Situations where emailing occurs:
1. Reset User Password (DONE)
    => Use a pre-formatted template / HTML in the body of the email
    => Uses the user data provided in the HTML page as an email sender.
    => Command: send_mail_template (subject, template_name, context, [user.email]) / Module: Account
2. User requests contact with portal manager (NEW)
    => Uses in the body of the email and how to email the user data provided in the HTML page
    => Command: send_mail_template (subject, template_name, context, [settings.CONTACT_EMAIL]
3. User has questions about course content. (DONE)
    => Uses in the body of the email and how to email the user data provided in the HTML page
    => Command: send_mail_template (subject, template_name, context, [settings.CONTACT_EMAIL] / Module: Account
4. User launched an advertisement in the course.
    => Uses to extend the machine user (DONE)
    => Command: send_mail_template (subject, template_name, context, recipient_list) / Module: Account

### Template Adjustment for Screen Size in Mobile Format
* DONE - by Andre Carvalho

### Attribute Name from Lesson and Material tabs set to UNIQUE **)
* DONE - by Andre Carvalho

### Inclusion of Teachers for Courses (List **)
* DONE - by Andre Carvalho
* A teacher can work in several courses.
* A course can have multiple teachers.

### Inclusion of Course Categories (List 1*)
* DONE - by Andre Carvalho
* One category will define the characteristic of several courses.
* Examples of categories: Information Technology, Business Management, Project Management ...

### Reuse panel that is repeated in two templates
* DONE - by Andre Carvalho

### Change Front End from PURE to Bootstrap
* DONE - by Andre Carvalho

### Security - Final Decouple Configuration
* DONE - by Andre Carvalho
* Decouple configuration to include in GitHUB.

### Third Party Library Removal
* DONE - by Andre Carvalho
* Third-party CSS library has been replaced by generating ERRO500 per browser security rule.

### Inclusion of Internationalization
* DONE - by Andre Carvalho
* Choose project language - English, Spanish and Brazilian Portuguese

### CSS Framework
* Udemy Professor Gileno Alves Santa Cruz Filho Course - Situation Completed
* "PURECSS" with "Landing Page" layout option was used

### Adding Icons to HTML
* Udemy Professor Gileno Alves Santa Cruz Filho Course - Situation Completed
* Added icon font CSS (font-awesome 3.1.0)

#### Using Predefined Domains for Table Fields (Model)
* Udemy Professor Gileno Alves Santa Cruz Filho Course - Situation Completed
* Check the Enrollment model,

### Django Administrative Module Changes
* Udemy Professor Gileno Alves Santa Cruz Filho Course - Situation Completed
* A USER ACCOUNTS class inherited from Django's USER class has been created.
So Django will stop using its default user auth, and will use the USER Accounts class to:
    <ul>
    <li> make access to admin module
    <li> create super user
    </ul>
* This way we can make the user table email field unique, which in this version of Django allows redundancy and we can also include more user control fields.

### Email Submission Setup
* Udemy Professor Gileno Alves Santa Cruz Filho Course - Situation Completed

### Templates Tag
* Udemy Professor Gileno Alves Santa Cruz Filho Course - Situation Completed
* It was used in app curses template tag to reuse a class in more than one HTML.

### Using Signals
* Udemy Professor Gileno Alves Santa Cruz Filho Course - Situation Completed
* Django offers a signals service so that when certain events occur warnings, messages ...
* View in app courses => courses.model.py => pos_save / pos_delete
* View in app Forum => Thread.model.py => pos_save / pos_delete

### Using Custom Decorator
* Udemy Professor Gileno Alves Santa Cruz Filho Course - Situation Completed
* We created a decorator to check if the user is allowed to access certain app modules / features.
* See decorator.py => def enrollment_required ()

### Migrating to the production server using local_settings.py
* Udemy Professor Gileno Alves Santa Cruz Filho Course - Situation Completed
* This method is very simple to overwrite the local environment over the production one.
* Note that the local_settings file is in gitignore, so it will not be migrated to the server which will cause the try below to fail and therefore no overwriting in the production environment will occur.

### Paged ListView with Side Menu
* Udemy Professor Gileno Alves Santa Cruz Filho Course - Situation Completed
* To the forum screen

### Including request variables in template
* Udemy Professor Gileno Alves Santa Cruz Filho Course - Situation Completed
* Some screen reloads some data may not be updated, such as a new pagination order index for a given object, so it is interesting to include the request variables in context in the reloads to update them.
* Check in settings TEMPLATE_CONTET_PROCESSORS

### Adding a View That Is Called by Two Different URLS
* Udemy Professor Gileno Alves Santa Cruz Filho Course - Situation Completed
* View class ForumFilter (ListView)

### Using Mommy Model Tests
* Udemy Professor Gileno Alves Santa Cruz Filho Course - Situation Completed
* Used to create automated data for testing.
* View usage in model testing.

### Using JS Aja JQuery
* Udemy Professor Gileno Alves Santa Cruz Filho Course - Situation Completed
* See button control pages thread.html

[Back to top](#top)

    
<div id = 'services' />


## List of Tables and Project Features

| Module | Model | Administration | API / Rest |
| --- | --- | --- | --- |
| Accounts | User | Admin | yes |
| Courses | Advertisements | Admin, App | |
| Courses | Categories | Admin, App | yes |
| Courses | Comments | Admin, App | |
| Courses | Courses | Admin, App | yes |
| Courses | Enrollments | Admin, App | |
| Courses | Lessons | Admin | |
| Courses | Materials | Admin, App | |
| Courses | Teachers | Admin | yes |
| Forum | Anwers | Admin, App | |
| Forum | Topic | Admin | |


| Module | Func |
| --- | --- |
| Access | Logout |
| Access | Login |
| Access | Change Language |
| Access | Register new user |
| Contact | Speak with us (general) |
| Courses | List advertisement |
| Courses | Comment advertisement |
| Courses | View course's details |
| Courses | Make your enrollment |
| Courses | Speak with us (courses) |
| Courses | Add teacher |
| Forum | Forum - View filter by more recently |
| Forum | Forum - View filter by more views |
| Forum | Forum - View filter by more comments |
| Forum | Forum - Add answers |
| Lesson and Materials | List Lessons |
| Lesson and Materials | Access lesson |
| Lesson and Materials | List materials of Lesson |
| Lesson and Materials | Access materials of Lesson |
| My Panel | List my courses |
| My Panel | Edit account |
| My Panel | Edit password |
| My Panel | Access my courses |
| My Panel | Cancel enrollment |


* Other project required entries available via Admin module


[Back to top](#top)


<div id = 'atention' />

## Good Practice / Care
In addition to best practices and care pointed out in other projects, remember that:

1. When using S3 to store static files we must remember to include their update to the automatic continuous update process.
2. Docker using Hyper-V not work in Win10 Home, you can install Docker Toolbox, which uses Oracle Virtual Box.

[Back to top](#top)


<div id = 'see' />

## Know the project

* Meet this application on [Heroku] (https://ocps3task.herokuapp.com/).
* Meet API of the application on [Heroku] https://ocps3task.herokuapp.com/api/

Login Profiles:
 
| User | Password |
| --- | --- |
| admin | admin |
| user01 | user |
| teacher01 | teacher |


[Back to top](#top)
