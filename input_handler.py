def get_url():
    url = input("Enter Link: ")
    if ("https" or "http") in url:
        return url
    else:
        return "https://" + url
