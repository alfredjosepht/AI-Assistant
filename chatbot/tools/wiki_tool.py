import wikipedia


def search_wikipedia(query):

    try:

        wikipedia.set_lang("en")

        # First search
        results = wikipedia.search(query)

        if not results:
            return "No results found."

        # Use first result
        page_title = results[0]

        summary = wikipedia.summary(
            page_title,
            sentences=3,
            auto_suggest=False
        )

        return summary

    except wikipedia.DisambiguationError as e:

        return f"Multiple matches found: {e.options[:5]}"

    except wikipedia.PageError:

        return "Page not found."

    except Exception as e:

        return f"Error: {e}"