classDiagram
    class User {
        +int id
        +string username
        +string password
        +string email
        +int idrole
        +__str__() string
    }
    
    class Child {
        +int id
        +string child_name
        +float sleep_average
        +int treatment_id
        +int time
    }
    
    class Tap {
        +int id
        +int child_id
        +int status_id
        +int user_id
        +datetime init
        +datetime end
    }
    
    class Status {
        +int id
        +string name
    }
    
    class Role {
        +int id
        +string type_rol
    }
    
    class Treatment {
        +int id
        +string name
    }
    
    class UserChildRelation {
        +int user_id
        +int child_id
        +int rol_id
    }
    
   