import streamlit as st

def arm(no):
    eq = no
    s = len(str(no))
    sum = 0
    while eq > 0:
        rev = eq % 10
        sum = rev ** s + sum
        eq = eq // 10
    if sum == no:
        st.success(f'{no} is a Armstrong number')
    else:
        st.error(f'{no} is not a Armstrong number')

def s(no):
    sp = no
    sum = 0
    mul = 1
    while sp > 0:
        rev = sp % 10
        sum = sum + rev
        mul = mul * rev
        sp = sp // 10
    if sum == mul:
        st.success(f'{no} is a Spy number')
    else:
        st.error(f'{no} is not a Spy number')

def happy(no):
    ha = no
    sum = 0
    while len(str(ha)) > 1:
        while ha > 0:
            rev = ha % 10
            sum = sum + rev ** 2
            ha = ha // 10
        ha = sum
        sum = 0
    if ha == 1:
        st.success(f'{no} is a Happy number')
    else:
        st.error(f'{no} is not a happy number')

def pali(no):
    pl = no
    rev = 0
    while pl > 0:
        rem = pl % 10
        rev = (rev + rem) * 10
        pl = pl // 10
    rev = rev // 10
    if rev == no:
        st.success(f'{no} is a Palindrome')
    else:
        st.error(f'{no} is not a Palindrome')

def prime(no):
    pri = 0
    for i in range(1, no):
        if no % i == 0:
            pri += 1
    if pri == 1:
        st.success(f'{no} is a Prime number')
    else:
        st.error(f'{no} is not a prime number')

def duck(no):
    n = str(no)
    if '0' in n and n[0] != '0':
        st.success(f'{no} is a Duck number')
    else:
        st.error(f'{no} is not a Duck number')

def hnn(no):
    n=no
    sum=0
    while n>0:
        rem=n%10
        sum=sum+rem
        n=n//10
    if no %sum==0:
        st.success(f'{no} is a Harshad/Nivan number')
    else:
        st.error(f'{no} is not a Harshad/Nivan number')

no=st.number_input('enter your number',min_value=0)
c=st.selectbox('Chose the action',['Armstrong number','Spy number','Happy number','Palindrome','Prime number','Duck number','Harshad/Nivan number'])
bu=st.button('Check', type='primary')

if bu:
    if c=='Armstrong number':
        arm(no)
    elif c=='Spy number':
        s(no)
    elif c=='Happy number':
        happy(no)
    elif c=='Palindrome':
        pali(no)
    elif c=='Prime number':
        prime(no)
    elif c=='Duck number':
        duck(no)
    elif c=='Harshad/Nivan number':
        hnn(no)


