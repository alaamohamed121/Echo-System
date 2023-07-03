from dataclasses import replace
from art import *

about = tprint("welcome    sir")
print("""
      E <= encurption
      U <= unencurption
      n <= exit
      """)
#user_opthion = input("what do u make : E OR U or n: ").capitalize()


# define letters


def encurption():
    # user input
    user_input = input("please enter the text :").lower()

    # define letters
    a = user_input.replace("a", "!@")
    b = a.replace("b", ";*")
    c = b.replace("c", "''%")
    d = c.replace("d", "'.$")
    e = d.replace("e", "(*)%")
    f = e.replace("f", "*%*")
    g = f.replace("g", "*&*&")
    h = g.replace("h", "+__-")
    i = h.replace("i", "+^__")
    j = i.replace("j", "^_%__")
    k = j.replace("k", "+&%--")
    l = k.replace("l", "%#")
    m = l.replace("m", "!#%")
    n = m.replace("n", "@%@!")
    o = n.replace("o", "(&)")
    p = o.replace("p", "()%")
    q = p.replace("q", "%(!)")
    r = q.replace("r", "(!&)")
    s = r.replace("s", "__%$$")
    t = s.replace("t", "_-^^")
    u = t.replace("u", "*$%^^")
    v = u.replace("v", "(!(!")
    w = v.replace("w", "!%!)")
    x = w.replace("x", "($*)")
    y = x.replace("y", "(++)")
    z = y.replace("z", "(==)")
    space = z.replace(" ", " ")
#    define numbers

    n_1 = space.replace("1", "--")
    n_2 = n_1.replace("2", "__")
    n_3 = n_2.replace("3", "&&")
    n_4 = n_3.replace("4", "!!")
    n_5 = n_4.replace("5", "&&!")
    n_6 = n_5.replace("6", "(^$)")
    n_7 = n_6.replace("7", "&@%")
    n_8 = n_7.replace("8", "(_=)")
    n_9 = n_8.replace("9", "^!^")
    n_0 = n_9.replace("0", "(^^)")
    print("ur encruption is done :")
    print(n_0)


def unti_encurption():
    # user input
    user_input = input("please enter the text :").lower()
    # define unti_encurption letters from a to z
    u_a = user_input.replace("!@", "a")
    u_b = u_a.replace(";*", "b")
    u_c = u_b.replace("''%", "c")
    u_d = u_c.replace("'.$", "d")
    u_e = u_d.replace("(*)%", "e")
    u_f = u_e.replace("*%*", "f")
    u_g = u_f.replace("*&*&", "g")
    u_h = u_g.replace("+__-", "h")
    u_i = u_h.replace("+^__", "i")
    u_j = u_i.replace("^_%__", "j")
    u_k = u_j.replace("+&%--", "k")
    u_l = u_k.replace("%#", "l")
    u_m = u_l.replace("!#%", "m")
    u_n = u_m.replace("@%@!", "n")
    u_o = u_n.replace("(&)", "o")
    u_p = u_o.replace("()%", "p")
    u_q = u_p.replace("%(!)", "q")
    u_r = u_q.replace("(!&)", "r")
    u_s = u_r.replace("__%$$", "s")
    u_t = u_s.replace("_-^^", "t")
    u_u = u_t.replace("*$%^^", "u")
    u_v = u_u.replace("(!(!", "v")
    u_w = u_v.replace("!%!)", "w")
    u_x = u_w.replace("($*)", "x")
    u_y = u_x.replace("(++)", "y")
    u_z = u_y.replace("(==)", "z")
    space_1 = u_z.replace(" ", " ")
    # define encurption numbers
    n_1u = space_1.replace("--", "1")
    n_2u = n_1u.replace("__", "2")
    n_3u = n_2u.replace("&&", "3")
    n_4u = n_3u.replace("!!", "4")
    n_5u = n_4u.replace("&&!", "5")
    n_6u = n_5u.replace("(^$)", "6")
    n_7u = n_6u.replace("&@%", "7")
    n_8u = n_7u.replace("(_=)", "8")
    n_9u = n_8u.replace("^!^", "9")
    n_0u = n_9u.replace("(^^)", "0")
    print("ur encruption is done :")
    print(n_0u)


while True:

    user_opthion = input("what do u make : E OR U or N: ").capitalize()
    if user_opthion == "E":
        encurption()
    elif user_opthion == "U":

        unti_encurption()

    elif user_opthion == "N":
        print("see u later")
        exit()

    else:
        print("wrong choise, please try again")
