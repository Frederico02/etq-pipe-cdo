def codigo_impressora3(colaborador):
    if colaborador == 'Arthur':
         colaborador = 'Principe'
    if colaborador == 'Felipe':
         colaborador = 'Felps'

    codigo_zpl ='CT~~CD,~CC^~CT~\n'\
                '^XA~TA000~JSN^LT0^MNW^MTT^PON^PMN^LH0,0^JMA^PR4,4~SD10^JUS^LRN^CI0^XZ\n'\
                '^XA\n'\
                '^MMT\n'\
                '^PW799\n'\
                '^LL0400\n'\
                '^LS0\n'\
                '^FO32,0^GFA,02560,02560,00016,:Z64:eJztVb1qG0EQnltFuuMKRSmMGoNUGhUidZqc4Qwu3BzIuApqXSoQSAqTO1SZPMWV4h7BlR4hLxC4Urg4VCQ4hZL1zu7sb5w2EPAIae/j07czOzszB/Bs/4FlPmStj+N9wDcBz797eNDdBzz3PLCmqT3+wd+AtXNvgwjGPIi4qXxcbn08b308Do+w8XF0CBx0AS4DPAsCmAQBDIMA/shhHQTgpxBg53BZECBqTyzs496fnb1RO7e4h9qJw+Ph08rg8Qd44gCWP1rgASyf3uEmf+eVk5YeLqVBpBMwa9BsAkqOH8trI30kxEXxaqR5JuWigOgGY7X/SieQqWWqE9hTywh+aj5RvNbDDS4rtSAvMpcI/lrrBXEk9IZ/g+qpvgDSv7Y87X8S+Jd8auOT/CSL8wyN/M8rcz5ZgW+3Pc5/XHG+j37L5CFfywaSTVhuY48X+q5r8av0k0rr4UD+hXaNeuUfIF8sRP4y5X9o839N/LtvaACfpL6C2V0jPqDyJ279I9oDgMy/UzU74snU/TlVUz/JS5xgllrFRy8gOxcjgPiafYHbJJlS/cT7wVm+vFgUq1j+n7UsFTysqf6Eqsjh/DIakacNS5CvKJLoMCjy/OL0dPRS8TvGprfJdK1PcgPvj/tnx8WI+se0XaoW03Y0IEzb0YNpOyoP03ZUfrrtdH+buUHlq+eGKf/aX2Mq+zjQ6YvQ+5r2ntGi4ygzN3ysILmY+TeRjmMzftKN/bXM0nQvk8p5rXHEt/SjAxDS1HmDLMXLoXSm27C7n3XO9OtzYV8tBmyPysFLzn85UETQ1S6Olh79bP/OHgEVxemS:B7AD\n'\
                '^FO22,13^GB755,374,8^FS\n'\
                '^FT254,184^A0N,175,172^FH\^FDA/C ^FS\n'\
                '^FT70,347^A0N,162,160^FH\^FD'+ colaborador + '^FS\n'\
                '^PQ1,0,1,Y^XZ\n'
    return codigo_zpl