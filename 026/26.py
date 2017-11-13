#euler26
#stolen from the internet

def division(num, den):
    ipart = str(num / den);
    fpart = ""
    rpart = ""
    seen  = [ num%den ]
    while num % den != 0:
        num        = (num%den) * 10
        multiple   = num / den
        fpart     += str(multiple)
        num        = num - (den * multiple)
        c = 0
        quit = False
        for i in seen:
            if num == i: # This number has been seen before.
                rpart = fpart[c:] # Make characters from c to end of list part of repeating part
                fpart = fpart[:c] # Truncate fpart
                quit = True
                break
            c = c + 1
        if quit:
            break
        seen += [num]
    return [ipart, fpart, rpart]
    
x = [(len(division(1,i)[2]),i) for i in range(1,1001)]
x.sort()
print x[0]
print x[-1]