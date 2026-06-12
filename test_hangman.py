from hangman import has_player_won,get_word_progress,get_help_letter,get_available_letters,choose_help


def test_has_player_won():
    assert has_player_won("apple", ["a", "p", "l", "e","x","f"]) == True
    assert has_player_won("apple", []) == False
    assert has_player_won("apple", ["a", "p","r","e"]) == False


def test_get_word_progress():
    assert get_word_progress("apple",[]) == "*****"
    assert get_word_progress("apple",["a","l","y"]) == "a**l*"
    assert get_word_progress("apple",["m","n","o"]) == "*****"
    assert get_word_progress("apple",["a","l","p","e"]) == "apple"

def test_get_help_letter():
    assert get_help_letter("apple","abcdfghpqrlmn") == "a" or "l" or"p"
    assert get_help_letter("apple","abcdwtuvwxyz") == "a"

def test_get_available_letters():
    assert get_available_letters(['a','b','c','x','y','z']) == "defghijklmnopqrstuvw"
    assert get_available_letters([]) == "abcdefghijklmnopqrstuvwxyz"


