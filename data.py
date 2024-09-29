headers = {
    "Content-Type": "application/json"
}

pet_body = {
    "id": "0",
    "category": {
        "id": "0",
        "name": "string"
    },
    "name": "doggie",
    "photoUrls": [
        "string"
    ],
    "tags": [
        {
            "id": 0,
            "name": "string"
        }
    ],
    "status": "available"
}

order_body = {
    "id": 0,
    "petId": 0,
    "quantity": 0,
    "shipDate": "2024-09-22T16:11:18.069Z",
    "status": "placed",
    "complete": 1
}

user_body = {
    "id": 0,
    "username": "string",
    "firstName": "string",
    "lastName": "string",
    "email": "string",
    "password": "string",
    "phone": "string",
    "userStatus": 0
}

users_bodies = [{
    "id": 0,
    "username": "string",
    "firstName": "string",
    "lastName": "string",
    "email": "string",
    "password": "string",
    "phone": "string",
    "userStatus": 0
}
]

login_user_body = {
    "username": "username",
    "password": "password"
}

pet_image_body = {
    "file": open('pet_image.jpeg', 'rb')
}
