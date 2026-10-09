"""
HIT220 - Team 5 - Assignment 3 - Part II

Part II contains three main tasks:
1. Find the most common meaningful words and their counts.
2. Find and display phrases containing a search word ("word tree").
3. Find common 3-word phrases between two documents.

The shared processing functions below should be used by all three tasks so
that the whole program handles files, words, punctuation and case consistently.
"""

import re
from collections import Counter


# ---------------------------------------------------------------------------
# SHARED SETTINGS
# ---------------------------------------------------------------------------

# Add words from this list if they are insignificant.
STOP_WORDS = {
    "a", "an", "the", "and", "or", "but", "of", "to", "in", "on",
    "at", "for", "from", "with", "is", "are", "was", "were", "be",
    "been", "being", "it", "its", "this", "that", "these", "those"
}


# ---------------------------------------------------------------------------
# SHARED TEXT PROCESSING LAYER
# Everyone should use these functions so all three tasks process text
# in the same way.
# ---------------------------------------------------------------------------

def read_text_file(file_path):
    """Read and return the contents of one text file."""
    with open(file_path, "r", encoding="utf-8") as file:
        return file.read()


def split_into_sentences(text):
    """
    Split text into sentences.

    Sentence boundaries are kept at full stops, question marks and
    exclamation marks. Empty results are removed.
    """
    sentences = re.split(r"(?<=[.!?])\s+", text.strip())

    return [sentence.strip() for sentence in sentences if sentence.strip()]


def normalise_word(word):
    """
    Convert one word to lowercase and remove surrounding punctuation.

    Apostrophes inside words are kept, so a word such as "don't"
    remains one word.
    """
    match = re.search(r"[A-Za-z0-9]+(?:'[A-Za-z0-9]+)*", word.lower())

    if match is None:
        return ""

    return match.group(0)


def split_into_words(text):
    """
    Return a lowercase list of words from text.

    This uses the same word rules as normalise_word().
    """
    return re.findall(r"[A-Za-z0-9]+(?:'[A-Za-z0-9]+)*", text.lower())


def remove_stop_words(words, stop_words=STOP_WORDS):
    """Remove common words that are not important to the document meaning."""
    return [word for word in words if word not in stop_words]


def load_documents(file_paths):
    """
    Read several text files.

    Returns a dictionary where:
        key   = file path
        value = file contents
    """
    documents = {}

    for file_path in file_paths:
        documents[file_path] = read_text_file(file_path)

    return documents


# ===========================================================================
# TASK 1 - MOST COMMON KEYWORDS
# MEMBER: [INSERT NAME HERE]
# ===========================================================================

def analyse_keywords(file_paths, top_n=10):
    """
    TASK 1:
    Analyse documents for the most common meaningful words.

    Requirements:
    - Read the supplied document(s).
    - Remove insignificant/common words using STOP_WORDS.
    - Count the remaining words.
    - Return up to the 10 most common keywords and their counts.

    Suggested return format:
        [("algorithm", 8), ("data", 6), ...]

    [INSERT TASK 1 IMPLEMENTATION HERE]
    """

    # TODO: Replace this placeholder with the Task 1 implementation.
    raise NotImplementedError("Task 1 has not been implemented yet.")


# ===========================================================================
# TASK 2 - WORD TREE / SEARCH WORD CONTEXT
# MEMBER: [INSERT NAME HERE]
# ===========================================================================

def build_word_tree(file_paths, search_word):
    """
    TASK 2:
    Find all phrases containing a chosen search word.

    Assignment requirement:
    - Search term appears in the middle.
    - Select one word before and one word after.
    - All three words must come from the same sentence.
    - Display/list the results alphabetically.

    Suggested return format:
        [
            ("previous", "searchword", "next"),
            ("another", "searchword", "example")
        ]

    [INSERT TASK 2 IMPLEMENTATION HERE]
    """

    # TODO: Replace this placeholder with the Task 2 implementation.
    raise NotImplementedError("Task 2 has not been implemented yet.")


# ===========================================================================
# TASK 3 - COMMON 3-WORD PHRASES
# MEMBER: [INSERT NAME HERE]
# ===========================================================================

def find_common_phrases(file_path_1, file_path_2):
    """
    TASK 3:
    Find 3-word phrases that appear in both documents.

    Requirements:
    - Read two separate documents.
    - Create phrases containing exactly 3 consecutive words.
    - Store the phrases using an appropriate data structure.
    - Output all phrases that occur in both documents.

    Suggested return format:
        [
            "data structure example",
            "search tree algorithm"
        ]

    [INSERT TASK 3 IMPLEMENTATION HERE]
    """

    # TODO: Replace this placeholder with the Task 3 implementation.
    raise NotImplementedError("Task 3 has not been implemented yet.")


# ---------------------------------------------------------------------------
# OUTPUT HELPERS
# ---------------------------------------------------------------------------

def print_keywords(results):
    """Print Task 1 results."""
    print("\nMost common keywords:")

    for word, count in results:
        print(f"{word}: {count}")


def print_word_tree(results):
    """Print Task 2 results."""
    print("\nWord tree results:")

    for previous_word, search_word, next_word in results:
        print(f"{previous_word}  {search_word}  {next_word}")


def print_common_phrases(results):
    """Print Task 3 results."""
    print("\nCommon 3-word phrases:")

    for phrase in results:
        print(phrase)


# ---------------------------------------------------------------------------
# TESTING / MAIN PROGRAM
# ---------------------------------------------------------------------------

def main():
    test_file_1 = "document1.txt"
    test_file_2 = "document2.txt"

    print("HIT220 Assignment 3 - Part II")
    print("=" * 40)

    # -------------------------------------------------------
    # TASK 1 TEST
    # Uncomment when Task 1 has been implemented.
    # -------------------------------------------------------

    # keyword_results = analyse_keywords(
    #     [test_file_1, test_file_2]
    # )
    # print_keywords(keyword_results)

    # -------------------------------------------------------
    # TASK 2 TEST
    # Uncomment when Task 2 has been implemented.
    # -------------------------------------------------------

    # search_word = "algorithm"
    # word_tree_results = build_word_tree(
    #     [test_file_1, test_file_2],
    #     search_word
    # )
    # print_word_tree(word_tree_results)

    # -------------------------------------------------------
    # TASK 3 TEST
    # Uncomment when Task 3 has been implemented.
    # -------------------------------------------------------

    # common_phrase_results = find_common_phrases(
    #     test_file_1,
    #     test_file_2
    # )
    # print_common_phrases(common_phrase_results)


if __name__ == "__main__":
    main()
