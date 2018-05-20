"""
For A Given Number "N" Print Lexicographically  All posibble balanced expresion of "()"
Balanced -- 1- Number of ( =  Number of )
2- Corresponding  ) should come after (
Ex - - (()) -- Valid
        ()) -- Invalid
        (()(- invalid
"""





def afuc(arr,index,openn,close,N):
  if index==N:
    for a in arr:
      print(a,end="")
    print('')
    return
  if openn<(N/2):
    arr[index]="(" 
    afuc(arr,index+1,openn+1,close,N)
  if close<openn:
    arr[index]=")"
    afuc(arr,index+1,openn,close+1,N)

abc=[None]*6 
afuc(abc,0,0,0,6)



Input----

N = 6



Output ----

((()))
(()())
(())()
()(())
()()()