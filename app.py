import openai
import pandas as pd
import streamlit as st
import os
from langchain.chat_models import ChatOpenAI


os.environ["OPENAI_API_KEY"] = ""
llm_model = ChatOpenAI(model="gpt-3.5-turbo-0125",openai_api_key=os.getenv("OPENAI_API_KEY"),temperature=0.0)





# Function to generate product recommendations for a DataFrame
def generate_product_recommendations(users_df, behavior_col, products_df):
    recommendations = []

    customer_ids = users_df['Customer ID'].unique()

    for customer_id in customer_ids:
        customer_data = users_df[users_df['Customer ID'] == customer_id]
        customer_name = customer_data['Customer Name'].iloc[0]
        user_behavior = ', '.join(customer_data[behavior_col].astype(str))

        prompt = f"Based on the following customer's previous purchases, generate a tailored product recommendation from the company's product catalog, excluding any products the customer has already purchased, and considering the product's price. Provide the recommended product name, price, and the reason for the recommendation.\n\nCustomer Name: {customer_name}\nPrevious Purchases: {user_behavior}\n\nProduct Catalog:\n{products_df.to_string(index=False)}\n\nRecommendation:"
        support_template = """{question}"""
    # st.text(prompt)
        response = llm_model.predict(support_template.format(question=prompt))
        recommendation = response
        recommendations.append({
            'Customer ID': customer_id,
            'Customer Name': customer_name,
            'Previous Purchases': user_behavior,
            'Recommendation': recommendation
        })

    recommendations_df = pd.DataFrame(recommendations)
    return recommendations_df

# Streamlit app
    # Set up custom CSS
with open('style.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

st.title("SelectSavvy: Your Ultimate Product Matchmaker")

# Upload user data CSV
users_data = st.file_uploader("Upload User Data CSV", type="csv")

# Upload company products CSV
products_data = st.file_uploader("Upload Company Products CSV", type="csv")

if users_data is not None and products_data is not None:
    users_df = pd.read_csv(users_data)
    products_df = pd.read_csv(products_data)

    # Ensure 'Product', 'Price', 'Customer ID', and 'Customer Name' columns exist
    required_columns = ['Product', 'Price', 'Customer ID', 'Customer Name']
    if not all(col in users_df.columns for col in ['Customer ID', 'Customer Name']) or \
        not all(col in products_df.columns for col in ['Product', 'Price']):
        st.error("The CSV files should contain 'Customer ID', 'Customer Name', 'Product', and 'Price' columns.")
    else:
        user_columns = users_df.columns.tolist()
        behavior_col = st.selectbox("Select Behavior Column (Previous Purchases)", user_columns)

        if st.button("Generate Recommendations"):
            recommendations_df = generate_product_recommendations(users_df, behavior_col, products_df)
            st.write(recommendations_df)

