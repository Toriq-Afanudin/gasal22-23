'''Type Hints pada Fungsi'''
# Bentuk standar fungsi yang sudah kita pelajari

'''
def fungsi(parameter):
    hasil = parameter**2
    print(hasil)


fungsi(3)
fungsi("Ucup")
'''


def fungsi_dengan_hints(argument: int):
    output = argument**2
    return output


hasil = fungsi_dengan_hints(8)
print(hasil)


def display(argument: str):
    print(f"Halo {argument}")


display("Ucup")
