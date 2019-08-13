import requests
import hashlib
import json

url = 'https://api.codenation.dev/v1/challenge/dev-ps/generate-data'
url_submit = 'https://api.codenation.dev/v1/challenge/dev-ps/submit-solution'
my_token = 'token'

def decrypt(encrypted, shift_size):
    decrypted = ''
    letter_a_ascii = 97
    letter_z_ascii = 122
    number_of_letters = 26

    for i in range( len(encrypted) ):
        current_ascii = ord(encrypted[i])
        
        if current_ascii >= letter_a_ascii and current_ascii <= letter_z_ascii:
            new_ascii = current_ascii - shift_size
            if new_ascii < letter_a_ascii:
                new_ascii += number_of_letters
            decrypted += chr(new_ascii)
        else:
            decrypted += encrypted[i]

    return decrypted

response = requests.get(url, params={'token': my_token})
json_response = response.json()

json_response['decifrado'] = decrypt(json_response['cifrado'], json_response['numero_casas'])
json_response['resumo_criptografico'] = hashlib.sha1(json_response['decifrado'].encode()).hexdigest()

print(json_response['numero_casas'])
print(json_response['token'])
print(json_response['cifrado'])
print(json_response['decifrado'])
print(json_response['resumo_criptografico'])

file = {'answer': json.dumps(json_response, ensure_ascii=False)}
response_post = requests.post(url_submit, params={'token': my_token}, files=file)
print(response_post)
print(response_post.content)

