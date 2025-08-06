# Simple E-commerce System in Python

This project is a complete e-commerce system simulation, built in Python to run directly in the terminal (command line). It was created for educational purposes to demonstrate concepts like programming logic, data structure manipulation (lists and dictionaries), and how to organize a project into modular functions.

The system does not use a persistent database, which means all information (new users, orders, etc.) is lost when the program closes. 💾

## 🚀 Key Features

### For Customers
-   👤 **User Authentication:** A secure login and registration system.
-   📚 **Product Catalog:** View products with their details, prices, and reviews from other customers.
-   🔎 **Search & Filtering:** Tools to search for products by name and sort them by price or alphabetical order.
-   🛒 **Shopping Cart:** Add, remove, and manage product quantities in your cart.
-   💳 **Checkout Process:**
    -   Apply **discount coupons** (both fixed-value and percentage-based).
    -   Select a delivery address from your saved addresses.
    -   Simulated payment process (for this initial test all payments will be approved as there is no payment API enabled).
-   📜 **Order History:** Check all your past orders with details on items, delivery address, and discounts applied.
-   ⭐ **Rating System:** Customers can rate products they have purchased with a score (1 to 5 stars) and a comment.
-   🔧 **Profile Management:** Change your password and manage multiple delivery addresses.
-   💬 **Customer Support:** Open and track support tickets.

### For Admins
-   ✅ **Full access to all customer features.**
-   🛠️ **Admin Panel:** An exclusive menu with advanced management functionalities.
-   📦 **Product Management:** Add new products, edit information, or remove products from the catalog.
-   🏷️ **Coupon Management:** Create new discount coupons (`percentage` or `fixed`) and activate or deactivate existing ones.
-   📨 **Support Ticket Handling:** View and reply to support tickets opened by customers.

## ⚙️ How to Run the System

1.  Make sure you have **Python 3** installed on your machine.
2.  Save the code in a file with a `.py` extension (e.g., `ecommerce.py`).
3.  Open a terminal or command prompt.
4.  Navigate to the folder where you saved the file.
5.  Run the following command:
    ```bash
    python ecommerce.py
    ```
6.  Follow the instructions displayed in the terminal.

## 🔑 Admin Access

The system comes with a pre-configured admin user so you can test all management features right away.

> **Admin Credentials:**
>
> -   **Username:** `admin`
> -   **Password:** `1234`

When you log in with these credentials, the main menu will display the **Admin Panel** with its exclusive management options.

## 📖 Function Descriptions

The code is organized into sections and modular functions to make it easier to read and maintain.

### 1. Helper Functions
-   `clear_screen()`: Clears the terminal screen.
-   `pause_and_clear()`: Pauses the execution for a few seconds and then clears the screen.
-   `wait_for_enter()`: Pauses the execution until the user presses ENTER.
-   `find_product_by_id(product_id)`: Finds and returns a product from the `PRODUCTS` list by its ID.
-   `generate_new_id(list, key)`: Generates a new sequential ID for an item in a list.
-   `generate_stars(rating)`: Converts a numerical rating into a star representation (e.g., ★★★★☆).
-   `calculate_average_rating(product_id)`: Calculates the average rating of a product based on its reviews.

### 2. Customer-Facing Functions
-   `filter_menu()`: Displays the catalog's filter and sorting menu.
-   `display_product_details(product_id)`: Shows all the details of a product, including its reviews.
-   `view_catalog_and_add()`: Displays the product catalog and allows the user to add items to the cart, search, or filter.
-   `manage_cart()`: Allows the user to view the shopping cart, change quantities, or remove items.
-   `place_order(user)`: Handles the checkout process, including applying coupons and processing the payment.
-   `payment_process(...)`: Simulates a payment confirmation.
-   `check_orders(user)`: Displays the logged-in user's order history.
-   `add_review(user)`: Allows a user to review a product they have purchased.
-   `manage_profile(user)`: A menu for the user to change their password and addresses.
-   `manage_addresses(user)`: A specific submenu for adding or removing addresses.
-   `customer_support_menu(user)`: A menu for the customer to open and check their support tickets.

### 3. Admin Panel Functions
-   `manage_products_admin()`: A complete menu for the admin to list, add, edit, or remove products.
-   `manage_coupons_admin()`: A menu for the admin to list, add, or activate/deactivate discount coupons.
-   `support_menu_admin()`: A menu for the admin to view and reply to customer support tickets.

### 4. Core Logic and Menu Functions
-   `login_signup_menu()`: The system's initial screen, where the user can log in, sign up, or exit.
-   `main_menu(user)`: The main menu that the user sees after logging in, containing all navigation options.
-   `main()`: The main function that controls the program's execution flow (runs the login menu and then the main menu).
