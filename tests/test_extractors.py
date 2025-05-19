import unittest
from src.extractors import (
    extract_emails,
    extract_urls,
    extract_phone_numbers,
    extract_credit_card_numbers,
    extract_time,
    extract_html_tags,
    extract_hashtags,
    extract_currency_amounts,
)

class TestExtractors(unittest.TestCase):

    def test_extract_emails(self):
        test_string = "Contact us at user@example.com or firstname.lastname@company.co.uk."
        expected = ["user@example.com", "firstname.lastname@company.co.uk"]
        self.assertEqual(extract_emails(test_string), expected)

    def test_extract_urls(self):
        test_string = "Visit us at https://www.example.com or https://subdomain.example.org/page."
        expected = ["https://www.example.com", "https://subdomain.example.org/page"]
        self.assertEqual(extract_urls(test_string), expected)

    def test_extract_phone_numbers(self):
        test_string = "Call us at (123) 456-7890 or 123-456-7890 or 123.456.7890."
        expected = ["(123) 456-7890", "123-456-7890", "123.456.7890"]
        self.assertEqual(extract_phone_numbers(test_string), expected)

    def test_extract_credit_card_numbers(self):
        test_string = "My credit card numbers are 1234 5678 9012 3456 and 1234-5678-9012-3456."
        expected = ["1234 5678 9012 3456", "1234-5678-9012-3456"]
        self.assertEqual(extract_credit_card_numbers(test_string), expected)

    def test_extract_time(self):
        test_string = "The meeting is at 14:30 or 2:30 PM."
        expected = ["14:30", "2:30 PM"]
        self.assertEqual(extract_time(test_string), expected)

    def test_extract_html_tags(self):
        test_string = "<p>This is a paragraph.</p><div class='example'></div>"
        expected = ["<p>", "</p>", "<div class='example'>", "</div>"]
        self.assertEqual(extract_html_tags(test_string), expected)

    def test_extract_hashtags(self):
        test_string = "Here are some hashtags: #example, #ThisIsAHashtag."
        expected = ["#example", "#ThisIsAHashtag"]
        self.assertEqual(extract_hashtags(test_string), expected)

    def test_extract_currency_amounts(self):
        test_string = "The prices are $19.99 and $1,234.56."
        expected = ["$19.99", "$1,234.56"]
        self.assertEqual(extract_currency_amounts(test_string), expected)

if __name__ == '__main__':
    unittest.main()