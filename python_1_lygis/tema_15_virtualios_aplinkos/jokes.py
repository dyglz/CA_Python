"""Module that uses the `pyjokes` package to generate random programming jokes."""

import pyjokes


def get_random_joke() -> str:
    """Returns a random programming joke."""
    return pyjokes.get_joke()


def get_random_joke_multilang(language: str = "en", category: str = "neutral") -> str:
    """Returns a random programming joke with the specified language and category."""
    try:
        return pyjokes.get_joke(language=language, category=category)
    except pyjokes.pyjokes.LanguageNotFoundError:
        return f"Error: Language '{language}' is not supported."
    except pyjokes.pyjokes.CategoryNotFoundError:
        return f"Error: Category '{category}' is not supported."
    except Exception as e:
        return f"Error: {e}"