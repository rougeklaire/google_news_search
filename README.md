# google_news_search
CustomTkinter GUI to automatically search through keywords on Google News

DEMO:

https://github.com/rougeklaire/google_news_search/assets/83010974/77cb0bb4-4ab3-425d-bdf6-1236d63fa00c

Description:

I came across the task to search through a list of keywords on google news and wanted to automate it. Therefore I created a Python GUI using CustomTkinter, Tkinter and Selenium making use of checkboxes to choose certain keywords and search for them on Google News automatically, instead of manually entering each keyword. See screenshot below.

<img width="490" alt="GUI" src="https://github.com/rougeklaire/google_news_search/assets/83010974/1ce572a2-37fd-4951-bf65-8a693d56038d">

Any checkbox that is selected will be used to perform the Google News search. There's also the option to temporarily modify the search words and checkboxes through the textfield on the right. You can add new search words and the corresponding checkbox through simply adding a tab with the desired search word in the texfield on the right. You can also remove checkboxes and search words if you simply delete them from the textfield.

The search is now limited to Firefox. Geckodriver must be in the same directory as the script in order for the program to work properly. Other browsers can be added through changing the "geckodriver.exe" reference in the code to the desired selenium driver used by the respective browser. I will upload the geckodriver.exe used.

The searches are limited to 7day (or newer) old results on Google News and search is performed in English (GB). Both references can be changed through modifying the "search_string" within the code.

IMPORTANT:
In order to properly use the script, make sure Python3 is installed, run the "prerequisites.py" script and make sure the respective driver reference is correct in the code and the driver used (Geckodriver for Firefox, etc.) is in the same directory as the script.

