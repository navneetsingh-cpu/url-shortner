import streamlit as st
from pyshorteners import Shortener


def main():
    st.title("URL Shortener")
    long_url = st.text_input("Enter the URL")
    if st.button("Shorten"):
        s = Shortener()
        short_url = s.tinyurl.short(long_url)
        st.success(f"Shortened URL is: {short_url}")


if __name__ == "__main__":
    main()
