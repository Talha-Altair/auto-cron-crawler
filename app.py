from cpu_stress import stress
from scraper import get_data

def startpy():

    get_data()

    stress()

if __name__ == '__main__':

    startpy()