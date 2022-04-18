def rndsf(num, sf):
    num = str(int(num))
    if sf >= len(num):
        return num
    rounded = ''
    ind = 0
    while ind < (sf - 1):
        rounded += num[ind]
        ind += 1
    if int(num[sf]) >= 5:
        rounded += str(int(num[ind]) + 1)
    else:
        rounded += num[ind]
    while ind < (len(num) - 1):
        rounded += '0'
        ind += 1
    return int(rounded)

def rearrange(eq, var):
    left, right = eq.replace(' ', '').split('=')
    if var in left:
        left, right = right, left
    if var == right:
        return left
    if '/' not in right:
        products = right.split('*')
        products.remove(var)
        return '(' + left + ')/(' + '*'.join(products) + ')'
    else:
        top, bottom = right.split('/')
        if var in top:
            left = '(' + left + ')*' + bottom
            if var == top:
                return left
            else:
                top_products = top.replace('(', '').replace(')', '').split('*')
                top_products.remove(var)
                return '(' + left + ')/(' + '*'.join(top_products) + ')'
        else:
            if var == bottom:
                return '(' + top + ')/(' + left + ')'
            else:
                bottom_products = bottom.replace('(', '').replace(')', '').split('*')
                bottom_products.remove(var)
                return '(' + top + ')/(' + left + '*' + '*'.join(bottom_products) + ')'

def find_value(eq, find, **vars):
    try:
        new_eq = rearrange(eq, find)
        return eval(new_eq, vars)
    except Exception as e:
        return e


# Use find_value() to rearrange an equation for any variable, for example:

print('m =', find_value('D=m/v', 'm', D=1.3, v=500)) # m = 650.0