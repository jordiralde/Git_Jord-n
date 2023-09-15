num = 0
s='abcde'
t='abcdefhg'
def FuncionDiferencias(s: str, t: str, num):
    for i in t:
        num+=1
        print(i, (num))
        print(t, (num))
        
        if s.count(i) != t.count(i):
            return print(f"letra demas= {i}")
FuncionDiferencias(s, t, num)