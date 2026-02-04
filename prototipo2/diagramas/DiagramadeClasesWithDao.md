classDiagram
    %% =============================================
    %% ENTIDADES DEL DOMINIO (Modelos)
    %% =============================================
    
    class User {
        -id: int
        -username: string
        -password: string
        -email: string
        -idrole: int
        +getId(): int
        +getUsername(): string
        +getEmail(): string
        +setUsername(string): void
        +setEmail(string): void
        +__str__(): string
    }
    
    class Child {
        -id: int
        -child_name: string
        -sleep_average: float
        -treatment_id: int
        -time: int
        +getId(): int
        +getName(): string
        +getSleepAverage(): float
        +setSleepAverage(float): void
        +getTreatmentId(): int
    }
    
    class Tap {
        -id: int
        -child_id: int
        -status_id: int
        -user_id: int
        -init: datetime
        -end: datetime
        +getId(): int
        +getChildId(): int
        +getStatusId(): int
        +getInitTime(): datetime
        +setEndTime(datetime): void
        +calculateDuration(): timedelta
    }
    
    class Status {
        -id: int
        -name: string
        +getId(): int
        +getName(): string
        +setName(string): void
    }
    
    class Role {
        -id: int
        -type_rol: string
        +getId(): int
        +getType(): string
        +setType(string): void
    }
    
    class Treatment {
        -id: int
        -name: string
        +getId(): int
        +getName(): string
        +setName(string): void
    }
    
    %% =============================================
    %% INTERFACES DAO
    %% =============================================
    
    class IUserDAO {
        <<interface>>
        +create(User): int
        +read(int): User
        +update(User): bool
        +delete(int): bool
        +findAll(): List~User~
        +findByUsername(string): User
        +findByEmail(string): User
    }
    
    class IChildDAO {
        <<interface>>
        +create(Child): int
        +read(int): Child
        +update(Child): bool
        +delete(int): bool
        +findAll(): List~Child~
        +findByName(string): List~Child~
        +findByTreatment(int): List~Child~
    }
    
    class ITapDAO {
        <<interface>>
        +create(Tap): int
        +read(int): Tap
        +update(Tap): bool
        +delete(int): bool
        +findAll(): List~Tap~
        +findByChild(int): List~Tap~
        +findByUser(int): List~Tap~
        +findByStatus(int): List~Tap~
        +findByDateRange(datetime, datetime): List~Tap~
    }
    
    class IStatusDAO {
        <<interface>>
        +create(Status): int
        +read(int): Status
        +update(Status): bool
        +delete(int): bool
        +findAll(): List~Status~
        +findByName(string): Status
    }
    
    class IRoleDAO {
        <<interface>>
        +create(Role): int
        +read(int): Role
        +update(Role): bool
        +delete(int): bool
        +findAll(): List~Role~
        +findByType(string): Role
    }
    
    class ITreatmentDAO {
        <<interface>>
        +create(Treatment): int
        +read(int): Treatment
        +update(Treatment): bool
        +delete(int): bool
        +findAll(): List~Treatment~
        +findByName(string): Treatment
    }
    
    %% =============================================
    %% IMPLEMENTACIONES CONCRETAS DE DAO
    %% =============================================
    
    class UserDAO {
        -connection: DatabaseConnection
        -tableName: string = "users"
        +UserDAO(connection)
        +create(User): int
        +read(int): User
        +update(User): bool
        +delete(int): bool
        +findAll(): List~User~
        +findByUsername(string): User
        +findByEmail(string): User
        -mapResultSetToUser(ResultSet): User
    }
    
    class ChildDAO {
        -connection: DatabaseConnection
        -tableName: string = "children"
        +ChildDAO(connection)
        +create(Child): int
        +read(int): Child
        +update(Child): bool
        +delete(int): bool
        +findAll(): List~Child~
        +findByName(string): List~Child~
        +findByTreatment(int): List~Child~
        -mapResultSetToChild(ResultSet): Child
    }
    
    class TapDAO {
        -connection: DatabaseConnection
        -tableName: string = "taps"
        +TapDAO(connection)
        +create(Tap): int
        +read(int): Tap
        +update(Tap): bool
        +delete(int): bool
        +findAll(): List~Tap~
        +findByChild(int): List~Tap~
        +findByUser(int): List~Tap~
        +findByStatus(int): List~Tap~
        +findByDateRange(datetime, datetime): List~Tap~
        -mapResultSetToTap(ResultSet): Tap
        +getAverageSleepByChild(int): float
        +getRecentTaps(int, int): List~Tap~
    }
    
    class StatusDAO {
        -connection: DatabaseConnection
        -tableName: string = "statuses"
        +StatusDAO(connection)
        +create(Status): int
        +read(int): Status
        +update(Status): bool
        +delete(int): bool
        +findAll(): List~Status~
        +findByName(string): Status
        -mapResultSetToStatus(ResultSet): Status
    }
    
    class RoleDAO {
        -connection: DatabaseConnection
        -tableName: string = "roles"
        +RoleDAO(connection)
        +create(Role): int
        +read(int): Role
        +update(Role): bool
        +delete(int): bool
        +findAll(): List~Role~
        +findByType(string): Role
        -mapResultSetToRole(ResultSet): Role
    }
    
    class TreatmentDAO {
        -connection: DatabaseConnection
        -tableName: string = "treatments"
        +TreatmentDAO(connection)
        +create(Treatment): int
        +read(int): Treatment
        +update(Treatment): bool
        +delete(int): bool
        +findAll(): List~Treatment~
        +findByName(string): Treatment
        -mapResultSetToTreatment(ResultSet): Treatment
    }
    
    %% =============================================
    %% CLASE ASOCIATIVA Y SU DAO
    %% =============================================
    
    class UserChildRelation {
        -user_id: int
        -child_id: int
        -rol_id: int
        +getUserId(): int
        +getChildId(): int
        +getRolId(): int
        +setRolId(int): void
    }
    
    class UserChildRelationDAO {
        -connection: DatabaseConnection
        -tableName: string = "user_child_relations"
        +UserChildRelationDAO(connection)
        +create(UserChildRelation): bool
        +read(int, int): UserChildRelation
        +update(UserChildRelation): bool
        +delete(int, int): bool
        +findByUser(int): List~UserChildRelation~
        +findByChild(int): List~UserChildRelation~
        +getChildrenByUser(int): List~Child~
        +getUsersByChild(int): List~User~
        +getRoleForUserChild(int, int): int
        -mapResultSetToRelation(ResultSet): UserChildRelation
    }
    
    %% =============================================
    %% CONEXIÓN A BASE DE DATOS
    %% =============================================
    
    class DatabaseConnection {
        -connection: Connection
        -config: DatabaseConfig
        +getConnection(): Connection
        +closeConnection(): void
        +beginTransaction(): void
        +commit(): void
        +rollback(): void
        +executeQuery(string): ResultSet
        +executeUpdate(string): int
    }
    
    class DatabaseConfig {
        -url: string
        -username: string
        -password: string
        -driver: string
        +getUrl(): string
        +getUsername(): string
        +getPassword(): string
        +getDriver(): string
    }
    
    %% =============================================
    %% RELACIONES DE IMPLEMENTACIÓN (DAO)
    %% =============================================
    
    IUserDAO <|.. UserDAO : implements
    IChildDAO <|.. ChildDAO : implements
    ITapDAO <|.. TapDAO : implements
    IStatusDAO <|.. StatusDAO : implements
    IRoleDAO <|.. RoleDAO : implements
    ITreatmentDAO <|.. TreatmentDAO : implements
    
    %% =============================================
    %% DEPENDENCIAS DE CONEXIÓN
    %% =============================================
    
    UserDAO --> DatabaseConnection : uses
    ChildDAO --> DatabaseConnection : uses
    TapDAO --> DatabaseConnection : uses
    StatusDAO --> DatabaseConnection : uses
    RoleDAO --> DatabaseConnection : uses
    TreatmentDAO --> DatabaseConnection : uses
    UserChildRelationDAO --> DatabaseConnection : uses
    
    DatabaseConnection --> DatabaseConfig : uses
    
    %% =============================================
    %% RELACIONES ENTRE ENTIDADES
    %% =============================================
    
    User "1" --> "1" Role : tiene rol
    User "1" --> "0..*" Tap : registra
    Child "1" --> "0..*" Tap : tiene
    Tap "1" --> "1" Status : tiene estado
    Child "1" --> "1" Treatment : recibe tratamiento
    
    %% Relación N:M entre User y Child
    User "1" --> "0..*" UserChildRelation : relaciones
    Child "1" --> "0..*" UserChildRelation : relaciones
    UserChildRelation "1" --> "1" Role : con rol específico