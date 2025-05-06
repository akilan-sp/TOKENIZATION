# 🔐 **TOKENIZATION**

## 💡 **Overview**

The **Tokenized Data Access System** securely stores and retrieves sensitive data by **tokenizing** it and **encrypting** it using the **Fernet** encryption algorithm. This system ensures that sensitive information is never stored in plaintext, improving data privacy and security. The system uses unique tokens to retrieve the original data when needed, ensuring that the actual data is not exposed in the database.

---

## ⚙️ **Technologies Used**

- **Python**: The main programming language used for implementing the system.
- **PostgreSQL**: Database System to Store Sensitive Data. 
- **psycopg2**: PostgreSQL database connector for Python.
- **cryptography**: Used to encrypt and decrypt Sensitive Data.
- **UUID**: For generating Unique Tokens to represent the Sensitive Data.

---

## 🏗️ **Features**

- **Tokenization**: Converts sensitive data into a secure token, which is then stored in the database.
- **Encryption**: Encrypts sensitive data using **Fernet encryption** before storing it, ensuring that data is securely handled.
- **Detokenization**: Allows users to retrieve the original data using the token.
- **Database Storage**: The system uses a PostgreSQL database to store the tokens and their associated encrypted data, ensuring secure data management.

---

## 🚀 **Setup and Usage**

### 1. **Install Dependencies**

Make sure Python is installed. Then, install the necessary libraries:

```bash
pip install psycopg2 cryptography
```
### 2. **Set Up PostgreSQL**
Ensure you have a PostgreSQL database named tokenization and create the following table schema:

```bash
CREATE TABLE sensitive_data (
    token VARCHAR(255) PRIMARY KEY,
    encrypted_data BYTEA
);
````
### 3. **Download the Script**
You can download the Python script by clicking the link below:

Download [tokenization.py](tokenization.py)

### 4. **Running the Program**
To start using the system, simply run the script:

```bash
python tokenization.py
```
This will present you with the following options:
- Store Sensitive Data: Enter the data you want to tokenize, and it will be securely stored in the database.

- Retrieve Data with Token: Enter a previously generated token to retrieve the original data.

- Exit: Exit the program.

## 💻 **Example Usage**
Storing Data:

```bash
Enter the sensitive data to tokenize: MySuperSecretPassword123
Data successfully stored! Use this token to retrieve your data: 4fd4bc...
```
Retrieving Data:

```bash
Enter the token to retrieve the original data: 4fd4bc...
Retrieved Data: MySuperSecretPassword123
```
## 🔒 **Security Considerations**
- Data Encryption: Sensitive data is encrypted using Fernet symmetric encryption to ensure that the data is not stored in plaintext.

- Tokenization: Tokens are used to reference sensitive data, eliminating the risk of plaintext exposure in the database. The actual sensitive data is only accessible through the token, which is required for decryption.
