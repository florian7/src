#!/usr/bin/python3 

from sys import argv 

ascii7 = (
    "<NUL>","<SOH>","<STX>","<ETX>","<EOT>","<END>","<ACK>","<BEL>","<BS>","<HT>","<LF>","<VT>","<FF>","<CR>","<SO>","<SI>",
    "<DCE>","<DC1>","<DC2>","<DC3>","<DC4>","<NAK>","<SYN>","<ETB>","<CAN>","<EM>","<SUB>","<ESC>","<FS>","<GS>","<RS>","<US>",
    " ","!","\"","#","$","%","&","'","(",")","*","+",",","-",".","/",
    "0","1","2","3","4","5","6","7","8","9",":",";","<","=",">","?",
    "@","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O",
    "P","Q","R","S","T","U","V","W","X","Y","Z","[","\\","]","^","_",
    "`","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o",
    "p","q","r","s","t","u","v","w","x","y","z","{","|","}","~","<DEL>")

gsm = (
    "@","£","$","¥","è","é","ù","ì","ò","Ç","<LF>","Ø","ø","<CR>","Å","å",
    "Δ","_","Φ","Γ","Λ","Ω","Π","Ψ","Σ","Θ","Ξ","<ESC>","Æ","æ","ß","É",
    " ","!","\"","#","¤","%","&","'","(",")","*","+",",","-",".","/",
    "0","1","2","3","4","5","6","7","8","9",":",";","<","=",">","?",
    "¡","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O",
    "P","Q","R","S","T","U","V","W","X","Y","Z","Ä","Ö","Ñ","Ü","§",
    "¿","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o",
    "p","q","r","s","t","u","v","w","x","y","z","ä","ö","ñ","ü","à")


def bin_to_int(bits):
    n = 0
    for i in range(len(bits)):
        n += int(bits[i]) * 2 ** (len(bits) - i -1)

    return n

def charset_to_text(bitstring, charset):
    chars = [charset[bin_to_int(bitstring[i:i + 7])] for i in range(0, len(bitstring), 7)]
    text = "".join(chars)

    return text


if len(argv) < 2:
    exit()

if "ascii" in argv[1]:
    charset = ascii7
    bitstrings = argv[2:]

else:
    charset = gsm
    bitstrings = argv[1:]

for bitstring in bitstrings:

    for j in range(7):
        bitstring_s = bitstring[j:] + bitstring[:j]
        bitstring_e = "".join([bitstring_s[k + 4:k + 8] + bitstring_s[k:k + 4] for k in range(0, len(bitstring), 8)])
        bitstring_r = "".join(reversed([bitstring_s[k + 4:k + 8] + bitstring_s[k:k + 4] for k in range(0, len(bitstring), 8)]))
        bitstring_t = "".join(reversed([bitstring_s[k:k + 7] for k in range(0, len(bitstring), 7)]))
        for l in (-1, 1):
            print(charset_to_text(bitstring_r[::l], charset) + "\n")
            print(charset_to_text(bitstring_e[::l], charset) + "\n")
            print(charset_to_text(bitstring_t[::l], charset) + "\n")
            print(charset_to_text(bitstring_s[::l], charset) + "\n")
