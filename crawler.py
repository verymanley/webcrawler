#webcrawler v0.01

# page = contents of a web page
page = ('<div class="udacity float-left"><a href="http://udacity.com">')
start_link = page.find('<a href=')
start_quote = page.find('"',start_link)
end_quote = page.find('"',start_quote+1)
url = page[start_quote+1:end_quote]
print url

def get_next_target(page):
    start_link = page.find('<a href=')

    # if the link tag sequence is not found, find returns a -1
    if start_link == -1:
        # return the error codes of None, 0 now and skip the rest!
        return None, 0

    start_quote = page.find('"', start_link)
    end_quote = page.find('"', start_quote + 1)
    url = page[start_quote + 1:end_quote]
    return url, end_quote
