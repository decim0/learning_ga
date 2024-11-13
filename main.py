import enchant

DICTIONARY = enchant.Dict("en_US")


class CaesarsCipher:
    """Класс представляет собой шифр Цезаря."""

    def __init__(self):
        self.alphabet: str = "ABCDEFGHIJKLMNOPQRSTUVWXYZ" \
                             "abcdefghijklmnopqrstuvwxyz1234567890 !?."

    def decrypt(self, message: str):
        """
        Расшифровывает сообщение с помощью шифра Цезаря.

        Args:
            message: Сообщение для расшифровки.
            key: Ключ.
            result: Расшифрованное сообщение.

        Returns:
            Расшифрованное сообщение.
        """
        key: int = self.find_key(message)
        result: str = "".join(self.shift_char(char, -key) for char in message)
        return result

    def encrypt(self, message: str):
        """
        Шифрует сообщение с помощью шифра Цезаря.

        Args:
            message: Сообщение для расшифровки.
            key: Ключ.
            result: Зашифрованное сообщение.

        Returns:
            str: Зашифрованное сообщение.
        """
        key: int = 21
        result: str = "".join(self.shift_char(char, key) for char in message)
        return result

    def find_key(self, message: str):
        """
        Поиск ключа для шифра Цезаря.

        Args:
            message: Сообщение для анализа.
            best_key: Лучший ключ.
            max_words: Максимальное количество корректных слов.
            decrypted: Дешифрованное сообщение.
            words: Дешифрованное сообщение, разбитое на слова.
            valid_words: Количество корректных слов в дешифрованном сообщении.

        Returns:
            Найденный ключ.
        """
        best_key: int = 0
        max_words: int = 0

        for key in range(len(self.alphabet)):
            decrypted: str = "".join(self.shift_char(char, -key)
                                     for char in message)
            words: list[str] = decrypted.split()
            valid_words: int = sum(
                1 for word in words if DICTIONARY.check(word))

            if valid_words > max_words:
                max_words = valid_words
                best_key = key

        return best_key

    def shift_char(self, char: str, shift: int):
        """
        Сдвигает символ на заданное количество позиций.

        Args:
            char: Символ для сдвига.
            shift: Количество позиций для сдвига.
            index: Индекс символа в алфавите.
            new_index: Новый индекс для сдвинутого символа.

        Returns:
            Сдвинутый символ.
        """
        if char in self.alphabet:
            index: int = self.alphabet.index(char)
            new_index: int = (index + shift) % len(self.alphabet)
            return self.alphabet[new_index]
        else:
            return char


if __name__ == "__main__":
    cipher = CaesarsCipher()

    message = "o3zR v..D0?yRA0R8FR8v47w0ER4.R1WdC!sLF5D"
    decrypted_message = cipher.decrypt(message)
    key = cipher.find_key(message)

    print(f"Подобранный ключ: {key}")
    print(f"Расшифрованное сообщение: {decrypted_message}")

    encrypted_message = cipher.encrypt(decrypted_message)
    print(encrypted_message)

    file_path = input("Укажите путь к файлу для записи: ")
    with open(file_path, "w") as file:
        file.write(f"Подобранный ключ: {key}")
        file.write(f"Расшифрованное сообщение: {decrypted_message}")