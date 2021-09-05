from time import sleep

def printt(text):
    try:
        for char in text:
            sleep(0.1)
            print(char, end='', flush=True)
        print("")
    except:
        raise TypeError('No concat or colour at the moment!')