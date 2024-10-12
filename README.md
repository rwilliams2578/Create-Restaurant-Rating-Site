# Assignment 3 - Creating a Restaurant Rating Site

## Author
Name: Revelle Williams
CIS 218: Django Project
Date: October 10, 2024




## Description

Create a Django Web Application to keep track of Restaurant Ratings.

Models will include the built-in Django User models, a Restaurant Model, and a Review Model. Details and the ERD can be found below in the [Database Requirements](#database-requirements) section.

Restaurants can only be added by a superuser via the admin.
This requirement makes less work for you as you won't have to make CRUD pages for restaurants. In addition, it will provide us a form of control as to which restaurants are added to the system rather than any old user being able to.

Regular users should have a way to sign up, login, and logout to use the site.
Regular users (and superusers) can see a list of restaurants, a list of reviews for a specific restaurant, as well as add, update, and delete reviews for a restaurant. It would make sense to limit the update and delete functionality so that users can only perform those actions on reviews that they added, however since we have not covered how to do any of that yet, I am not expecting that. Though it might be something you could try on your own. As with all the assignments thus far, all views should be Class-Based Views.

I am expecting that you will do what you can with Bootstrap and/or your own CSS to make the site less ugly.
You can see screenshots of what I did with Bootstrap below in the [screenshots](#screenshots) section. In addition, these screenshots should hopefully give you a better idea as to how the site should function. Be sure to read the [Screenshot](#screenshots) section for more info.

Tests for the site should be similar to the ones we have written in-class thus far. At this point you should know what is a sufficient amount of testing. I am expecting that all views and models will be properly tested. And in case you aren't sure, there is no need to test any admin views.

Add required files and settings for publishing the site on Heroku. Fully hosting is worth extra credit. If doing so, publish the site on Heroku with a project name of "cis218-assignment-3-{your_name}" and submit the URL for the site to Canvas as the submission for this assignment. Regardless, have your most recent commit pushed up to GitHub.

Ensure that you have a `requirements.txt` file with your required packages. I will not grade the assignment if I can't restore the packages easily!

In general, the program should allow the following functionality:

1.  New Restaurant can be created by a superuser in the system via the admin.
2.  A non-admin page to see all of the created Restaurants. This should be the "home" route.
3.  A non-admin page to see all of the reviews and ratings of a single Restaurant.
4.  A non-admin page to see the details of a review and a rating for a restaurant.
5.  A non-admin page to add a review and a rating for a restaurant.
6.  A non-admin page to update a review and a rating for a restaurant.
7.  A non-admin page to delete a review and a rating for a restaurant.
8.  A non-admin page to login to the site.
9.  A non-admin page to sign up as a user for the site.
10.  Some form of styling. Bootstrap would be an easy way and is probably what I will use in my key.
11. Automated Tests to verify everything.
12. Files and Settings correct for publishing to Heroku.
13. Ensure `requirements.txt` is included in your project.
14. If doing Extra Credit, URL submitted to Canvas as Assignment Submission.

Documentation should include the following for this, and all future assignments:
* Comments at the top of each source code file that you add or edit with:
  * Your Name
  * Class
  * Date
* A comment after the definition of each method describing what it does. Use the """ (triple quote) doc string method for the comment.
* Comments in the rest of the code where it isn't obvious what is going on. (I prefer above the line comments vs at the end of the line because who likes to horizontally scroll, but either will work)

### Database Requirements
Here are the requirements for the database in an ERD. You do not need to worry about the user model as this is already provided via Django. It is only in here for reference and to show the relations to the other tables / models that you do need to worry about.

**NOTE:** This database will have one more table than the work we did for the in-class.
![Database Entity Relationship Diagram](https://barnesbrothers.ddns.net/cis218/assignment_images/assignment_3/cis218_assignment_3_erd.png "Databse Entity Relationship Diagram")

### Screenshots
Here are some images of the non-admin pages that I made for my key. This is more or less to give you an idea as to what the general concept is in case the written description is not clear. I realize that your assignment may not end up as elaborate in style as mine, so don't feel as though it needs to visually match mine exactly. I am looking for the general concept though. I will also mention that these screenshots used Bootstrap for styling. Additionally, there is some functionality that I added that we may not have covered in the In-Class depending on time. These things are listed below and although not required, do make the site fancier. If I was unable to cover some of these things and you are curious about them, don't hesitate to ask me about them.

#### Non-required features shown in Screenshots
* Average rating for a restaurant
* Review count for a restaurant
* User image for reviewer

#### Login Page
![Login View](https://barnesbrothers.net/cis218/assignment_images/assignment_3/cis218_assignment_3_screenshot_login.png "Login View")
#### Sign Up Page
![Sign Up View](https://barnesbrothers.net/cis218/assignment_images/assignment_3/cis218_assignment_3_screenshot_signup.png "Sign Up View")

#### Restaurant List View - Home
![Restaurant List View](https://barnesbrothers.net/cis218/assignment_images/assignment_3/cis218_assignment_3_screenshot_home.png "Restaurant List View")
#### Restaurant Detail View - No Reviews
![Restaurant Detail View - No Reviews](https://barnesbrothers.net/cis218/assignment_images/assignment_3/cis218_assignment_3_screenshot_restaurant_detail_no_reviews.png "Restaurant Detail View - No Reviews")
#### Restaurant Detail View - With Reviews
![Restaurant Detail View](https://barnesbrothers.net/cis218/assignment_images/assignment_3/cis218_assignment_3_screenshot_restaurant_detail.png "Restaurant Detail View")

#### Review Detail
![Review Detail View](https://barnesbrothers.net/cis218/assignment_images/assignment_3/cis218_assignment_3_screenshot_review_detail.png "Review Detail View")
#### Review Create
![Review Create View](https://barnesbrothers.net/cis218/assignment_images/assignment_3/cis218_assignment_3_screenshot_review_add.png "Review Create View")
#### Review Update
![Review Update View](https://barnesbrothers.net/cis218/assignment_images/assignment_3/cis218_assignment_3_screenshot_review_edit.png "Review Update View")
#### Review Delete
![Review Delete View](https://barnesbrothers.net/cis218/assignment_images/assignment_3/cis218_assignment_3_screenshot_review_delete.png "Review Delete View")

### Notes
All Views must be Class-Based Views. Function-Based views will not be graded.

Ensure that you have a requirements.txt file with your required packages. I will not grade the assignment if I can't restore the packages easily!

Making the relationship between a Restaurant and Review should be similar to the relationship that we made between a post and a user in the in-class. In the in-class one user could write many posts. Here one user can write many reviews. Additionally, one Restaurant can have many Reviews.

It is easiest to visualize this from the Review model. When thinking about one single Review, it will have exactly one User (The one who wrote it) and one Restaurant (The one the review belongs to). With that said, it shouldn't be too hard to add this additional relationship but if you are stuck, ask.

When creating the templates, you may want to refer to the below links about Bootstrap. There are plenty of examples that can aid you in coming up with a good looking site. I myself used a combination of what I did for the last assignment, the headers example, and the "Cards" component.

https://getbootstrap.com/docs/5.2/examples/

Here is the page on the "Card" component.

https://getbootstrap.com/docs/5.2/components/card/

In addition, you can find the documentation for Bootstrap in general here:

https://getbootstrap.com/docs/5.2/getting-started/introduction/

You should also be able to load bootstrap via a CDN link which will save you from having to manually include the css files. Just like I did for my Assignment 2 key.

## Grading
| Feature                                  | Points |
|------------------------------------------|--------|
| Correct Models                           |    10  |
| Ability to create a Restaurant via admin |     5  |
| Login, Logout, and Sign Up functionality |     5  |
| List Page for Restaurants                |    10  |
| List Pages for Reviews/Ratings           |    10  |
| Detail / Create Page for a Review/Rating |    15  |
| Update / Delete Page for a Review/Rating |    15  |
| Styling                                  |     5  |
| Automated Tests                          |    10  |
| Heroku Deployment Files and Settings     |     5  |
| Documentation                            |     5  |
| Readme                                   |     5  |
| **Total**                                | **100**|
| **Extra Credit** Full Heroku Deployment  |   **5**|

## Outside Resources Used
TestBook
Videos
Tutor


## Known Problems, Issues, And/Or Errors in the Program
None

