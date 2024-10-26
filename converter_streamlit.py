import streamlit as st
import requests

base_url = " https://marketdata.tradermade.com/api/v1/convert"
api_key = "fs6R3_ZUzsCKrCRF_r2Y"

# define the convert currency function


def convert_currency(amount, from_currency, to_currency):

    url = f"{base_url}?api_key={api_key}&from={from_currency}&to={to_currency}&amount={amount}"

    response = requests.get(url)

    if response.status_code == 200:

        rate = response.json()["quote"]

        print(rate)

        converted_amount = response.json()["total"]

        return rate, converted_amount

    else:

        return None, None


# define function that request currencies provided and use that to form a dropdown list

def fetch_supported_currencies():

    url = "https://marketdata.tradermade.com/api/v1/live_currencies_list?api_key=fs6R3_ZUzsCKrCRF_r2Y"

    response = requests.get(url)

    print(response)

    # Check if the request was successful

    if response.status_code == 200:

        currencies_data = response.json()

        if "available_currencies" in currencies_data:

            currencies = currencies_data["available_currencies"]

            return list(currencies.keys())

        else:

            st.write("Error: 'available_currencies' key not found in response.")

            return None

    else:

        st.write(f"Error {response.status_code}: {response.text}")

        return None

 # Define the Streamlit app for currency conversion


def currency_converter():

    # Input amount

    amount = st.number_input(
        "Enter an integer amount to convert:", value=100, step=1)

 # Fetch all supported currencies from the API

    supported_currencies = fetch_supported_currencies()

    if supported_currencies is not None:

        # Input 'from' currency

        from_currency = st.selectbox(
            "From currency:", supported_currencies, index=19)

        # Input 'to' currencies

        to_currencies = st.multiselect(
            "To currencies:", supported_currencies, default=["USD"])

        # Convert currency and display result

        if st.button("Convert"):

            st.write("Conversion results:")

            for to_currency in to_currencies:

                print(to_currency, from_currency)

                try:

                    rate, converted_amount = convert_currency(
                        amount, from_currency, to_currency)

                    if rate:

                        st.write(
                            f"{amount} {from_currency} = {converted_amount} {to_currency} - 1{from_currency} = {rate} {to_currency}")

                    else:

                        st.write(
                            f"Something Went Wrong Please Check with your API Provider")

                except:

                    st.write(
                        f"Error: Exchange rates not available for {from_currency} to {to_currency}.")

# Run the Streamlit app


if __name__ == "__main__":

    currency_converter()
