class Usuario {
    constructor(nombre, correo) {
        this.nombre = nombre;
        this.correo = correo;
    }

    mostrarDatos() {
        return `Nombre: ${this.nombre} - Correo: ${this.correo}`;
    }
}

class Cliente extends Usuario {
    constructor(nombre, correo, numeroCliente) {
        super(nombre, correo);
        this.numeroCliente = numeroCliente;
    }

    mostrarDatos() {
        return `Cliente: ${this.nombre}, número: ${this.numeroCliente}`;
    }
}

const cliente = new Cliente("Ana", "ana@correo.com", 101);

console.log(cliente.mostrarDatos());



/*Diferencia principal
- Python: class Cliente(Usuario)
- JavaScript: class Cliente extends Usuario
*/