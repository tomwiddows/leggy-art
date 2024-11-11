# Leggy Art Readme

Welcome to the Leggy Art website. As part of my Level 5 Web Development Diploma with Code Institute, I have been tasked with creating and deploying a fully-functional e-commerce site. 


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

### All Potential Customers

- As a potential customer, I want to be able to view all products or filter the products based on various categories
- As a potential customer, I want to be able to view more details and an enlarged image of the prints I am interested in
- As a potential customer, I want to be able to add and remove products from my basket once logged in

### Site Admin

- As a site administrator, I should be able to add more prints to the website 
- As a site administrator, I should be able to remove certain prints 
- As a site administrator, I should be able to edit certain prints 
- As a site administrator, I should be able to see when a customer has purchased a print

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

Deciding the colourscheme was straightforward. The Leggy Art logo already existed as just a capital letter L with the letter fading from a dark purple shade at the bottom to a hot pink at the top. Other than this, there isn't much more colour on the page; The background colour is white and the text is mostly black (or white when background is not white). There is an information banner just below the navigation bar which is a deep purple colour. This colour was chosen (instead of black) to be more eye-catching without taking the viewer's eye away from the rest of the site too much. The hero image consists of two framed prints on a bright blue wall. This was an image of a real wall with the prints stuck to it. The blue is different enough to the rest of the site to make the homepage unique, and yet is not an eyesore. The combination of a few bold and bright colours is ideal for a playful look. I also used this blue shade for links. Upon hover, they change colour. I found the colour of a certain pixel of the image using ManageEngine's <a href="https://www.site24x7.com/tools/color-code-picker.html#:~:text=Sign%20Up-,Color%20Code%20Picker,file%20size%20is%20upto%201MB." target="__blank">Color Code Picker</a>. Here is a list of the colours chosen for the site:

Code | Colour
--- | ---
#ffffff | ![#ffffff](https://placehold.co/100x100/ffffff/ffffff.png)
#000000 | ![#ffffff](https://placehold.co/100x100/000000/000000.png)
#43077f | ![#ffffff](https://placehold.co/100x100/43077f/43077f.png)
#5998c7 | ![#5998c7](https://placehold.co/100x100/5998c7/5998c7.png)


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

#### About Button

The About button links to the About page, which contains information about the artist and the site.

The artist section contains a brief description about my brother, Eddie, who has allowed me to use his artwork for my project. It discusses his passion for art, his inspirations and a link to his instagram page.

The site section contains an important disclaimer informing users that the site is only an assessment project for my personal education with Code Institute. It explains how a lot of the prints cannot be sold due to copyright reasons.

#### Search Bar

The search bar links to the prints.html page, and filters based on the keyword entered. It can filter based on the product names, categories as well as any words contained within the description of a product. 

<img src="/workspace/leggy-art/documentation/images/readme_images/searchbar.png">

#### Register Button

This links to the registration page, where the user will be able to create an account using an email address and a chosen email. 

#### Login Button

The login button directs the user to the login page where they can use either their email or username to access their account. They can also opt for theis browser to remember them and not have to login again within that browser, unless cache is cleared

#### Basket

The basket button is a FontAwesome icon with the running total underneath. Once an item is added to the basket, its value will be added to this total. This item is also displayed in a pop-up message:

<img src="/workspace/leggy-art/documentation/images/readme_images/basket_popup.png">

Within the basket.html page, any added product's info is displayed. Each item total is shown as well as delivery, and at the bottm, the grand total is calculated. If the free delivery threshold is not reached, his is followed by an alert stating the amount extra that could be spent to get free delivery. Finally, Two buttons are present; One allows the user to continue shopping and the other takes the user to the checkout page:

<img src="/workspace/leggy-art/documentation/images/readme_images/basket_page.png">

#### Checkout

The checkout page consists of a two-column container. The left column contains a form with delivery fields. If the user is signed in and has default delivery information in their profile, these fields will be pre-filled. The right column displays the order information:

<img src="/workspace/leggy-art/documentation/images/readme_images/checkout.png">

#### Checkout Success

Once the order is complete, the checkout success page is rendered, explaining that the order is complete and a confirmation email has been sent to the relevant user. A popup is also loaded:

<img src="/workspace/leggy-art/documentation/images/readme_images/checkout_success.png">

#### Profile

The profile page is only accessible once a user is authenticated. It displays a form for saving/updating default delivery information in the left-hand column, and the user's order history in the right-hand column.

<img src="/workspace/leggy-art/documentation/images/readme_images/profile.png">

if the user is a superuser, all orders are displayed here:

<img src="/workspace/leggy-art/documentation/images/readme_images/superuser_profile.png">

#### Footer

The footer contains three features: The name of the brand, an instagram link using FontAwesome's instagram icon, and a comment about the site being created for a CodeInstitute diploma, as well as a link to CodeInstitute:

<img src="/workspace/leggy-art/documentation/images/readme_images/footer.png">

### Future Features

#### Social accounts

The site does not yet have social account signup functionality. This can be implemented by adding socialaccount settings to settings.py

#### Ratings

Users can not yet leave a rating of products they have purchased. This will be added before the site is actually used for business. The change would require adding a review model and updating the profile template to display a five-star review button.

#### Delete account

Users do not yet have the option to delete their account from the database. This feature would work similarly to how a superuser can delete products. 

### Unfixed Bugs

I had some issues near the beginning of my project with positioning the homepage heading element and shop now button at a consistent height within the hero-image. I found a workaround for this which involved using the hero-images' aspect ratios, and setting its height relative to the screen width and image aspect ratio. However, I later realised that when the navigation bar is collapsed on small screens, and the menu is opened, these elements get pushed down as the height of the navigation bar is larger. I am unsure on how to fix this but will keep researching.

## Tools & Technologies Used

- [HTML](https://en.wikipedia.org/wiki/HTML) used for the main site content.
- [CSS](https://en.wikipedia.org/wiki/CSS) used for the main site design and layout.
- [Bootstrap](https://getbootstrap.com) used as the front-end CSS framework for modern responsiveness and pre-built components.
- [JS](https://en.wikipedia.org/wiki/JavaScript) used for interactive elements.
- [Python](https://en.wikipedia.org/wiki/Python_(programming_language)) used for server-side logic, handling data processing, and powering the backend framework to manage requests, responses, and interactions with the database.
- [Django](https://www.djangoproject.com/) used as the backend web framework to streamline development, handle database interactions and manage user authentication.
- [Heroku](https://dashboard.heroku.com/) used for deployment and as an external environment.
- [AWS](https://aws.amazon.com/) used for external storage of static and media files 
- [Git](https://git-scm.com) used for version control. (`git add`, `git commit`, `git push`)
- [GitHub](https://github.com) used for secure online code storage.
- [GitHub Pages](https://pages.github.com) used for hosting the deployed front-end site.
- [Gitpod](https://gitpod.io) used as a cloud-based IDE for development.

## Testing

For all testing, please refer to the [TESTING.md](TESTING.md) file.

## Deployment

This project is deployed to Heroku. It is set to automatically update within heroku upon being pushed to GitHub. The steps to Deployment are as follows:

1. Create a PostgreSql database and obtain the database URL.

2. In the terminal, install dj_database_url and psycopg2. Both of these are needed to connect to the external database. Also import both of these into settings.py.

3. A requirements.txt file is needed for Heroku to run the app. This file contains a list of python dependencies for the project, including the two above. The following command is entered to the terminal to create the requirements.txt file filled with the dependencies:

        pip freeze --local > requirements.txt

4. Ensure these files are pushed to GitHub

5. Go to Heroku and log in. Do so with a GitHub account to make deployment easier. 

6. Now create a new app and give it an appropriate name. The name of this app in Heroku is 'leggy-art'. Heroku also needs to know which region you are closest to. 

7. Navigate to the Settings tab, scroll down to Config vars and add a variable called DATABASE_URL, with the value being the url string obtained from postgreSQL.

8. Go to the DATABASES section of settings.py and update it to the following code, so that you can connect to the new database. Tne if/else block ensures that upon deployment, the PostgreSQL database is used, but during development, the local django database is used:

        DATABASES = {
            'default': dj_database_url.parse(os.environ.get('your-database-url-here'))
        }

9. Migrate your database using pip3 showmigrations, makemigrations and migrate in the terminal.

10. Create a django superuser with the following command:

        python3 manage.py createsuperuser

    Go to the django admin page and manually verify the email address associated with the superuser.

11. Load the fixtures in the correct order, ensuring that if any tables have a foreign key, the table relating to that foreign key is loaded first.

12. Go back to settings.py databases, and alter the code to contain an if/else statement. If the DATABASE_URL is found within the environment, the PostgreSQL database will be accessed (Ensure the os.environ.get() syntax is used to prevent exposing the database url). If no DATABASE_URL variable is found, revert back to using the local django database:

        if 'DATABASE_URL' in os.environ:
            DATABASES = {
                'default': dj_database_url.parse(os.environ.get('DATABASE_URL'))
                }
        else:
            DATABASES = {
                'default': {
                    'ENGINE': 'django.db.backends.sqlite3',
                    'NAME': BASE_DIR / 'db.sqlite3',
                }
            }

13. Next, install gunicorn with pip3 in the terminal and freeze to requirements.txt.

14. Heroku also requires a Procfile to run the app. This contains the start command (which app should be run and how to run it) and should contain the single line of code which tells Heroku to create a web dyno:

        web: gunicorn leggy_art.wsgi:application

15. For the next step, you must disable collectstatic with the following command:

        heroku config:set DISABLE_COLLECTSTATIC=1 --app leggy-art

16. Before deployment, add the heroku app hostname to ALLOWED_HOSTS in settings.py. Then, add, commit and push all changes.

17. To deploy, first initialise the git remote in the terminal:

        heroku git:remote -a leggy-art

    and then push to heroku with:

        git push heroku main

18. To deploy automatically on each future push, go to the 'Deploy' tab in Heroku and ensure you are connected to github. Search for your repository and then click connect. Now you will be able to 'Enable Automatic Deploys".

19. Generate a secret key online, and add the value to a new config var named SECRET_KEY.

20. In settings.py, set the secret key to get the Heroku secret key from the environment: 

        SECRET_KEY = os.environ.get('SECRET_KEY')

    Push this change to GitHub.

21. In a new tab, navigate to [https://aws.amazon.com](https://aws.amazon.com). Create a personal AWS account and sign in.

22. In the services menu, search for S3 and create a new bucket with the same (or similar) name to your Heroku app name. Deselect 'Block all public access'. Also make sure 'ACLs Enabled' is selected, as well as 'Bucket owner preferred' under Object Ownership. Now click 'Create Bucket'

23. Click on the bucket and in the 'Properties' tab, turn on 'Static website hosting'. Fill ouot index and error with default values of 'index.html' and 'error.html'. Click save.

24. Go to the 'Permissions tab, and in 'CORS Configuration', copy in the following configuration:

        [
            {
                "AllowedHeaders": [
                    "Authorization"
                ],
                "AllowedMethods": [
                    "GET",
                    "PUT",
                    "POST",
                    "DELETE"
                ],
                "AllowedOrigins": [
                    "*"
                ],
                "ExposeHeaders": []
            }
        ]

25. Next, go to 'Bucket Policy' and then 'Policy generator. 
    Policy type is 'S3 Bucket Policy' 
    in 'Principals' allow all principles with an *
    in 'Action' select the following:

    s3:GetObject
    s3:PutObject

    Copy the ARN from the Permissions tab and paste that in before clicking 'Add Statement' and then 'Generate Policy'. Copy the policy and paste in the Bucket Policy editor field. Before clicking save, add /* to the end of the resource key. Now click save.

26. Still in Permissions, in the ACLs section, check the 'list' box next to 'Everyone (public access)'.

27. Go back to the services menu and open 'IAM' in a new tab.

28. Click on User Groups in the left-hand menu and create a group called manage-leggy-art.

29. Now navigate to the Permissions tab, select the dropdown menu that says 'Add permissions' and select 'Attach policies'. In the JSON tab, click on 'Import managed policy' and search for S3. Select the policy called 'AmazonS3FullAccess' and import it. 

30. From the S3 bucket policy page, copy the ARN and paste it into the JSON "Resource" variable twice to form a list, with the second iteration being followed by /* as shown below:

        "Resource": [
            "arn:aws:s3:::leggy-art",
            "arn:aws:s3:::leggy-art/*"
        ]

    Click 'Review policy', name it 'leggy-art-policy' and give it a descriptiion, e.g. 'Accesss to S3 bucket for Leggy Art static files'. Then click 'Create policy'

31. Attach the policy to the group in the Groups tab by clicking 'Attach Policy' in Permissions. Search for the previously created policy and select it. Then click 'Attach Policy' again.

32. Now navigate to the 'Users' tab and click 'Add User', create a user named 'leggy-art-staticfiles-user', give the user programatic access and select Next. Add the user to the group and click 'Create user'.

33. Select the user and go to the 'Security Credentials' tab. Scroll to 'Access Keys' and click 'Create access key'. Select 'Application running outside AWS', and click next. On the next screen, you can leave the 'Description tag value' blank. Click 'Create Access Key'. Click the 'Download .csv file' button.

34. With AWS set up, go back to your workspace and install boto3 and django-storages with pip3. Freeze these to requirements.txt. In settings.py add 'storages' to installed apps.

35. Add the following settings to settings.py:

        # Cache control
        AWS_S3_OBJECT_PARAMETERS = {
            'Expires': 'Thu, 31 Dec 2099 20:00:00 GMT',
            'CacheControl': 'max-age=94608000',
        }
        # Bucket config
        AWS_STORAGE_BUCKET_NAME = 'leggy-art'
        AWS_S3_REGION_NAME = 'eu-west-2'
        AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
        AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')
        AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com'

        # Static and media files
        STATICFILES_LOCATION = 'static'
        MEDIAFILES_LOCATION = 'media'

        # Static and media urls
        STATIC_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{STATICFILES_LOCATION}/'
        MEDIA_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{MEDIAFILES_LOCATION}/'

        # Set storage file for collectstatic process
        STORAGES = {
            "default": {"BACKEND": "leggy_art.custom_storages.MediaStorage"},
            "staticfiles": {"BACKEND": "leggy_art.custom_storages.StaticStorage"},
        }

36. Back in Heroku, add the AWS_ACCESS_KEY_ID and AWS_SECRET_ACCESS_KEY as config vars. These are found in the .csv file downloaded earlier. Also, remove the DISABLE_COLLECTSTATIC variable.

37. Create a file called custom_storages.py in the leggy-art app. Add the following code:

        # Import settings.py file
        from django.conf import settings 
        # Import S3's Boto3 which is required for collectstatic to run
        from storages.backends.s3boto3 import S3Boto3Storage


        # Set storage for static files upon collectstatic
        class StaticStorage(S3Boto3Storage):
            location = settings.STATICFILES_LOCATION


        # Set storage for media files upon collectstatic
        class MediaStorage(S3Boto3Storage):
            location = settings.MEDIAFILES_LOCATION

    Push to GitHub, which will automatically deploy to Heroku as well.

38. For media files, go to the S3 bucket ad create a new folder called 'media'. Inside the folder, click 'Upload' and select all the product images. Click next and under 'manage public permissions', select 'grant public read access to these objects'. Click Upload.

39. After creating a stripe account, navigate to 'API Keys' under 'Developers', copy the STRIPE_SECRET_KEY and STRIPE_PUBLIC_KEY and store them as Heroku Config vars. Now create a new webhook endpoint. Add the url for the heroku app followed by /checkout/wh/. Select 'Receive all events' and click 'Add endpoint'. Reveal the webhook signing secret and add it as a Heroku config var as STRIPE_WH_HANDLER.

## Citations

- https://github.com/sachingupta006/django-allauth/blob/master/allauth/account/forms.py used to research how to alter django-allauth forms

- https://docs.allauth.org/en/latest/common/templates.html used to research how to alter django-allauth templates 

- https://devncoffee.com/responsive-image-slider-in-html-css/ used to create image slider in print_details.html

- https://medium.com/@iamalisaleh/how-to-get-the-current-url-within-a-django-template-8270b977f280 - used to research how to return to current url when incorrect details are entered in forms

- https://stackoverflow.com/questions/6308850/relative-position-with-background-image used to position heading elements in index.html relative to background image

- https://w3schools.invisionzone.com/topic/30695-my-page-content-overflows-but-i-cant-scroll-down used to fix scrolling bug

- https://docs.djangoproject.com/en/5.1/ref/request-response/ used to researchdjango's HttpRequest objects work

- https://compresspng.com/ used to compress hero images for faster page loading

- https://django-crispy-forms.readthedocs.io/en/latest/crispy_tag_forms.html used to research crispy forms

- https://randomkeygen.com/ used to generate Heroku secret key

- https://github.com/django/django/blob/main/django/forms/templates/django/forms/widgets/clearable_file_input.html used this code to clear widget

- https://forum.djangoproject.com/t/static-path-with-s3/28696/9 used this code to fix bug in settings.py for uploading static files to S3

- https://css-tricks.com/snippets/css/css-triangle/ used this CSS code for left and right arrows in print_detail.html slideshow

- https://stackoverflow.com/questions/68425724/what-is-the-use-of-apps-py-appconfig-in-django-project-how-and-why-to-use-it used to understand how AppConfig works

- https://www.site24x7.com/tools/color-code-picker.html#:~:text=Sign%20Up-,Color%20Code%20Picker,file%20size%20is%20upto%201MB. used  to obtain hexcode of part of the blue wall in hero images

## Acknowledgements

Thank you to my brother, 'Leggy' for allowing me to use his artwork, for writing the product descriptions, and for writing about himself in the about.html page

Thank you to my mentor, Sheryl, for supporting me through Slack huddles and via Slack DMs. Sheryl has always found the time to help me fix bugs when I am struggling by finding documentation for me to check out and providing examples from other students on how to write a good README.md and TESTING.md file. She gave great feedback in our video calls about what I am doing right and aspects I could think about changing. I am very grateful for her help.

Thank you to Kaynat for also helping me with bug fixes and for providing guidance before I started the project. Also I really appreciate the time you spend marking our projects.

Thank you to ckz8780, the creator of the Boutiqe Ado walthrough project videos on Code Institute, for your in-depth explanations on implementing all the necessary functionality when creating a Django app and on how to deploy correctly.

Thank you to everyone else at Code Institute and Peterborough University Centre that helps to keep up the running of this course. I feel very fulfulled at the end of my course and I am excited for the rest of my future as a web developer.