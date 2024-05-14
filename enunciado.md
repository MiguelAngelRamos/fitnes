
### Versión Nivel de Dificultad:
V2 Medio

### Nombre del proyecto:
"FitZone" – Iteración 1

### Tema:
● Acceso a datos con Django

### Objetivo del proyecto:
(Competencias del Módulo):

Construir aplicaciones web que manipulen datos en una base de datos SQL utilizando Python/Django y las componentes que el lenguaje dispone para su uso para dar solución a un requerimiento

### Aprendizaje esperado a trabajar (AD) a evaluar (Ev)

- Reconoce las características del framework Django aplicado a las bases de datos
- Reconoce los paquetes de instalación de bases de datos de Django.
- Reconoce las características de Django como ORM para su integración con una base de datos

### Ejecución: Grupal

### Descripción de la Evaluación
#### CONTEXTO
El incremento en la conciencia sobre la salud física y el bienestar ha llevado a un aumento en la demanda de gimnasios y servicios de entrenamiento personalizado. En este escenario, muchos gimnasios están buscando digitalizar sus operaciones para mejorar la experiencia del usuario y la eficiencia del negocio.

#### PROBLEMA
El gimnasio "FitZone" busca modernizar su sistema de gestión de miembros y clases. Actualmente, la información está dispersa entre registros en papel y hojas de cálculo. Esta falta de un sistema centralizado dificulta el seguimiento del progreso de los clientes, la gestión de las clases y el control de las membresías.

#### SOLUCIÓN
Desarrollar una solución tecnológica que integre todas las operaciones del gimnasio en un solo sistema, mejorando la gestión de clientes, la reserva de clases, el seguimiento del progreso y la comunicación con los miembros.

### REQUERIMIENTOS FUNCIONALES
#### Módulo de Gestión de Membresías
- **RFG-001 - Registro de miembros**: Los administradores podrán registrar nuevos miembros, almacenando datos como nombre, dirección, fecha de inicio de la membresía, y detalles de salud.
- **RFG-002 - Gestión de clases**: Permitir a los entrenadores y administradores gestionar el horario de clases, incluyendo creación, modificación y cancelación de clases.

#### Módulo de Cliente
- **RFW-001 - Registro de usuarios**: Los clientes nuevos se registrarán en el sitio, proporcionando datos básicos y detalles de salud. El sistema enviará un correo de verificación con una contraseña temporal.
- **RFW-002 - Reserva de clases**: Los usuarios podrán inscribirse en clases disponibles, las cuales se podrán filtrar por tipo, horario, y entrenador.
- **RFW-003 - Seguimiento del progreso**: Los usuarios podrán ingresar y visualizar su progreso en diversas actividades físicas y metas de salud.

### DESARROLLO
- Crear un proyecto en Django, con aplicaciones necesarias para abordar el problema.
- Conectar el proyecto a una base de datos en PostgreSQL.
- Realizar la migración inicial y verificar que se refleje en la base de datos.
- Definir usuarios de tipo superuser y usuarios del sistema.
- La página principal presentará información básica sobre "FitZone" y permitirá el acceso a las diferentes funcionalidades según el rol del usuario.

Este ejercicio ofrece una oportunidad para que los estudiantes apliquen y profundicen su conocimiento en Django, especialmente en la manipulación de datos y el manejo de relaciones en bases de datos a través de un ORM.