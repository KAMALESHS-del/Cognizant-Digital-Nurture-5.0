# Module: Angular

---

# 1. TypeScript Basics

### Definition

TypeScript is a **superset of JavaScript** developed by **Microsoft**. It adds **static typing**, interfaces, classes, and other features to JavaScript. Angular applications are written using TypeScript.

**Why use TypeScript?**

* Detects errors during development
* Supports Object-Oriented Programming (OOP)
* Improves code readability and maintenance
* Better IDE support (auto-completion, debugging)

---

### Variable Declaration

```typescript
let name: string = "John";
let age: number = 22;
let isStudent: boolean = true;

console.log(name, age, isStudent);
```

**Output**

```
John 22 true
```

---

### Function Example

```typescript
function add(a: number, b: number): number {
    return a + b;
}

console.log(add(10, 20));
```

**Output**

```
30
```

---

### Interface Example

```typescript
interface Student {
    name: string;
    age: number;
}

let s1: Student = {
    name: "Rahul",
    age: 20
};
```

---

### Advantages

✔ Static typing

✔ Better error checking

✔ Supports OOP

✔ Easy maintenance

---

### Cognizant Interview Questions

**Q1. What is TypeScript?**

TypeScript is a strongly typed superset of JavaScript that compiles into JavaScript.

**Q2. Why does Angular use TypeScript?**

Because it provides type safety, better tooling, and object-oriented features.

---

############################################################

# 2. Components & Modules

### Definition

A **Component** is the basic building block of an Angular application. It controls a part of the user interface.

A **Module (NgModule)** groups related components, directives, pipes, and services.

---

### Component Example

```typescript
import { Component } from '@angular/core';

@Component({
  selector: 'app-home',
  template: `<h1>Welcome to Angular</h1>`
})

export class HomeComponent {}
```

---

### Module Example

```typescript
import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

@NgModule({
  declarations: [HomeComponent],
  imports: [BrowserModule],
  bootstrap: [HomeComponent]
})

export class AppModule {}
```

---

### Output

```
Welcome to Angular
```

---

### Advantages

✔ Reusable UI

✔ Organized project

✔ Easy maintenance

✔ Modular architecture

---

### Interview Question

**What is the difference between Component and Module?**

* Component builds the UI.
* Module organizes components and other Angular features.

---

############################################################

# 3. Services & Dependency Injection (DI)

### Definition

A **Service** contains reusable business logic such as fetching data or performing calculations.

**Dependency Injection (DI)** automatically provides services to components.

---

### Service Example

```typescript
import { Injectable } from '@angular/core';

@Injectable({
  providedIn: 'root'
})

export class UserService {

  getName() {
    return "John";
  }

}
```

---

### Injecting Service

```typescript
constructor(private userService: UserService) {}

ngOnInit() {
   console.log(this.userService.getName());
}
```

---

### Output

```
John
```

---

### Advantages

✔ Reusable code

✔ Loose coupling

✔ Easy testing

✔ Better architecture

---

### Interview Question

**What is Dependency Injection?**

Dependency Injection is a design pattern where Angular automatically creates and supplies required objects (services) to components.

---

############################################################

# 4. RxJS

### Definition

RxJS (Reactive Extensions for JavaScript) is a library used by Angular for handling **asynchronous data streams** using **Observables**.

Used for:

* API calls
* Events
* Timers
* Real-time data

---

### Observable Example

```typescript
import { of } from 'rxjs';

const numbers = of(1, 2, 3);

numbers.subscribe(value => {
    console.log(value);
});
```

---

### Output

```
1
2
3
```

---

### Observable vs Promise

| Observable      | Promise              |
| --------------- | -------------------- |
| Multiple values | One value            |
| Cancelable      | Not cancelable       |
| Lazy execution  | Executes immediately |

---

### Advantages

✔ Handles async operations

✔ Supports multiple values

✔ Powerful operators

---

### Interview Question

**What is an Observable?**

An Observable is a stream of data that components can subscribe to and receive values over time.

---

############################################################

# 5. Routing

### Definition

Angular Routing allows navigation between different pages without reloading the application.

---

### Route Configuration

```typescript
const routes = [
  { path: '', component: HomeComponent },
  { path: 'about', component: AboutComponent }
];
```

---

### HTML Navigation

```html
<a routerLink="/">Home</a>

<a routerLink="/about">About</a>

<router-outlet></router-outlet>
```

---

### Output

```
/       → Home Page

/about  → About Page
```

---

### Advantages

✔ Fast navigation

✔ Single Page Application

✔ URL management

---

### Interview Question

**What is `<router-outlet>`?**

`<router-outlet>` is a placeholder where Angular displays the routed component.

---

############################################################

# 6. Reactive Forms

### Definition

Reactive Forms provide a model-driven approach for handling forms with validation.

---

### Example

```typescript
import { FormControl } from '@angular/forms';

name = new FormControl('');
```

---

### HTML

```html
<input [formControl]="name">

<p>{{ name.value }}</p>
```

---

### Output

If user types:

```
Rahul
```

Display:

```
Rahul
```

---

### Validation Example

```typescript
name = new FormControl('', Validators.required);
```

---

### Advantages

✔ Easy validation

✔ Dynamic forms

✔ Better testing

✔ Scalable

---

### Interview Question

**Why use Reactive Forms instead of Template-driven Forms?**

Reactive Forms are more scalable, easier to test, and better suited for complex forms.

---

############################################################

# 7. HttpClient

### Definition

`HttpClient` is Angular's built-in service used to communicate with REST APIs.

Supports:

* GET
* POST
* PUT
* DELETE

---

### Import

```typescript
import { HttpClient } from '@angular/common/http';
```

---

### GET Request Example

```typescript
constructor(private http: HttpClient) {}

ngOnInit() {

this.http.get('https://jsonplaceholder.typicode.com/users')
.subscribe(data => {

console.log(data);

});

}
```

---

### Output

```
[
 { id:1, name:"Leanne Graham" },
 { id:2, name:"Ervin Howell" }
]
```

---

### POST Request Example

```typescript
this.http.post(url, {
   name: "John"
}).subscribe();
```

---

### Advantages

✔ Easy API integration

✔ Returns Observables

✔ Supports error handling

✔ JSON support

---

### Interview Question

**Why does HttpClient return an Observable instead of a Promise?**

Because Observables can emit multiple values, support cancellation, and provide powerful RxJS operators for handling asynchronous data.

---

# Angular – Cognizant Technical Assessment Frequently Asked Questions

### 1. What is TypeScript?

TypeScript is a strongly typed superset of JavaScript used by Angular.

---

### 2. What is an Angular Component?

A Component controls a specific part of the user interface.

---

### 3. What is an Angular Module?

A Module groups related components, services, directives, and pipes.

---

### 4. What is a Service?

A Service contains reusable business logic shared across components.

---

### 5. What is Dependency Injection (DI)?

A design pattern where Angular automatically provides required services to components.

---

### 6. What is RxJS?

A library for reactive programming using Observables to manage asynchronous data streams.

---

### 7. What is an Observable?

An Observable is a stream of data that can emit one or more values over time.

---

### 8. What is Angular Routing?

Angular Routing enables navigation between pages in a Single Page Application without reloading.

---

### 9. What are Reactive Forms?

Reactive Forms are model-driven forms that provide better validation and scalability.

---

### 10. What is HttpClient?

`HttpClient` is Angular's service for sending HTTP requests and communicating with REST APIs.

---

# Angular Interview Quick Revision Table

| Concept              | Key Point                                          |
| -------------------- | -------------------------------------------------- |
| TypeScript           | Strongly typed JavaScript with OOP support         |
| Components           | Reusable UI building blocks                        |
| Modules              | Organize Angular application features              |
| Services             | Reusable business logic                            |
| Dependency Injection | Automatically provides services to components      |
| RxJS                 | Handles asynchronous programming using Observables |
| Routing              | Navigates between pages in a SPA                   |
| Reactive Forms       | Model-driven forms with validation                 |
| HttpClient           | Sends HTTP requests to REST APIs                   |

