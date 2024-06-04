
# SelectSavvy: Your Ultimate Product Matchmaker

SelectSavvy is a Streamlit application that provides personalized product recommendations for customers based on their previous purchases. Leveraging the OpenAI GPT-3 language model, the app analyzes customer purchase history and suggests relevant products from the company's catalog while considering product prices and excluding already purchased items.

## Features

- Upload user data and company product data from CSV files
- Select the column for previous purchases from the user data CSV
- Generate tailored product recommendations for each customer
- Display recommendations with customer details, previous purchases, suggested product, product price, and reason for the recommendation

## Requirements

- Python 3.x
- OpenAI API key
- Streamlit library
- Pandas library

## Installation

1. Clone the repository or download the source code.
2. Install the required Python packages by running the following command:

   ```
   pip install openai pandas streamlit
   ```

3. Replace `"YOUR_API_KEY"` in the script with your actual OpenAI API key.
4. Ensure that the `style.css` file is in the same directory as the script.

## Usage

1. Run the SelectSavvy app by executing the following command in your terminal or command prompt:

   ```
   streamlit run app.py
   ```

2. The app will open in your default web browser.
3. Upload the user data CSV file containing columns for 'Customer ID', 'Customer Name', and the column for previous purchases (behavior).
4. Upload the company products CSV file containing columns for 'Product' and 'Price'.
5. Select the column for previous purchases from the dropdown menu.
6. Click the "Generate Recommendations" button.
7. The app will display a table with one row per customer, showing the customer ID, customer name, previous purchases, recommended product, recommended product price, and the reason for the recommendation.

## CSV File Format

### User Data CSV

The user data CSV file should contain the following columns:

- `Customer ID`: A unique identifier for each customer.
- `Customer Name`: The name of the customer.
- `Previous Purchases` (or any other column name): A column containing the previous purchases made by the customer, separated by commas.

### Company Products CSV

The company products CSV file should contain the following columns:

- `Product`: The name of the product.
- `Price`: The price of the product.

## Customization

You can customize the app's appearance by modifying the `style.css` file. The CSS file is used to style the Streamlit app with a blue theme, but you can change the colors and styles to suit your preferences.


![image](https://github.com/rohanmatt/Product-Recommendation/assets/77683536/0b9a6ebf-1c55-425e-abbf-3149bc31abc3)

![image](https://github.com/rohanmatt/Product-Recommendation/assets/77683536/a9b4b29d-8715-4777-b753-965737c72664)

![image](https://github.com/rohanmatt/Product-Recommendation/assets/77683536/6d0c726a-3d1a-4734-b394-b7693f6070a0)

![image](https://github.com/rohanmatt/Product-Recommendation/assets/77683536/ffc1a093-c029-494a-9dd1-fac9e96de32e)


![image](https://github.com/rohanmatt/Product-Recommendation/assets/77683536/434d5a79-0cba-44f5-b673-c4f2c1a260d9)


