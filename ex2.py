text = input( 'Enter your text:')
while not isFoundA:   
    if text=='a':
        print('Found Letter')
        isFoundA=True
    else:
        print('Try agian!')
        text = input( 'Enter your text:')