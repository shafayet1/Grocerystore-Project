from order_management_app.models import Category
from order_management_app.models import Supplier
from order_management_app.models import Product, Category, Supplier
from order_management_app.models import Customer

categories_data = [
    {'name': 'Fruits'},
    {'name': 'Vegetables'},
    {'name': 'Dairy'},
    {'name': 'Meat'},
    {'name': 'Beverages'},
    {'name': 'Bakery'},
    {'name': 'Snacks'},
    {'name': 'Frozen Foods'},
    {'name': 'Canned Goods'},
    {'name': 'Personal Care'}
]

for data in categories_data:
    Category.objects.create(**data)


suppliers_data = [
    {'name': 'Fresh Farms', 'contact_name': 'John Doe', 'phone': '123-456-7890', 'email': 'john@freshfarms.com', 'address': '123 Main St, City'},
    {'name': 'Green Gardens', 'contact_name': 'Jane Smith', 'phone': '987-654-3210', 'email': 'jane@greengardens.com', 'address': '456 Elm St, Town'},
    {'name': 'Dairy Delights', 'contact_name': 'Mike Johnson', 'phone': '555-123-4567', 'email': 'mike@dairydelights.com', 'address': '789 Oak Ave, Village'},
    {'name': 'Quality Meats', 'contact_name': 'Sam Brown', 'phone': '333-999-8888', 'email': 'sam@qualitymeats.com', 'address': '321 Pine St, Rural'},
    {'name': 'Soda Co.', 'contact_name': 'Sarah White', 'phone': '777-444-2222', 'email': 'sarah@sodaco.com', 'address': '555 Maple Blvd, Suburb'},
    {'name': 'Snack Shack', 'contact_name': 'Lisa Green', 'phone': '999-888-7777', 'email': 'lisa@snackshack.com', 'address': '777 Pine Ave, Town'},
    {'name': 'Frozen Foods Inc.', 'contact_name': 'Tom Adams', 'phone': '222-333-4444', 'email': 'tom@frozenfoods.com', 'address': '444 Oak St, Village'},
    {'name': 'Canned Goods Co.', 'contact_name': 'Emily Davis', 'phone': '666-555-4444', 'email': 'emily@cannedgoods.com', 'address': '666 Elm Ave, Rural'},
    {'name': 'Health & Beauty Supply', 'contact_name': 'Mark Taylor', 'phone': '888-999-0000', 'email': 'mark@healthbeauty.com', 'address': '999 Cedar Rd, Suburb'}
]

for data in suppliers_data:
    Supplier.objects.create(**data)


# Retrieve categories and suppliers
categories = Category.objects.all()
suppliers = Supplier.objects.all()

products_data = [
    {'name': 'Apple', 'category': categories[0], 'price': 1.50, 'quantity_in_stock': 100, 'supplier': suppliers[0]},
    {'name': 'Banana', 'category': categories[0], 'price': 1.00, 'quantity_in_stock': 150, 'supplier': suppliers[0]},
    {'name': 'Carrot', 'category': categories[1], 'price': 0.75, 'quantity_in_stock': 200, 'supplier': suppliers[1]},
    {'name': 'Milk', 'category': categories[2], 'price': 2.50, 'quantity_in_stock': 50, 'supplier': suppliers[2]},
    {'name': 'Chicken Breast', 'category': categories[3], 'price': 5.99, 'quantity_in_stock': 80, 'supplier': suppliers[3]},
    {'name': 'Orange Juice', 'category': categories[4], 'price': 3.00, 'quantity_in_stock': 120, 'supplier': suppliers[4]},
    {'name': 'Baguette', 'category': categories[5], 'price': 2.25, 'quantity_in_stock': 60, 'supplier': suppliers[5]},
    {'name': 'Potato Chips', 'category': categories[6], 'price': 1.99, 'quantity_in_stock': 100, 'supplier': suppliers[6]},
    {'name': 'Frozen Pizza', 'category': categories[7], 'price': 4.50, 'quantity_in_stock': 70, 'supplier': suppliers[7]},
    {'name': 'Canned Tomato Soup', 'category': categories[8], 'price': 1.25, 'quantity_in_stock': 90, 'supplier': suppliers[8]}
]

for data in products_data:
    Product.objects.create(**data)


customers_data = [
    {'first_name': 'Alice', 'last_name': 'Smith', 'address': '123 Apple St, City', 'phone': '111-222-3333', 'email': 'alice@example.com'},
    {'first_name': 'Bob', 'last_name': 'Johnson', 'address': '456 Banana Ave, Town', 'phone': '444-555-6666', 'email': 'bob@example.com'},
    {'first_name': 'Charlie', 'last_name': 'Brown', 'address': '789 Carrot Rd, Village', 'phone': '777-888-9999', 'email': 'charlie@example.com'},
    {'first_name': 'David', 'last_name': 'Lee', 'address': '321 Dairy Blvd, Rural', 'phone': '222-333-4444', 'email': 'david@example.com'},
    {'first_name': 'Eve', 'last_name': 'Taylor', 'address': '555 Meat St, Suburb', 'phone': '999-888-7777', 'email': 'eve@example.com'},
    {'first_name': 'Frank', 'last_name': 'Adams', 'address': '888 Bread Ave, City', 'phone': '333-444-5555', 'email': 'frank@example.com'},
    {'first_name': 'Grace', 'last_name': 'Clark', 'address': '444 Snack Rd, Town', 'phone': '666-777-8888', 'email': 'grace@example.com'},
]