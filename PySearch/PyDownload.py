import validators

from svn.remote import RemoteClient

def download_folder(url):
    if 'tree/master' in url:
        url = url.replace('tree/master', 'trunk')

    r = RemoteClient(url)
    r.export('output')
    

if __name__ == '__main__':
    url = input('Enter folder url: ')
    if not validators.url(url):
        print('Invalid url')
    else:
        download_folder(url)
