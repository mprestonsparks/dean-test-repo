# Code that needs comprehensive test coverage

def calculate_compound_interest(principal, rate, time, compounds_per_year=1):
    """
    Calculate compound interest using the formula A = P(1 + r/n)^(nt)
    
    Args:
        principal: Initial amount
        rate: Annual interest rate (as decimal)
        time: Time in years
        compounds_per_year: Number of times interest compounds per year
    
    Returns:
        Final amount after compound interest
    """
    if principal <= 0:
        raise ValueError("Principal must be positive")
    if rate < 0:
        raise ValueError("Interest rate cannot be negative")
    if time < 0:
        raise ValueError("Time cannot be negative")
    if compounds_per_year <= 0:
        raise ValueError("Compounds per year must be positive")
    
    amount = principal * (1 + rate / compounds_per_year) ** (compounds_per_year * time)
    return round(amount, 2)

def validate_email(email):
    """
    Basic email validation
    
    Args:
        email: Email string to validate
    
    Returns:
        bool: True if email is valid, False otherwise
    """
    if not email or not isinstance(email, str):
        return False
    
    if email.count('@') != 1:
        return False
    
    local, domain = email.split('@')
    
    if not local or not domain:
        return False
    
    if '.' not in domain:
        return False
    
    return True

class BankAccount:
    """
    Simple bank account class for testing
    """
    def __init__(self, account_number, initial_balance=0):
        self.account_number = account_number
        self.balance = initial_balance
        self.transaction_history = []
    
    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit amount must be positive")
        
        self.balance += amount
        self.transaction_history.append(f"Deposited: ${amount}")
        return self.balance
    
    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive")
        
        if amount > self.balance:
            raise ValueError("Insufficient funds")
        
        self.balance -= amount
        self.transaction_history.append(f"Withdrew: ${amount}")
        return self.balance
    
    def get_balance(self):
        return self.balance
    
    def get_transaction_history(self):
        return self.transaction_history.copy()

def process_shopping_cart(items):
    """
    Process shopping cart and calculate totals
    
    Args:
        items: List of dicts with 'name', 'price', 'quantity'
    
    Returns:
        dict: Cart summary with totals
    """
    if not items:
        return {"total": 0, "tax": 0, "final_total": 0, "item_count": 0}
    
    subtotal = 0
    item_count = 0
    
    for item in items:
        if not all(key in item for key in ['name', 'price', 'quantity']):
            raise ValueError("Each item must have name, price, and quantity")
        
        if item['price'] < 0 or item['quantity'] < 0:
            raise ValueError("Price and quantity must be non-negative")
        
        subtotal += item['price'] * item['quantity']
        item_count += item['quantity']
    
    tax_rate = 0.08  # 8% tax
    tax = subtotal * tax_rate
    final_total = subtotal + tax
    
    return {
        "subtotal": round(subtotal, 2),
        "tax": round(tax, 2),
        "final_total": round(final_total, 2),
        "item_count": item_count
    }

def fibonacci_sequence(n):
    """
    Generate fibonacci sequence up to n terms
    
    Args:
        n: Number of terms to generate
    
    Returns:
        list: Fibonacci sequence
    """
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    
    sequence = [0, 1]
    for i in range(2, n):
        sequence.append(sequence[i-1] + sequence[i-2])
    
    return sequence

if __name__ == "__main__":
    # Example usage - these need comprehensive tests
    print(f"Compound interest: {calculate_compound_interest(1000, 0.05, 2)}")
    print(f"Email valid: {validate_email('test@example.com')}")
    
    account = BankAccount("ACC123", 1000)
    account.deposit(500)
    account.withdraw(200)
    print(f"Account balance: {account.get_balance()}")
    
    cart = [
        {"name": "Item 1", "price": 10.99, "quantity": 2},
        {"name": "Item 2", "price": 5.50, "quantity": 1}
    ]
    print(f"Cart total: {process_shopping_cart(cart)}")
    
    print(f"Fibonacci: {fibonacci_sequence(10)}")