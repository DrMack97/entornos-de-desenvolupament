sequenceDiagram
    participant App as Aplicación Python
    participant DAO as UserDAO/ChildDAO/TapDAO
    participant APIClient as APIClient
    participant Server as Servidor API
    
    App->>DAO: create(user)
    DAO->>APIClient: post("/users", user_data)
    APIClient->>Server: POST /api/v1/users
    Note over APIClient,Server: Headers: Content-Type: application/json<br/>Authorization: Bearer {api_key}
    Server-->>APIClient: 201 Created + JSON
    APIClient-->>DAO: response_data
    DAO-->>App: user_id
    
    App->>DAO: find_by_child(child_id)
    DAO->>APIClient: get("/taps/search", params)
    APIClient->>Server: GET /api/v1/taps/search?child_id=1
    Server-->>APIClient: 200 OK + JSON array
    APIClient-->>DAO: response_data
    DAO-->>App: List[Tap]