# Testing

## User Stories Testing

### Navigation


| User Story | <div style="width:50%">Screenshot(s)</div> | Comments/Fixes |
| --- | --- | --- |
| As a new shopper, I want to know what the site is about within seconds | <img src="images/test_images/homepage.png" alt="Homepage"> | Hero image displays framed prints. Logo informs the page is for artwork. |
| As a new shopper, I want the site navigation to clear and intuitive | <img src="/workspace/leggy-art/documentation/images/readme_images/navbar-md.png"><br><img src="images/test_images/link-hover.png" alt="Link on hover"> | All navigation links working. Links changing colour on hover for accessibility |
| As a new shopper, I might want to find out information about the artist in an 'About' page | <img src="images/test_images/about.png" alt="Homepage"> | About page contains ralevant info |
| As a new shopper, I want to be able to register with an email or social account | <img src="images/test_images/reg_test_signup.png" alt="Signup form"> | Social account signup functionality not yet implemented, as discussed in README.md future features section |
| As a newly registered shopper, I want to receive a confirmation email upon registration | <img src="images/test_images/reg_conf_email.png" alt="Confirmation email"> | Confirmation email sent with link to finalise process |
| As a returning shopper, I want to be able to login quickly <br><br> As a returning shopper, I want the option to sign in with my username, email or social account <br><br> As a returning shopper, I want the option for the site to remember me on the browser I am using | <img src="images/test_images/signin_page.png" alt="Sign-up form with placeholder text showing"> | User has option between username or email. Signin is not complicated and can be accessed within one click of homepage. Remember me button works for given browser |
| As a returning shopper, I want to be able to view my profile page <br><br> As a returning shopper, I want to be able to view my previosuly purchased products see reviews and comments I have left on my products | <img src="images/test_images/profile.png" alt="Profile page"> | Default info showing. Order history showing |
| As a potential customer, I want to be able to view all products or filter the products based on various categories | <img src="images/test_images/sort.png" alt="Sorting list"> <br> <img src="images/test_images/filter.png" alt="Fliter list"> | Filter and sort tables. Both work as expected |
| As a potential customer, I want to be able to view more details and an enlarged image of the prints I am interested in | <img src="images/test_images/print_detail.png" alt="Print detail"> | Enlarged image slideshow, more detail, ability to alter number of prints to add to basket. |
| As a potential customer, I want to be able to add and remove products from my basket once logged in | <img src="images/test_images/basket.png" alt="Print detail"> | Ablility to remove and update number of selected prints works as expected |
| As a site administrator, I should be able to add more prints to the website <br><br> As a site administrator, I should be able to alter the availability of certain prints | <img src="images/test_images/add_product.png" alt="Print detail"><br><img src="images/test_images/edit_delete.png" alt="Print detail"> | Superusers can add products in management page and edit/delete products via prints/print_detail pages |


- As a returning shopper, I want to be able to view my profile page.
- As a returning shopper, I want to be able to see my previously viewed products

    Once logged in, the profile page works as expected, displaying previous purchases.

- As a returning shopper, I want to be able to view my previosuly purchased products see reviews and comments I have left on my products
- As a returning shopper, I want to be able to see recently added products


### Registration

- As a new shopper, I want to be able to register with an email or social account
- As a newly registered shopper, I want to receive a confirmation email upon registration

Upon registering, an email confirmation is sent to the user. Before the confirmation link is clicked, the user is added to the django admin Users database. The screenshots below show the filled signup form, the admin page Users database, and the confirmation email. The attempted sign up was done using an already existing user to test whether the site deals with an identical username effectively. I also entered the repeated password incorrectly to test this error handling as well.

<figure>
  <img src="images/test_images/reg_test_signup.png" alt="Signup form">
  <figcaption>Completed signup form</figcaption>
</figure>
<figure>
  <img src="images/test_images/reg_test_admin.png" alt="Admin page displaying Users">
  <figcaption>Admin page displaying Users.</figcaption>
</figure>
<figure>
  <img src="images/test_images/reg_conf_email.png" alt="Terminal displaying confirmation email">
  <figcaption>Confirmation email.</figcaption>
</figure>

I have not yet implemented the social account registration method.

## Login

- As a returning shopper, I want to be able to login quickly
- As a returning shopper, I want the option to sign in with my username, email or social account
- As a returning shopper, I want the option for the site to remember me on the browser I am using

<figure>
  <img src="images/test_images/signin_page.png" alt="Sign-up form with placeholder text showing">
  <figcaption>Sign-up form with placeholder text showing.</figcaption>
</figure>

The placeholder text shows the user that either the username or email can be used to log in using the form.

I first attempted to sign in with the username and this worked. I then tried the same with the email and achieved the same result.

I have not yet Added a social account login, as shown in README.md 'Future Features' section.

