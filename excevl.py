import os
import time
import base64
import marshal
import zlib
import platform
import datetime

# Import modul random
import random
from random import randint
# Import modul rich
from rich.panel import Panel
from rich import print as tulis
from rich import print

Hitam = "\u001b[30m"
Merah = "\u001b[31m"
Hijau = "\u001b[32m"
Kuning = "\u001b[33m"
Orange = "\u001b[38;5;208m"
Biru = "\u001b[34m"
Biru_muda = "\u001b[36m"
Pink = "\u001b[38;5;205m"
Violet = "\u001b[35m"
Abu = "\u001b[90m"
Orange_muda = "\u001b[38;5;214m"
Putih = "\u001b[37m"

# Kode warna ANSI
Z2 = "[#000000]"  # Hitam
M2 = "[#FF0000]"  # Merah
H2 = "[#00FF00]"  # Hijau
K2 = "[#FFFF00]"  # Kuning
B2 = "[#00C8FF]"  # Biru
U2 = "[#AF00FF]"  # Ungu
N2 = "[#FF00FF]"  # Pink
O2 = "[#00FFFF]"  # Biru Muda
P2 = "[#FFFFFF]"  # Putih
J2 = "[#FF8F00]"  # Jingga
A2 = "[#AAAAAA]"  # Abu-Abu
T2 = "[#FFA500]"  # Oranye

variable_value = "__import__('marshal').loads;__import__('zlib').decompress;__import__('base64).b64encode" * 140  # Gantilah ini dengan nilai yang Anda inginkan

class ____LambdaObfuscators____:
    def __init__(self):
        current_time = datetime.datetime.now()
        current_time_str = current_time.strftime("%A, %B %d, %Y %H:%M:%S")
        self.mzb = f'''
# Time : {current_time_str}
# Platform : {platform.system()}-{platform.machine()}
# Obfuscated by : Ferly Afriliyan (Ryougaa Hideki)

Ryougaa_ = (\n'''
        denventa_lines = [f'"{variable_value}", "=(:__:-_= __, lambda c; _ = ,__ .", "import", "as", "from", "marshal", "zlib", "base64", "(eval((lambda ____,__,_ : ____.join([_(___) for ___ in __]))(,[95, 95, 105, 109, 112, 111, 114, 116, 95, 95, 40, 39, 109, 97, 114, 115, 104, 97, 108, 39, 41, 46, 108, 111, 97, 100, 115],chr))(eval((lambda ____,__,_ : ____.join([_(___) for ___ in __]))(,[95, 95, 105, 109, 112, 111, 114, 116, 95, 95, 40, 34, 122, 108, 105, 98, 34, 41, 46, 100, 101, 99, 111, 109, 112, 114, 101, 115, 115],chr))(eval((lambda ____,__,_ : ____.join([_(___) for ___ in __]))(,[95, 95, 105, 109, 112, 111, 114, 116, 95, 95, 40, 34, 98, 97, 115, 101, 54, 52, 34, 41, 46, 98, 54, 52, 100, 101, 99, 111, 100, 101],chr))"' for _ in range(150, 4444)]

        self.mzb += ',\n'.join(denventa_lines)
        self.mzb += f'''\n)

# Time : {current_time_str}
# Platform : {platform.system()}-{platform.machine()}
# Obfuscated by : Ferly Afriliyan (Ryougaa Hideki)

# Variable teks : {len(denventa_lines)} Line
Ryougaa_Hidekii__=(eval((lambda ____,__,_ : ____.join([_(___) for ___ in __]))('',[95, 95, 105, 109, 112, 111, 114, 116, 95, 95, 40, 39, 109, 97, 114, 115, 104, 97, 108, 39, 41, 46, 108, 111, 97, 100, 115],chr))(eval((lambda ____,__,_ : ____.join([_(___) for ___ in __]))('',[95, 95, 105, 109, 112, 111, 114, 116, 95, 95, 40, 34, 122, 108, 105, 98, 34, 41, 46, 100, 101, 99, 111, 109, 112, 114, 101, 115, 115],chr))(eval((lambda ____,__,_ : ____.join([_(___) for ___ in __]))('',[95, 95, 105, 109, 112, 111, 114, 116, 95, 95, 40, 34, 98, 97, 115, 101, 54, 52, 34, 41, 46, 98, 54, 52, 100, 101, 99, 111, 100, 101],chr))(%s))));exec(Ryougaa_Hidekii__)

Hidekii_ = (\n'''
        denventa_lines = [f'"{variable_value}", "=(:__:-_= __, lambda c; _ = ,__ .", "import", "as", "from", "marshal", "zlib", "base64", "(eval((lambda ____,__,_ : ____.join([_(___) for ___ in __]))(,[95, 95, 105, 109, 112, 111, 114, 116, 95, 95, 40, 39, 109, 97, 114, 115, 104, 97, 108, 39, 41, 46, 108, 111, 97, 100, 115],chr))(eval((lambda ____,__,_ : ____.join([_(___) for ___ in __]))(,[95, 95, 105, 109, 112, 111, 114, 116, 95, 95, 40, 34, 122, 108, 105, 98, 34, 41, 46, 100, 101, 99, 111, 109, 112, 114, 101, 115, 115],chr))(eval((lambda ____,__,_ : ____.join([_(___) for ___ in __]))(,[95, 95, 105, 109, 112, 111, 114, 116, 95, 95, 40, 34, 98, 97, 115, 101, 54, 52, 34, 41, 46, 98, 54, 52, 100, 101, 99, 111, 100, 101],chr))"' for _ in range(150, 4444)]

        self.mzb += ',\n'.join(denventa_lines)
        self.mzb += f'''\n)'''

    def encrypt_file(self, input_file, output_file, count):
        try:
            __Fer = open(input_file, 'rb').read()
            __com = compile(__Fer, '<Ryougaacoli>', 'exec')
            __Cum__ = repr(base64.b64encode(zlib.compress(marshal.dumps(__com))))

            with open(output_file, 'w') as f:
                f.write(self.mzb % __Cum__)

            total_iterations = count
            current_iteration = 0

            while current_iteration < total_iterations:
                obf__ = open(output_file, 'rb').read()
                ___zlb__ = compile(obf__, '<Ryougaacoli>', 'exec')
                ___mars___ = repr(base64.b64encode(zlib.compress(marshal.dumps(___zlb__))))

                with open(output_file, 'w') as f:
                    f.write(self.mzb % ___mars___)

                current_iteration += 1
                loading_percentage = (current_iteration / total_iterations) * 100
                print(f"Encrypting: [{loading_percentage:.2f}%]", end='\r')
                time.sleep(0.00)

            print(f"\n{H2}[{A2}!!{H2}]{P2} Berhasil, File tersimpan di {A2}: {output_file}")
            exit()
        except Exception as e:
            print(f"{M2}[{A2}•{M2}]{P2} Error : {P2}\n└──>{M2}[{A2}•{M2}] {P2}Isi Yang Benar {M2}!")
            
if __name__ == "__main__":
    encryptor = ____LambdaObfuscators____()
    os.system("clear")
    tulis(Panel("""[#00BFFF]    ╔═╗┬  ┬┌─┐┬   ┌─┐┌┐ ┌─┐  [#808080]Python3 with lambda[#00BFFF]
    ║╣ └┐┌┘├─┤│───│ │├┴┐├┤   
    ╚═╝ └┘ ┴ ┴┴─┘ └─┘└─┘└    
        """, title='[#FF8F00][ [#00FF33]By Ferly Afriliyan [#FF8F00]]',
        subtitle='[#FF8F00][ [#00FF33]Obfuscate Your Python File [#FF8F00]]', style='#FFFFFF'))
    input_file = input(f"└──>{Hijau}[{Abu}•{Hijau}]{Putih} Input File {Abu}: {Putih}")
    count = int(input(f"     └──>{Biru}[{Abu}+{Biru}]{Putih} Count {Orange_muda}({Putih}Ex{Orange_muda}) •4• : {Putih}"))
    
    if count < 300:
        output_file = input(f"     └──>{Hijau}[{Abu}•{Hijau}]{Putih} Output File {Abu}: {Putih}")
        encryptor.encrypt_file(input_file, output_file, count)
    else:
        print(f"{B2}[{A2}!{B2}]{P2} Count must be < 300")
