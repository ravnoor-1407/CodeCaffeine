# ☕ CodeCaffeine

![Python](https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python&logoColor=white)
![Status](https://img.shields.io/badge/Status-Active-success?style=for-the-badge)


## 📖 About
**CodeCaffeine** is a terminal-based Cafe Management System built using Python. It simulates a real-world cafe ordering experience, allowing users to browse a complex, categorized menu, place orders, calculate totals, and select dining preferences. 
This project was created to demonstrate the practical application of fundamental Python programming concepts, specifically focusing on data structure manipulation and logic flow.


## 🧠 Prerequisite Knowledge
To understand the codebase, the reader should be familiar with the following concepts:
* **Basic Python Syntax:** Variable assignment and print statements.
* **Data Structures:** Understanding how Dictionaries (`{}`) work, specifically Key-Value pairs.
* **Control Structures:** Basic knowledge of loops (`for`) and conditionals (`if/else`).
* **Terminal/Console:** How to run a Python script and interact with command-line inputs.


## 🚀 Features
* **Interactive Menu:** clearly displays a multi-level menu (Beverages > Hot Coffees > Item).
* **Smart Search Logic:** The system searches through nested categories to find items, regardless of where they are located in the menu.
* **Automated Billing:** Automatically calculates and updates the total bill in INR (₹) as items are added.
* **Availability Checks:** Validates if an item exists in the menu and notifies the user if it doesn't.
* **Workflow Simulation:** simulate the full customer journey: Greeting → Ordering → Payment Method → Dining Preference → Closing.


## 🛠️ Technical Python Concepts
This project implements several core Python concepts:

### 1. Nested Dictionaries
The menu is not a simple list; it is a dictionary containing other dictionaries. This models real-world hierarchical data.
* *Usage:* `menu = { "Category": { "Subcategory": { "Item": Price } } }`

### 2. Nested Loops (Iterative Logic)
To access the items deep inside the nested dictionaries, the program uses loops inside of loops.
* *Usage:* Iterating through Categories → then Subcategories → then Items to display the menu or search for a user's order.

### 3. Control Flow (If/Elif/Else)
The program makes decisions based on user input.
* *Usage:* Determining if a user wants "Dine In" vs "Take Away", or checking if an item was found (`if found:`).

### 4. F-String Formatting
Used for clean, dynamic string output.
* *Usage:* `print(f"{item}: ₹{price}")` inserts the variable values directly into the text.

### 5. Boolean Flags
Used to manage the state of the search.
* *Usage:* The variable `found = False` is used to track whether an ordered item has been located in the menu loop.


## 📂 Project Structure
The core data structure relies on a deep nesting strategy. Here is a simplified view of the data schema:

```text
CodeCaffeine/
├── main.py          # The primary script containing logic and data
└── README.md        # Project documentation
```

**Data Schema inside main.py:
```text
menu = {
    "Beverages": {
        "Hot Coffees": { ... },
        "Cold Coffees": { ... }
    },
    "Food": {
        "Breakfast": { ... },
        "Snacks": { ... }
    }
}
```

## 💻 How to Run the Project
### 1. Clone the Repository
   ```bash
   git clone [https://github.com/your-username/CodeCaffeine.git](https://github.com/your-username/CodeCaffeine.git)
   ```
### 2. Navigate to the Directory
   ```bash
   cd CodeCaffeine
   ```
### 3. Run the Script
   ```bash
   python main.py
   ```
### 4. Interact: Follow the prompts in the terminal to place your order.


## 🎓 What I Learnt
Building CodeCaffeine helped me understand:
* **Data Modeling:** How to structure complex information (like a cafe menu) using Python dictionaries rather than simple lists.
* **Algorithm Logic:** How to write search algorithms that can traverse multiple layers of data to find a specific value.
* **User Experience (UX):** The importance of clear print statements and input prompts to guide the user through a terminal application.
* **State Management:** Keeping track of running totals (order_total) throughout the lifecycle of the program.


## 🤝 Contributing
Contributions are welcome! If you have ideas for improvements (like adding a GUI or a database):
 1. Fork the repository.
 2. Create a new branch (git checkout -b feature-branch).
 3. Commit your changes.
 4. Push to the branch.
 5. Open a Pull Request.


## 👤 Author

~ Ravnoor Kaur 

[![GitHub](https://img.shields.io/badge/GitHub-ravnoor--1407-181717?style=for-the-badge&logo=github)](https://github.com/ravnoor-1407)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-0077B5?style=for-the-badge&logo=linkedin)](https://www.linkedin.com/in/ravnoor-kaur-rk2007)
