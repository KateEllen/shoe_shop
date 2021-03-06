<h1> Funky Feet </h1>

**View a live version of the site [here](https://funky-feet.herokuapp.com/).**

This project has been created for educational purposes.

It is an E-Commerce site for a fictional company 'Funky Feet' which offers a variety of ladies shoes for sale.

![Responsive](https://github.com/KateEllen/shoe_shop/blob/main/media/responsive.png)
___

## Project Goals

The goal of this project is to create E*Commerce store for a ladies shoe shop. 
This project is for educational purposes only.

### Importance and Feasibility chart

| Opportunity/Problem                                                                            | Importance | Viability/Feasibility |
|------------------------------------------------------------------------------------------------|------------|-----------------------|
| Users are able to register an account and login                                                | 5          | 5                     |
| Users can add, edit and remove items from their shopping bag                                   | 5          | 5                     |
| Blog Section so users can read related articles from celeb/fashion experts concerning products | 5          | 5                     |
| Super users can add, edit, delete blogs                                                        | 5          | 5                     |
| Allow users to add and edit, delete their own blog comments                                    | 4          | 4                     |
| Super users can edit any blog comments                                                         | 4          | 4                     |
| Users can search for products by keyworkds                                                     | 4          | 5                     |
| Users are notified of their actions while interacting with the site                            | 4          | 4                     |
| Users can sign up to the newsletter                                                            | 3          | 4                     |

## User Stories

I used the Project page of Github to help keep track of my work. You can find it [here](https://github.com/KateEllen/shoe_shop/projects/1)

### User Goals

* As a **User**, I want to easily understand the purpose of the site when navigating on it.
* As a **User**, I want to be able to intuitively navigate the entire site in an easy way.
* As a **User**, I want to be able to have the same functionalities on different devices (mobile, tablet and PC).
* As a **User**, I want to be able to see what items are available for purchase on the site.
* As a **User**, I want to know the prices of the items.
* As a **User**, I want to be able to sign up for an account and receive a confirmation email.
* As a **User**, I want to be able to sign up for the newsletter.


### Registered User goals

* As a **Registered User**, I want to be able to easily login and logout of my account.
* As a **Registered User**, I want to be able to easily add and remove items in my shopping bag.
* As a **Registered User**, I want to be able to easily purchase items on my shopping bag.
* As a **Registered User**, I want to receive a purchase confirmation email.
* As a **Registered User**, I want to be able to easily update my contact and delivery information.
* As a **Registered User**, I want to be able to view my previous orders.


### Site Owner/Superuser goals

* As a **Site Owner/Superuser**, I want to be able to add new products.
* As a **Site Owner/Superuser**, I want to be able to edit and delete products.
* As a **Site Owner/Superuser**, I want to be able to access the admin section of the site to view orders made, the items they contain and the delivery information.
* As a **Site Owner/Superuser**, I want to be able to access the admin section of the site to view users registered. 


## Site Structure

The aim of the site is offer an easy to navigate and accesible uer experience.
The different elements on the site (header/footer/nav links) remain the same across the site but will be displayed differently from mobile to other devices. The header will always contain a link to the products page and different links based on whether a user is logged in or a super*user.

### Other links:
* User not logged in: 
    * Register
    * Login

* Logged in:
    * My Profile
    * Shopping Bag
    * Logout

    * **Only as superuser** 
        * Admin (dropdown)
            * My profile
            * Explore management
            * Product management

### Wireframes 

The wireframes of the site can be found in the following links: 

* ![Homepage](https://github.com/KateEllen/shoe_shop/blob/main/media/home-wireframe.png)
* ![All products](https://github.com/KateEllen/shoe_shop/blob/main/media/all-products-wireframe.png)
* ![Product detail](https://github.com/KateEllen/shoe_shop/blob/main/media/product-detail-wireframe.png)
* ![Profile](https://github.com/KateEllen/shoe_shop/blob/main/media/profile-wireframe.png)
* ![Bag](https://github.com/KateEllen/shoe_shop/blob/main/media/bag-wireframe.png)
* ![Checkout](https://github.com/KateEllen/shoe_shop/blob/main/media/checkout-wireframe.png)

The final result is slightly different as during the development stage the way things were displayed was not as user friendly as expected. 

## Styling

### Colours

The palette of colors for the site is simple, the main colors are black and white. I added a pop of yellow to catch the eye. 

![Color-palette](https://github.com/KateEllen/shoe_shop/blob/main/media/colour-scheme.png)

# Features

## Existing Features 

### Features in all apps
* Toast Messages, which are pop up messages appear. The toast messages will notify the user when an action has been successful or unsuccessful. These messages can be dismissed by the user by clicking the x button.
![Footer](https://github.com/KateEllen/shoe_shop/blob/main/media/order-success.png)

* Navbar 
  * Contains the site name, My Account dropdown, Shopping bag, Search bar, all shoes, boots, heels, trainers, flats and special offers.
  * My Profile and Logout links. Logged in superusers will also find the Manage Products.
  * The Basket link will take users to their shopping basket page. 
  * The search function allows users to input keywords that filter the content to meet the inputed criteria.

* Funky Feet Logo 
  * A clickable link that brings you back to the homepage.

![Nav and Logo](https://github.com/KateEllen/shoe_shop/blob/main/media/nav-and-logo.png)

### Footer 
  * Subscribe, so the users can sign up for the NewsLetter.
  * Users can sign up for newsletters to get previews of celebrity blogs and sales

  * Facebook link. 
  ![Footer](https://github.com/KateEllen/shoe_shop/blob/main/media/footer.png)

### Features on the Home Page
* Home Image 
  * An image that shows to the user what the site is about.
![Home page](https://github.com/KateEllen/shoe_shop/blob/main/media/homepage.png)

### Features on the Sign Up Page 
* Sign Up Form 
  * A very simply form, with instructions on how to register for the site. The text is clear and legible.
  * Has form control that will tell the user if any fields haven't been filled out correctly whilst ensuring the form doesn't get sent without the required information.
  * It includes the following fields:
    *  Email field
    *  Confirm email
    *  Username
    *  Password
    *  Confirm password fields. 
    *  Link to redirect users who have already registered in the site.

* Sign Up Button 
  * This button generates and sends a verification email link, to the email address provided. 
  * This will allow the user to have accesible that information in their personal area. 

    ![Sign Up](https://github.com/KateEllen/shoe_shop/blob/main/media/sign-up.png)

### Features on the Sign In Page 
* Sign In Form 
  * Another easy Form, with instructions on how to log into the site. 
  * Form control.
  * Includes a username and password field, with a link at the top to direct users who haven't registered to the Sign Up page.
  * Within the form there is also a remember me tick box which will save your login information for future visits.

* Home Button 
  * Button to return to the home page.

* Sign In Button 
  *  Authenticates the user and return to the home page.

* Unique Email Required. 
  * ![Unique Email](https://github.com/KateEllen/shoe_shop/blob/main/media/unique-email.png)

* Forgotten Password Link 
  * Users can reset their password if they've forgotten it. An email containing a link that directs users to simple instructions on how to reset their password. 
    ![Sign In](https://github.com/KateEllen/shoe_shop/blob/main/media/login.png)

### Features on All Products
* Page Title 
  * Helps the user to make sure they are on the correct page.

* Sort By Dropdown 
  * Sort All Products by price (high/low) or alphabetically.

* Edit/Delete links 
  * (Superusers Only) Access to the Edit/Delete links allowing them to delete products and directing them to the Edit page to edit the different products.
      ![All products](https://github.com/KateEllen/shoe_shop/blob/main/media/product-example.png)


### Features on the Products Information Page
* Image 
  * Image of the selected product. 

* Product Information 
  * Name
  * Price
  * Category
  * Description
  * Size selector
  * Quantity selector
![Product Information](https://github.com/KateEllen/shoe_shop/blob/main/media/product-info.png)

### Features on the Profile Page  

* Delivery Information Form 
  * This form shows the user's default delivery information. 
  * There are required fields that need to be filled/updated before being able to save it.
  * The information from this form will automatically be taken from the order form when the user is buying something if they have filled out the checkout form and clicking the tick box 'Save this delivery information to my profile'.

* Form Fields 
  * The input fields are: 
    * Phone Number
    * Street Address 1
    * Street Address 2
    * Town or City
    * County
    * Postcode
    * Country dropdown to make easier for the user to find their country.

  * The form has instructions in how to be completed and also has form validation 

* Update Information Button 
  * If the users want to update their delivery information, fill out the fields in the form above with the required information and click this button to save the updated information to their profile.

* Order History 
  * This section provides users with their personal order history, including date, time, items ordered, order number, etc.
  * The most recent order will be displayed at the top.

  ![Profile](https://github.com/KateEllen/shoe_shop/blob/main/media/my-profile.png)


### Features on the Shopping Bag
* List of Added Items
  *  The list contains:
     *  Product Info section
     *  Image
     *  Product name 
     *  SKU 
     *  Total price section 
     *  Quantity function with -/+ buttons to adjust the amount of items that the user wants to buy, in case they want to add more items.

* Basket Total 
  *  This is the total items the user will have in their shopping bag. 

* Delivery  
  * Delivery charge the user will be charged if they don't reach the $80 to get a free delivery.

* Grand Total  
  * The sum of the total of all the items in the bag and delivery charge. This is the total amount the users will be charged in their cards. 

![Product Information](https://github.com/KateEllen/shoe_shop/blob/main/media/product-info.png)

### Features on the Checkout Page 
* Payment form 
  * Follow same structures and form validation. 
  * If the user have ordered before the information will be populated as well.

* Save Information Tickbox 
  * If the user ticks their information will be saved for thenext time.
  * If a field needs to be updated the user can enter the information in the checkout form and it will override the data on the profile page if the user select 'Save this delivery information to my profile'.

* Payment Form Field 
  * This box will require users their card information (card number, month/year, cvc and zip code). To test you must use stripe default test card.

* Adjust Bag Button 
  * Redirect the users back to the Shopping Bag page.

* Complete Order Button 
  * The order for the user is processed. 
  * Generates a confirmation email that is sent to the email address provided in the checkout form.
  ![Email confirmation](https://github.com/KateEllen/shoe_shop/blob/main/media/email.png)

* Card Charge Warning 
* Reminder for the users to tell them that their card will be charged with the stated amount.

![Checkout](https://github.com/KateEllen/shoe_shop/blob/main/media/checkout.png)

### Features on the Subscription feature
** Please note that email from site (Funky Feet) may end up in spam folder **

* The user can subscribe to the page.
* The user have an input box and a button to subscribe.
* The user will be receiving an email in their inbox.

### Features on the Blog
* The site supports a blog which will host product writes ups by famous people or  instagram influencers to help better sell products and increase product awareness.

* CRUD functionality
* View Blog Posts
![Blog](https://github.com/KateEllen/shoe_shop/blob/main/media/blog-list.png)
* Post Title gives information for the user about what the blog post is about.
* Post Link
  * A link to redirect the users back to the Explore page with all the posts available.
* Date and Time Post was Published
  * Date and time stamp and the profile name of the super user who created the post entry.
* Post Content/Body
  * The content of the blog that has been included by the super user.

* Comments
* Comments were included in blogs to help enrich a community environment among frequent visitors and encourage interaction with customers.

  * The comments section shows users responses to the blog.
  * Only registered users can post comments.
  * To post comments to the blogs is through the form directly under this section on the site page.
  * When no comments have been add it will display 'No Comments Yet'.
  * This will include:
    * Comment title
    * Date and time the comment was added
    * Edit/Delete comment
    * Leave a comment

![Blog](https://github.com/KateEllen/shoe_shop/blob/main/media/blog.png)

### Add Post **(superuser only)**
Super user's can create blog posts.
![Add Post](https://github.com/KateEllen/shoe_shop/blob/main/media/add-blog.png)

### Delete Post **(superuser only)**
Super user's can delete their blog posts.
![Delete Post](https://github.com/KateEllen/shoe_shop/blob/main/media/delete-blog.png) 

### Edit Post **(superuser only)**
Super user's can edit their blog posts. 
![Edit Post](https://github.com/KateEllen/shoe_shop/blob/main/media/edit-blog.png)

### Features on the Comments 

* CRUD functionality

* Create comments
![Create Comments](https://github.com/KateEllen/shoe_shop/blob/main/media/create-comment.png)

* Read comments under specific blog post
![Comments](https://github.com/KateEllen/shoe_shop/blob/main/media/comments.png)

* Edit comments you have left
![Edit Comments](https://github.com/KateEllen/shoe_shop/blob/main/media/edit-comment.png)

* Superuser can delete comments you have left
![Delete Comments](https://github.com/KateEllen/shoe_shop/blob/main/media/delete-comment.png)

## Future features 
* Returns
* Product rating
* Live chat
* Images for blog posts

# Testing

The full testing performed can be found [here](./TESTING.md)


# Deployment 
## Heroku Deployment
It's required to have an [AWS](https://aws.amazon.com/s3/) account and a [S3 bucket](https://aws.amazon.com/s3/) to hold all the static files for this project.

1. Open and login to [Heroku](https://id.heroku.com/login)

2. Add all of your Config Vars. Such as keys for AWS, Stripe, Secret Key, Database URL and Email keys. 

3. In your local terminal type "heroku login"

4. Use git to clone your repository's sorce code to your local machine. You can do this by typing "heroku git:clone -a (REPO NAME) then cd (REPO NAME) into yout terminal.

5. Now make some changes to the code you just clined and deploy them to Heorku using Git. You can do this by typing "git add ." followed by "git commit -m 'commit message' " then you will finally type "git push heroku main" to deploy to Heorku. This is all done in your local terminal. 

6. When your app is deployed successfully. Click _Open App_ in to top right hand corner of Heroku to open app in a new tab in the browser.

## Entity Relationship Diagram


## Database Choice
I used postgres as the database because the data is relational and heroku serves this up realitvely easily with no cost.The models used to construct the site are outlined below:

* Post

| DB Key 	         | Data Type 	   |          Purpose          	        | Form Validation                        	|
|--------	         |:---------:	   |:-------------------------:	        |----------------------------------------	|
| pk   	           | ObjectId  	   | unique identifier, auto generated  | None                                   	|
| post_title   	   | CharField     | Display name of blog entry         | Required<br>Min 1 char<br>Max 50 chars 	|
| post_content     | TextField     | Body of blog 	                    | Required                               	|
| post_date_posted | DateTimeField | Date of blog being created 	      | Required                               	|
| post_content     | ForeignKey    | User who created blog 	            | Required                               	|

* Comment

| DB Key              | Data Type     | Purpose                       | Form Validation |
|---------------------|---------------|-------------------------------|-----------------|
| post_id             | ForeignKey    | Unique identifier             | None            |
| comment_title       | CharField     | Display comment title         | Required        |
| comment_content     | TextField     | Body of comment               | Required        |
| comment_date_posted | DateTimeField | Date of comment being created | Required        |
| comment_author      | ForeignKey    | User who created comment      | Required        |

* Order

| DB Key          | Data Type     | Purpose                       | Form Validation           |
|-----------------|---------------|-------------------------------|---------------------------|
| order_number    | CharField     | Unique identifier             | None                      |
| user_profile    | ForeignKey    | Display comment title         | Required                  |
| full_name       | CharField     | Users name                    | Required                  |
| email           | EmailField    | Users email                   | Required                  |
| phone_number    | CharField     | Users phone number            | Required                  |
| country         | CountryField  | Users country                 | Required                  |
| postcode        | CharField     | Users postcode                | Required                  |
| town_or_city    | CharField     | Users town or city            | Required                  |
| street_address1 | CharField     | Users street address 1        | Required                  |
| street_address2 | CharField     | Users street address 2        | Not required              |
| county          | CharField     | Users county                  | Required                  |
| date            | DateTimeField | Date of order                 | Required, auto populated  |
| delivery_cost   | DecimalField  | Delivery cost                 | Required, auto populated  |
| order_total     | DecimalField  | Cost of items in bag          | Required, auto populated  |
| grand_total     | DecimalField  | Total cost including delivery | Required, auto populated  |
| original_bag    | TextField     | Bag total                     | Required, auto populated  |
| stripe_pid      | CharField     | Stripe payments               | Required                  |

* Order Line Item

| DB Key         | Data Type    | Purpose           | Form Validation          |
|----------------|--------------|-------------------|--------------------------|
| order          | ForeignKey   | Show order        | Required                 |
| product        | ForeignKey   | Products in order | Required                 |
| product_size   | CharField    | Size of shoe      | Required                 |
| quantity       | IntegerField | Amount selected   | Required                 |
| lineitem_total | DecimalField | total amount      | Required, auto populated |

* Product

| DB Key      | Data Type    | Purpose                     | Form Validation          |
|-------------|--------------|-----------------------------|--------------------------|
| category    | ForeignKey   | Category of product         | Required                 |
| sku         | CharField    | Stock keeping unit          | Required, auto populated |
| name        | CharField    | Name of product             | Required                 |
| description | TextField    | Description of product      | Required                 |
| price       | DecimalField | Price of product            | Required                 |
| image_url   | URLField     | URL image of product        | Not Required             |
| image       | ImageField   | Image of product            | Not Required             |
| has_sizes   | BooleanField | Available sizes for product | Not Required             |

* User profile

| DB Key                  | Data Type     | Purpose                | Form Validation                                 |
|-------------------------|---------------|------------------------|-------------------------------------------------|
| user                    | OneToOneField | Logged in user         | Required                                        |
| default_phone_number    | CharField     | Saved phone number     | Not Required, auto populated if saved by user   |
| default_street_address1 | CharField     | Saved street address 1 | Not Required, auto populated if saved by user   |
| default_street_address2 | CharField     | Saved street address 2 | Not Required, auto populated if saved by user** |
| default_town_or_city    | CharField     | Saved town or city     | Not Required, auto populated if saved by user   |
| default_country         | CountryField  | Saved country          | Not Required, auto populated if saved by user   |
| default_postcode        | CharField     | Saved postcode         | Not Required, auto populated if saved by user   |
| default_county          | CharField     | Saved county           | Not Required, auto populated if saved by user   |

* Subscription

| DB Key    | Data Type  | Purpose        | Form Validation          |
|-----------|------------|----------------|--------------------------|
| email     | EmailField | Logged in user | Required                 |
| timestamp | CharField  | DateTimeField  | Required, auto populated |

## SEO Strategy

- Each page has key words meta data= xxxx as well as a description =xxx Product detail pages include the name of the shoe being sold in the description. Key words are also in content on the home page to re-enforce to search engines that the keywords aren???t being stuffed.

- I used sites like [Zappos](https://www.zappos.com/) and [Office](https://www.office.co.uk/)to deicde what keywords I would need. The keywords I selected are listed below. 

* shoes
* elusive
* unique
* free shipping
* ladies
* girls
* fashion
* womens shoes
* casual shoes
* new shoes
* shoe shop
* sale
* special offer

# E-commerce Business Model
This site is designed for women who love shoes. They can find comfortable and unique styles for any ocassion. The user is also able to subscribe the the newsletter to receive news about the store.

## Facebook Business Page
Below are screenshots of the Funky Feet Facebook page. This page gives users the oppertunity to see extra updates outside of the website. The facebook page can be viewed here [Facebook](https://www.facebook.com/Funky-Feet-100119349392932)

![Facebook1](https://github.com/KateEllen/shoe_shop/blob/main/media/facebook1.png)
![Facebook2](https://github.com/KateEllen/shoe_shop/blob/main/media/facebook2.png)

### Sitemap
![Sitemap](https://github.com/KateEllen/shoe_shop/blob/main/output.png)

# Credits

## Content 
* Products info and pictures - [Office](https://www.office.co.uk/)
* Wireframes - [Balsamiq](https://balsamiq.com/wireframes/)

## Media 
Images - [Office](https://www.office.co.uk/)
Facebook cover photo - [Canva](https://www.canva.com/)
* [Font-Awesome](https://fontawesome.com/)


## Acknowledgements

### I received inspiration for this project from:
* [Boutique Ado](https://github.com/ckz8780/ci-fsf-hello-django/tree/c13b414fd2e87a54b4f2788ceffec55be4ade925)
* [Office](https://www.office.co.uk/)
* [StackOverflow](https://stackoverflow.com/)
* [Coolors](https://coolors.co/)


### I received advice and support from
* [Niall Maher](https://www.linkedin.com/in/nialljoemaher/?originalSubdomain=ie)
* Code Institute [Slack Community](code-institute-room.slack.com)
* My mentor Malia was a huge help in this project as always. She constantly steered me in the right direction and helped me with my many questions on queries. 


