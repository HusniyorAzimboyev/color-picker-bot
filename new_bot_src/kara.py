def kara(a:int,b:int):
    result = []
    for i in range(1,b+1):
        result.append(f'{a} * {i} = {a*i}')
    return "\n".join(tuple(result))
