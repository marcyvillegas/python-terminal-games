def text_to_character(text: str, character: str, space_below=False) -> str:
    new_text = character * len(text)

    if space_below:
        return new_text + "\n"

    return new_text
