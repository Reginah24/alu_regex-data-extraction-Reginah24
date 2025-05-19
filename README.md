# Regex Data Extraction Project

## Overview

This project implements a set of regular expressions to extract various data types from text. It was created as part of the ALU Regex Onboarding Hackathon to demonstrate the power of regular expressions for data extraction.

## Features

The project can extract the following data types from text:

1. **Email addresses** - Extracts valid email formats like:

   - user@example.com
   - firstname.lastname@company.co.uk

2. **URLs** - Extracts web URLs including:

   - https://www.example.com
   - https://subdomain.example.org/page

3. **Phone numbers** - Extracts phone numbers in formats:

   - (123) 456-7890
   - 123-456-7890
   - 123.456.7890

4. **Credit card numbers** - Extracts card numbers in formats:

   - 1234 5678 9012 3456
   - 1234-5678-9012-3456

5. **Time** - Extracts time in both 12-hour and 24-hour formats:

   - 14:30 (24-hour format)
   - 2:30 PM (12-hour format)

6. **HTML tags** - Extracts HTML tags like:

   - `<p>`
   - `<div class="example">`
   - `<img src="image.jpg" alt="description">`

7. **Hashtags** - Extracts hashtags like:

   - #example
   - #ThisIsAHashtag

8. **Currency amounts** - Extracts currency values:
   - $19.99
   - $1,234.56

## Project Structure

```
alu_regex-data-extraction-project/
├── src/
│   ├── extractors.py    # Contains functions to extract data using regex
│   ├── utils.py         # Contains utility functions and validation methods
│   └── main.py          # Main script to run the program
├── sample_data.txt      # Sample test data
└── README.md            # Project documentation
```

## How to Run

1. Clone the repository
2. Navigate to the src directory:
   ```
   cd alu_regex-data-extraction-project/src
   ```
3. Run the main script:
   ```
   python3 main.py
   ```

## Regex Patterns Explained

### Email Pattern

```python
r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
```

- Matches username part with allowed characters
- Followed by @ symbol
- Followed by domain with at least one subdomain
- Domain ends with at least 2 letter TLD (.com, .org, etc.)

### URL Pattern

```python
r'https?://[^\s]+'
```

- Matches http or https protocol
- Followed by ://
- Captures everything until whitespace

### Phone Number Pattern

```python
r'\(?\d{3}\)?[-.\s]\d{3}[-.\s]\d{4}|\(\d{3}\)\s\d{3}-\d{4}|\d{3}-\d{3}-\d{4}|\d{3}\.\d{3}\.\d{4}'
```

- Matches various phone number formats including parentheses, dots, and hyphens
- Captures area codes and separators in different styles

### Credit Card Pattern

```python
r'\b(?:\d{4}[-\s]?){3}\d{4}\b'
```

- Matches 16-digit numbers in groups of 4
- Allows spaces or hyphens as separators
- Uses word boundaries to ensure complete card numbers

### Time Pattern

```python
r'(\b[01]?\d:[0-5]\d\s?[AP]M\b|\b[0-2]?\d:[0-5]\d\b)'
```

- First part matches 12-hour format with AM/PM
- Second part matches 24-hour format
- Validates hours and minutes ranges

### HTML Tag Pattern

```python
r'<[^>]+>'
```

- Matches anything between < and >
- Captures complete HTML tags including attributes

### Hashtag Pattern

```python
r'#[\w]+'
```

- Matches # followed by word characters (letters, numbers, underscore)

### Currency Pattern

```python
r'\$\d{1,3}(?:,\d{3})*(?:\.\d{2})?'
```

- Matches dollar sign followed by numbers
- Supports thousands separators (commas)
- Optional decimal part with cents

## Future Improvements

- Add more validation for extracted data
- Implement more robust error handling
- Create unit tests for each regex pattern
- Support additional data formats and currencies
- Improve performance for large text processing

## Author

Regina Anthony Majura

## License

This project is open source and available under the [MIT License](LICENSE).
