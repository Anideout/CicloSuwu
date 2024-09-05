ORDEN DE COMANDOS: "Evaluacion 3 de CLOUD"
1.- ec2-user (para iniciar sesion en instancia)
1.- sudo useradd eliasd     (crear usuario y contraseña)
2.- sudo passwd eliasd
3.- sudo mkdir carpeta1     (crear directorio)
4.- ls       (confirmar que se creo la carpeta)
5.- sudo chown eliasd:eliasd carpeta1     (Definir propietario del archivo)
6.- cd carpeta1             (Acceder a una ruta o carpeta especifica)
7.- sudo nano file1.txt     (Se utiliza para abrir y editar un archivo)
8.- cat file1.txt           (Mostrar el contenido del archivo)
9.- sudo dnf update -y      (Actualizar todos los paquetes instalados en la instancia)
10.- sudo yum install -y nginx    (Para instalar el servidor web 'Nginx')
11.- sudo systemctl start nginx.service    (Para poner en funcionamiento el servidor web nginx después de su instalación)
