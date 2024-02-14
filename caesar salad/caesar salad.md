# caesar salad?

## Problem
I was trying to make some Caesar salad for New Year's, but I couldn't find the recipe! I found a really old image of the recipe on my phone, but one of the ingredients is very blurry, and I can't find the name. Can you help me find the name of the missing ingredient?

[Original problem](https://ctf.mcpt.ca/problem/salad)

### Attachment

[salad.py](./salad.py)

## Solution

When we open the file, we see a method ```rotate(input,key)``` that seems to take each character in the given input and rotate it forwards ```key``` amount of characters forwards in the given alphabet (In this case, ASCII values 33 to 125)

Rereading the method ```rotate```, we notice that in the recursive statement, the key is incremented by one after each character.

We know the flag header is ```CTF{``` thus the orginal key must first rotate ```C (ASCII 67)``` to ```e (ASCII 101)```. Doing some simple math, we figure the key is originally 34. 

Now, to reverse the process, we want to input a key such that ```e``` will map back to ```C```. The alphabet has length 93, so our new key must be ```93-34=59```

In addition, the part of the method where the key is incremented for each additional character must also be reversed, so we change the ```+1``` to ```-1```. Running our new program gives our flag ```CTF{5aUC3_AlwaY$_loOk5_b1urry}```

***
### Flag 
```CTF{5aUC3_AlwaY$_loOk5_b1urry}```