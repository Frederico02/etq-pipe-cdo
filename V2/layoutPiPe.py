def codigo_impressora(dia_var,hora_atual,codigo,nome,qrcode,ativo,colaborador):
    codigo_zpl = 'CT~~CD,~CC^~CT~ \n'\
                '^XA~TA000~JSN^LT0^MNW^MTT^PON^PMN^LH0,0^JMA^PR4,4~SD10^JUS^LRN^CI0^XZ\n'\
                    '^XA\n'\
                    '^MMT\n'\
                    '^PW799\n'\
                    '^LL0400\n'\
                    '^LS0\n'\
                    '^FO288,32^GFA,02688,02688,00028,:Z64:eJztlTGO2zAQRUkDggJWWSDCVgZS6xTKDbaQokp3cLHsVecUKok5hXMDFylSmHfJnyEpk7aUTZnChKyhZH49/RlzrNR/PPRbGYuxxOgev6rey5iPgytjobuWcUtnCKcvsqpL39V9uFV/x6ld0qpV13LEncr/wmzyGU9PkWeIAURzpqMYG2uRBGsTkH3hjtKILRE/nJY7nfrKJM9Qf8l4Cd4yCjqX6yJ8GIdO1cPYJx0mQ9ItWGXIFLow1f7ndFZH3wDzwKMZiTGOl4Py6cab2QusNSfY4pxa+INZ2NWnpFuQPrNwJg8OL413hx7PPl5wAIOIq+qqPcaZ80mzEZ0THa9fdWpUr284UDZEXNV9PWJ0XEfhrLxCt/J84M1/56lVZ2Eu+EMUf+qb7Tqpo3DanLfWfcNfyOfKawue5JPjoBr4YzuIuEr1q/p/4E3n5O+e53Z48FedUMLcn7bxdwoOdPMe7zfzdvyJbssfV0xJuVL9+Bz2IfGKXR6efPM3l7zDHk+Lo9Kfuvn7mLftj38h2/6kYmOsn76vX9BFnsrfM+yAuazf+YHn7nVhx7EdPqK/bvVH4RQPF1pc4Gn/IpjKfz7KRE2Xl8hT9EOWH8ihy4iOTNx/GtuNy1Uh9lK313X/8b6RdkkUdQbtLfHQ0qoQL8I5YpJ4cTlxN8x0XCtr34Mt7qI8qawUlHntbXns87FPoDc3wOgrRxSOJxrtm2MbWrr8/Ujz5Q+nNjXi53iO5/ho/AFuAH62:7BBA\n'\
                    '^FO17,18^GB761,367,8^FS\n'\
                    '^FT30,155^A0N,50,50^FH\^FDPIPE:'+ codigo +' ^FS\n'\
                    '^FT30,218^A0N,50,50^FH\^FDNOME:'+ nome +'^FS\n'\
                    '^FT30,281^A0N,50,50^FH\^FDQRCODE:'+ qrcode +'^FS\n'\
                    '^FT30,340^A0N,50,50^FH\^FDATIVO:'+ ativo +'^FS\n'\
                    '^FT478,371^A0N,43,45^FH\^FDResp.: '+ colaborador + '^FS\n'\
                    '^FT639,76^A0N,20,19^FH\^FD' + dia_var +'^FS\n'\
                    '^FT633,100^A0N,20,19^FH\^FD' + hora_atual + '^FS\n'\
                    '^PQ1,0,1,Y^XZ\n'
    return codigo_zpl
