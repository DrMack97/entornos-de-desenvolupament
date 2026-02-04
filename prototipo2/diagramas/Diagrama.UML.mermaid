%% =============================================
    %% 1- Modelo de datos (entidad/relacion)
%% =============================================
%% =============================================
    %% 2- Diagrama Arquitectura
%% =============================================
%% =============================================
    %% 3- Diagrama Clases 
%% =============================================
%% =============================================
    %% 4- WireFrames
%% =============================================
%% =============================================
    %% Sistema de Gestión de Eventos 
%% =============================================

classDiagram
    direction TB
    
    %% =============================================
    %% GRUPO 1: JERARQUÍA DE USUARIOS (HERENCIA)
    %% =============================================
    class Usuario {
        <<abstract>>
        #id: String
        #nombre: String
        #email: String
        #contraseña: String
        +registrar()
        +iniciarSesion()
        +cerrarSesion()
    }
    
    class Cliente {
        -telefono: String
        -direccion: String
        +comprarEntrada()
        +verHistorialCompras()
    }
    
    class Administrador {
        -nivelAcceso: String
        +crearEvento()
        +modificarEvento()
        +eliminarEvento()
        +generarReporte()
    }
    
    Usuario <|-- Cliente
    Usuario <|-- Administrador
    
    %% =============================================
    %% GRUPO 2: GESTIÓN DE EVENTOS
    %% =============================================
    class Evento {
        -id: String
        -nombre: String
        -fecha: Date
        -hora: Time
        -lugar: String
        -capacidadMaxima: int
        -descripcion: String
        +mostrarDetalles()
        +verDisponibilidad()
    }
    
    %% =============================================
    %% GRUPO 3: JERARQUÍA DE ENTRADAS (HERENCIA)
    %% =============================================
    class Entrada {
        <<abstract>>
        #id: String
        #precio: float
        #asiento: String
        #fechaCompra: Date
        #estado: String
        +reservar()
        +cancelar()
        +mostrarInfo()
    }
    
    class EntradaGeneral {
        -zona: String
        +accederEvento()
    }
    
    class EntradaVIP {
        -beneficios: String[]
        -accesoPreferencial: boolean
        +accesoLounge()
        +estacionamientoGratis()
    }
    
    Entrada <|-- EntradaGeneral
    Entrada <|-- EntradaVIP
    
    %% =============================================
    %% GRUPO 4: SISTEMA DE PAGOS
    %% =============================================
    class Pago {
        -id: String
        -monto: float
        -fecha: Date
        -metodoPago: String
        -estado: String
        +procesarPago()
        +generarRecibo()
        +verificarEstado()
    }
    
    %% =============================================
    %% RELACIONES PRINCIPALES (CENTRALIZADAS)
    %% =============================================
    
    %% Relación 1: Gestión de Eventos por Administrador
    Administrador "1" --> "0..*" Evento : gestiona
    
    %% Relación 2: Composición Evento-Entrada
    Evento "1" *-- "0..*" Entrada : contiene
    
    %% Relación 3: Cliente compra Entradas
    Cliente "1" --> "0..*" Entrada : compra
    
    %% Relación 4: Sistema de Pagos
    Cliente "1" --> "0..*" Pago : realiza
    Entrada "1" -- "1" Pago : tiene
    Pago ..> Entrada : referencia para