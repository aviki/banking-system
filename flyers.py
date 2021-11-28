import sys


def fly_sound(flyer: str):
    """
    Print the sound of flying objects.

    >>> fly_sound("airplane")
    airplane: wroom
    >>> fly_sound("duck")
    duck: flap flap
    >>> fly_sound("helicopter")
    helicopter: chop chop
    """
    flyer_sounds = {
        'airplane': 'wroom',
        'duck': 'flap flap',
        'helicopter': 'chop chop'
    }
    sound = flyer_sounds[flyer]
    print(f"{flyer}: {sound}")


def main():
    try:
        flyer = sys.argv[1]
    except IndexError:
        flyer = 'duck'
    finally:
        fly_sound(flyer)


if __name__ == '__main__':
    import doctest
    doctest.testmod()

    main()
