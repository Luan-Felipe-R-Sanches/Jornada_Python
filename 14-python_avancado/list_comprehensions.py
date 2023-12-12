# Lista de emails com diferentes formatos e espaços em branco
emails = [
    ',henRy@gmail.com',
    ' ,juLIa@hotmail.com  ',
    'ivaN@gmail.com ',
    'mar,coS@yahoo.com.br ',
    '  SandovAL@hotmail.com',
    'IVANA@gmail.com',
    'ItamaR@edu.gov.b'
]

# Tratamento dos emails: remoção de espaços em branco no início e final,
# remoção de vírgulas e conversão para letras minúsculas
emails_tratados = [email.strip().replace(",", "").lower() for email in emails]

# Filtragem apenas dos emails do domínio 'gmail' na lista tratada de emails
emails_tratados_gmail = [email.strip().replace(",", "").lower() for email in emails if '@gmail' in email]

# Imprimir a lista de emails tratados e a lista de emails do domínio 'gmail'
print(emails_tratados)
print(emails_tratados_gmail)
