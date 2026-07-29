# Module: API Integration & State Management 

---

# 1. API Integration

### Definition

API (Application Programming Interface) Integration is the process of connecting a frontend application with a backend server or external service to exchange data.

Common API operations:

* **GET** – Retrieve data
* **POST** – Create new data
* **PUT** – Update existing data
* **DELETE** – Remove data

---

### Example

```text
Frontend (React/Angular/Vue)
           │
     HTTP Request
           │
        REST API
           │
        Database
```

---

### Advantages

✔ Dynamic data

✔ Real-time updates

✔ Backend communication

✔ Data sharing

---

### Cognizant Interview Questions

**Q1. What is API Integration?**

API Integration allows frontend applications to communicate with backend servers to send and receive data.

**Q2. Why are APIs used?**

To exchange data between applications and services.

---

############################################################

# 2. Fetch API

### Definition

The **Fetch API** is a built-in JavaScript API used to make HTTP requests.

Supports:

* GET
* POST
* PUT
* DELETE

---

### GET Request Example

```javascript
fetch("https://jsonplaceholder.typicode.com/users")
.then(response => response.json())
.then(data => console.log(data))
.catch(error => console.log(error));
```

---

### Output

```text
[
 {id:1, name:"Leanne Graham"},
 {id:2, name:"Ervin Howell"}
]
```

---

### POST Request Example

```javascript
fetch("https://jsonplaceholder.typicode.com/posts",{

method:"POST",

headers:{
"Content-Type":"application/json"
},

body:JSON.stringify({
title:"React",
body:"Learning Fetch API"
})

});
```

---

### Advantages

✔ Built into JavaScript

✔ Easy to use

✔ Promise-based

---

### Interview Question

**What is Fetch API?**

Fetch API is a built-in JavaScript interface for making HTTP requests and handling responses.

---

############################################################

# 3. Axios

### Definition

Axios is a popular JavaScript library used to send HTTP requests.

Install:

```bash
npm install axios
```

---

### GET Request Example

```javascript
import axios from "axios";

axios.get("https://jsonplaceholder.typicode.com/users")

.then(response => {

console.log(response.data);

});
```

---

### POST Request Example

```javascript
axios.post(url,{
name:"John"
});
```

---

### Fetch vs Axios

| Fetch API              | Axios                     |
| ---------------------- | ------------------------- |
| Built into browser     | External library          |
| Manual JSON conversion | Automatic JSON conversion |
| Manual error checking  | Better error handling     |
| Smaller                | More features             |

---

### Advantages

✔ Automatic JSON parsing

✔ Request/response interceptors

✔ Better error handling

✔ Widely used

---

### Interview Question

**Why is Axios preferred over Fetch?**

Axios automatically parses JSON, provides better error handling, supports interceptors, and has a simpler API.

---

############################################################

# 4. Promises

### Definition

A **Promise** represents the eventual completion or failure of an asynchronous operation.

Promise States:

* Pending
* Fulfilled
* Rejected

---

### Example

```javascript
let promise = new Promise((resolve,reject)=>{

let success=true;

if(success)

resolve("Login Successful");

else

reject("Login Failed");

});

promise

.then(result=>console.log(result))

.catch(error=>console.log(error));
```

---

### Output

```text
Login Successful
```

---

### Advantages

✔ Handles asynchronous tasks

✔ Avoids callback hell

✔ Improves readability

---

### Interview Question

**What are the states of a Promise?**

Pending, Fulfilled, and Rejected.

---

############################################################

# 5. async / await

### Definition

`async` and `await` simplify working with Promises by making asynchronous code look like synchronous code.

* **async** declares an asynchronous function.
* **await** waits for a Promise to resolve.

---

### Example

```javascript
async function getUsers(){

const response = await fetch(
"https://jsonplaceholder.typicode.com/users"
);

const data = await response.json();

console.log(data);

}

getUsers();
```

---

### Output

```text
User data displayed
```

---

### Advantages

✔ Cleaner code

✔ Easy debugging

✔ Better readability

---

### Interview Question

**Difference between Promise and async/await?**

Promises use `.then()` and `.catch()`, while `async/await` provides cleaner syntax built on top of Promises.

---

############################################################

# 6. Error Handling

### Definition

Error Handling ensures applications can handle failures gracefully instead of crashing.

Common errors:

* Network errors
* Server errors
* Invalid responses
* Timeout errors

---

### Fetch Error Handling

```javascript
fetch(url)

.then(response=>{

if(!response.ok){

throw new Error("Request Failed");

}

return response.json();

})

.catch(error=>{

console.log(error.message);

});
```

---

### async/await Error Handling

```javascript
async function getData(){

try{

const response = await fetch(url);

const data = await response.json();

console.log(data);

}

catch(error){

console.log(error);

}

}
```

---

### Advantages

✔ Prevents crashes

✔ Better user experience

✔ Easier debugging

---

### Interview Question

**Why use try...catch with async/await?**

It catches errors from asynchronous operations and prevents the application from crashing.

---

############################################################

# 7. State Management

### Definition

State Management is the process of storing, updating, and sharing application data across multiple components.

Popular state management libraries:

* **Redux** (React)
* **NgRx** (Angular)
* **Pinia** (Vue)

---

## Redux (React)

### Definition

Redux stores application data in a single centralized store.

---

### Example

```javascript
const initialState = {

count:0

};
```

---

### Flow

```text
Component

↓

Dispatch Action

↓

Reducer

↓

Store Updated

↓

UI Updated
```

---

### Advantages

✔ Predictable state

✔ Centralized data

✔ Easy debugging

---

############################################################

## NgRx (Angular)

### Definition

NgRx is Angular's reactive state management library based on Redux principles and RxJS.

---

### Flow

```text
Component

↓

Action

↓

Reducer

↓

Store

↓

Component
```

---

### Advantages

✔ Predictable state

✔ RxJS integration

✔ Suitable for large Angular applications

---

############################################################

## Pinia (Vue)

### Definition

Pinia is the official state management library for Vue 3.

---

### Example

```javascript
import { defineStore } from "pinia";

export const useCounter = defineStore("counter",{

state:()=>({

count:0

}),

actions:{

increment(){

this.count++;

}

}

});
```

---

### Output

Initially

```text
0
```

After increment

```text
1
```

---

### Advantages

✔ Simple API

✔ Lightweight

✔ Excellent TypeScript support

✔ Official Vue 3 state library

---

### Redux vs NgRx vs Pinia

| Feature     | Redux       | NgRx         | Pinia          |
| ----------- | ----------- | ------------ | -------------- |
| Framework   | React       | Angular      | Vue            |
| State Store | Centralized | Centralized  | Centralized    |
| Based On    | Redux       | Redux + RxJS | Vue Reactivity |
| Best For    | React Apps  | Angular Apps | Vue Apps       |

---

### Interview Question

**Which state management library is used with React, Angular, and Vue?**

* React → Redux
* Angular → NgRx
* Vue → Pinia

---

# API Integration & State Management – Cognizant Technical Assessment Frequently Asked Questions

### 1. What is API Integration?

Connecting a frontend application with a backend server or external service to exchange data.

---

### 2. What is the Fetch API?

A built-in JavaScript API used to make HTTP requests.

---

### 3. What is Axios?

A JavaScript library for making HTTP requests with features like automatic JSON parsing and interceptors.

---

### 4. Difference between Fetch and Axios?

| Fetch                 | Axios                  |
| --------------------- | ---------------------- |
| Built into JavaScript | External library       |
| Manual JSON parsing   | Automatic JSON parsing |
| Basic error handling  | Better error handling  |

---

### 5. What is a Promise?

An object representing the eventual success or failure of an asynchronous operation.

---

### 6. What is `async/await`?

A modern syntax for handling Promises in a cleaner and more readable way.

---

### 7. Why use `try...catch`?

To catch and handle errors in asynchronous code gracefully.

---

### 8. What is State Management?

The process of storing, updating, and sharing application data across components.

---

### 9. Which state management library is used with each framework?

| Framework | State Management |
| --------- | ---------------- |
| React     | Redux            |
| Angular   | NgRx             |
| Vue       | Pinia            |

---

### 10. Difference between Redux, NgRx, and Pinia?

| Redux             | NgRx                       | Pinia                 |
| ----------------- | -------------------------- | --------------------- |
| React             | Angular                    | Vue                   |
| Centralized store | Uses RxJS + Redux concepts | Uses Vue's reactivity |
| Best for React    | Best for Angular           | Best for Vue          |

---

# API Integration & State Management Interview Quick Revision Table

| Concept          | Key Point                                                      |
| ---------------- | -------------------------------------------------------------- |
| API Integration  | Connects frontend and backend applications                     |
| Fetch API        | Built-in JavaScript API for HTTP requests                      |
| Axios            | Third-party HTTP client with additional features               |
| Promise          | Handles asynchronous operations (Pending, Fulfilled, Rejected) |
| async/await      | Cleaner syntax for working with Promises                       |
| Error Handling   | Uses `.catch()` or `try...catch` to manage failures            |
| Redux            | State management for React                                     |
| NgRx             | Reactive state management for Angular                          |
| Pinia            | Official state management library for Vue 3                    |
| State Management | Centralizes and shares application data across components      |

