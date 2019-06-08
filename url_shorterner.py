class UrlShortenere(object):
    def shorten(self, url):
        parts = len(url) / 6
        print(parts)
        for letter in url:
            print(ord(letter))


if __name__ == '__main__':
    shortener = UrlShortenere()
    shortener.shorten('http://localhost:600')
