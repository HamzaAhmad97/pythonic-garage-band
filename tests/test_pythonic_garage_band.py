import pytest

from pythonic_garage_band.band import (
    Band,
    Musician,
    Guitarist,
    Bassist,
    Drummer,
)


@pytest.mark.skip("todo")
def test_guitarist_str():
    """
    test if the guitarist instance's string representation returns the correct value
    """
    joan = Guitarist("Joan Jett")
    actual = str(joan)
    expected = "My name is Joan Jett and I play guitar"
    assert actual == expected


@pytest.mark.skip("todo")
def test_guitarist_repr():
    """
    test if the string representation of a guitarist using repr returns the correct data
    """
    joan = Guitarist("Joan Jett")
    actual = repr(joan)
    expected = "Guitarist instance. Name = Joan Jett"
    assert actual == expected


@pytest.mark.skip("todo")
def test_drummer_str():
    """
    test if the Drummer instance's string representation returns the correct value
    """
    sheila = Drummer("Sheila E.")
    actual = str(sheila)
    expected = "My name is Sheila E. and I play drums"
    assert actual == expected


@pytest.mark.skip("todo")
def test_drummer_repr():
    """
    test if the string representation of a Drummer using repr returns the correct data
    """
    sheila = Drummer("Sheila E.")
    actual = repr(sheila)
    expected = "Drummer instance. Name = Sheila E."
    assert actual == expected


@pytest.mark.skip("todo")
def test_bassist_str():
    """
    test if the Bassist instance's string representation returns the correct value
    """
    meshell = Bassist("Meshell Ndegeocello")
    actual = str(meshell)
    expected = "My name is Meshell Ndegeocello and I play bass"
    assert actual == expected


@pytest.mark.skip("todo")
def test_bassist_repr():
    """
    test if the string representation of a Bassist using repr returns the correct data
    """
    meshell = Bassist("Meshell Ndegeocello")
    actual = repr(meshell)
    expected = "Bassist instance. Name = Meshell Ndegeocello"
    assert actual == expected


@pytest.mark.skip("todo")
def test_band_name():
    """
    test if a band name can be retrieved with no errors
    """
    nirvana = Band("Nirvana", [])

    assert nirvana.name == "Nirvana"


@pytest.mark.skip("todo")
def test_guitarist():
    """
    test the creation of a guitarist instance and for accessing its properties
    """
    jimi = Guitarist("Jimi Hendrix")
    assert jimi.name == "Jimi Hendrix"
    assert jimi.get_instrument() == "guitar"


@pytest.mark.skip("todo")
def test_bassist():
    """
    test the creation of a Bassist instance and for accessing its properties
    """
    flea = Bassist("Flea")
    assert flea.name == "Flea"
    assert flea.get_instrument() == "bass"


@pytest.mark.skip("todo")
def test_drummer():
    """
    test the creation of a Drummer instance and for accessing its properties
    """
    ginger = Drummer("Ginger Baker")
    assert ginger.name == "Ginger Baker"
    assert ginger.get_instrument() == "drums"


@pytest.mark.skip("todo")
def test_instruments(one_band):
    """
    test if we can get the instruments of all musician instances from the members of a band

    Args:
        one_band (Band): [a band instance]
    """
    instruments = ["guitar", "bass", "drums"]
    for i, member in enumerate(one_band.members):
        # NOTE: see stretch goal where zip used
        assert member.get_instrument() == instruments[i]


@pytest.mark.skip("todo")
def test_individual_solos(one_band):
    """
    test if the musician instances method get_instrument and play_solo return the correct data

    Args:
        one_band (Band): [a band instance]
    """
    for member in one_band.members:
        if member.get_instrument() == "guitar":
            assert member.play_solo() == "face melting guitar solo"
        elif member.get_instrument() == "bass":
            assert member.play_solo() == "bom bom buh bom"
        elif member.get_instrument() == "drums":
            assert member.play_solo() == "rattle boom crash"


@pytest.mark.skip("todo")
def test_band_members(one_band):
    """
    test a band instance member property

    Args:
        one_band (Band): [a band instance]
    """

    assert len(one_band.members) == 3

    assert isinstance(one_band.members[0], Musician)
    assert isinstance(one_band.members[0], Guitarist)
    assert one_band.members[0].name == "Kurt Cobain"

    assert isinstance(one_band.members[1], Musician)
    assert isinstance(one_band.members[1], Bassist)
    assert one_band.members[1].name == "Krist Novoselic"

    assert isinstance(one_band.members[2], Musician)
    assert isinstance(one_band.members[2], Drummer)
    assert one_band.members[2].name == "Dave Grohl"


@pytest.mark.skip("todo")
def test_play_solos_for_whole_band(one_band):
    """
    test a band instance's play_solos method

    Args:
        one_band (Band): [a band instance]
    """
    solos = one_band.play_solos()
    assert len(solos) == 3
    assert solos[0] == "face melting guitar solo"
    assert solos[1] == "bom bom buh bom"
    assert solos[2] == "rattle boom crash"


@pytest.mark.skip("todo")
def test_class_tracks_instances():
    """
    test the to_list method of a band instance
    """
    assert Band.to_list() == []
    the_nobodies = Band("The Nobodies", [])
    assert len(Band.instances) == 1
    assert Band.instances[0] == the_nobodies


@pytest.mark.skip("todo")
def test_to_list():
    """
    test the to_list method of a band instance
    """
    assert Band.to_list() == []
    the_nobodies = Band("The Nobodies", [])
    all_bands = Band.to_list()
    assert len(all_bands) == 1
    assert all_bands[0] == the_nobodies


#######################
# Fixtures
#######################


@pytest.fixture
def nirvana_data():
    """
    return a dictionary of data for creating a band instance

    Returns:
        dictionary: the name and data for creating musician instances for a band
    """
    return {
        "name": "Nirvana",
        "members": [
            {"name": "Kurt Cobain", "instrument": "Guitar"},
            {"name": "Krist Novoselic", "instrument": "Bass"},
            {"name": "Dave Grohl", "instrument": "Drums"},
        ],
    }


@pytest.fixture
def one_band():
    """
    create and return a band instnace

    Returns:
        Band: a music band having a name and a list of musicions
    """
    members = [
        Guitarist("Kurt Cobain"),
        Bassist("Krist Novoselic"),
        Drummer("Dave Grohl"),
    ]

    some_band = Band("Nirvana", members)

    return some_band


@pytest.fixture(autouse=True)
def clean():
    """runs before each test automatically.
    This is necessary because otherwise band instances added in one test
    will bleed over to other tests
    There's also a more advanced way to run code after each test as well
    Check the docs for that. Hint: it uses yield
    """
    Band.instances = []


#######################
# Stretch
#######################


# @pytest.mark.skip("stretch")
# def test_from_file():
#     with open("assets/bands.json") as f:
#         bands = json.loads(f.read())

#     assert len(bands) == 1

#     nirvana_data = bands[0]

#     nirvana = Band(nirvana_data["name"], nirvana_data["members"])

#     assert nirvana.name == "Nirvana"


# @pytest.mark.skip("stretch")
# def test_from_yaml():
#     bands = yaml.safe_load(open("assets/bands.yml"))

#     assert bands[0]["name"] == "Nirvana"

#     assert bands[1]["name"] == "The Pixies"


# @pytest.mark.skip("stretch")
# def test_abstract_musician():
#     with pytest.raises(TypeError):
#         Musician("nobody", "nothing", "silence")


# @pytest.mark.skip("stretch")
# def test_incomplete_keyboardist():
#     with pytest.raises(TypeError) as e:
#         Keyboardist("Booker T. Jones")

#     assert (
#         repr(e)
#         == """<ExceptionInfo TypeError("Can't instantiate abstract class Keyboardist with abstract method some_method_that_must_be_implemented_in_base_class") tblen=1>"""  # noqa: E501
#     )