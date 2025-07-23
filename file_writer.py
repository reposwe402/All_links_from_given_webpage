def save_links(links, filename="myLinks.txt"):
    # Writing the output to a file (myLinks.txt) instead of to stdout
    # You can change 'a' to 'w' to overwrite the file each time
    with open(filename, 'a') as saved:
        print(links[:10], file=saved)
