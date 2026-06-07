# Pruebas End-to-End (E2E) - BibliotecaSteam

**TP Final - Punto 4.1 (documentacion E2E)**
**Universidad de Belgrano** - Tecnico en Programacion de Computadoras

## 1. Objetivo

Verificar el sistema completo desde la perspectiva del usuario validando el flujo de registro de usuarios, alta de juegos, administracion del catalogo y gestion de bibliotecas personales.

## 2. Alcance

| Incluido | Excluido |
|----------|----------|
| Registro de usuarios | Pruebas unitarias |
| Alta de juegos | Detalles internos de implementacion |
| Busquedas en catalogo | Medicion avanzada de rendimiento |
| Asociacion de juegos a usuarios | |

## 3. Casos de Prueba

1. Registrar usuario.
2. Agregar juego al catalogo.
3. Asociar juego a biblioteca.
4. Consultar biblioteca.
5. Calcular valor total de biblioteca.

## 4. Ejecucion

pytest tests/test_e2e.py -v

## 5. Resultado Esperado

Todos los escenarios deben finalizar correctamente verificando la integracion entre Juego, Usuario y Catalogo.
