# Project 3

Web Programming with Python and JavaScript

http://marrozh.pythonanywhere.com/


## MENU 
There are 7 models overall. 
'Item' model for items from menu that have one size.
'Size' model for item from menu that have different sizes.
Both store item name, category, prices. 
'Topping' model stores toppings for pizzas.
'Subtopping' model stores toppings for Subs.
'Order' model stores items chosen by a user and passes them into shopping cart page.
'Confirmed' model stores items that have been checked out by a user from shopping cart.
'Complete' model stores orders that the staff have marked as completed in their dashboard.


## Adding Items
Site administrators can users can use Django Admin page to register new staff members, users, add and update the items on the menu. 

## Registration, Login, Logout
New user will be directed to Log in page, where they can log in their account or follow the link to register for new account. Once a user registers, they will be able to enter the main website. 
In views.py login_view function allows for a user to login using their username and password.
logout_view funtion allows a user to log out of the website.
register function allows a user to register for a new account. 

## Shopping Cart
Once the user has logged in, the will be redirected to home page, that displays the restaurants menu.
In views.py index function checks if the user is authenticated, and if yes, passes information about the menu items into index.html.
User can add the items to their shopping cart from the menu, that will be passed into one of the functions: 'add', 'addsize', 'addsizecheese', addsizetop' and 'addsizepizza'. Different functions deal with different types of menu items. 
For subs, when a user chooses extra cheese or toppings, the total price is changes automatically using JavaScript (index.js file).
To view all the topping for each pizza a user also can click an appropriate link and see the available toppings for the item.
If the pizza is 1 topping pizza, user will only be able to select 1 topping, same applies if the pizza has 2 or 3 toppings.

When the user chooses all the items, they can click 'checkout' at the bottom of the menu, or click on 'your cart' in the navigation panel. 

If the user does not checkout, the shopping cart will still remain the same, if user closes the window or logs out.

## Placing an Order
After user chooses at least 1 item, the item/s will be added to shopping cart, with details about all the items and total price for the whole order. 
User can checkout from the shopping cart page by clicking on checkout button. The information will be sent to 'Confirmed' model through 'confirmorder' function. 

## Viewing orders
On the index page, site administrators will have a seperate link to access the 'dashboard', where staff can view all the placed orders, which are displayed from 'Confrirmed' model. 

## Personal touch
In the dashboard, which is only available to staff members, staff member can view each of the placed orders, and once it is complete, can mark the order as complete. 
This will send the order to 'Confirmed' model, using 'complete' function.
When the order is marked as complete by the staff member, user that has placed it, can acess 'My Orders' part of the site, where the user can see all the pending orders, that are still being prepared, and completed orders, that have been marked by staff as complete. 
