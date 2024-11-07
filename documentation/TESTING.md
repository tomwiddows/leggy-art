# Testing

## User Stories

### Navigation

- As a new shopper, I want the site navigation to clear and intuitive

The site has been designed with accessibility in mind. There should be a clear indication that there is a link when the mouse hovers over it. the shop now button, category links and product links change colour when hovered over. the new colour is light enough so that visually impaired users will not struggle to notice it. The example below is of the category links:

<img src="images/test_images/link-hover.png" alt="Link on hover">


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

