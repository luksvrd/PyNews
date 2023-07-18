# format_date() is a custom filter that recieves a datetime object & uses strftime() method to convert to a string.
def format_date(date):
    return date.strftime("%m/%d/%y")
# With virtual environment activated, run python app/utils/filters.py to directly run the script
# See the comand line output of the current date
from datetime import datetime
print(format_date(datetime.now()))

# This code removes all extraneous info form a URL string, leaving only the domain name
# Using replace() method to remove http://, https://, and www. from the URL
# Using split() method to split the URL at the first / or ? character
def format_url(url):
  return url.replace('http://', '').replace('https://', '').replace('www.', '').split('/')[0].split('?')[0]

# Uncomment lines 17/18 to test the format_url() function
# by running python app/utils/filters.py
# print(format_url('http://google.com/test/'))
# print(format_url('https://www.google.com?q=test'))

def format_plural(amount, word):
  if amount != 1:
    return word + 's'

  return word

# Address correctly pluralizing the word "Comment" in the comment count
def format_plural(amount, word):
  if amount != 1:
    return word + 's'

  return word

# Uncomment lines 34/35 to test the format_plural() function
# print(format_plural(2, 'cat'))
# print(format_plural(1, 'dog'))

