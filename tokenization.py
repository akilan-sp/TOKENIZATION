import psycopg2
import uuid
from cryptography.fernet import Fernet

key = Fernet.generate_key()
cipher_suite = Fernet(key)

def connect_to_db():
    try:
        conn = psycopg2.connect(
            dbname="tokenization",
            user="postgres",  
            password="pgadmin",  
            host="localhost",
            port="5432"
        )
        return conn
    except Exception as e:
        print(f"Error connecting to database: {e}")
        return None

def tokenize_data(sensitive_info):
    token = uuid.uuid4().hex  
    encrypted_data = cipher_suite.encrypt(sensitive_info.encode()) 
    
    conn = connect_to_db()
    if conn:
        try:
            cursor = conn.cursor()
            cursor.execute("INSERT INTO sensitive_data (token, encrypted_data) VALUES (%s, %s)", 
                           (token, encrypted_data))
            conn.commit()
            conn.close()
            print(f"Data successfully stored! Use this token to retrieve your data: {token}")
            return token
        except Exception as e:
            print(f"Error inserting data: {e}")
            conn.rollback()
        finally:
            conn.close()
    return None

def detokenize_data(token):
    conn = connect_to_db()
    if conn:
        try:
            cursor = conn.cursor()
            cursor.execute("SELECT encrypted_data FROM sensitive_data WHERE token = %s", (token,))
            result = cursor.fetchone()
            conn.close()
            if result:
                encrypted_bytes = bytes(result[0])  
                decrypted_data = cipher_suite.decrypt(encrypted_bytes).decode()  
                return decrypted_data
            else:
                print("Invalid token! No matching data found.")
        except Exception as e:
            print(f"Error retrieving data: {e}")
    return None

if __name__ == "__main__":
    while True:
        print("\nOptions:")
        print("1. Store Sensitive Data")
        print("2. Retrieve Data with Token")
        print("3. Exit")
        
        choice = input("Select an option (1/2/3): ").strip()
        
        if choice == "1":
            sensitive_info = input("Enter the sensitive data to tokenize: ").strip()
            tokenize_data(sensitive_info)
        
        elif choice == "2":
            token = input("Enter the token to retrieve the original data: ").strip()
            original_data = detokenize_data(token)
            if original_data:
                print(f"Retrieved Data: {original_data}")
        
        elif choice == "3":
            print("Exiting...")
            break
        
        else:
            print("Invalid choice. Please select 1, 2, or 3.")