# main.py

from extractors import (
    extract_emails, extract_urls, extract_phone_numbers, 
    extract_credit_card_numbers, extract_time, extract_html_tags,
    extract_hashtags, extract_currency_amounts
)
from utils import read_sample_data

def main():
    # Read sample data from the file
    sample_data = read_sample_data('../sample_data.txt')  # Use relative path
    
    if not sample_data:
        return
    
    # Extract various types of data
    emails = extract_emails(sample_data)
    urls = extract_urls(sample_data)
    phone_numbers = extract_phone_numbers(sample_data)
    credit_card_numbers = extract_credit_card_numbers(sample_data)
    times = extract_time(sample_data)
    html_tags = extract_html_tags(sample_data)
    hashtags = extract_hashtags(sample_data)
    currencies = extract_currency_amounts(sample_data)

    # Display the extracted information
    print("Extracted Emails:")
    print(emails)
    print("\nExtracted URLs:")
    print(urls)
    print("\nExtracted Phone Numbers:")
    print(phone_numbers)
    print("\nExtracted Credit Card Numbers:")
    print(credit_card_numbers)
    print("\nExtracted Times:")
    print(times)
    print("\nExtracted HTML Tags:")
    print(html_tags)
    print("\nExtracted Hashtags:")
    print(hashtags)
    print("\nExtracted Currency Amounts:")
    print(currencies)

if __name__ == "__main__":
    main()