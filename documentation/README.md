# Leggy Art Readme

Welcome to the Leggy Art website. As part of my Level 5 Web Development Diploma with Code Institute, I have been tasked with creating and deploying a fully-functional e-commerce site. The 

## User Stories

### New Potential Customers

#### Viewing and Navigation

- As a new shopper, I want to know what the site is about within seconds
- As a new shopper, I want the site navigation to clear and intuitive
- As a new shopper, I might want to find out information about the artist in an 'About' page

#### Registration

- As a new shopper, I want to be able to register with an email or social account
- As a newly registered shopper, I want to receive a confirmation email upon registration

### Returning Customers

#### Login

- As a returning shopper, I want to be able to login quickly
- As a returning shopper, I want the option to sign in with my username, email or social account
- As a returning shopper, I want the option for the site to remember me on the browser I am using

#### Viewing and Navigation

- As a returning shopper, I want to be able to view my profile page
- As a returning shopper, I want to be able to view my previosuly purchased products see reviews and comments I have left on my products
- As a returning shopper, I want to be able to see recently added products

### All Potential Customers

- As a potential customer, I want to be able to view all products or filter the products based on various categories
- As a potential customer, I want to be able to view more details and an enlarged image of the prints I am interested in
- As a potential customer, I want to be able to add and remove products from my basket once logged in

### Site Admin

- As a site administrator, I should be able to navigate the website using the links, so that I can ensure that all pages and links are working as they should.
- As a site administrator, I should be able to add more prints to the website 
- As a site administrator, I should be able to see when a customer has purchased a print
- As a site administrator, I should be able to alter the availability of certain prints or print sizes

## UX

### Wireframes

<table>
    <tr>
        <th>
            Small screens
        </th>
        <th>
            Medium screens and larger
        </th>
    </tr>
    <tr>
        <td>
            <img src="/workspace/leggy-art/documentation/images/readme_images/wireframe_sm.png" height="300px" style="padding:5px">
        </td>
        <td>
            <img src="/workspace/leggy-art/documentation/images/readme_images/wireframe_lg.png" height="300px" style="padding:5px">
        </td>
    </tr>
</table>

When creating the wireframes, the idea was to have the same page layout for medium screens and above. As seen from the final design above, this decision was slightly altered.

### Colourscheme

Deciding the colourscheme was straightforward. The Leggy Art logo already existed as just a capital letter L with the letter fading from a dark indigo esque shade at the bottom to a hot pink at the top. Other than this, there isn't much more colour on the page; The background colour is white and the text is mostly black (or white when background is not white). There is an information banner just below the navigation bar which is a deep purple colour. This colour was chosen (instead of black) to be more eye-catching without taking the viewer's eye away from the rest of the site too much. The hero image consists of two framed prints on a bright blue wall. This was an image of a real wall with the prints stuck to it. The blue is different enough to the rest of the site to make the homepage unique, and yet is not an eyesore. The combination of a few bold and bright colours is ideal for a playful look.

There are various pop-up alerts within the site which inform the user an action has just taken place. The nature of this action determines the colour of the alert and Bootsrap's inbuilt colour system is used. For example, Adding a product to the basket will display a message with a green top border. Three more alert colours are used througout the site: yellow (warnings), blue (general information) and red (danger).

### Typography

As I already had a logo design to work from, looking for the right font was based upon it. The chosen font, <a href="https://fonts.google.com/specimen/Yeseva+One">Yeseva One</a>  from Google Fonts, is bold and curved and includes serifs. There are sections pf each character that use a much thinner line, which resembles the penstroke of a marker pen. The font strikes a good balance between exuberance and elegance.

### Features

#### Navigation

The navigation bar consists of a Logo, search bar and button, and six other buttons: Prints, About, Register, Login and Basket. Bootstrap's collapsible navbar is used, which moves all features except the logo into a dropdown menu. The logo acts as a home button.

<img src="/workspace/leggy-art/documentation/images/readme_images/navbar-md.png">
<img src="/workspace/leggy-art/documentation/images/readme_images/navbar-sm.png">

#### Prints

The prints button is a dropdown menu with five options which link to the prints.html template. The first option will display all prints, with the other options filtering the prints based on their category.

Within the prints.html template, the prints are given a minimum and maximum width. The layout of the prints is altered depending on how many can fit horizontally.

The 'Sort By...' button allows the user to order the prints based on the following:

- Price (Low to High or High to Low)
- Rating (Low to High or High to Low)
- Name (A-Z or Z-A)
- Category (A-Z or Z-A)

<img src="/workspace/leggy-art/documentation/images/readme_images/sort-by.png">

##### About Button

The About button links to the About page, which contains information about the artist and the site.

The artist section contains a brief description about my brother, Eddie, who has allowed me to use his artwork for my project. It discusses his passion for art, his inspirations and a link to his instagram page.

The site section contains an important disclaimer informing users that the site is only an assessment project for my personal education with Code Institute. It explains how a lot of the prints cannot be sold due to copyright reasons. 