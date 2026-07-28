# Authentication & Security (with Real Examples)

....................................................................

# 1. What is Authentication?

## Definition

**Authentication** is the process of verifying the identity of a user before allowing access to an application or system.

It answers the question:

> **"Who are you?"**

### Exam Definition

> Authentication is the process of verifying the identity of a user using credentials such as a username and password, OTP, or biometric data.

### Real-Life Example

When you log in to your Gmail account:

1. Enter your username.
2. Enter your password.
3. Gmail verifies your credentials.
4. If they are correct, you are logged in.

```text
User
   │
Username + Password
   │
   ▼
Authentication Server
   │
Credentials Verified
   │
   ▼
Access Granted
```

....................................................................

# 2. What is Authorization?

## Definition

**Authorization** determines what an authenticated user is allowed to do.

It answers the question:

> **"What are you allowed to access?"**

### Real-Life Example

In a college portal:

* Student → View marks only
* Teacher → Enter and edit marks
* Admin → Manage users and departments

```text
User Logged In
      │
      ▼
Check Role
      │
 ┌────┴────┐
 ▼         ▼
Student   Admin
View      Full Access
```

### Authentication vs Authorization

| Authentication      | Authorization                |
| ------------------- | ---------------------------- |
| Verifies identity   | Verifies permissions         |
| Happens first       | Happens after authentication |
| Example: Login      | Example: Access control      |
| Username & Password | User Roles                   |

....................................................................

# 3. Authentication Methods

## A. Username and Password

The most common authentication method.

### Example

```text
Username : king123
Password : ********
```

### Real-Life Example

Logging into Facebook or Instagram.

..................................................................

## B. One-Time Password (OTP)

A temporary password sent to a mobile number or email.

### Example

```text
OTP : 482731
```

Valid only for a short period.

### Real-Life Example

Internet banking sends an OTP before completing a transaction.

..................................................................

## C. Biometric Authentication

Uses physical characteristics.

Examples:

* Fingerprint
* Face Recognition
* Iris Scan

### Real-Life Example

Unlocking a smartphone using your fingerprint.

..................................................................

## D. Multi-Factor Authentication (MFA)

Uses two or more authentication methods.

Example:

```text
Username + Password
        │
        ▼
OTP
        │
        ▼
Login Success
```

### Real-Life Example

Google Account Login:

* Password
* OTP sent to mobile

....................................................................

# 4. Session-Based Authentication

## Definition

After successful login, the server creates a session and stores user information.

### Workflow

```text
User Login
     │
     ▼
Server Creates Session
     │
Session ID
     │
     ▼
Browser Stores Session Cookie
```

### Real-Life Example

An online shopping website remembers that you are logged in while browsing different pages.

### Advantages

* Simple to implement
* Suitable for traditional web applications

### Disadvantages

* Requires server-side session storage
* Harder to scale across multiple servers

....................................................................

# 5. Token-Based Authentication

## Definition

Instead of storing a session on the server, the server issues a **token** after successful login.

The client sends this token with every request.

### Workflow

```text
Login
   │
   ▼
Server Generates Token
   │
   ▼
Client Stores Token
   │
Every Request
Authorization: Bearer Token
```

### Real-Life Example

Mobile banking apps use tokens to verify each API request.

### Advantages

* Stateless
* Easy to scale
* Suitable for REST APIs

....................................................................

# 6. JWT (JSON Web Token)

## Definition

**JWT (JSON Web Token)** is a secure token format used for authentication and authorization in REST APIs.

A JWT contains:

* Header
* Payload
* Signature

### Structure

```text
Header.Payload.Signature
```

### Example

```text
eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.
eyJ1c2VySWQiOjEwMSwicm9sZSI6IkFkbWluIn0.
SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c
```

### JWT Authentication Flow

```text
User Login
     │
     ▼
JWT Generated
     │
     ▼
Client Stores JWT
     │
Authorization: Bearer JWT
     │
     ▼
Protected API
```

### Real-Life Example

A shopping app sends a JWT with every request to access the user's cart and orders.

....................................................................

# 7. Password Hashing

## Definition

Passwords should never be stored as plain text. They are converted into a secure hash before storage.

### Example

Plain Password

```text
password123
```

Stored in Database

```text
$2b$12$AbCdEfGhIjKlMnOpQrStUvWxYz...
```

### Common Hashing Algorithms

* bcrypt
* Argon2
* PBKDF2

### Real-Life Example

When creating a Gmail account, Google stores a hashed version of your password rather than the actual password.

....................................................................

# 8. HTTPS

## Definition

**HTTPS (HyperText Transfer Protocol Secure)** encrypts data transmitted between the client and server using SSL/TLS.

### HTTP

```text
Browser
    │
Plain Text
    │
Server
```

### HTTPS

```text
Browser
    │
Encrypted Data
    │
Server
```

### Real-Life Example

Online banking websites use HTTPS to protect passwords and payment details.

### Advantages

* Encrypts communication
* Prevents data theft
* Builds user trust

....................................................................

# 9. Common Web Security Threats

## A. SQL Injection

Attackers insert malicious SQL into input fields.

### Example

Unsafe SQL:

```sql
SELECT * FROM users WHERE username='admin';
```

### Prevention

* Parameterized queries
* ORM (SQLAlchemy, Django ORM)
* Input validation

### Real-Life Example

A login form that directly inserts user input into an SQL query can be exploited.

..................................................................

## B. Cross-Site Scripting (XSS)

Attackers inject malicious JavaScript into web pages.

### Example

```html
<script>alert("Hacked")</script>
```

### Prevention

* Escape HTML output
* Validate user input
* Use Content Security Policy (CSP)

### Real-Life Example

A comment section allowing JavaScript execution could display malicious pop-ups.

..................................................................

## C. Cross-Site Request Forgery (CSRF)

An attacker tricks a logged-in user into performing unwanted actions.

### Example

A logged-in user unknowingly clicks a malicious link that transfers money.

### Prevention

* CSRF tokens
* SameSite cookies
* Re-authentication for sensitive actions

..................................................................

## D. Brute Force Attack

Attackers repeatedly try different passwords until one works.

### Prevention

* Account lockout
* CAPTCHA
* Rate limiting
* Multi-Factor Authentication

....................................................................

# 10. Security Best Practices

* Use HTTPS for all communication.
* Hash passwords using bcrypt or Argon2.
* Enable Multi-Factor Authentication (MFA).
* Validate all user input.
* Use parameterized SQL queries or an ORM.
* Store secrets (API keys, passwords) in environment variables.
* Keep software and dependencies updated.
* Apply role-based access control (RBAC).
* Use secure session management.
* Monitor logs for suspicious activity.

....................................................................

# 11. Authentication Workflow

```text
User
   │
Enter Username & Password
   │
   ▼
Authentication Server
   │
Credentials Verified
   │
   ▼
Generate Session / JWT Token
   │
   ▼
User Accesses Protected Resources
```

....................................................................

# 12. Real-World Example – Online Banking

```text
Customer
     │
Username + Password
     │
     ▼
Authentication
     │
     ▼
OTP Verification
     │
     ▼
JWT / Session Created
     │
     ▼
Access Account
     │
     ▼
HTTPS Encrypts Communication
```

The customer can securely view account details, transfer money, and pay bills.

....................................................................

# Summary Table

| Concept                  | Purpose                       | Real-Life Example     |
| ------------------------ | ----------------------------- | --------------------- |
| Authentication           | Verify user identity          | Gmail Login           |
| Authorization            | Control user permissions      | Admin dashboard       |
| Session Authentication   | Store login session on server | Shopping website      |
| Token Authentication     | Authenticate using tokens     | Mobile banking app    |
| JWT                      | Secure token for REST APIs    | Shopping app          |
| Password Hashing         | Protect stored passwords      | Google account        |
| HTTPS                    | Encrypt communication         | Online banking        |
| SQL Injection Protection | Prevent database attacks      | Secure login form     |
| XSS Protection           | Prevent malicious scripts     | Safe comment section  |
| CSRF Protection          | Prevent unauthorized requests | Secure money transfer |

....................................................................

# Interview / Exam Questions

### 1. What is authentication?

Authentication is the process of verifying a user's identity before granting access to a system.

### 2. What is the difference between authentication and authorization?

Authentication verifies **who the user is**, while authorization determines **what the user is allowed to access**.

### 3. What is JWT?

JWT (JSON Web Token) is a compact, secure token format used for authentication and authorization in REST APIs.

### 4. Why should passwords be hashed?

Hashing protects passwords by storing an irreversible encrypted representation instead of the original password, reducing the risk if the database is compromised.

### 5. What is HTTPS?

HTTPS is the secure version of HTTP that encrypts communication between the client and server using SSL/TLS.

### 6. Name four common web security threats.

* SQL Injection
* Cross-Site Scripting (XSS)
* Cross-Site Request Forgery (CSRF)
* Brute Force Attack

....................................................................

# Key Points to Remember

* **Authentication** = Verifies identity (**Who are you?**)
* **Authorization** = Verifies permissions (**What can you access?**)
* **JWT** is widely used for securing REST APIs.
* **HTTPS** encrypts data exchanged between client and server.
* **Passwords should always be hashed**, not stored in plain text.
* Protect applications from **SQL Injection, XSS, CSRF, and Brute Force attacks** using secure coding practices and authentication mechanisms.

