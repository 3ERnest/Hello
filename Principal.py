from individo import Individo
print('{:-^74}'.format( '\033[1;32;40m Bem vindo ao Servico de Registo Civil\033[m'))

pessoa = Individo('110104790630A','ERNESTO HERMINIO MACHAVA', '13/07/1997','MAPUTO','HERMINIO MACHAVA',
                     'MARIA CECILIA ERNESTO DJEJDJE','SOLTEIRO','M','Q.24 CASA Nᵒ85 CIDADE DE MAPUTO MAGOANINE"C"',
                       '1.74m','CIDADE DE MAPUTO','14/05/2014','14/05/2019')

print('                    REPÚBLICA DE MOÇAMBIQUE')
print('                      BILHETE DE IDENTIDADE')
print('...' * 32)
print(f'        \033[1;31mNᵒ:{pessoa.numero_de_BI}\033[m ')
print(f'Nome/Name:\033[37m{pessoa.nome}\033[m')
print( f'Data de Nascimento/Birthdate:\033[37m{pessoa.data_de_nascimento}\033[m            Naturalidade/Place of Birth:\033[37m{pessoa.naturalidade} \033[m ')
print(f"Nome do Pai/Father's Name:\033[37m{pessoa.nome_do_pai}\033[m" )
print(f"Nome da Mae/Mother's Name:\033[37m{pessoa.nome_da_mae}\033[m ")
print(f'Estado Civil/Marital State:{pessoa.estado_civil}\033[m                              Sexo/Sex:\033[37m{pessoa.sexo}\033[m')
print(f'Local de Residencia/Address:\033[37m{pessoa.local_de_residencia}\033[m   Altura/Helght:\033[37m{pessoa.altura}\033[m')
print(f'Emitido em/Issued in:\033[37m{pessoa.emitido_em}\033[m')
print(f"Data de emissao/Issuance date:\033[37m{pessoa.data_de_emissao}\033[m                 Valido ate/Expiry date:\033[37m{pessoa.validade_ate}\033[m")
print('...' * 32)
print()

