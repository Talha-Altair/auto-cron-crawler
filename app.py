from cpu_stress import stress
from scraper import get_data as invoke_crawler

def startpy():

    invoke_crawler()

    stress()

if __name__ == '__main__':

    startpy()