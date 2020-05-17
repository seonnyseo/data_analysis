def solution(S):
    # write your code in Python 3.6
    
    pairs = {')' : '(', ']':'[', '}':'{'}
    par = {}
    for idx, c in enumerate(S):
        
        if c in pairs.values():
            par[c] = par.get(c, []).append(idx)
        
        else:
            paren = pairs[c]
            
            if par[paren][-1] == max([x[-1] for x in par.values()]):
                par[paren].pop()
            else:
                return 0
    
    if len(par.values()):
        return 0
    return 1


solution("{[()()]}")