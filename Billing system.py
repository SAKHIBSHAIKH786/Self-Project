#Billing system
import tkinter as tk
from tkinter import messagebox

class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class Invoice:
    def __init__(self, customer, products):
        self.customer = customer
        self.products = products
        self.total = 0

    def calculate_total(self):
        for product in self.products:
            self.total += product.price

class ProductManager:
    def __init__(self):
        self.products = []

    def add_product(self, name, price):
        self.products.append(Product(name, price))

    def display_products(self):
        return self.products

class BillingApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Offline Billing System")

        self.product_manager = ProductManager()
        self.products = []
        self.current_customer = None

        self.create_widgets()

    def create_widgets(self):
        # Product Management
        tk.Label(self.root, text="Product Management").grid(row=0, column=0, columnspan=2, pady=10)
        tk.Label(self.root, text="Product Name:").grid(row=1, column=0)
        tk.Label(self.root, text="Product Price:").grid(row=2, column=0)
        self.product_name_entry = tk.Entry(self.root)
        self.product_price_entry = tk.Entry(self.root)
        self.product_name_entry.grid(row=1, column=1)
        self.product_price_entry.grid(row=2, column=1)
        tk.Button(self.root, text="Add Product", command=self.add_product).grid(row=3, column=0, columnspan=2, pady=10)
        tk.Button(self.root, text="Display Products", command=self.display_products).grid(row=4, column=0, columnspan=2)

        # Customer Information
        tk.Label(self.root, text="Customer Information").grid(row=5, column=0, columnspan=2, pady=10)
        tk.Label(self.root, text="Name:").grid(row=6, column=0)
        tk.Label(self.root, text="Address:").grid(row=7, column=0)
        self.customer_name_entry = tk.Entry(self.root)
        self.customer_address_entry = tk.Entry(self.root)
        self.customer_name_entry.grid(row=6, column=1)
        self.customer_address_entry.grid(row=7, column=1)

        # Buttons
        tk.Button(self.root, text="Add Product to Invoice", command=self.add_product_to_invoice).grid(row=8, column=0, columnspan=2, pady=10)
        tk.Button(self.root, text="Generate Invoice", command=self.generate_invoice).grid(row=9, column=0, columnspan=2)

    def add_product(self):
        product_name = self.product_name_entry.get()
        product_price = float(self.product_price_entry.get())

        if product_name and product_price:
            self.product_manager.add_product(product_name, product_price)
            messagebox.showinfo("Product Added", f"{product_name} added.")
        else:
            messagebox.showwarning("Missing Information", "Please enter both product name and price.")

    def display_products(self):
        products = self.product_manager.display_products()
        if products:
            product_list = "\n".join([f"{product.name}: ${product.price}" for product in products])
            messagebox.showinfo("Product List", product_list)
        else:
            messagebox.showinfo("Product List", "No products available.")

    def add_product_to_invoice(self):
        if self.product_manager.products:
            product_name = self.product_name_entry.get()
            product_price = next((product.price for product in self.product_manager.products if product.name == product_name), None)

            if product_name and product_price is not None:
                self.products.append(Product(product_name, product_price))
                messagebox.showinfo("Product Added to Invoice", f"{product_name} added to the invoice.")
            else:
                messagebox.showwarning("Product Not Found", "The specified product was not found.")
        else:
            messagebox.showwarning("Product List Empty", "Please add products before adding them to the invoice.")

    def generate_invoice(self):
        customer_name = self.customer_name_entry.get()
        customer_address = self.customer_address_entry.get()

        if customer_name and customer_address and self.products:
            self.current_customer = Customer(customer_name, customer_address)
            invoice = Invoice(self.current_customer, self.products)
            invoice.calculate_total()

            messagebox.showinfo("Invoice Generated", f"Invoice total: ${invoice.total}")
        else:
            messagebox.showwarning("Missing Information", "Please enter customer information and add at least one product.")

if __name__ == "__main__":
    root = tk.Tk()
    app = BillingApp(root)
    root.mainloop()
