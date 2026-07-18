# Instrucciones para Revertir la Actividad

Hola Adrián. He guardado este archivo con la instrucción exacta por si en algún momento en el futuro deseas limpiar tu historial de GitHub y volverlo a su estado original (removiendo todos los "cuantos verdes" que generamos).

Si alguna vez decides borrar este historial falso, tienes que abrir una terminal en esta misma carpeta y simplemente ejecutar los siguientes dos comandos:

```bash
git reset --hard dc269123f9c689e252c44b4b0811952521b95a6c
git push -f origin main
```

Esto devolverá todo mágicamente al punto exacto de la última modificación seria (cuando ajustamos los permisos del gusanito). ¡Conserva este archivo sin borrarlo para no perder el código de respaldo!
