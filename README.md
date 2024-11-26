# **Manufacturer Verification Backend Service**

This is a Node.js-based backend API that verifies manufacturer details provided by users. The backend uses dummy data to validate the information and returns a truthy response to the frontend. It is designed to work alongside a smart contract that stores manufacturer details on-chain.

----------

## **Features**

-   Validate manufacturer details such as name and registration number using pre-defined dummy data.
-   Return a success or failure response based on the validation.
-   Simple and easy-to-use RESTful API endpoint.
-   No database required; verification is handled with in-memory dummy data.

----------

## **Technologies Used**

-   **Node.js**: JavaScript runtime for building the backend.
-   **Express**: Framework for building the API.
-   **CORS**: For handling cross-origin requests.
-   **Body-parser**: Middleware for parsing request bodies.

----------

## **Installation and Setup**

### **Prerequisites**

-   Node.js (v18 or higher)
-   npm (Node Package Manager)

### **Steps**

1.  Clone the repository:
    
    ```bash
    git clone https://github.com/AuthChain-Platform/AuthChain_Backend.git
    cd AuthChain_Backend
    
    ```
    
2.  Install dependencies:
    
    ```bash
    npm install
    ```
    
3.  Start the server:
    
    ```bash
    node src/app.js 
    ```
    
4.  Server runs on https://authchain-backend-1-b9sq.onrender.com/
    

----------

## **API Documentation**

### **Base URL**

```
[https://manufacturerverification.onrender.com](https://authchain-backend-1-b9sq.onrender.com/api/manufacturers/verify)
		or

http://localhost:5000

```

### **Endpoints**

#### **POST /api/manufacturers/verify**

-   **Description**: Verifies manufacturer details using dummy data.
-   **Headers**:
    -   `Content-Type: application/json`
-   **Request Body**:
    
    ```json
    {
        "name": "Manufacturer Name",
        "registrationNumber": "123456789"
    }
    
    ```
    
-   **Responses**:
    -   **200 (Success)**: Manufacturer verified successfully.
        
        ```json
        {
            "message": "Manufacturer verified successfully",
            "verified": true,
            "details": {
                "verified": true,
                "name": "Manufacturer Name",
                "registrationNumber": "123456789",
                "country": "Country Name"
            }
        }
        
        ```
        
    -   **400 (Failure)**: Manufacturer verification failed.
        
        ```json
        {
            "message": "Manufacturer verification failed",
            "verified": false
        }
        
        ```
        

----------

## **Testing the API**

1.  Open [Postman](https://www.postman.com/downloads/) or a similar API testing tool.
2.  Create a new `POST` request either localll or using the live link mentioned in Installation and setup, if you decide to work with local, here is the URL to work with:
    
    ```
    https://manufacturerverification.onrender.com/api/manufacturers/verify
            or
    http://localhost:5000/api/manufacturers/verify
    ```
    
3.  Add the `Content-Type` header:
    
    ```
    Key: Content-Type
    Value: application/json
    
    ```
    
4.  In the request body, provide manufacturer details:
    
    ```json
    {
        "brandName": 'Rite Foods Ng Ltd',
        "registrationNumber": '123456789'
    }
    ```
    
5.  Send the request and verify the response.
