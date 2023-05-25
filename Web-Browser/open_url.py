# a simple web script to open up the urls that I need to check on daily basis
import webbrowser
# we need to find chrome location on our device
chrome_path = "C:/Program Files/Google/Chrome/Application/chrome.exe"

# Register Chrome as the browser
webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chrome_path))
# list urls I need to check
url_list = ["your urls go here" ]

for url in url_list:
    # we use get chrome to be able to use google chrome, and add the urls we want as tabs
    webbrowser.get('chrome').open_new_tab("http://" + url)
