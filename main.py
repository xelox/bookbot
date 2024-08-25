def count_letters(book: str):
    letters = {}
    for b in book:
        if not b.isalpha():
            continue

        c = b.lower()
        if c in letters:
            letters[c] += 1
        else:
            letters[c] = 1
    return dict(sorted(letters.items(), reverse=True, key=lambda item: item[1]))

def main(): 
    path_to_file = "books/frankenstein.txt"
    with open(path_to_file) as f:
        file_contents = f.read()
        words = file_contents.split()
        letters = count_letters(file_contents)

        print("--- Begin report of books/frankenstein.txt ---") 
        print(f"{words} words found in the document")
        for [letter, count] in letters.items():
            print(f"The {letter} character was found {count} times")

main()
