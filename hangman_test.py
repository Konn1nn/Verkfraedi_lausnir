import hangman

def test_hangman():
    input_values = ["HANGMAN","ABCDEFGHIJKLMNOPQRSTUVWXYZ", "BANANA","ABCDEFGHIJKLMNOPQRSTUVWXYZ", "RAINBOWS","USIANBVLOJRKWXZCTQGHPFMYDE"]
    output = []

    def mock_input():
        return input_values.pop(0)

    hangman.input = mock_input
    hangman.print = lambda s: output.append(s)

    hangman.main()
    hangman.main()
    hangman.main()

    assert output == [
        'WIN',
        'LOSE',
        'WIN',
    ]
