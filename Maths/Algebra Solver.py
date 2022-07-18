def one_var(equation, var):

    try:

        equation = equation.replace(" ", "")

        left = equation.split("=")[0]
        right = int(equation.split("=")[1])

        try:
            coefficient = int(left.split(var)[0])
        except:
            coefficient = int(left.split(var)[0] + "1")
        try:
            plus = int(left.split(var)[1])
        except:
            plus = 0

        solution = (right - plus) / coefficient
        return solution
    
    except:

        raise ValueError('Wrong format')

            
def two_vars(eq1, eq2, var1, var2):

    try:

        eq1 = eq1.replace(" ", "")
        eq2 = eq2.replace(" ", "")
        
        left1 = eq1.split("=")[0]
        right1 = int(eq1.split("=")[1].replace('+-', '-'))
        left2 = eq2.split("=")[0]
        right2 = int(eq2.split("=")[1].replace('+-', '-'))

        try:
            ce1_1 = int(left1.split(var1)[0].replace('+-', '-'))
        except:
            ce1_1 = int(left1.split(var1)[0].replace('+-', '-') + "1")
        try:
            ce1_2 = int(left1.split(var1)[1].split(var2)[0].replace('+-', '-'))
        except:
            ce1_2 = int(left1.split(var1)[1].split(var2)[0].replace('+-', '-') + "1")
        try:
            ce2_1 = int(left2.split(var1)[0].replace('+-', '-'))
        except:
            ce2_1 = int(left2.split(var1)[0].replace('+-', '-') + "1")
        try:
            ce2_2 = int(left2.split(var1)[1].split(var2)[0].replace('+-', '-'))
        except:
            ce2_2 = int(left2.split(var1)[1].split(var2)[0].replace('+-', '-') + "1")

        ce1_2, right1 = ce1_2 * ce2_1, right1 * ce2_1
        ce2_2, right2 = ce2_2 * ce1_1, right2 * ce1_1

        eq1 = f'{ce1_1*ce2_1}{var1}+{ce1_2}{var2}={right1}'
        eq2 = f'{ce1_1*ce2_1}{var1}+{ce2_2}{var2}={right2}'

        diff_var = ce1_2 - ce2_2
        diff_num = right1 - right2

        eq3 = f'{diff_var}{var2}={diff_num}'

        var2_value = diff_num / diff_var

        v2 = int((ce1_2 / ce2_1) * var2_value * ce2_1)
        if var2_value >= 0:
            v2 = ('+' + str(int((ce1_2 / ce2_1) * var2_value * ce2_1))).replace('+-', '-')

        var1_value = one_var(f'{ce1_1*ce2_1}{var1}{v2}={right1}', var1)

        eq4 = f'{ce1_1*ce2_1}{var1}+{v2}={right1}'.replace('++', '+')
        eq5 = f'{ce1_1*ce2_1}{var1}={right1-int(v2)}'

        return {var1: var1_value, var2: var2_value, 'steps': (eq1.replace('+-', '-'),    eq2.replace('+-', '-'),    eq3.replace('+-', '-'),    eq4.replace('+-', '-'), eq5.replace('+-', '-'))}
    
    except:

        return False


while True:
        print('Enter the equations and variables (leave blank to exit):\n')
        eq_1 = input('Equation 1: ')
        if eq_1 == '':
                break
        eq_2 = input('Equation 2: ')
        var_1 = input('Variable name 1: ')
        var_2 = input('Variable name 2: ')
        result = two_vars(eq_1, eq_2, var_1, var_2)
        print('')
        if result:
                print(var_1, '=', result[var_1])
                print(var_2, '=', result[var_2])
                print('Steps:', '; '.join(result['steps']))
        else:
                print('Invalid format')
        print('\n' + ('- ' * 30) + '\n')