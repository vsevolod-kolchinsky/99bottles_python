class Entity:
    """Bottle(s) of beverage."""

    def __init__(
        self,
        amount: int,
        *,
        content: str = "beer",
        container_singular: str = "bottle",
        container_plural: str = "bottles",
    ) -> None:
        self._amount = amount
        self._content = content
        self._container_singular = container_singular
        self._container_plural = container_plural

    def __str__(self) -> str:
        return (
            f"{self._get_amount_representation(self._amount)} "
            f"{self._get_pluralization(self._amount)} of {self._content}"
        )

    def _get_amount_representation(self, amount: int) -> str:
        mapping = (
            (lambda: amount == 0, "no more"),
            (lambda: amount > 0, str(amount)),
        )
        for condition, result in mapping:
            if condition():
                return result
        raise NotImplementedError(f"Unable to represent amount properly: {amount=}")

    def _get_pluralization(self, amount: int) -> str:
        mapping = (
            (lambda: amount == 1, self._container_singular),
            (lambda: amount == 0 or amount > 1, self._container_plural),
        )
        for condition, result in mapping:
            if condition():
                return result
        raise NotImplementedError(f"Unable to pluralize properly: {amount=}")


class WhatYouHave:
    """Initial state on the wall."""

    def __init__(self, verse_number: int, *, where: str = "on the wall") -> None:
        self._verse_number = verse_number
        self._where = where
        self._entity = Entity(verse_number)

    def __str__(self) -> str:
        return f"{self._entity} {self._where}, {self._entity}."

    def __sub__(self, how_many: int) -> str:
        if self._verse_number >= how_many:
            new_number = self._verse_number - how_many
        else:
            new_number = 99
        new_entity = Entity(new_number)
        return f"{new_entity} {self._where}."


class Verse:
    """Song verse."""

    def __init__(self, verse_number: int) -> None:
        self._verse_number = verse_number
        self._what_you_have = WhatYouHave(verse_number)
        self._what_you_will_have = self._what_you_have - 1

    def __str__(self) -> str:
        return (
            f"{str(self._what_you_have).capitalize()}\n"
            f"{self._what_you_can_do(self._verse_number)}, "
            f"{self._what_you_will_have}\n"
        )

    def _get_amount_representation(self, amount: int) -> str:
        mapping = (
            (lambda: amount == 1, "it"),
            (lambda: amount > 0, "one"),
        )
        for condition, result in mapping:
            if condition():
                return result
        raise NotImplementedError(f"Unable to represent amount properly: {amount=}")

    def _what_you_can_do(self, amount: int) -> str:
        mapping = (
            (lambda: amount == 0, lambda: "Go to the store and buy some more"),
            (
                lambda: amount > 0,
                lambda: (
                    f"Take {self._get_amount_representation(self._verse_number)} "
                    "down and pass it around"
                ),
            ),
        )
        for condition, result_getter in mapping:
            if condition():
                return result_getter()
        raise NotImplementedError(f"What to do with {amount=}?")


class Bottles:
    """Song."""

    def verse(self, verse_number: int) -> str:
        """Given a verse number, creates a single verse

        Args:
            verse_number (int): What number verse of the song we are on

        Returns:
            str: The string representation of this verse
        """
        return str(Verse(verse_number))

    def verses(self, starting_verse: int, ending_verse: int) -> str:
        """Given a list of verse numbers, creates and attaches verses together

        Args:
            starting_verse (int): What verse to start on
            ending_verse (int): What verse to end on (inclusive)

        Returns:
            str: Verse attached together with a new line between them
        """
        return "\n".join(
            str(Verse(verse_number))
            for verse_number in self._get_range(starting_verse, ending_verse)
        )

    def song(self) -> str:
        """Creates the entire song of 99 bottles, from verse 99 to 0

        Returns:
            str: A string representation of 99 Bottles song
        """
        return self.verses(99, 0)

    def _get_range(self, starting_verse: int, ending_verse: int) -> range:
        return (
            range(starting_verse, ending_verse)
            if starting_verse < ending_verse
            else range(starting_verse, ending_verse - 1, -1)
        )
