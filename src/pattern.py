# Tristan Protzman
# Created 2019-02-07
# Holds the note patters


class Pattern:
    def __init__(self, beats, subdivisions, notes):
        self.beats = beats  # How many beats per measure
        self.subdivisions = subdivisions  # How many divisions per beat
        self.divisions = self.beats * self.subdivisions  # Total divisions in pattern
        self.notes = notes  # How many different notes are in the patters
        self.pattern = [set() for _ in range(self.divisions)]  # Top level list, one entry per division

    def __str__(self):
        """
         Returns a printable representation of the current pattern state.
         A # represents the slot is active, a - means it isn't.
         Prints 1 line per pitch, doesn't print a line if it contains no active notes.
         Guaranteed to print at least one line if no notes are present in pattern

         :return: A multiline string representing the state
         :rtype: str
         """
        representation = ""
        for i in range(self.notes):
            line = "{:0=3d}| ".format(i)
            for j in range(self.divisions):
                if i in self.pattern[j]:
                    line += "# "
                else:
                    line += "- "
            if "#" in line:
                representation += line + "\n"
        if representation == "":
            representation = "000| " + self.divisions * "- "
        else:
            representation = representation[:-1]
        return representation

    def __repr__(self):
        """
        Returns a printable representation of the current pattern state.
        A # represents the slot is active, a - means it isn't.
        Prints 1 line per pitch, doesn't print a line if it contains no active notes.
        Guaranteed to print at least one line if no notes are present in pattern

        :return: A multiline string representing the state
        :rtype: str
        """
        return str(self)

    def add_note(self, note, div):
        """
        Adds the given note to the pattern.  Returns true if the note is allowed to be added, false otherwise.
        A note may be prevented from being added if it is outside the division range, outside the note range,
        or already exists.

        :param note: The note to add
        :param div: The division to place the note at
        :type note: int
        :type div: int
        :return: True if successful
        :rtype: bool
        """
        if note >= self.notes or note < 0:
            return False
        if div >= self.divisions or div < 0:
            return False
        if note in self.pattern[div]:
            return False
        self.pattern[div].add(note)
        return True

    def remove_note(self, note, div):
        """
        Removes the specified note from the pattern.  True if note is removed, false if it doesn't
        xists/can't be removed.

        :param note: The note to remove
        :param div: The division to remove it from
        :type note: int
        :type div: int
        :return: True if successful
        :rtype: bool
        """

        if note >= self.notes:
            return False
        if div >= self.divisions:
            return False
        if note not in self.pattern[div]:
            return False
        self.pattern[div].remove(note)
        return True

    def notes_at_div(self, div):
        """
        Returns the notes active at the specified division

        :param div: The division we want the active notes at
        :type div: int
        :return: The set of notes active at div
        :rtype: set
        """

        if self.divisions > div >= 0:
            return self.pattern[div]
        return None
