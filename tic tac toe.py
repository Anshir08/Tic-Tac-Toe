print("Welcome to play TIC-TAC-TOE World\n *For reference to Players*\n")
def main():
    mat = [['_'] * 3, ['_'] * 3, ['_'] * 3]
    for i in mat:
        for j in i:
            print(j.rjust(8),end="")
        print('\n')
    while 1:
        Q,e=input('Enter X or O for player 1: '),0
        if Q=='X':
            W='O'
        elif Q=='O':
            W='X'
        else:
            e=1
            print('Wrong input')
        if e!=1:
            break
    for i in range(9):
      while 1:
        a,r,u = int(input('Enter position(0-8): ')),0,0
        print()
        if a >= 0 and a < 3:
            if mat[0][a] == '_':
              if i%2==0:
                mat[0][a] = Q
              else:
                mat[0][a] = W
            else:
                r = 1
                print("choose other position")
        elif a > 2 and a < 6:
            a = a%3
            if mat[1][a] == '_':
                if i % 2 == 0:
                    mat[1][a] = Q
                else:
                    mat[1][a] = W
            else:
                r = 1
                print("choose other position")
        elif a > 5 and a < 9:
            a = a%3
            if mat[2][a] == '_':
                if i % 2 == 0:
                    mat[2][a] = Q
                else:
                    mat[2][a] = W
            else:
                r = 1
                print("choose other position")
        else:
            r=1
            print('Wrong Input')
        if r!=1:
            break
      for j in mat:
          for k in j:
             print(k.rjust(8), end="")
          print('\n')
      for l in range(3):
         if mat[l][0] ==mat[l][1]==mat[l][2]==Q or mat[0][l]==mat[1][l]==mat[2][l]==Q or mat[0][0]==mat[1][1]==mat[2][2]==Q or mat[0][2]==mat[1][1]==mat[2][0]==Q:
             u = 1
             print("Player 1 Wins")
             break
         if mat[l][0] == mat[l][1] == mat[l][2] == W or mat[0][l] == mat[1][l] == mat[2][l] == W or mat[0][0] == mat[1][1] == mat[2][2] == W or mat[0][2] == mat[1][1] == mat[2][0] == W:
             u = 1
             print("Player 2 Wins")
             break
      if i==8 and u==0:
          u=1
          print("Match Drawn")
      if u==1:
          fuck = int(input("agar kattas zero m mazza aaya aur agar dubbara khelna chahte ho to 1 dabao varna 0 dabado!!!!!\n"))
          if fuck==1:
              main()
          else:
             exit()
main()