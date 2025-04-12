import wikipedia

while True:
    search = input("Enter a page title or search phrase (or leave blank to exit): ")
    if not search:
        break  # Exit the loop if the input is blank

    try:
        page = wikipedia.page(search)
        print("Title:", page.title)
        print("Summary:", page.summary)
        print("URL:", page.url)
        print()
    except wikipedia.DisambiguationError as e:
        print("Disambiguation error.  Multiple pages match your search.  Please be more specific.")
        for i, option in enumerate(e.options, start=1):
            print(f"{i}. {option}")
        print()  # Added a newline for better readability

    except wikipedia.PageError:
        print("Wikipedia page not found. Please check your spelling or try a different search term.")
        print()
    except wikipedia.exceptions.HTTPTimeoutError:
        print("Request timed out. Please check your internet connection and try again.")
        print()
    except Exception as e: # Catch other unexpected errors
        print(f"An unexpected error occurred: {e}")
        print()