"""Madlibs Stories."""


class Story:
    """Madlibs story.

    To  make a story, pass a list of prompts, and the text
    of the template.

        >>> s = Story(["noun", "verb"],
        ...     "I love to {verb} a good {noun}.")

    To generate text from a story, pass in a dictionary-like thing
    of {prompt: answer, promp:answer):

        >>> ans = {"verb": "eat", "noun": "mango"}
        >>> s.generate(ans)
        'I love to eat a good mango.'
    """

    def __init__(self, words, text):
        """Create story with words and template text."""

        self.prompts = words
        self.template = text

    def generate(self, answers):
        """Substitute answers into text."""

        text = self.template

        for (key, val) in answers.items():
            text = text.replace("{" + key + "}", val)

        return text


# Here's a story to get you started


story = Story(
    ["place", "noun", "verb", "adjective", "plural_noun"],
    """Once upon a time in a long-ago {place}, there lived a
       large {adjective} {noun}. It loved to {verb} {plural_noun}."""
)

the_gym = Story(["adjective", "adjective2", "bird_type", "room_in_a_house",
                "verb_past_tense", "verb", "relative_name", "noun",
                "liquid", "verb_ing", "plural_body_part", "plural_noun",
                "verb_ing2", "noun2"],

    """
    It was a {adjective}, cold November day. I woke up to the
    {adjective2} smell of {bird_type} roasting in the {room_in_a_house}
    downstairs. I {verb_past_tense} down the stairs to see if I couljd
    help {verb} the dinner. My mom said, \"See if {relative_name} needs
    a fresh {noun}.\" So I carried a tray of glasses full of {liquid} into
    the {verb_ing} room. When I got there, I couldn't believe my
    {plural_body_part}! There were {plural_noun} {verb_ing2} on the {noun2}
    """
)
