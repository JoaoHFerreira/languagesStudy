import random

class LanguageTarget:
    LANGUAGES = [
        # "Lua", After a brief study about Lua, the conclusion was that I need to go slowly in programming language, I'll focus first in Go and Rust, when I felt more capable I'll add a new language.
        "Go",
        "Rust",
        # "Java",
        # "Scala",
        # "Clojure",
        # "C++",
        # "C"
    ]
    SPACE_CHAR = " "
    
    def show_language(self):
        print(self._choose_language())

    def _choose_language(self):
        base = len(self.LANGUAGES)
        language_index =  random.randint(0, base - 1)
        while self._is_language_previously_used(language_index):
            language_index =  random.randint(0, base - 1)

        self._write_language(language_index)
        return self.LANGUAGES[language_index], language_index

    def _is_language_previously_used(self, language_index):
        with open(".last_used_languages", "r") as file:
            used_languages = list(
                filter(None, file.read().split(self.SPACE_CHAR))
            )
        
        if len(used_languages) == len(self.LANGUAGES):
            self._clear_file()
            return False
        
        if self.LANGUAGES[language_index] in used_languages:
            return True
    
    def _clear_file(self):
        with open(".last_used_languages", "a") as file:
            file.truncate(0)
    
    def _write_language(self, language_index):
        with open(".last_used_languages", "a") as file:
            file.write(f"{self.SPACE_CHAR}{self.LANGUAGES[language_index]}")

if __name__ == "__main__":
    language_target = LanguageTarget()
    language_target.show_language()
    
    