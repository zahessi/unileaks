# Fred:Corwill;Wilfred:Corwill;Barney:Tornbull;Betty:Tornbull;Bjon:Tornbull;Raphael:Corwill;Alfred:Corwill

def meet(s):
    s = sorted([(f.split(":")[1], f.split(":")[0])for f in s.split(';')])
    s = ", ".join(["({}, {})".format(a[0], a[1]) for a in s])
    print(s)

meet("Fred:Corwill;Wilfred:Corwill;Barney:Tornbull;Betty:Tornbull;Bjon:Tornbull;Raphael:Corwill;Alfred:Corwill")