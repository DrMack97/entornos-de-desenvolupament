classDiagram
    %% =============================================
    %% CLASES PRINCIPALES
    %% =============================================
    
    class User {
        +id: int
        +username: string
        +password: string
        +email: string
        +idrole: int
        +__str__(): string
    }
    
    class Child {
        +id: int
        +child_name: string
        +sleep_average: float
        +treatment_id: int
        +time: int
    }
    
    class Tap {
        +id: int
        +child_id: int
        +status_id: int
        +user_id: int
        +init: datetime
        +end: datetime
    }
    
    class Status {
        +id: int
        +name: string
    }
    
    class Role {
        +id: int
        +type_rol: string
    }
    
    class Treatment {
        +id: int
        +name: string
    }
    
    %% =============================================
    %% CLASE ASOCIATIVA PARA RELACIÓN N:M
    %% =============================================
    class UserChildRelation {
        +user_id: int
        +child_id: int
        +rol_id: int
    }
    
    %% =============================================
    %% RELACIONES ENTRE CLASES
    %% =============================================
    
    %% Un User tiene un Role (1:1)
    User "1" --> "1" Role : tiene
    
    %% Un User puede registrar múltiples Taps (1:N)
    User "1" --> "0..*" Tap : registra
    
    %% Un Child tiene múltiples Taps (1:N)
    Child "1" --> "0..*" Tap : tiene
    
    %% Un Tap tiene un Status (1:1)
    Tap "1" --> "1" Status : tiene estado
    
    %% Un Child tiene un Treatment (1:1)
    Child "1" --> "1" Treatment : recibe
    
    %% Relación N:M entre User y Child a través de UserChildRelation
    User "1" --> "0..*" UserChildRelation : está relacionado con
    Child "1" --> "0..*" UserChildRelation : está relacionado con
    UserChildRelation "0..*" --> "1" Role : con rol