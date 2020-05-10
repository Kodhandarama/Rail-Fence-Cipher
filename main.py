
from rail_encrypt import RailFenceEncrypt
from rail_decrypt import RailFenceDecrypt

print("Bank Account number 1 :","1234567891")

Bank_account_no1_encrypt=RailFenceEncrypt("1234567891",3)
print("Encrypted Bank account number : ",Bank_account_no1_encrypt)

Bank_account_no1_decrypt=RailFenceDecrypt(Bank_account_no1_encrypt,3)
print("Decrypted Bank account number :",Bank_account_no1_decrypt)


print("Bank Account number 2 :","34545667893")

Bank_account_no2_encrypt=RailFenceEncrypt("34545667893",3)
print("Encrypted Bank account number : ",Bank_account_no2_encrypt)

Bank_account_no2_decrypt=RailFenceDecrypt(Bank_account_no2_encrypt,3)
print("Decrypted Bank account number :",Bank_account_no2_decrypt)


print("Bank Account number 3 :","70293847567")

Bank_account_no3_encrypt=RailFenceEncrypt("70293847567",3)
print("Encrypted Bank account number : ",Bank_account_no3_encrypt)

Bank_account_no3_decrypt=RailFenceDecrypt(Bank_account_no3_encrypt,3)
print("Decrypted Bank account number :",Bank_account_no3_decrypt)


