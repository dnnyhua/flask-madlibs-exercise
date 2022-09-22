"""Madlibs Stories."""


class Story:
    """Madlibs story.

    To  make a story, pass a list of prompts, and the text
    of the template.

        >>> s = Story(["noun", "verb"],
        ...     "I love to {verb} a good {noun}.")

    To generate text from a story, pass in a dictionary-like thing
    of {prompt: answer, prompt:answer):

        >>> ans = {"verb": "eat", "noun": "mango"}
        >>> s.generate(ans)
        'I love to eat a good mango.'
    """

    def __init__(self, words, text):
        """Create story with words and template text."""

        self.placeholders = words
        self.template = text

    def generate(self, answers):
        """Substitute answers into text."""

        text = self.template

        # example if answers.items() was [("place", "Mars"), ("noun","dog"), ("adjective","happy"), ... ]
        for (key, val) in answers.items():
            # ie, replacing "place" with {place}, so that we can look for {place} in text to replace with val
            text = text.replace("{" + key + "}", val)

        # once all of the prompts in the text are replaced with val, we return the text
        return text


# Here's a story to get you started


story = Story(
    ["place", "noun", "verb", "adjective", "plural_noun"], # this is considered the placeholders
    """Once upon a time in a long-ago {place}, there lived a
       large {adjective} {noun}. It loved to {verb} {plural_noun}."""
)
