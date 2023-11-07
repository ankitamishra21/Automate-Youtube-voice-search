from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import speech_recognition as sr

def voice_search_youtube(search_query):
    # Initialize the Chrome WebDriver
    driver = webdriver.Chrome()

    # Open the YouTube website
    driver.get("https://www.youtube.com")

    # Find the search bar element and input the search query
    search_box = driver.find_element_by_name("search_query")
    search_box.send_keys(search_query)

    # Submit the search query by pressing Enter
    search_box.send_keys(Keys.RETURN)

    # Wait for the search results to load
    driver.implicitly_wait(10)

    # Close the browser (you can comment out this line to keep the browser open)
    driver.quit()

def main():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Please say your YouTube search query...")
        audio = recognizer.listen(source)

    try:
        search_query = recognizer.recognize_google(audio)
        print("You said:", search_query)

        voice_search_youtube(search_query)

    except sr.UnknownValueError:
        print("Sorry, I could not understand your voice.")

if __name__ == "__main__":
    main()
    
    


