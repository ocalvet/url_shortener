class UrlShortenere(object):
    def shorten(self, url):
        parts = len(url) / 6
        letter_codes = [ord(letter) for letter in url]
        print(letter_codes)


if __name__ == '__main__':
    shortener = UrlShortenere()
    shortener.shorten('http://localhost:600')
