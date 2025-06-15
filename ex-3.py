pw = "12345^&*"
is_correct = True
while is_correct:
    input_pw = input('Please enter your password:')
    if input_pw == pw :
        print('Log in success!!')
        is_correct = False
    else:
        print('Please try again.')