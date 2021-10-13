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

class Guitarist(Musician):
    """
    An class to represent a Guitarist.

    Attributes
    ----------
    name : string
        name of Guitarist
    INSTRUMENT : string (class attribute)
        guitar

    Methods
    -------
    play_solo():
        Returns a solo played by a Guitarist
    get_instrument():
        returns guitar
    """
    INSTRUMENT = 'guitar'

    def __init__(self, name):
        """
        The constructor method for the class Guitarist

        Parameters
        ----------
        name : string
                The name of the Guitarist
        """
        self.name = name

    def play_solo(self):
        """
        Return a solo played by the current Guitarist instance

        Returns
        -------
        string
            a solo played by a guitarist
        """
        return "face melting guitar solo"

    def get_instrument(self):
        """
        Return guitar

        Returns
        -------
        string
            the instrument, which is the guitar
        """
        return Guitarist.INSTRUMENT

    def __str__(self):
        """
        Return a string representation for a guitarist instance by str()

        Returns
        -------
        string
            Returns a string representation for a guitarist instance by str() print()

        """
        return f"My name is {self.name} and I play {Guitarist.INSTRUMENT}"

    def __repr__(self):
        """
        Return a string representation for a guitarist instance by repr()

        Returns
        -------
        string
            Returns a string representation for a guitarist instance by str() repr()

        """
        return f"Guitarist instance. Name = {self.name}"