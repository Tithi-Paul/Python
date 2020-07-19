# Operate with numerator and denominator to 
    # keep just the fractional part of the quotient
def fractional_part(numerator, denominator):
    if denominator == 0:
        return 0
    else:
        res = numerator/denominator
        if numerator == 0:
            return 0
        else:
            result = numerator/denominator
            while(result>=1):
                result= result-1;
            if result < 1 :
                return result

print(fractional_part(5, 5)) # Should be 0
print(fractional_part(5, 4)) # Should be 0.25
print(fractional_part(5, 3)) # Should be 0.66...
print(fractional_part(5, 2)) # Should be 0.5
print(fractional_part(5, 0)) # Should be 0
print(fractional_part(0, 5)) # Should be 0
