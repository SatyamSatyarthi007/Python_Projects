import pyshorteners

url = input("Enter the URL to shorten: ")

print("Shortening URL...", pyshorteners.Shortener().tinyurl.short(url))
print("URL shortened successfully!")