# https://www.codewars.com/kata/salesmans-travel
import re

def travel(r, zipcode):
    addresses = [*filter(lambda x: re.findall(r"[A-Z]{2} \d{5}", x)[0] == zipcode, r.split(","))]
    if not addresses: return f"{zipcode}:/"
    numbers = []
    for i, a in enumerate(addresses):
        n = re.findall(r"\d{1,3}(?= \w+)", a)[0]
        numbers.append(n)
        addresses[i] = a.strip(n).strip(zipcode)
    return f"{zipcode}:{','.join(addresses)}/{','.join(numbers)}"

r = "123 Main Street St. Louisville OH 43071,432 Main Long Road St. Louisville OH 43071,786 High Street Pollocksville NY 56432"
assert travel(r, "OH 43071") == "OH 43071:Main Street St. Louisville,Main Long Road St. Louisville/123,432"
