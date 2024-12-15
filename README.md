# 🛒 Amazon Price Tracker

## 🌟 Overview

The **Amazon Price Tracker** is a Python application that monitors the price of a specific product on Amazon. If the product's price drops below a user-defined target price, the application sends an email alert with the product details and a link to purchase.

## 🛠 Features
* **Web Scraping:** Extracts product information and current price from Amazon.
* **Email Alerts:** Sends an email notification when the product price falls below the target price.
* **Customizable Target Price:** Allows users to define the price threshold for notifications.
* **Automation-Ready:** Can be scheduled to run periodically for continuous monitoring.

## 📂 Project Structure

    .
    ├── main.py                 # Main Python script for the application
    ├── requirements.txt        # Project dependencies
    ├── README.md               # Project documentation

## 🔧 Setup Guide

**Prerequisites**

* Python 3.x installed.
* A valid SMTP server and email account for sending notifications.

**Installation**

1. Clone this repository:

    ```
    git clone https://github.com/matanohana433/amazon-price-tracker.git
    cd amazon-price-tracker
    ```

2. Create and activate a virtual environment (optional but recommended):

**Windows:**

    
    python -m venv venv
    venv\Scripts\activate
    

**macOS/Linux:**

    
    python3 -m venv venv
    source venv/bin/activate
    

3. Install dependencies:

    
    pip install -r requirements.txt
    

4. Set environment variables:

   * Create a `.env` file or set the variables manually:

    ```plaintext
    SMTP_ADDRESS=your_smtp_server_address
    EMAIL_ADDRESS=your_email_address
    EMAIL_PASSWORD=your_email_password
    ```

## 🚀 Usage

1. **Run the Application:**

    
    python main.py
    

2. **Product Monitoring:**

* The application fetches the product's current price from the provided Amazon link.
* If the price is below the defined `TARGET_PRICE`, an email alert is sent with the product details and a link to purchase.

## 🌟 Key Features

1. **Price Monitoring:**
   * Tracks the price of a product and compares it to a user-defined target.
2. **Email Notifications:**
   * Alerts users via email when the target price is met or exceeded.
3. **Web Scraping:**
   * Uses `BeautifulSoup` to extract data directly from the Amazon product page.

## 🚀 Future Enhancements

1. Add support for multiple products with individual target prices.
2. Extend functionality to track prices on other e-commerce platforms.
3. Implement a database to store product history and monitor trends.

## 📬 Contact

For questions or collaboration:

* **Email:** matanohana433@gmail.com
* **GitHub:** [matanohana433](https://github.com/matanohana433)