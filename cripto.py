import requests

def decrypt(encrypted, shift_size):
    decrypted = ''
    letter_a_ascii = 97
    letter_z_ascii = 122
    number_of_letters = 26

    for i in range( len(encrypted) ):
        current_ascii = ord(encrypted[i])
        
        if current_ascii >= letter_a_ascii and current_ascii <= letter_z_ascii:
            new_ascii = current_ascii + shift_size
            if new_ascii > letter_z_ascii:
                new_ascii -= number_of_letters
            decrypted += chr(new_ascii)
        else:
            decrypted += encrypted[i]

    return decrypted

url = 'https://api.codenation.dev/v1/challenge/dev-ps/generate-data'
my_token = '4646090ebb3fd4037ecb08134825732b36e73e84'

response = requests.get(url, params={'token': my_token})
json_response = response.json()

json_response['decifrado'] = decrypt(json_response['cifrado'], json_response['numero_casas'])
print(json_response['numero_casas'])
print(json_response['token'])
print(json_response['cifrado'])
print(json_response['decifrado'])
print(json_response['resumo_criptografico'])


