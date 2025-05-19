def clean_input(data):
    """Cleans the input data by stripping unnecessary whitespace and normalizing line breaks."""
    return data.strip().replace('\r\n', '\n')

def validate_email(email):
    """Validates the format of an email address."""
    import re
    email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(email_regex, email) is not None

def validate_url(url):
    """Validates the format of a URL."""
    import re
    url_regex = r'^(https?://)?(www\.)?[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}(/.*)?$'
    return re.match(url_regex, url) is not None

def validate_phone_number(phone):
    """Validates the format of a phone number."""
    import re
    phone_regex = r'^\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}$'
    return re.match(phone_regex, phone) is not None

def validate_credit_card(card_number):
    """Validates the format of a credit card number."""
    import re
    card_regex = r'^\d{4}[-\s]?\d{4}[-\s]?\d{4}[-\s]?\d{4}$'
    return re.match(card_regex, card_number) is not None

def validate_time(time_str):
    """Validates the format of a time string in 12-hour or 24-hour format."""
    import re
    time_regex_24 = r'^(?:[01]\d|2[0-3]):[0-5]\d$'
    time_regex_12 = r'^(0?[1-9]|1[0-2]):[0-5]\d\s?[APap][mM]$'
    return re.match(time_regex_24, time_str) is not None or re.match(time_regex_12, time_str) is not None

def validate_hashtag(hashtag):
    """Validates the format of a hashtag."""
    import re
    hashtag_regex = r'^#[A-Za-z0-9_]+$'
    return re.match(hashtag_regex, hashtag) is not None

def validate_currency(amount):
    """Validates the format of a currency amount."""
    import re
    currency_regex = r'^\$?\d{1,3}(,\d{3})*(\.\d{2})?$'
    return re.match(currency_regex, amount) is not None

def read_sample_data(file_path):
    """Reads and returns data from a sample file."""
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return file.read()
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        return ""
    except Exception as e:
        print(f"Error reading file: {e}")
        return ""