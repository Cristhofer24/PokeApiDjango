
import { Component } from '@angular/core';
import { ClienteService } from '../../Services/cliente.service';
import { Cliente } from '../../Interfaces/Cliente';
import { FormsModule } from '@angular/forms';
import { CommonModule } from '@angular/common';
import { Router } from '@angular/router';

@Component({
  selector: 'app-cliente',
  imports: [FormsModule,CommonModule],
  templateUrl: './cliente.component.html',
  styleUrl: './cliente.component.css'
})
export default class ClienteComponent {


  cliente: Cliente = {};
    constructor(private clienteService:ClienteService ,  private router: Router) { }

    RegistroCliente(): void {
      this.clienteService.createCliente(this.cliente).subscribe(
        (response: any) => {
          console.log("Respuesta del servidor:", response);  // Depuración

          // Verifica que la respuesta contenga el clienteId
          if (response && response.clienteId) {
            console.log("Sus datos fueron guardados exitosamente");
            this.router.navigate(['/CrearCuenta', response.clienteId]);  // Redirige a la página para crear cuenta
          } else {
            console.error("El clienteId no está presente en la respuesta.");
          }
        },
        (error) => {
          console.error("Error al guardar sus datos:", error); // Muestra el error completo
        }
      );
    }
    }


