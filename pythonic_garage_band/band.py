from abc import ABC, abstractmethod


class Musician(ABC):
    """
    An abstract class to represent a musician.

    Attributes
    ----------
    name : str
        name of band
    members : list
        members of the band

    Methods
    -------
    play_solos():
        Returns a list of solos by each member.
    to_list(cls):
        returns the prviously created band instances.
    """
    @abstractmethod
    def __str__(self):
        """
        Return a string representation for a Musician instance by str()

        Abstract method -> Override
        """
        pass

    @abstractmethod
    def __repr__(self):
        """
        Return a string representation for a Musician instance by str()

        Abstract method -> Override
        """
        pass

    @abstractmethod
    def get_instrument(self):
        """
        Return the instrument of a musician instance

        Abstract method -> Override
        """
        pass

    @abstractmethod
    def play_solo(self):
        """
        Return a solo played by a musician instance

        Abstract method -> Override
        """
        pass
