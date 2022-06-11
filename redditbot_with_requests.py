import requests
from requests.auth import HTTPBasicAuth
import click
from googletrans import Translator

@click.command()
@click.argument('post_url')
def main(post_url):
    r = requests.get(f'{post_url}.json', headers={'User-agent': 'comment translator bot (by /u/MrAySian)'}).json()
    translator = Translator()
    #print(r)
    #'''
    for i in range(len(r[1]['data']['children'])):
        print(f'Comment {i+1}:')

        print(translator.translate(r[1]['data']['children'][i]['data']['body'], dest='es').text)
    #'''


if __name__ == '__main__':
    main()