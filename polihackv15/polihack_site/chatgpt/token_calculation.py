def return_token_price(text: str, token_price_raport=2.00) -> float:
    """
    Calculate the price of the token based on the text.
    :param text: The text to be analyzed.
    :param token_price_raport: The price of the token in comparison to an ai token. Default=2.00 (more expensive than ai token)
    :return: The price of the token.
    """
    # Tokenize the text
    tokenized_text = text.split()  # Split by whitespace
    # Remove empty tokens
    tokenized_text = [token for token in tokenized_text if token.strip() != ""]
    # separate punctuation from words and add them as separate tokens
    for i in range(len(tokenized_text)):
        tokenized_text[i] = ''.join([char if char.isalnum() else f" {char} " for char in tokenized_text[i]])
    tokenized_text = ' '.join(tokenized_text).split()
    print(tokenized_text)
    # Count the number of tokens
    num_tokens = len(tokenized_text)
    return num_tokens * token_price_raport


if (__name__ == "__main__"):
    print(return_token_price("Hello, how are you?"))  # Output: 12.00
