# Module: Vue.js 

---

# 1. Template Syntax

### Definition

Template Syntax in Vue.js allows you to create dynamic HTML by combining HTML with JavaScript expressions. Vue automatically updates the DOM whenever the data changes.

**Why use Template Syntax?**

* Easy to build dynamic UI
* Supports data binding
* Makes code readable

---

### Interpolation (Displaying Data)

```vue
<template>
  <h1>{{ message }}</h1>
</template>

<script setup>
const message = "Welcome to Vue.js";
</script>
```

**Output**

```
Welcome to Vue.js
```

---

### Attribute Binding

```vue
<template>
  <img :src="imageUrl">
</template>

<script setup>
const imageUrl = "logo.png";
</script>
```

---

### Event Binding

```vue
<template>
  <button @click="showMessage">
    Click
  </button>
</template>

<script setup>
function showMessage() {
  alert("Button Clicked");
}
</script>
```

---

### Conditional Rendering

```vue
<template>
  <p v-if="isLoggedIn">Welcome User</p>
</template>

<script setup>
const isLoggedIn = true;
</script>
```

---

### List Rendering

```vue
<template>
  <li v-for="name in names" :key="name">
    {{ name }}
  </li>
</template>

<script setup>
const names = ["John", "David", "Sara"];
</script>
```

---

### Advantages

✔ Easy data binding

✔ Dynamic HTML

✔ Simple syntax

✔ Automatic UI updates

---

### Cognizant Interview Questions

**Q1. What is Template Syntax?**

Template Syntax allows HTML to display dynamic data using Vue directives and expressions.

**Q2. What is `{{ }}`?**

It is called **Interpolation**, used to display variables inside HTML.

---

############################################################

# 2. Reactivity

### Definition

Reactivity is Vue's feature that automatically updates the UI whenever the underlying data changes.

Vue tracks changes in data and refreshes only the affected parts of the page.

---

### Example

```vue
<template>
  <h2>{{ count }}</h2>

  <button @click="count++">
    Increment
  </button>
</template>

<script setup>
import { ref } from "vue";

const count = ref(0);
</script>
```

---

### Output

Initially

```
0
```

After Click

```
1
```

---

### Reactive Object

```javascript
import { reactive } from "vue";

const student = reactive({
  name: "Rahul",
  age: 20
});
```

---

### `ref()` vs `reactive()`

| ref()                               | reactive()                  |
| ----------------------------------- | --------------------------- |
| Stores primitive or object values   | Best for objects and arrays |
| Access using `.value` in JavaScript | Access properties directly  |

---

### Advantages

✔ Automatic DOM updates

✔ Better performance

✔ Less manual coding

---

### Interview Question

**Difference between `ref()` and `reactive()`?**

`ref()` is mainly used for primitive values (and can also wrap objects), while `reactive()` is used for objects and arrays.

---

############################################################

# 3. Components

### Definition

A Component is a reusable piece of UI in Vue.

Applications are built by combining multiple components.

---

### Child Component

```vue
<template>
  <h1>Hello Vue</h1>
</template>
```

---

### Parent Component

```vue
<template>
  <HelloComponent />
</template>

<script setup>
import HelloComponent from "./HelloComponent.vue";
</script>
```

---

### Output

```
Hello Vue
```

---

### Passing Props

```vue
<!-- Parent -->
<Student name="Rahul" />
```

```vue
<!-- Child -->
<script setup>
defineProps({
  name: String
});
</script>

<template>
  <h2>{{ name }}</h2>
</template>
```

---

### Advantages

✔ Reusable

✔ Modular

✔ Easy maintenance

---

### Interview Question

**What is a Vue Component?**

A reusable block of UI that contains its own template, logic, and styles.

---

############################################################

# 4. Composition API

### Definition

The Composition API is the modern way of organizing Vue component logic using reusable functions.

It is commonly used with the `<script setup>` syntax.

---

### Example

```vue
<template>
  <h2>{{ count }}</h2>

  <button @click="increment">
    Add
  </button>
</template>

<script setup>
import { ref } from "vue";

const count = ref(0);

function increment() {
  count.value++;
}
</script>
```

---

### Why Composition API?

✔ Better code organization

✔ Logic reuse

✔ Easier maintenance

✔ Preferred in Vue 3

---

### Composition API vs Options API

| Composition API                    | Options API                          |
| ---------------------------------- | ------------------------------------ |
| Uses `setup()` or `<script setup>` | Uses `data()`, `methods`, `computed` |
| Better for large projects          | Easier for beginners                 |
| Reusable logic                     | Less flexible                        |

---

### Interview Question

**Why use the Composition API?**

It improves code organization, logic reuse, and maintainability, especially in large applications.

---

############################################################

# 5. Vue Router

### Definition

Vue Router enables navigation between pages in a Single Page Application (SPA).

---

### Install

```bash
npm install vue-router
```

---

### Route Configuration

```javascript
import { createRouter, createWebHistory } from "vue-router";

const routes = [
  {
    path: "/",
    component: Home
  },
  {
    path: "/about",
    component: About
  }
];

const router = createRouter({
  history: createWebHistory(),
  routes
});

export default router;
```

---

### Navigation

```vue
<router-link to="/">Home</router-link>

<router-link to="/about">
  About
</router-link>

<router-view />
```

---

### Output

```
/       → Home

/about  → About
```

---

### Advantages

✔ Fast navigation

✔ No page reload

✔ Dynamic routing

---

### Interview Question

**What is `<router-view>`?**

`<router-view>` is the placeholder where the matched route component is displayed.

---

############################################################

# 6. Pinia / Vuex State Management

### Definition

State Management is used to share application data across multiple components.

* **Pinia** is the recommended state management library for Vue 3.
* **Vuex** is the older state management library used mainly with Vue 2 and some existing Vue 3 projects.

---

### Pinia Store Example

```javascript
import { defineStore } from "pinia";

export const useCounterStore = defineStore("counter", {

  state: () => ({
    count: 0
  }),

  actions: {
    increment() {
      this.count++;
    }
  }

});
```

---

### Using Store

```vue
<script setup>
import { useCounterStore } from "./store";

const store = useCounterStore();
</script>

<template>
  <h2>{{ store.count }}</h2>

  <button @click="store.increment()">
    Add
  </button>
</template>
```

---

### Output

Initially

```
0
```

After Click

```
1
```

---

### Pinia vs Vuex

| Pinia                     | Vuex                       |
| ------------------------- | -------------------------- |
| Recommended for Vue 3     | Older library              |
| Simpler syntax            | More boilerplate code      |
| Better TypeScript support | Limited TypeScript support |
| Lightweight               | Larger API                 |

---

### Advantages

✔ Centralized state

✔ Easy data sharing

✔ Predictable application state

✔ Simplifies large applications

---

### Interview Question

**Why is Pinia preferred over Vuex?**

Pinia has a simpler API, better TypeScript support, improved performance, and is the officially recommended state management solution for Vue 3.

---

# Vue.js – Cognizant Technical Assessment Frequently Asked Questions

### 1. What is Template Syntax?

Template Syntax combines HTML with JavaScript expressions to create dynamic user interfaces.

---

### 2. What is Reactivity?

Reactivity automatically updates the user interface whenever application data changes.

---

### 3. What is a Vue Component?

A reusable block of UI containing its own template, logic, and styles.

---

### 4. What is the Composition API?

A modern API in Vue 3 used to organize and reuse component logic with `setup()` or `<script setup>`.

---

### 5. What is `ref()`?

`ref()` creates a reactive reference, commonly used for primitive values.

---

### 6. What is `reactive()`?

`reactive()` creates a reactive object or array.

---

### 7. What is Vue Router?

Vue Router enables client-side routing between pages in a Single Page Application.

---

### 8. What is `<router-view>`?

It is the placeholder where the current route's component is rendered.

---

### 9. What is Pinia?

Pinia is the official state management library recommended for Vue 3 applications.

---

### 10. Difference between Pinia and Vuex?

| Pinia                     | Vuex                           |
| ------------------------- | ------------------------------ |
| Recommended for Vue 3     | Older state management library |
| Simple API                | More boilerplate               |
| Better TypeScript support | Less TypeScript-friendly       |
| Lightweight               | More configuration required    |

---

# Vue.js Interview Quick Revision Table

| Concept         | Key Point                                        |
| --------------- | ------------------------------------------------ |
| Template Syntax | Dynamic HTML using directives and interpolation  |
| Interpolation   | Displays data using `{{ }}`                      |
| Reactivity      | Automatically updates the UI when data changes   |
| `ref()`         | Creates reactive primitive values                |
| `reactive()`    | Creates reactive objects and arrays              |
| Components      | Reusable UI building blocks                      |
| Composition API | Modern way to organize and reuse component logic |
| Vue Router      | Handles navigation in Single Page Applications   |
| Pinia           | Official Vue 3 state management library          |
| Vuex            | Older centralized state management library       |

