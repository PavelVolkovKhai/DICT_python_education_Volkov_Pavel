camel = r"""
The camel habitat...
 ___.-''''-.
 /___ @    |
 ',,,,.     |         _.'''''''._
      '     |        /           \
      |     \    _.-'             \
      |      '.-'                  '-.
      |                              ',
      |                               '',
       ',,-,                           ':;
            ',,| ;,,                 ,' ;;
               ! ; !'',,,',',,,,'! ;   ;:
              : ; ! !       ! ! ; ;    :;
              ; ; ! !       ! ! ; ;    ;,
              ; ; ! !       ! ! ; ;
              ; ; ! !       ! ! ; ;
              ;,, !,!       !,! ;,;
              /_I L_I       L_I /_I
Look at that!"""


lion = r"""
The lion habitat...
                                               ,w.
                                             ,YWMMw  ,M  ,
                        _.---.._   __..---._.'MMMMMw,wMWmW,
                   _.-""        '''           YP"WMMMMMMMMMb,
                .-' __.'                   .'     MMMMW^WMMMM;
    _,        .'.-'"; `,       /`     .--""      :MMM[==MWMW^;
 ,mM^"     ,-'.'   /    ;      ;      /   ,       MMMMb_wMW"  @\
,MM:.    .'.-'   .'     ;     `\    ;     `,     MMMMMMMW `"=./`-,
WMMm__,-'.'     /      _.\      F'''-+,,   ;_,_.dMMMMMMMM[,_ / `=_}
"^MP__.-'    ,-' _.--""   `-,   ;       \  ; ;MMMMMMMMMMW^``; __|
           / .'          ; ;     ) )`{  \ `"^W^`,   \    :
          / .'           /  (    .'  /     Ww._     `.  `"
         / Y,       `,   `-,=,_{   ;       MMMP`""-,  `-._.-,
        (--, )        `,_ / `) \/"")      ^"      `-, -;"\:
The lion is roaring!"""


deer = r"""
The deer habitat...
   /|       |\
`__\\       //__'
   ||       ||
 \__`\     |'__/
   `_\\   //_'
   _.,:---;,._
   \_:     :_/
     |@. .@|
     |     |
     ,\.-./ \
     ;;`-'   `---__________-----.-.
     ;;;                         \_\
     ';;;                         |
      ;    |                      ;
       \   \     \        |      /
        \_, \    /        \     |\
          |';|  |,,,,,,,,/ \    \ \_
          |  |  |           \   /   |
          \  \  |           |  / \  |
           | || |           | |   | |
           | || |           | |   | |
           | || |           | |   | |
           |_||_|           |_|   |_|
          /_//_/           /_/   /_/
Pretty good!"""


goose = r"""
The goose habitat...
                                    _
                                ,-"" "".
                              ,'  ____  `.
                            ,'  ,'    `.  `._
   (`.         _..--.._   ,'  ,'        \    \
  (`-.\    .-""        ""'   /          (  d _b
 (`._  `-"" ,._             (            `-(   \
 <_  `     (  <`<            \              `-._\
  <`-       (__< <           :
   (__        (_<_<          ;
    `------------------------------------------
Beautiful!"""


bat = r"""
The bat habitat...
_________________               _________________
 ~-.              \  |\___/|  /              .-~
     ~-.           \ / o o \ /           .-~
        >           \\  W  //           <
       /             /~---~\             \
      /_            |       |            _\
         ~-.        |       |        .-~
            ;        \     /        i
           /___      /\   /\      ___\
                ~-. /  \_/  \ .-~
                   V         V
It's doing fine."""


rabbit = r"""
The rabbit habitat...
         ,
        /|      __
       / |   ,-~ /
      Y :|  //  /
      | jj /( .^
      >-"~"-v"
     /       Y
    jo  o    |
   ( ~T~     j
    >._-' _./
   /   "~"  |
  Y     _,  |
 /| ;-"~ _  l
/ l/ ,-"~    \
\//\/      .- \
 Y        /    Y
 l       I     !
 ]\      _\    /"\
(" ~----( ~   Y.  )
It looks fine!"""


animals = [camel, lion, deer, goose, bat, rabbit]

while True:
    choice = input(
        "Please enter the number of the habitat you would like to view (1-6), "
        "or 'exit' to quit: "
    ).strip()

    if choice.lower() == "exit":
        break

    try:
        number = int(choice)
    except ValueError:
        print("Invalid input. Please enter a number from 1 to 6.")
        continue

    if number < 1 or number > len(animals):
        print("Invalid number. Please enter a number from 1 to 6.")
        continue

    print(animals[number - 1])

print("See you later!")