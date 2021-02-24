    def cokolwiek(self):
        global out
        out = ''
        klucz = self.keyIn.text()
        zasz = self.textIn.text()
        szyfr1 = []
        szyfr2 = []
        alfabet = [chr(i) for i in range(1423)]
        try:
            for j in klucz:
                szyfr1.append(j)
            for k in range(len(szyfr1)):
                if szyfr1[k] not in szyfr2:
                    szyfr2.append(szyfr1[k])
            for i in range(len(alfabet)):
                if alfabet[i] not in szyfr2:
                    szyfr2.append(alfabet[i])
            try:
                for l in zasz:
                    if szyfr2.index(l) + 1 < 10:
                        out += '000'
                    if szyfr2.index(l) + 1 < 100 and szyfr2.index(l) + 1 > 9:
                        out += '00'
                    if szyfr2.index(l) + 1 < 1000 and szyfr2.index(l) + 1 > 99:
                        out += '0'
                    out += str(szyfr2.index(l) + 1)
                print(out)
            except ValueError:
                print('Użyto niedopuszczalnego znaku. Skontaktuj się z twórcą programu. Kod błędu: 020310041102')
        except:
            print('Wystąpił błąd. Skontaktuj się z twórcą programu. Kod błędu: 0603260110062002')
