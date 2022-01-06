class TestEnterString:
    def test_check_symbols(self):
        phrase = input("Введите фразу: ")
        assert len(phrase) < 15, f"Фраза длиннее 15 символов. Введите фразу короче 15 символов."
        print(f"В фразе '{len(phrase)}' символов")
