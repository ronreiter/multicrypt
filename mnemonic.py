import os
import unicodedata

class Mnemonic(object):
    # Seed derivation no longer follows BIP39
    # Mnemonic phrase uses a hash based checksum, instead of a wordlist-dependent checksum

    def __init__(self, lang=None):
        lang = lang or 'en'
        path = os.path.join(os.path.dirname(__file__), 'wordlist', 'english.txt')
        s = open(path,'r').read().strip()
        #s = unicodedata.normalize('NFKD', s.decode('utf8'))
        lines = s.split('\n')
        self.wordlist = []
        for line in lines:
            line = line.split('#')[0]
            line = line.strip(' \r')
            assert ' ' not in line
            if line:
                self.wordlist.append(line)


    def mnemonic_encode(self, i):
        n = len(self.wordlist)
        words = []
        while i:
            x = i%n
            i = i//n
            words.append(self.wordlist[x])
        return ' '.join(words)

    def mnemonic_decode(self, seed):
        n = len(self.wordlist)
        words = seed.split()
        i = 0
        while words:
            w = words.pop()
            k = self.wordlist.index(w)
            i = i*n + k
        return i
