def text_to_character(text: str, character: str, space_below=False) -> str:

    if space_below:
        new_text = character * len(text)
        return new_text + "\n"

    return character * len(text)
