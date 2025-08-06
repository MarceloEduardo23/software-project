# ==============================================================================
# 1. IMPORTS AND INITIAL CONFIGURATION
# ==============================================================================
import os
import time
import random

# --- (Simulated) Database ---
USERS = {
    'admin': {'password': '1234', 'addresses': []},
    'customer': {'password': '123', 'addresses': [{'nickname': 'Home', 'street': 'Fictional Street, 123', 'city': 'São Paulo, SP'}]}
}
PRODUCTS = [
    {'id': 1, 'name': 'Gaming Notebook', 'description': 'Notebook with RTX 4080 graphics card', 'price': 8500.00},
    {'id': 2, 'name': 'Gaming Mouse', 'description': 'Wireless mouse with 16000 DPI', 'price': 350.50},
    {'id': 3, 'name': 'Mechanical Keyboard', 'description': 'Keyboard with blue switches and RGB', 'price': 450.00},
]
REVIEWS = []
COUPONS = [{'code': 'PROMO10', 'type': 'percentage', 'value': 10, 'active': True}]
TICKETS = []
CART = {}
ORDERS = []

# ==============================================================================
# 2. HELPER FUNCTIONS
# ==============================================================================
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def pause_and_clear(seconds=2):
    time.sleep(seconds)
    clear_screen()

def wait_for_enter():
    input("\n\tPress ENTER to continue...")

def find_product_by_id(product_id):
    return next((p for p in PRODUCTS if p['id'] == product_id), None)

def generate_new_id(data_list, key='id'):
    return max(item[key] for item in data_list) + 1 if data_list else 1

def generate_stars(rating):
    rounded_rating = round(rating)
    return '★' * rounded_rating + '☆' * (5 - rounded_rating)

def calculate_average_rating(product_id):
    product_reviews = [r['rating'] for r in REVIEWS if r['product_id'] == product_id]
    if not product_reviews: return 0, 0
    return sum(product_reviews) / len(product_reviews), len(product_reviews)

# ==============================================================================
# 3. SYSTEM FEATURES FUNCTIONS
# ==============================================================================

def filter_menu():
    clear_screen()
    print("\n\t--- Apply Filters and Sorting ---\n\t1 - By Price (Lowest to Highest)\n\t2 - By Price (Highest to Lowest)\n\t3 - By Name (A-Z)\n\t0 - Back")
    try:
        option = int(input("\n\t=> "))
        if option == 1: return 'price_asc'
        if option == 2: return 'price_desc'
        if option == 3: return 'name_asc'
        return None
    except ValueError: return None

def display_product_details(product_id):
    clear_screen()
    product = find_product_by_id(product_id)
    if not product: print("\n\t[ERROR] Product not found."); pause_and_clear(); return

    average, num_reviews = calculate_average_rating(product_id)
    print(f"\n\t--- Details of: {product['name']} ---")
    print(f"\tID: {product['id']}\n\tPrice: $ {product['price']:.2f}\n\tDescription: {product['description']}")
    if num_reviews > 0: print(f"\tAverage Rating: {average:.1f}/5.0 ({generate_stars(average)})")
    print("\t" + "="*50 + "\n\n\tCUSTOMER REVIEWS:")

    comments = [r for r in REVIEWS if r['product_id'] == product_id]
    if not comments: print("\tThis product has no reviews yet.")
    else:
        for review in comments:
            print("\t" + "-"*30 + f"\n\tUser: {review['user']}\n\tRating:   {generate_stars(review['rating'])}\n\tComment: {review['comment']}")
    wait_for_enter()

def view_catalog_and_add():
    search_term, sort_order = "", None
    while True:
        clear_screen()
        products_to_display = list(PRODUCTS)
        if search_term: products_to_display = [p for p in products_to_display if search_term.lower() in p['name'].lower()]
        if sort_order == 'price_asc': products_to_display.sort(key=lambda p: p['price'])
        elif sort_order == 'price_desc': products_to_display.sort(key=lambda p: p['price'], reverse=True)
        elif sort_order == 'name_asc': products_to_display.sort(key=lambda p: p['name'])

        print("\n\t--- Product Catalog ---")
        print(f"\tActive filters: [Search: '{search_term}' | Sort: {sort_order or 'Default'}]")
        print("\t" + "="*60)
        if not products_to_display: print("\n\tNo products found.")
        else:
            for p in products_to_display:
                average, n_rev = calculate_average_rating(p['id'])
                rating_str = f"| Rating: {average:.1f}/5 ({n_rev})" if n_rev > 0 else "| No reviews"
                print(f"\tID {p['id']}: {p['name']} ($ {p['price']:.2f}) {rating_str}")

        print("\n\t--- Actions ---\n\t1 - View details\n\t2 - Add to cart\n\t3 - Search\n\t4 - Filter / Sort\n\t5 - Clear filters\n\t0 - Back")
        try:
            choice = int(input("\n\t=> "))
            if choice == 1:
                details_id = int(input("\tProduct ID to view details: "))
                display_product_details(details_id)
            elif choice == 2:
                add_id = int(input("\tProduct ID to add: "))
                product = find_product_by_id(add_id)
                if product:
                    quantity = int(input(f"\tQuantity of '{product['name']}': "))
                    if quantity > 0:
                        CART[add_id] = CART.get(add_id, 0) + quantity
                        print(f"\n\t>>> Added!"); time.sleep(1)
                else: print("\n\t[ERROR] Product not found."); time.sleep(2)
            elif choice == 3: search_term = input("\tTerm to search for: ")
            elif choice == 4:
                new_order = filter_menu()
                if new_order: sort_order = new_order
            elif choice == 5: search_term, sort_order = "", None; print("\n\tFilters cleared."); time.sleep(1)
            elif choice == 0: break
        except (ValueError, KeyError): print("\n\t[ERROR] Invalid option."); time.sleep(2)

def manage_cart():
    while True:
        clear_screen(); print("\n\t--- Shopping Cart ---")
        cart_total = 0
        if not CART: print("\n\tYour cart is empty.")
        else:
            for p_id, quantity in CART.items():
                product = find_product_by_id(p_id)
                if product:
                    subtotal = product['price'] * quantity
                    cart_total += subtotal
                    print(f"\t- {product['name']} | Qty: {quantity} | Subtotal: $ {subtotal:.2f}")
            print("\n\t" + "="*30 + f"\n\tTOTAL: $ {cart_total:.2f}\n" + "\t" + "="*30)

        print("\n\t1 - Add more items\n\t2 - Remove item\n\t0 - Back")
        try:
            option = int(input("\n\t=> "))
            if option == 1: view_catalog_and_add()
            elif option == 2:
                if not CART: print("\n\t[ERROR] Cart is already empty."); pause_and_clear(); continue
                remove_id = int(input("\tProduct ID to remove: "))
                if remove_id in CART:
                    current_qty = CART[remove_id]
                    name = find_product_by_id(remove_id)['name']
                    print(f"\n\tYou have {current_qty} of '{name}'.")
                    remove_qty = int(input("\tHow many do you want to remove? "))
                    if 0 < remove_qty < current_qty: CART[remove_id] -= remove_qty; print(f"\n\t{remove_qty} unit(s) removed.")
                    elif remove_qty >= current_qty: del CART[remove_id]; print(f"\n\tItem '{name}' removed.")
                    else: print("\n\t[ERROR] Invalid quantity.")
                else: print("\n\t[ERROR] Product not in cart.")
                pause_and_clear()
            elif option == 0: break
        except (ValueError, KeyError): print("\n\t[ERROR] Invalid option or ID."); pause_and_clear()

def place_order(logged_in_user):
    clear_screen(); print("\n\t--- Checkout ---")
    if not CART: print("\n\tYour cart is empty."); pause_and_clear(); return

    original_total = sum(find_product_by_id(p_id)['price'] * quantity for p_id, quantity in CART.items())
    print(f"\n\tSubtotal: $ {original_total:.2f}")

    applied_coupon, discount = None, 0
    coupon_code = input("\tDiscount coupon? (Leave blank if none): ").upper()
    if coupon_code:
        coupon = next((c for c in COUPONS if c['code'] == coupon_code), None)
        if coupon and coupon['active']:
            if coupon['type'] == 'percentage': discount = original_total * (coupon['value'] / 100)
            else: discount = coupon['value']
            applied_coupon = {'code': coupon['code'], 'calculated_discount': discount}
            print(f"\n\t>>> Coupon '{coupon['code']}' applied! Discount of $ {discount:.2f} <<<")
        else: print("\n\t[ERROR] Invalid or inactive coupon.")

    final_total = max(0, original_total - discount)
    print(f"\n\tTOTAL TO PAY: $ {final_total:.2f}")
    wait_for_enter()

    addresses = USERS[logged_in_user]['addresses']
    if not addresses: print("\n\tNo registered addresses."); pause_and_clear(); return
    print("\n\tSelect the address:")
    for i, addr in enumerate(addresses): print(f"\t{i+1} - {addr['nickname']}")
    try:
        selected_address = addresses[int(input("\n\t=> ")) - 1]
    except (ValueError, IndexError): print("\n\t[ERROR] Invalid choice."); pause_and_clear(); return

    success = payment_process(logged_in_user, selected_address, final_total, applied_coupon)
    if success: print("\n\tOrder placed successfully!"); CART.clear()
    else: print("\n\tPayment failed. The order was not completed.")
    pause_and_clear(4)

def payment_process(user, address, total, coupon_info):
    clear_screen(); print("\n\t--- Payment Simulation ---")
    print("\n\tProcessing your payment...")
    time.sleep(3)

    # Simulate a random payment success or failure
    if random.choice([True, False]):
        print("\n\tPayment confirmed!")
        new_order = {
            'id': generate_new_id(ORDERS),
            'user': user,
            'items': CART.copy(),
            'total': total,
            'status': 'Payment Approved',
            'delivery_address': address,
            'applied_coupon': coupon_info,
            'payment_id': f'SIM_{random.randint(1000, 9999)}'
        }
        ORDERS.append(new_order)
        return True
    else:
        print("\n\t[ERROR] Payment was declined by the operator.")
        return False

def check_orders(logged_in_user):
    clear_screen(); print("\n\t--- My Orders ---")
    user_orders = [p for p in ORDERS if p['user'] == logged_in_user]
    if not user_orders: print("\n\tYou have no orders.")
    else:
        for order in user_orders:
            print("\n" + "="*45)
            print(f"\tOrder ID: {order['id']} | Status: {order['status']}\n\tTOTAL PAID: $ {order['total']:.2f}")
            if order['applied_coupon']: print(f"\tDiscount: $ {order['applied_coupon']['calculated_discount']:.2f} (Coupon: {order['applied_coupon']['code']})")
            print(f"\tAddress: {order['delivery_address']['street']}")
            print("\tItems:")
            for p_id, quantity in order['items'].items(): print(f"\t  - {quantity}x {find_product_by_id(p_id)['name']}")
            print("="*45)
    wait_for_enter()

def add_review(logged_in_user):
    clear_screen(); print("\n\t--- Review Purchased Products ---")
    orders = [p for p in ORDERS if p['user'] == logged_in_user]
    if not orders: print("\n\tYou have no orders to review."); pause_and_clear(); return
    purchased_products = {id_p: find_product_by_id(id_p) for p in orders for id_p in p['items']}
    print("\n\tSelect the product to review:")
    for id_prod, prod_info in purchased_products.items(): print(f"\tID {id_prod}: {prod_info['name']}")
    try:
        review_id = int(input("\n\t=> "))
        if review_id not in purchased_products: raise ValueError
        rating = int(input("\tRating from 1 to 5: "))
        if not 1 <= rating <= 5: print("\n\t[ERROR] Invalid rating."); pause_and_clear(); return
        comment = input("\tComment (optional): ")
        REVIEWS.append({'product_id': review_id, 'user': logged_in_user, 'rating': rating, 'comment': comment})
        print("\n\tReview registered!"); pause_and_clear()
    except (ValueError, KeyError): print("\n\t[ERROR] Invalid ID."); pause_and_clear()

def manage_profile(logged_in_user):
    while True:
        clear_screen(); print(f"\n\t--- Manage Profile of {logged_in_user} ---\n\t1 - Change Password\n\t2 - Manage Addresses\n\t0 - Back")
        try:
            choice = int(input("\n\t=> "))
            if choice == 1:
                current_password = input("\tCurrent password: ")
                if USERS[logged_in_user]['password'] == current_password:
                    new_password = input("\tNew password: ")
                    if new_password and new_password == input("\tConfirm: "): USERS[logged_in_user]['password'] = new_password; print("\n\tPassword changed!")
                    else: print("\n\t[ERROR] Passwords do not match or are blank.")
                else: print("\n\t[ERROR] Incorrect current password.")
                pause_and_clear()
            elif choice == 2: manage_addresses(logged_in_user)
            elif choice == 0: break
        except ValueError: print("\n\t[ERROR] Invalid option."); pause_and_clear()

def manage_addresses(logged_in_user):
    while True:
        clear_screen(); addresses = USERS[logged_in_user]['addresses']
        print("\n\t--- My Addresses ---")
        if not addresses: print("\n\tNo registered addresses.")
        else:
            for i, addr in enumerate(addresses): print(f"\t{i+1} - {addr['nickname']}: {addr['street']}, {addr['city']}")
        print("\n\t1 - Add Address\n\t2 - Remove Address\n\t0 - Back")
        try:
            choice = int(input("\n\t=> "))
            if choice == 1:
                nickname, street, city = input("\tNickname: "), input("\tStreet and number: "), input("\tCity and state: ")
                if nickname and street and city: addresses.append({'nickname': nickname, 'street': street, 'city': city}); print("\n\tAddress added!")
                else: print("\n\t[ERROR] All fields are required.")
            elif choice == 2:
                if not addresses: print("\n\t[ERROR] No addresses to remove."); pause_and_clear(); continue
                remove_num = int(input("\tNumber of the address to remove: "))
                if 1 <= remove_num <= len(addresses): print(f"\n\tAddress '{addresses.pop(remove_num - 1)['nickname']}' removed!")
            elif choice == 0: break
            pause_and_clear()
        except ValueError: print("\n\t[ERROR] Invalid option."); pause_and_clear()

def customer_support_menu(logged_in_user):
    while True:
        clear_screen(); print("\n\t--- Customer Support ---\n\t1 - Open Ticket\n\t2 - My Tickets\n\t0 - Back")
        try:
            choice = int(input("\n\t=> "))
            if choice == 1:
                subject = input("\tSubject: ")
                message = input("\tDescribe your problem: ")
                if subject and message:
                    TICKETS.append({'id': generate_new_id(TICKETS), 'user': logged_in_user, 'subject': subject, 'message': message, 'status': 'Open', 'admin_response': None}); print("\n\tTicket created successfully!")
                else: print("\n\t[ERROR] Subject and message cannot be empty.")
                pause_and_clear()
            elif choice == 2:
                clear_screen(); print("\n\t--- My Support Tickets ---")
                user_tickets = [t for t in TICKETS if t['user'] == logged_in_user]
                if not user_tickets: print("\n\tYou have not opened any tickets.")
                else:
                    for ticket in user_tickets:
                        print("\n\t" + "="*40 + f"\n\tID: {ticket['id']} | Status: {ticket['status']}\n\tSubject: {ticket['subject']}\n\tYour Message: {ticket['message']}")
                        if ticket['admin_response']: print(f"\tSupport Response: {ticket['admin_response']}")
                wait_for_enter()
            elif choice == 0: break
        except ValueError: print("\n\t[ERROR] Invalid option."); pause_and_clear()

# ==============================================================================
# 5. ADMINISTRATION FUNCTIONS
# ==============================================================================
def manage_products_admin():
    while True:
        clear_screen(); print("\n\t--- Manage Products ---\n\n\t1 - List\n\t2 - Add\n\t3 - Edit\n\t4 - Remove\n\t0 - Back")
        try:
            option = int(input("\n\t=> "))
            if option == 1:
                clear_screen(); print("\n\t--- Catalog ---")
                for p in PRODUCTS: print(f"\tID {p['id']}: {p['name']} - $ {p['price']:.2f}")
                wait_for_enter()
            elif option == 2:
                clear_screen(); print("\n\t--- Add ---")
                name, desc, price = input("\tName: "), input("\tDescription: "), float(input("\tPrice: "))
                PRODUCTS.append({'id': generate_new_id(PRODUCTS), 'name': name, 'description': desc, 'price': price}); print("\n\tProduct added!")
                pause_and_clear()
            elif option == 3:
                clear_screen(); print("\n\t--- Edit ---")
                product = find_product_by_id(int(input("\tProduct ID: ")))
                if product:
                    print(f"\n\tEditing '{product['name']}'. Leave blank to not change.")
                    new_name, new_desc, new_price = input("\tNew name: "), input("\tNew description: "), input("\tNew price: ")
                    if new_name: product['name'] = new_name
                    if new_desc: product['description'] = new_desc
                    if new_price: product['price'] = float(new_price)
                    print("\n\tProduct updated!")
                else: print("\n\t[ERROR] Product not found.")
                pause_and_clear()
            elif option == 4:
                clear_screen(); print("\n\t--- Remove ---")
                product = find_product_by_id(int(input("\tProduct ID: ")))
                if product: PRODUCTS.remove(product); print(f"\n\tProduct '{product['name']}' removed!")
                else: print("\n\t[ERROR] Product not found.")
                pause_and_clear()
            elif option == 0: break
        except (ValueError, KeyError): print("\n\t[ERROR] Invalid option or ID."); pause_and_clear()

def manage_coupons_admin():
    while True:
        clear_screen(); print("\n\t--- Manage Coupons ---\n\t1 - List\n\t2 - Add\n\t3 - Activate/Deactivate\n\t0 - Back")
        try:
            choice = int(input("\n\t=> "))
            if choice == 1:
                clear_screen(); print("\n\t--- Coupon List ---")
                if not COUPONS: print("\n\tNo coupons.")
                else:
                    for c in COUPONS: print(f"\t- {c['code']} | {c['type']} | {c['value']}{'%' if c['type']=='percentage' else ''} | {'Active' if c['active'] else 'Inactive'}")
                wait_for_enter()
            elif choice == 2:
                clear_screen(); print("\n\t--- Add Coupon ---")
                code = input("\tCode: ").upper()
                if any(c['code'] == code for c in COUPONS): print("\n\t[ERROR] Code already exists."); pause_and_clear(); continue
                coupon_type = input("\tType ('percentage' or 'fixed'): ").lower()
                if coupon_type not in ['percentage', 'fixed']: print("\n\t[ERROR] Invalid type."); pause_and_clear(); continue
                value = float(input(f"\tValue ({'%' if coupon_type=='percentage' else '$'}): "))
                COUPONS.append({'code': code, 'type': coupon_type, 'value': value, 'active': True}); print("\n\tCoupon added!")
                pause_and_clear()
            elif choice == 3:
                code = input("\tCoupon code to change: ").upper()
                coupon = next((c for c in COUPONS if c['code'] == code), None)
                if coupon:
                    coupon['active'] = not coupon['active']
                    print(f"\n\tStatus changed to {'ACTIVE' if coupon['active'] else 'INACTIVE'}.")
                else: print("\n\t[ERROR] Coupon not found.")
                pause_and_clear()
            elif choice == 0: break
        except ValueError: print("\n\t[ERROR] Invalid option."); pause_and_clear()

def support_menu_admin():
    while True:
        clear_screen()
        open_tickets = [t for t in TICKETS if t['status'] == 'Open']
        print(f"\n\t--- Customer Service (Admin) ---\n\tYou have {len(open_tickets)} open ticket(s).")
        print("\n\t1 - View/Reply to Open Tickets\n\t2 - View Full History\n\t0 - Back")
        try:
            choice = int(input("\n\t=> "))
            if choice == 1:
                clear_screen(); print("\n\t--- Open Tickets ---")
                if not open_tickets: print("\n\tNo open tickets."); pause_and_clear(); continue
                for ticket in open_tickets: print("\n\t" + "="*40 + f"\n\tID: {ticket['id']} | User: {ticket['user']}\n\tSubject: {ticket['subject']}\n\tMessage: {ticket['message']}")
                reply_id = int(input("\n\tID of the ticket to reply to (0 to go back): "))
                if reply_id == 0: continue
                target = next((t for t in open_tickets if t['id'] == reply_id), None)
                if target:
                    target['admin_response'] = input(f"\tYour response to ticket #{target['id']}: ")
                    target['status'] = 'Answered'
                    print("\n\tResponse sent!"); pause_and_clear()
                else: print("\n\t[ERROR] Invalid ID."); pause_and_clear()
            elif choice == 2:
                clear_screen(); print("\n\t--- Ticket History ---")
                if not TICKETS: print("\n\tNo tickets.")
                else:
                    for ticket in TICKETS:
                        print("\n\t" + "="*40 + f"\n\tID: {ticket['id']} | Status: {ticket['status']}\n\tSubject: {ticket['subject']}")
                        if ticket['admin_response']: print(f"\tResponse: {ticket['admin_response']}")
                wait_for_enter()
            elif choice == 0: break
        except ValueError: print("\n\t[ERROR] Invalid option."); pause_and_clear()

# ==============================================================================
# 6. INTERFACE AND MENUS FUNCTIONS
# ==============================================================================
def login_signup_menu():
    while True:
        clear_screen(); print("\n\tWelcome!\n\t1 - Login\n\t2 - Sign Up\n\t0 - Exit System")
        try:
            option = int(input("\n\t=> "))
            if option == 1:
                clear_screen(); print("\n\t--- Login Screen ---")
                user, password = input("\tLogin: "), input("\tPassword: ")
                if user in USERS and USERS[user]['password'] == password:
                    clear_screen(); print(f"\n\tWelcome, {user}."); pause_and_clear(); return user
                else: print("\n\t[ERROR] Invalid login or password."); pause_and_clear()
            elif option == 2:
                clear_screen(); print("\n\t--- Sign Up Screen ---")
                new_user = input("\tUsername: ")
                if new_user in USERS: print("\n\t[ERROR] User already exists.")
                elif not new_user: print("\n\t[ERROR] Username cannot be empty.")
                else:
                    new_password = input("\tPassword: ")
                    if new_password: USERS[new_user] = {'password': new_password, 'addresses': []}; print(f"\n\tUser '{new_user}' registered!")
                    else: print("\n\t[ERROR] Password cannot be empty.")
                pause_and_clear(3)
            elif option == 0: return None
        except ValueError: print("\n\t[ERROR] Invalid option."); pause_and_clear()

def main_menu(logged_in_user):
    while True:
        clear_screen(); print(f"\n\tUser: {logged_in_user}\n\tWhat do you want to do?")
        print("\t" + "="*45)
        print("\t1 - Catalog\n\t2 - Cart\n\t3 - Checkout\n\t4 - My Orders\n\t5 - Review Products\n\t6 - My Profile\n\t7 - Customer Support")
        if logged_in_user == 'admin':
            print("\t--- Administrator Panel ---")
            print("\t8 - Manage Products\n\t9 - Manage Coupons\n\t10 - Handle Tickets")
        print("\t" + "="*45 + "\n\t99 - Logout\n\t0 - Exit System\n" + "="*45)
        try:
            choice = int(input("\t=> "))
            if choice == 1: view_catalog_and_add()
            elif choice == 2: manage_cart()
            elif choice == 3: place_order(logged_in_user)
            elif choice == 4: check_orders(logged_in_user)
            elif choice == 5: add_review(logged_in_user)
            elif choice == 6: manage_profile(logged_in_user)
            elif choice == 7: customer_support_menu(logged_in_user)
            elif choice == 8 and logged_in_user == 'admin': manage_products_admin()
            elif choice == 9 and logged_in_user == 'admin': manage_coupons_admin()
            elif choice == 10 and logged_in_user == 'admin': support_menu_admin()
            elif choice == 99: CART.clear(); return 'logout'
            elif choice == 0: return 'exit'
        except ValueError: print("\n\t[ERROR] Invalid option."); pause_and_clear()

# ==============================================================================
# 7. MAIN EXECUTION BLOCK
# ==============================================================================
def main():
    while True:
        active_user = login_signup_menu()
        if active_user is None: break
        exit_command = main_menu(active_user)
        if exit_command == 'exit': break
    clear_screen()
    print("\n\tThank you for using the system. See you soon!\n")

if __name__ == "__main__":
    main()
