...
Write a program to check whether the given character is vowel or consonant.
Input format:
The input consist of a character
Output format:
The output consists of a below-given string
“Vowel” / “Consonant” / “Not an alphabet”
Sample Input:
e

Sample Output:
Vowel
...


def check_character(character):
    vowels = "aeiouAEIOU"  # List of vowels
    if character.isalpha():  # Check if the character is an alphabet
        if character in vowels:
            return "Vowel"
        else:
            return "Consonant"
    else:
        return "Not an alphabet"


def main():
   
    character = input().strip()  # Remove any extra spaces
    
 
    if len(character) == 1:
        result = check_character(character)
        print(result)
    else:
        print("Not an alphabet")  # In case of more than one character


if __name__ == "__main__":
    main()
