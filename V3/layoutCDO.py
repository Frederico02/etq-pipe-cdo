def codigo_impressora2(dia_var,hora_atual,codigo,nome,qrcode,ativo,colaborador):
    codigo_zpl = 'CT~~CD,~CC^~CT~\n'\
                '^XA~TA000~JSN^LT0^MNW^MTT^PON^PMN^LH0,0^JMA^PR4,4~SD10^JUS^LRN^CI0^XZ\n'\
                '^XA\n'\
                '^MMT\n'\
                '^PW799\n'\
                '^LL0400\n'\
                '^LS0\n'\
                '^FO288,0^GFA,02688,02688,00028,:Z64:eJztlD1uwzAMhRUFWlQgU30JG8gBMvkIHqz76ChCJyMGPAeeepSMQhHoDH2kLP+0SjJ1agSDTGA/PX+iSSFe67X++ZI2Zpu5p2LaNZl72kX5JXOvqKM8pzteOR1uD3Qtp5Iczum9Kic0fr91/EamoVAvOlUnnQ5+CsnvAEvN/5Vpp5B0ZBn5ynGcAq+To0sIxiyMmcJaNxmEYGNY+8VlSGLyuvIDbNVHbxc+N+uEmcJvXbCDRQhWwsbDTw9fZyv9pKs50NG3EOGdTR35RnuyHKhkI+BO4zi6WD9D+yNQyXazLtYv2OMnBXuARYAfWMP14Fc6k9NVFkhnJCoZsqv6vnf7Luu3K5r0vcDqypDJj89TbvzqpONzUYnPEdfMx/Vb+PD88p4rXbDYHz5bP+2f6Uqrt3xcP9mtdMU9PxnE8Mgvz6edvMunmgd+Xv7iS/VjXZYPYG6/4cMlUv2e+N1+8smN3x2+C2iYTzJfueVr7tbPY/ej1Tcho59fzlM1ivggUqxTzVI/2aFalQWkjvXrlvqpFk8VmDECXybp2sVPhsELasKv4NkvDNfktzMYTdSElEk398NoJfpNUBNydkKu+g86QPGwYDjaJ/kJ9Bv4pkmDwwzBJz/BE4aGmonzc/YrUcIzlVHse+Q3HGaV+u89whRxtvCcB2l2zr/Wn61vk2ci7Q==:7980\n'\
                '^FO20,14^GB758,368,8^FS\n'\
                '^FT35,152^A0N,50,50^FH\^FDCHAMADO:'+ codigo +'^FS\n'\
                '^FT35,204^A0N,50,50^FH\^FDNOME:'+ nome +'^FS\n'\
                '^FT35,262^A0N,50,50^FH\^FDQRCODE:'+ qrcode +'^FS\n'\
                '^FT35,317^A0N,50,50^FH\^FDATIVO:'+ ativo +'^FS\n'\
                '^FT590,59^A0N,26,26^FH\^FD' + dia_var +'^FS\n'\
                '^FT590,87^A0N,26,26^FH\^FD' + hora_atual + '^FS\n'\
                '^FT477,364^A0N,43,43^FH\^FDResp.:'+ colaborador + '^FS\n'\
                '^PQ1,0,1,Y^XZ\n'
    return codigo_zpl