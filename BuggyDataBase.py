'''
###################
# Buggy Data Base #
###################
Project 01 for FP

by Miguel Cardsoso
(ist 21-22)
'''


# internal functions


def seperate_words(s):
    return s.split(" ")


def back_to_normal(s):
    new_str = str()

    for i in s:
        new_str = new_str + i + " "

    if new_str[-1:] == " ":
        new_str = new_str[:-1]

    return new_str


def position_finder(sequence, start):
    position = {
        (0, 0): 1,
        (0, 1): 2,
        (0, 2): 3,
        (1, 0): 4,
        (1, 1): 5,
        (1, 2): 6,
        (2, 0): 7,
        (2, 1): 8,
        (2, 2): 9
    }

    finalPosition = []

    for key in position:
        if position[key] == start:
            for x in key:
                finalPosition.append(x)

    for x in sequence:
        if x == "C":
            if 0 < finalPosition[0] <= 2:
                finalPosition[0] += -1
        if x == "B":
            if 0 <= finalPosition[0] < 2:
                finalPosition[0] += 1
        if x == "E":
            if 0 < finalPosition[1] <= 2:
                finalPosition[1] += -1
        if x == "D":
            if 0 <= finalPosition[1] < 2:
                finalPosition[1] += 1

    return position[tuple(finalPosition)]


def character_corrector(c):
    if ord(c) > ord("z"):
        return chr(ord(c) - 26)
    return c


def check_checksum(checksum):
    return (type(checksum) == str
            and len(checksum) == 7
            and checksum[0] == "["
            and checksum[6] == "]"
            and checksum[1:-1].islower()
            and checksum[1:-1].isalpha())


def check_name(name):
    return type(name) == str and len(name) >= 1


def check_pswrd(pswrd):
    return (type(pswrd) == str
            and len(pswrd) >= 3
            and check_vowel(pswrd)
            and any(pswrd[i] == pswrd[i+1] for i in range(len(pswrd)-1)))


def check_rule(rule):
    return (type(rule) == dict
            and "vals" in rule.keys()
            and "char" in rule.keys()
            and type(rule["vals"]) == tuple
            and len(rule["vals"]) == 2
            and all(type(rule["vals"][i]) == int for i in range(2))
            and all(rule["vals"][i] >= 0 for i in range(2))
            and type(rule["char"]) == str and len(rule["char"]) == 1)


def check_vowel(data_pass):
    vowel = "aeiou"
    vowel_number = 0
    for letter in data_pass:
        if letter in vowel:
            vowel_number += 1
    return vowel_number >= 3


# Test Functions


def corrigir_palavra(s):
    '''corrects a corrupted word following a set of rules

rules:
> data has to be a string
    (this function does not check if the input is correct)

> if there is a lowercase character followed
    by an uppercase character or voiceovers they both disappear

> check the data multiple times until there are no changes

input --> type(str) corrupted data
output --> type(str) corrected data

by Miguel Cardoso for FP(ist 21-22)
    '''

    data = seperate_words(s)
    data_list = list()

    for x in data:
        old_data = x
        ver_data = False
        while ver_data is not True:
            i = 0
            length = len(old_data) - 1

            while i <= length:

                new_data = str()

                while i < length:

                    char = ord(old_data[i])
                    next_char = ord(old_data[(i + 1)])

                    if ((ord("a") <= char <= ord("z"))
                            and (char == next_char + 32)):
                        i += 2

                    elif ((ord("A") <= char <= ord("Z"))
                          and (char == next_char - 32)):
                        i += 2

                    else:
                        new_data = new_data + old_data[i]
                        i += 1

                if i > length:
                    new_data = new_data
                else:
                    new_data = new_data + old_data[i]
                i += 1

            ver_data = old_data == new_data
            old_data = new_data

        data_list.append(new_data)

        verified_data = str()

        for n in data_list:
            verified_data = verified_data + n + " "

    if verified_data[-1:] == " ":
        verified_data = verified_data[:-1]

    return verified_data


def eh_anagrama(char01, char02):
    '''compares two words and checks if they are an anagram

rules:
> if they are the same word (not case sensitive) it returns False

> if the are anagrams of each other it returns True

input --> type(str) two separate words
output --> type(bol)

by Miguel Cardoso for FP(ist 21-22)
    '''

    if char01.lower() != char02.lower():
        return sorted(char01.lower()) == sorted(char02.lower())

    return False


def corrigir_doc(s):
    '''corrects a corrupted document following a set of rules

this function separates word by word and calls corrigir_palavra()
and eh_anagrama()

rules:
> data has to be a string
    (this function check if the input is correct)

> if there is a lowercase character followed
    by an uppercase character or voiceovers they both disappear

> if there is an anagram it will keep the first time the word
    appears and deletes all future anagrams

> check the data multiple times until there are no changes

input --> type(str) corrupted data
output --> type(str) corrected data

by Miguel Cardoso for FP(ist 21-22)
    '''

    if type(s) == str:
        new_doc = []
        if all(x.isalpha() for x in seperate_words(s)):
            doc = corrigir_palavra(s)
            doc = seperate_words(doc)
            i = 0
            while i < len(doc):
                if any(eh_anagrama(doc[i], word) for word in new_doc):
                    i += 1
                else:
                    new_doc.append(doc[i])
                    i += 1
            new_doc = back_to_normal(new_doc)
        else:
            raise ValueError("corrigir_doc: argumento invalido")

        return new_doc
    else:
        raise ValueError("corrigir_doc: argumento invalido")


def obter_posicao(sequence, start):
    '''receives a character and a position and finds the next number

    1 2 3
    4 5 6
    7 8 9

rules:
> C is up, B is down, E is Left and D is right

> if the direction hits a wall it stays the same

(This function checks if the inputs are valid)

input --> type(str) direction, type(int) position
output --> type(int) position

by Miguel Cardoso for FP(ist 21-22)
    '''

    return position_finder(sequence, start)


def obter_digito(sequence, start):
    '''receives a chain of character and a position
and finds the next number

    1 2 3
    4 5 6
    7 8 9

rules:
> C is up, B is down, E is Left and D is right

> if the direction hits a wall it stays the same

(This function checks if the inputs are valid)

input --> type(str) direction, type(int) position
output --> type(int) position

by Miguel Cardoso for FP(ist 21-22)
    '''

    return position_finder(sequence, start)


def obter_pin(sequence):
    '''receives between 4 and 10 chains of character
and a position and finds the next number

    1 2 3
    4 5 6
    7 8 9

rules:

> Starting position for the first chain is 5 and the
following ones are the previous position of the chain

> C is up, B is down, E is Left and D is right

> if the direction hits a wall it stays the same

(This function checks if the inputs are valid)

input --> type(str) direction, type(int) position
output --> type(int) position

by Miguel Cardoso for FP(ist 21-22)
    '''

    if type(sequence) == tuple:

        vowel = ("C", "B", "E", "D")

        if (len(sequence) > 10
            or len(sequence) < 4
            or any(len(i) == 0 for i in sequence)
                or any(any(x not in vowel for x in i) for i in sequence)):
            raise ValueError("obter_pin: argumento invalido")

        else:
            start = 5
            pin = []
            for x in sequence:
                pin.append(position_finder(x, start))
                start = pin[-1]

        return tuple(pin)

    raise ValueError("obter_pin: argumento invalido")


def eh_entrada(data):
    '''receives a tuple with 3 elements (cipher, checksum,
security) and returns True if it follows the following rules

rules:
> cipher is a string of character where each word is separated by a "-"

> checksum is a string of 5 character and in-between square brackets

> security is a tuple of between 4 and 10 group of characters

input --> type(tuple)
output --> type(bol)

by Miguel Cardoso for FP(ist 21-22)
    '''

    if type(data) == tuple:
        if len(data) == 3:
            cifra = str()
            checksum = data[1]
            security = data[2]
            if (type(data[0]) == str
                and check_checksum(checksum)
                and type(security) == tuple
                    and len(security) > 1):
                if len(data[0]) > 0:
                    for x in data[0]:
                        if x != "-":
                            cifra += x
                        else:
                            cifra = cifra
                    return (len(cifra) > 0
                            and cifra.islower()
                            and cifra.isalpha()
                            and all(type(x) == int for x in security)
                            and all(x > 0 for x in security))
                else:
                    return False
            else:
                return False
        else:
            return False
    else:
        return False


def validar_cifra(cifra, checksum):
    '''Receives two inputs (cipher and checksum)
inside a tuple and verifies if its correct

input --> type(tuple)
output --> type(bol)

by Miguel Cardoso for FP(ist 21-22)
    '''

    v = str()
    letters = {}
    for i in sorted(cifra):
        if i != "-":
            letters[i] = letters[i] + 1 if i in letters else 1

    temp = sorted(letters.values(), reverse=True)
    letters = [(k, v) for k, v in letters.items()]
    v = []

    for n in range(5):
        for letter, times in letters:
            if times == temp[n]:
                if letter not in v:
                    v.append(letter)
    v = v[:5]
    checksum_v = "["
    for letter in v:
        checksum_v = checksum_v + letter
    checksum_v = checksum_v + "]"

    return checksum == checksum_v


def filtrar_bdb(data_base):
    '''Receives a list with one or more groups
of elements (cipher, checksum, security) and
delivers a list of all the groups that contain errors

input --> type(lst)
output --> type(lst)

by Miguel Cardoso for FP(ist 21-22)
    '''

    if type(data_base) == list and len(data_base) > 0:

        data_error = []
        i = 0
        for data in data_base:
            if eh_entrada(data):
                if not validar_cifra(data[0], data[1]):
                    i += 1
                    data_error.append(data)
            else:
                raise ValueError("filtrar_bdb: argumento invalido")

        return data_error

    else:
        raise ValueError("filtrar_bdb: argumento invalido")


def obter_num_seguranca(security):
    '''Receives a tuple with multiple numbers and delivers the number
    of shortest difference between all the numbers

input --> type(tuple)
output --> type(int)

by Miguel Cardoso for FP(ist 21-22)
    '''

    security = sorted(security, reverse=True)
    code = 0
    for i in range(len(security)-1):
        new_code = security[i]-security[i+1]
        code = new_code if code == 0 else code
        code = new_code if new_code < code else code

    return code


def decifrar_texto(cifra, security):
    '''Receives a sting of characters and a number and decodes the string
advancing each character the number of times inputed

input --> type(str), type(int)
output --> type(int)

by Miguel Cardoso for FP(ist 21-22)
    '''
    decode = str()
    distance = security % 26
    i = 0
    while i < len(cifra):

        if cifra[i] == "-":
            decode += chr(ord(" "))
            i += 1

        elif i % 2 == 0:
            char = chr(
                ord("a") + ((ord(cifra[i]) - ord("a") + distance) % 26) + 1)
            decode += character_corrector(char)
            i += 1

        else:
            char = chr(
                ord("a") + (ord(cifra[i]) - ord("a") + distance) % 26 - 1)
            decode += character_corrector(char)
            i += 1

    return decode


def decifrar_bdb(data):
    '''recives a list with one or more entries and returns a list
of decoded entries

input --> type(list)
output --> type(list)

by Miguel Cardoso for FP(ist 21-22)
    '''

    final_data = []
    if type(data) == list:
        for i in data:
            if not eh_entrada(i):
                raise ValueError("decifrar_bdb: argumento invalido")
            else:
                final_data.append(decifrar_texto(
                    i[0], obter_num_seguranca(i[2])))
        return final_data
    else:
        raise ValueError("decifrar_bdb: argumento invalido")


def eh_utilizador(data):
    '''recives an input and if it is a dictionary with name,
pass and rule as keys it returns True

input --> type(dict)
output --> type(bol)

by Miguel Cardoso for FP(ist 21-22)
    '''

    if type(data) == dict:
        if ("name" in data.keys()
            and "pass" in data.keys()
                and "rule" in data.keys()):
            return (check_name(data["name"])
                    and check_pswrd(data["pass"])
                    and check_rule(data["rule"]))
        else:
            return False
    else:
        return False


def eh_senha_valida(pswrd, rule):
    '''receives password and a set of rules verifies if it's True

input --> type(str), type(dict)
output --> type(bol)

by Miguel Cardoso for FP(ist 21-22)
    '''

    if check_pswrd(pswrd) and check_rule(rule):
        char_check = {}
        for c in pswrd:
            char_check[c] = char_check[c] + 1 if c in char_check.keys() else 1
        if rule["char"] in char_check.keys():
            return (char_check[rule["char"]] >= rule["vals"][0]
                    and char_check[rule["char"]] <= rule["vals"][1])
        else:
            return False
    else:
        return False


def filtrar_senhas(data_base):
    '''Receives a list with multiple entrees of usernames and passwords
and returns a list of user with wrong passwords.

input --> type(list)
output --> type(list)

by Miguel Cardoso for FP(ist 21-22)
    '''

    if type(data_base) == list:
        if len(data_base) > 0:
            if all(len(d) == 3 for d in data_base):
                if not all(eh_utilizador(x) for x in data_base):
                    names = []
                    for data in data_base:
                        if (not eh_senha_valida(data["pass"], data["rule"])
                                or not eh_utilizador(data)):
                            names.append(data["name"])
                    names = sorted(names)
                    return names
                else:
                    raise ValueError("filtrar_senhas: argumento invalido")

            else:
                raise ValueError("filtrar_senhas: argumento invalido")

        else:
            raise ValueError("filtrar_senhas: argumento invalido")

    else:
        raise ValueError("filtrar_senhas: argumento invalido")
