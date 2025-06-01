import random
import string
from abc import ABC, abstractmethod

import nltk

nltk.download('words')


class PasswordGenerator(ABC):
    @abstractmethod
    def generate(self):
        pass


class PinGenerator(PasswordGenerator):
    def __init__(self, length):
        self.length = length

    def generate(self):
        return ''.join([random.choice(string.digits) for _ in range(self.length)])


class RandomPasswordGenerator(PasswordGenerator):
    def __init__(self, length: int = 8, include_numbers: bool = False, include_symbols: bool = False):
        self.length = length
        self.characters = string.ascii_letters
        if include_numbers:
            self.characters += string.digits

        if include_symbols:
            self.characters += string.punctuation

    def generate(self):
              return ''.join([random.choice(self.characters) for _ in range(self.length)])



class MemorablePasswordGenerator(PasswordGenerator):
    def __init__(
        self,
        num_of_words: int = 4,
        separator: str = '-' ,
        capitalization: bool = False,
        vocabulary: list = None
    ):

        if vocabulary is None:
            vocabulary = nltk.corpus.words.words()

        self.vocabulary = vocabulary
        self.num_of_words = num_of_words
        self.capitalization = capitalization
        self.separator = separator

    def generate(self):
        password_words = [random.choice(self.vocabulary) for _ in range(self.num_of_words)]
        if self.capitalization:
            password_words = [word.upper() if random.choice([True, False]) else word.lower() for word in password_words]

        return self.separator.join(password_words)


import random
import string
from abc import ABC, abstractmethod
import nltk

nltk.download('words', quiet=True)


class PasswordGenerator(ABC):
    @abstractmethod
    def generate(self):
        pass


class PinGenerator(PasswordGenerator):
    def __init__(self, length):
        self.length = length

    def generate(self):
        return ''.join([random.choice(string.digits) for _ in range(self.length)])


class RandomPasswordGenerator(PasswordGenerator):
    def __init__(self, length: int = 8, include_numbers: bool = False, include_symbols: bool = False):
        self.length = length
        self.characters = string.ascii_letters
        if include_numbers:
            self.characters += string.digits
        if include_symbols:
            self.characters += string.punctuation

    def generate(self):
        return ''.join([random.choice(self.characters) for _ in range(self.length)])


class MemorablePasswordGenerator(PasswordGenerator):
    def __init__(
        self,
        num_of_words: int = 4,
        separator: str = '-',
        capitalization: bool = False,
        vocabulary: list = None
    ):
        if vocabulary is None:
            vocabulary = nltk.corpus.words.words()
        self.vocabulary = vocabulary
        self.num_of_words = num_of_words
        self.capitalization = capitalization
        self.separator = separator

    def generate(self):
        password_words = [random.choice(self.vocabulary) for _ in range(self.num_of_words)]
        if self.capitalization:
            password_words = [word.upper() if random.choice([True, False]) else word.lower() for word in password_words]
        return self.separator.join(password_words)


def run_program():
    while True:
        print("\nChoose password type:")
        print("1 - Random Password")
        print("2 - PIN Code")
        print("3 - Memorable Password")

        choice = input("Enter choice (1/2/3): ")

        if choice == "1":
            length = int(input("Password length: "))
            include_numbers = input("Include numbers? (y/n): ").lower() == 'y'
            include_symbols = input("Include symbols? (y/n): ").lower() == 'y'
            generator = RandomPasswordGenerator(length, include_numbers, include_symbols)

        elif choice == "2":
            length = int(input("PIN length: "))
            generator = PinGenerator(length)

        elif choice == "3":
            num_words = int(input("How many words?: "))
            separator = input("Separator (default '-'): ") or "-"
            capitalization = input("Random capitalization? (y/n): ").lower() == 'y'
            generator = MemorablePasswordGenerator(num_words, separator, capitalization)

        else:
            print("Invalid choice. Try again.")
            continue

        print("\nGenerated password:")
        print(generator.generate())
        print("Done! ✅")

        again = input("\nDo you want to generate another password? (y/n): ").lower()
        if again != 'y':
            print("Goodbye 👋")
            break


if __name__ == "__main__":
    run_program()








