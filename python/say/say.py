def say(number):
    number = int(number)
    if number == 0:
        return "zero"
    if number <0 or number > 999999999999:
        raise ValueError("invalid number")
    number = str(number)
    length = len(number)

    if length % 3 != 0:
        number = (3-(length%3))*'0'+number

    hundOneMap = {
        "0" : "",
        "1" : "one",
        "2" : "two",
        "3" : "three",
        "4" : "four",
        "5" : "five",
        "6" : "six",
        "7" : "seven",
        "8" : "eight",
        "9" : "nine",
    }

    tenMap = {
        "0" : "",
        "2" : "twenty",
        "3" : "thirty",
        "4" : "forty",
        "5" : "fifty",
        "6" : "sixty",
        "7" : "seventy",
        "8" : "eighty",
        "9" : "ninty",
        "10": "ten",
        "11": "eleven",
        "12": "twelve",
        "13": "thirteen",
        "14": "fourteen",
        "15": "fifteen",
        "16": "sixteen",
        "17": "seventeen",
        "18": "eighteen",
        "19": "nineteen",
    }

    segmentMap = {
        0 : "",
        1 : "thousand",
        2 : "million",
        3 : "billion"
    }

    import textwrap
    numbers = textwrap.wrap(number,3)
    length = len(numbers)
    finalword = ""
    segmentcount = 0
    for i in range(length-1,-1,-1):
        word = ""
        hundred = ""
        tens = ""
        if numbers[i][0] != "0":
            hundred = hundOneMap[numbers[i][0]]+" hundred"

        if numbers[i][1] == "1":
            tens= tenMap[numbers[i][1]+numbers[i][2]]
        else:
            if tenMap[numbers[i][1]]!="":
                tens= tenMap[numbers[i][1]]
                if hundOneMap[numbers[i][2]] != "":
                    tens= tenMap[numbers[i][1]]+"-"+hundOneMap[numbers[i][2]]

            else:
                if hundOneMap[numbers[i][2]] != "":
                    tens= hundOneMap[numbers[i][2]]

        if segmentcount == 0 and length>1:
            if hundred == "" and tens != "":
                tens = "and "+tens

        if tens != "" and hundred != "":
            word += hundred +" and "+ tens
        elif tens != "":
            word=tens
        else:
            word=hundred

        if word != "":
            word += (" "+segmentMap[segmentcount])
            finalword = word + " " + finalword

        segmentcount +=1

    return finalword.strip()
