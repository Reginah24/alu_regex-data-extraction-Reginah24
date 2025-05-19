def extract_emails(text):
    """
    Extract all email addresses from the given text.
    
    The regex pattern matches standard email formats with:
    - Alphanumeric characters, dots, underscores, percent signs, plus and minus signs in the username
    - @ symbol
    - Domain name with letters, numbers, dots, and hyphens
    - TLD with at least 2 characters
    
    Args:
        text (str): The text to search for email addresses
        
    Returns:
        list: List of extracted email addresses
    """
    import re
    email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
    return re.findall(email_pattern, text)

def extract_urls(text):
    """
    Extract all URLs from the given text.
    
    The regex pattern matches HTTP and HTTPS URLs including:
    - http:// or https:// protocol
    - Domain and any path that follows
    - Stops at whitespace
    
    Args:
        text (str): The text to search for URLs
        
    Returns:
        list: List of extracted URLs
    """
    import re
    url_pattern = r'https?://[^\s]+'
    return re.findall(url_pattern, text)

def extract_phone_numbers(text):
    """
    Extract all phone numbers from the given text.
    
    The regex pattern matches these formats:
    - (123) 456-7890
    - 123-456-7890
    - 123.456.7890
    
    Args:
        text (str): The text to search for phone numbers
        
    Returns:
        list: List of extracted phone numbers
    """
    import re
    # This pattern strictly matches the three formats specified in requirements
    phone_pattern = r'\(?\d{3}\)?[-.\s]\d{3}[-.\s]\d{4}|\(\d{3}\)\s\d{3}-\d{4}|\d{3}-\d{3}-\d{4}|\d{3}\.\d{3}\.\d{4}'
    return re.findall(phone_pattern, text)

def extract_credit_card_numbers(text):
    """
    Extract all credit card numbers from the given text.
    
    The regex pattern matches 16-digit card numbers in formats:
    - 1234 5678 9012 3456 (with spaces)
    - 1234-5678-9012-3456 (with hyphens)
    - 1234567890123456 (without separators)
    
    Args:
        text (str): The text to search for credit card numbers
        
    Returns:
        list: List of extracted credit card numbers
    """
    import re
    credit_card_pattern = r'\b(?:\d{4}[-\s]?){3}\d{4}\b'
    return re.findall(credit_card_pattern, text)

def extract_time(text):
    """
    Extract all time references from the given text.
    
    The regex pattern matches:
    - 24-hour format (e.g., 14:30)
    - 12-hour format with AM/PM (e.g., 2:30 PM)
    
    Args:
        text (str): The text to search for time formats
        
    Returns:
        list: List of extracted time strings
    """
    import re
    time_pattern = r'(\b[01]?\d:[0-5]\d\s?[AP]M\b|\b[0-2]?\d:[0-5]\d\b)'
    return re.findall(time_pattern, text)

def extract_html_tags(text):
    """
    Extract all HTML tags from the given text.
    
    The regex pattern matches anything between < and > symbols,
    capturing both opening and closing tags with all attributes.
    
    Args:
        text (str): The text to search for HTML tags
        
    Returns:
        list: List of extracted HTML tags
    """
    import re
    html_pattern = r'<[^>]+>'
    return re.findall(html_pattern, text)

def extract_hashtags(text):
    """
    Extract all hashtags from the given text.
    
    The regex pattern matches:
    - # symbol followed by word characters (letters, numbers, underscores)
    
    Args:
        text (str): The text to search for hashtags
        
    Returns:
        list: List of extracted hashtags
    """
    import re
    hashtag_pattern = r'#[\w]+'
    return re.findall(hashtag_pattern, text)

def extract_currency_amounts(text):
    """
    Extract all currency amounts from the given text.
    
    The regex pattern matches:
    - Dollar amounts with $ symbol
    - Optional commas as thousands separators
    - Optional decimal point with cents
    
    Args:
        text (str): The text to search for currency amounts
        
    Returns:
        list: List of extracted currency amounts
    """
    import re
    currency_pattern = r'\$\d{1,3}(?:,\d{3})*(?:\.\d{2})?'
    return re.findall(currency_pattern, text)