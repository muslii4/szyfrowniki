
        out = ''
        szyfr1 = []
        szyfr2 = []
        lzasz = []
        m = 0
        alfabet = [chr(i) for i in range(1423)]
        for j in klucz:
            szyfr1.append(j)
        for k in range(len(szyfr1)):
            if szyfr1[k] not in szyfr2:
                szyfr2.append(szyfr1[k])
        for i in range(len(alfabet)):
            if alfabet[i] not in szyfr2:
                szyfr2.append(alfabet[i])
        for l in range(int(len(str(zasz))/4)):
            lzasz.append(zasz[m] + zasz[m + 1] + zasz[m + 2] + zasz[m + 3])
            m += 4
        try:
            for n in lzasz:
                out += szyfr2[int(n) - 1]
        except IndexError:
            self.lOut.setText(_translate("Form", "Ktoś coś źle wpisał.", None))
