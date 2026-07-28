# JWT Tokens, OAuth2 Flow, Session-Based Authentication, Password Hashing, CORS, Common Vulnerabilities (OWASP Top 10)

....................................................................

# 1. JWT Tokens (JSON Web Tokens)

## Definition

**JWT (JSON Web Token)** is a compact and secure method used for transmitting information between a client and server as a JSON object.

JWT is commonly used for **authentication and authorization** in REST APIs.

### Exam Definition

> JWT is a token-based authentication mechanism where the server generates a signed token after successful login, and the client sends this token with future requests.

....................................................................

# JWT Structure

A JWT contains three parts:

```text
Header.Payload.Signature
```

Example:

```text
xxxxx.yyyyy.zzzzz
```

### 1. Header

Contains information about the token type and encryption algorithm.

Example:

```json
{
  "alg": "HS256",
  "typ": "JWT"
}
```

..................................................................

### 2. Payload

Contains user information and claims.

Example:

```json
{
  "user_id":101,
  "username":"king",
  "role":"admin"
}
```

..................................................................

### 3. Signature

Used to verify that the token has not been modified.

```text
Signature = 
Hash(Header + Payload + Secret Key)
```

....................................................................

# JWT Authentication Flow

```text
User
 │
 │ 1. Login (Username + Password)
 ▼
Authentication Server
 │
 │ 2. Verify Credentials
 ▼
Generate JWT Token
 │
 │ 3. Send Token
 ▼
Client Stores Token
 │
 │ 4. Send Token With Requests
 ▼
Protected API
```

### Request Example

```http
GET /profile

Authorization: Bearer eyJhbGciOiJIUzI1...
```

Server verifies the token and allows access.

....................................................................

# JWT Advantages

* Stateless authentication
* Easy scaling
* Suitable for mobile applications
* Works well with REST APIs
* No server-side session storage required

....................................................................

# JWT Disadvantages

* Cannot easily revoke tokens
* Token theft can allow unauthorized access
* Requires secure storage

....................................................................

# Real-Life Example

An online shopping application:

```text
Login
  ↓
JWT Generated
  ↓
User Opens Cart
  ↓
JWT Sent
  ↓
Cart Data Returned
```

....................................................................

# 2. OAuth2 Flow

## Definition

**OAuth 2.0** is an authorization framework that allows users to give applications limited access to their resources without sharing passwords.

### Exam Definition

> OAuth2 is a protocol that enables secure delegated access to resources using access tokens.

....................................................................

# OAuth2 Example

When you click:

```text
"Login with Google"
```

The application does not receive your Google password.

Instead:

```text
Google
  ↓
Provides Access Token
  ↓
Application Accesses User Data
```

....................................................................

# OAuth2 Components

| Component            | Meaning                       |
| -------------------- | ----------------------------- |
| Resource Owner       | User                          |
| Client               | Application requesting access |
| Authorization Server | Provides tokens               |
| Resource Server      | Stores protected data         |

....................................................................

# OAuth2 Authorization Code Flow

```text
User
 │
 │ 1. Login Request
 ▼
Client Application
 │
 │ 2. Redirect to Authorization Server
 ▼
Google / Facebook
 │
 │ 3. User Permission
 ▼
Authorization Code
 │
 │ 4. Exchange Code
 ▼
Access Token
 │
 ▼
Access Protected Resources
```

....................................................................

# Example: Login with Google

Step 1:

User clicks:

```text
Login with Google
```

..................................................................

Step 2:

Google asks permission:

```text
Allow application to access profile?
```

..................................................................

Step 3:

Google sends access token:

```text
Access Token = abc123xyz
```

..................................................................

Step 4:

Application uses token to get user information.

....................................................................

# OAuth2 Grant Types

## 1. Authorization Code Grant

Used by web applications.

Example:

* Gmail login
* Banking applications

..................................................................

## 2. Client Credentials Grant

Used for machine-to-machine communication.

Example:

```text
Service A
   |
   |
Service B
```

..................................................................

## 3. Refresh Token Grant

Used to generate a new access token.

Example:

Mobile applications keeping users logged in.

....................................................................

# 3. Session-Based Authentication

## Definition

Session-based authentication stores user login information on the server after successful authentication.

The server creates a session ID and sends it to the client.

....................................................................

# Session Authentication Flow

```text
User
 │
 │ Username + Password
 ▼
Server
 │
 │ Create Session
 ▼
Session ID Generated
 │
 ▼
Browser Stores Cookie
 │
 ▼
Future Requests Use Cookie
```

....................................................................

# Example

Login:

```text
Username: King
Password: ******
```

Server creates:

```text
Session ID:
abc987xyz
```

Browser stores:

```text
Cookie:
session_id=abc987xyz
```

....................................................................

# Session vs JWT

| Feature    | Session          | JWT       |
| ---------- | ---------------- | --------- |
| Storage    | Server           | Client    |
| State      | Stateful         | Stateless |
| Scaling    | More difficult   | Easier    |
| Revocation | Easy             | Difficult |
| Usage      | Web applications | REST APIs |

....................................................................

# Advantages of Session Authentication

* Easy logout
* Easy session control
* Secure for traditional websites

....................................................................

# Disadvantages

* Requires server storage
* Difficult with distributed systems
* Needs session synchronization

....................................................................

# 4. Password Hashing

## Definition

Password hashing converts a password into a fixed-length encrypted value that cannot be reversed.

Passwords should never be stored as plain text.

....................................................................

# Password Storage

### Incorrect:

Database:

```text
password123
```

Anyone accessing the database can see passwords.

..................................................................

### Correct:

Database:

```text
$2b$12$LJ3df87s9sKdf....
```

Only the hash is stored.

....................................................................

# Hashing Process

```text
User Password

      ↓

Hash Algorithm

      ↓

Encrypted Hash

      ↓

Database Storage
```

....................................................................

# Popular Password Hashing Algorithms

| Algorithm | Usage                 |
| --------- | --------------------- |
| bcrypt    | Web applications      |
| Argon2    | Modern secure hashing |
| PBKDF2    | Security systems      |

....................................................................

# Password Verification

During login:

```text
Entered Password
        |
        ↓
Hash Again
        |
        ↓
Compare With Database Hash
        |
        ↓
Login Success
```

....................................................................

# Salting

## Definition

Salt is a random value added to passwords before hashing.

Example:

Without Salt:

```text
password123 → same hash every time
```

With Salt:

```text
password123 + random salt
        ↓
Different hash
```

Benefits:

* Prevents rainbow table attacks
* Improves security

....................................................................

# 5. CORS (Cross-Origin Resource Sharing)

## Definition

CORS is a browser security mechanism that controls whether a web application can request resources from another domain.

....................................................................

# Why CORS is Needed?

Example:

Frontend:

```text
http://localhost:3000
```

Backend:

```text
http://localhost:5000
```

Different origins.

Browser blocks requests unless the server allows them.

....................................................................

# CORS Flow

```text
Frontend
localhost:3000

      |
      |
Request
      |
      ▼

Backend
localhost:5000

      |
      |
CORS Check
      |
      ▼

Response Allowed
```

....................................................................

# CORS Headers

Example:

```http
Access-Control-Allow-Origin:
http://localhost:3000
```

This allows that frontend application.

....................................................................

# Flask CORS Example

Install:

```bash
pip install flask-cors
```

Code:

```python
from flask_cors import CORS

CORS(app)
```

Now frontend applications can access the API.

....................................................................

# CORS Problems

### Too Permissive:

```http
Access-Control-Allow-Origin: *
```

Allows every website.

Risk:

* Unauthorized access attempts
* Data exposure

....................................................................

# 6. OWASP Top 10 Common Vulnerabilities

## Definition

**OWASP Top 10** is a list of the most critical security risks in web applications published by the Open Web Application Security Project.

....................................................................

# OWASP Top 10 (2021)

## 1. Broken Access Control

### Meaning

Users can access resources they are not authorized to access.

### Example

Normal user accesses:

```text
/admin/deleteUser
```

### Prevention

* Role-based access control
* Proper authorization checks

....................................................................

# 2. Cryptographic Failures

### Meaning

Sensitive data is not properly protected.

Examples:

* Storing passwords as plain text
* Using weak encryption

### Prevention

* HTTPS
* Strong encryption
* Password hashing

....................................................................

# 3. Injection

### Meaning

Attackers send malicious commands through input fields.

Examples:

* SQL Injection
* Command Injection

Example:

```sql
SELECT * FROM users WHERE id=1
```

### Prevention

* Parameterized queries
* Input validation

....................................................................

# 4. Insecure Design

### Meaning

Security is not considered during application design.

Example:

No limit on password attempts.

### Prevention

* Security-first design
* Threat modeling

....................................................................

# 5. Security Misconfiguration

### Meaning

Incorrect security settings.

Examples:

* Default passwords
* Debug mode enabled in production

### Prevention

* Secure configuration
* Regular updates

....................................................................

# 6. Vulnerable and Outdated Components

### Meaning

Using outdated libraries with known vulnerabilities.

Example:

Old Flask or Django versions.

### Prevention

* Update dependencies
* Security scanning

....................................................................

# 7. Identification and Authentication Failures

### Meaning

Weak authentication implementation.

Examples:

* Weak passwords
* No MFA
* Poor session management

### Prevention

* Strong passwords
* MFA
* Secure JWT handling

....................................................................

# 8. Software and Data Integrity Failures

### Meaning

Application does not verify software updates or data integrity.

Example:

Installing untrusted packages.

### Prevention

* Verify packages
* Use secure deployment pipelines

....................................................................

# 9. Security Logging and Monitoring Failures

### Meaning

Application cannot detect attacks.

Example:

No login failure logs.

### Prevention

* Maintain security logs
* Monitor suspicious activity

....................................................................

# 10. Server-Side Request Forgery (SSRF)

### Meaning

Attackers force the server to send requests to internal systems.

Example:

Attacker accesses internal admin services.

### Prevention

* Validate URLs
* Restrict network access

....................................................................

# Security Best Practices

* Use HTTPS everywhere
* Implement JWT securely
* Use OAuth2 for third-party login
* Hash passwords using bcrypt/Argon2
* Enable CORS properly
* Validate user inputs
* Apply authorization checks
* Keep dependencies updated
* Monitor security logs
* Follow OWASP guidelines

....................................................................

# Summary Table

| Concept          | Purpose                        | Example              |
| ---------------- | ------------------------------ | -------------------- |
| JWT              | Token-based authentication     | REST API login       |
| OAuth2           | Secure delegated authorization | Login with Google    |
| Session Auth     | Server-side user sessions      | Traditional websites |
| Password Hashing | Protect passwords              | bcrypt               |
| CORS             | Control cross-origin requests  | React + Flask apps   |
| OWASP Top 10     | Identify security risks        | SQL Injection, XSS   |

....................................................................

# Key Points to Remember

* **JWT** → Stateless token authentication.
* **OAuth2** → Secure authorization using access tokens.
* **Session Authentication** → Server stores user session information.
* **Password Hashing** → Converts passwords into secure hashes.
* **CORS** → Controls browser cross-origin requests.
* **OWASP Top 10** → List of major web application security vulnerabilities.

