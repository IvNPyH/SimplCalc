# **Hello, this repository hosts a calculator written in FastAPI.**

### **Implemented**:

1. Written web application "Calculator" on FastAPI without client part. Basic methods (addition, subtraction, multiplication, division).

2. Written unit tests for the main methods.
 
3. The result is entered into PostgreSQL without using ORM.

4. Documentation can be seen http://127.0.0.1:8000/docs

**The main requests should be submitted in the json request body and look like this:**

    {
      "operation": "str",
      "x": int,
      "y": int
    }


**The application handles errors:** 

    - Division by zero 

    - Entering an invalid math operator

### **Additional protection**

    If the application crashes, the data sent to the database at the time of the crash will be canceled
