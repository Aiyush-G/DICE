from time import sleep

def printt(text):
    """This is a typing effect which means that each letter is printed on the same line but with an arbitary time delay.

    Args:
        text (text): this is the text that should be printed out into the console.

    Raises:
        TypeError: this is incase the user tries to use the code in conjunction with colouringIDLE.py which can be found here:
        https://github.com/Aiyush-G/colouringIDLE 
        and:
        https://ooshimus.com/printing-colour-in-idle-in-less-than-2-minutes 
    """
    try:
        for char in text:
            sleep(0.1)
            print(char, end='', flush=True)
        print("")
    except:
        raise TypeError('No concat or colour at the moment!')