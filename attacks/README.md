![image](../docs/robot2.jpg)

En esta carpeta se almacenan y organizan los diferentes *ataques* predefinidos, que se definirán en el parámetro **-a** del comando.


**Cuando se habla de ataques, se refiere a las diferentes combinaciones entre diccionarios, reglas y mascaras que se pueden realizar para crackear una contraseña.**


La estructura de carpetas creada es la siguiente:
* **_old**: Serie de ataques antiguos.
* **ES**: Diferentes ataques para crackear contraseñas, mayormente centradas en contraseñas en castellano. Para ello hace uso de los diccionarios kaonashi14M.txt, cyclone_hk.txt y hashkiller-dict.txt.
* **ANY**: Diferentes ataques para crackear contraseñas independiente del idioma. Combina una serie de diccionarios y reglas para intentar optimizar el proceso de cracking.
* **LM_NTLM**: Ataques centrados en crackear contraseñas almacenadas en LM y su transformación a NT.
* **ONLY_CUSTOM**: Son una serie de ataques para realizar únicamente contra el diccionario custom creado para el proyecto.
* **BIG_HITS**: En este caso se busca el mayor rendimiento posible, en base a nuestra experiencia, para crackear contraseñas. Para ello se han creado tres subcarpetas para realizar diferentes combinaciones específicas de diccionarios y reglas con las que habitualmente se consiguen crackear contraseñas.
    * **FAST**: En este caso se busca obtener el mayor numero de contraseñas en el menor tiempo posible, intentando que cada prueba sobre credenciales NTLM no sea mayor a 10 minutos.
    * **MEDIUM**: Obtener el mayor numero de contraseñas en un tiempo algo mayor, intentando que cada prueba sobre credenciales NTLM no sea mayor a 2 horas.
    * **MEDIUM**: Se trata de ejecutar ataques de mayor duración a 2 horas sobre credenciales NTLM. Mediante los dicionarios identificados como BIG HITS, se trata de realizar las pruebas mediante archivos de reglas de mayor tamaño.
* **quick_test.json**: Test rápido que ejecuta pruebas básicas.
* **all_*.json**: Cada uno de estos ataques, engloba una serie de los ataques almacenados en las carpetas anteriores.



## Licencia

Shield: [![CC BY-NC-SA 4.0][cc-by-nc-sa-shield]][cc-by-nc-sa]

This work is licensed under a
[Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License][cc-by-nc-sa].

[![CC BY-NC-SA 4.0][cc-by-nc-sa-image]][cc-by-nc-sa]

[cc-by-nc-sa]: http://creativecommons.org/licenses/by-nc-sa/4.0/
[cc-by-nc-sa-image]: https://licensebuttons.net/l/by-nc-sa/4.0/88x31.png
[cc-by-nc-sa-shield]: https://img.shields.io/badge/License-CC%20BY--NC--SA%204.0-lightgrey.svg
## 

## Autores
* **Eneritz Azqueta** → Auditora en **SIA**
* **Dimas Pastor** → Auditor en **Cybertix**
