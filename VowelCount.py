def vowelCount(str):
    vowels=0
    for i in str:
        if i in "aeiouAEIOU":
           vowels = vowels+1
    return vowels

print(vowelCount("etihauuuusy"))