# WebSoc API

---

# Introduction

Returns data on UCI classes by scrapping WebSoc. Classes can be filtered by departments and breadths, as well as other query paramteters.

# Overview

This service is in its early stages and will likely see significant updates, deprecating functionalities currently avaliable.

# Authentication

There is no authentication in this iteration of the service.

# Error Codes

200 - data was returned ok
404 - data not found
500 - internal server error

# Rate limit

There is no limit on the number of requests. A future iteration of this API will have authentication and all users will have to register and be approved. Upon approval, your account will be created.

---

## /filters

```
GET {{url}}/filters
```

Returns all of the possible filters that can be used to select classes.

---

### Request

>

### Examples:

>

---

## /Breadths

```
GET {{url}}/Breadths
```

Gives a list of the possible breadths maped to their codes.

---

### Request

>

### Examples:

>

---

## /Breadth/<breadth_name>

```
GET {{url}}/Breadth/2
```

Returns all of the classes under a specified Breadth

---

### Request

>

### Examples:

>

---

## /Depts

```
GET {{url}}/Depts
```

Gives a list of all of the possible departments mapped to their code.

---

### Request

>

### Examples:

>

---

## /Dept/<department_name>

```
GET {{url}}/Dept/I&C SCI
```

Returns all of the classes under a specified Department.

---

### Request

>

### Examples:

>

---

## /YearTerms

```
GET {{url}}/YearTerms
```

Gives a list of the possible YearTerms mapped to their code.

---

### Request

>

### Examples:

>

---

## /Divisions

```
GET {{url}}/Divisions
```

Gives a list of the possible Divisions with their codes.

---

### Request

>

### Examples:

>

---

---

Built with [Postdown][pypi].

Author: [Titor](https://github.com/TitorX)

[pypi]: https://pypi.python.org/pypi/Postdown
