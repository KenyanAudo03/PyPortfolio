from colorama import Fore
def load_bible():
    bible_data = {}
    current_book = ""
    current_chapter = 0
    current_verse = 0

    with open("bible_text.txt", "r", encoding="utf-8") as file:
        for line in file:
            line = line.strip()
            if line:
                parts = line.split(" ", 3)
                book, chapter_verse, verse_text = parts[0], parts[1], " ".join(parts[2:])
                
                if book != current_book:
                    current_book = book
                    bible_data[current_book] = {}
                    current_chapter = 0
                    current_verse = 0
                
                chapter, verse = map(int, chapter_verse.split(":"))
                
                if chapter != current_chapter:
                    current_chapter = chapter
                    current_verse = 0
                    bible_data[current_book][current_chapter] = []
                
                current_verse += 1
                bible_data[current_book][current_chapter].append((current_verse, verse_text))
    return bible_data

def display_verse(bible_data, book, chapter, verse):
    try:
        verse_text = next(verse_text for v, verse_text in bible_data[book][chapter] if v == verse)
        print(Fore.GREEN + f"{book} {chapter}:{verse}\t {verse_text}")
        print( Fore.WHITE)
    except KeyError:
        print("Verse not found.")

def main():
    bible_data = load_bible()

    book_input = input("Enter Book: ").strip()
    chapter = int(input("Enter Chapter: "))
    verse = int(input("Enter Verse: "))
    print()

    try:
        book = next(key for key in bible_data.keys() if key.lower().startswith(book_input.lower()))
        display_verse(bible_data, book, chapter, verse)
    except StopIteration:
        print(Fore.RED + "Book not found.")
while True:
    if __name__ == "__main__":
        main()
