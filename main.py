class Bottles:
    def verse(self, verse_number: int) -> str:
        """Given a verse number, creates a single verse

        Args:
            verse_number (int): What number verse of the song we are on

        Returns:
            str: The string representation of this verse
        """
        return ''


    def verses(self, *verse_numbers: int) -> str:
        """Given a list of verse numbers, creates and attaches verses together

        Args:
            verse_numbers (int, int, int...): Any number of verse numbers

        Returns:
            str: Verse attached together with a new line between them
        """
        return ''


    def song(self) -> str:
        """Creates the entire song of 99 bottles, from verse 99 to 0

        Returns:
            str: A string representation of 99 Bottles song
        """
        return ''
