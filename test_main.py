from main import main

def test_main_part1(capsys):
    main()
    captured = capsys.readouterr()
    assert captured.out == 'Bibliotheks-Anwendung\n=====================\n\nKunden:\nKunde: Moritz\nKunde: Ursula\n---\n'