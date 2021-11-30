import CipherAtbash, CipherMorse, CipherNeco, CipherPigLatin, CipherROT13, CipherTapcode

print(CipherAtbash.atbash("Hello world"))
print(CipherAtbash.atbash(CipherAtbash.atbash("Hello world")))

print("")

print(CipherMorse.encode("Hello world"))
print(CipherMorse.decode(CipherMorse.encode("Hello world")))

print("")

print(CipherNeco.encode("Hello world", "Python"))

print("")

print(CipherPigLatin.encode("Hello world"))

print("")

print(CipherROT13.rot13("Hello world"))
print(CipherROT13.rot13(CipherROT13.rot13("Hello world")))

print("")

print(CipherTapcode.encode("Hello world"))
print(CipherTapcode.decode(CipherTapcode.encode("Hello world")))