# Lesson 5

startMoney = float(input('Start Money (decimal): '))
cookies = input('cookie Str: ')

cookieCost = 1.25
makeCookieCost = 0.5
bigCookieCost = 2
makeBigCookieCost = 0.75

amtBigCookie = cookies.count('b')
amtSmallCookie = cookies.count('c')

totalCookies = len(cookies)

############## PROFITS ##################
bigCookieProfit = (amtBigCookie * bigCookieCost) - (amtBigCookie * makeBigCookieCost)
smallCookieProfit = (amtSmallCookie * cookieCost) - (amtSmallCookie * cookieCost)
totalProfit = bigCookieCost + smallCookieProfit
########### TOTAL AMT MONEY ###########

totalMoney = startMoney + (amtBigCookie * bigCookieCost) + (amtSmallCookie * cookieCost)

############## OUTPUT ##############

print(f'{cookies} contains {amtBigCookie} big cookies and {amtSmallCookie} normal cookies.')
print(f'The total number of cookies is {totalCookies}')
print(f'Profits will be ${totalMoney}, with big cookies earning ${bigCookieProfit} and normal cookies earning ${smallCookieProfit}.')
print(f'The total amount earned would be ${totalMoney}')