import { Cuenta } from './../../Interfaces/Cuenta';
import { Cliente } from './../../Interfaces/Cliente';
import { Component, OnInit } from '@angular/core';
import { ActivatedRoute, Router } from '@angular/router';
import { FormsModule } from '@angular/forms';
import { CuentaService } from '../../Services/cuenta.service';

@Component({
  selector: 'app-abrir-cuenta',
  imports: [FormsModule],
  templateUrl: './abrir-cuenta.component.html',  // Verifica esta ruta
  styleUrls: ['./abrir-cuenta.component.css']
})
export default class AbrirCuentaComponent implements OnInit {

  clienteId?: number;
  cuenta: Cuenta = {};

  constructor(
    private route: ActivatedRoute,
    private cuentaService: CuentaService,
    private router: Router
  ) { }

  //Inicializa para poder obtener el clienteId tanto el la url como en el input 
  ngOnInit(): void {
    const clienteId = this.route.snapshot.paramMap.get('clienteId');
    console.log("clienteId obtenido de la URL:", clienteId);  // Depuración
    if (clienteId) {
      this.clienteId = +clienteId;
      this.cuenta.fkCliente = this.clienteId;  // Asigna el clienteId a la cuenta
      console.log("clienteId asignado a cuenta.fkCliente:", this.cuenta.fkCliente);
    } else {
      console.error("Error: No se encontró el clienteId en la URL.");
    }
  }

  crearCuenta(): void {
      this.cuentaService.createCuenta(this.cuenta).subscribe(
        (response: any) => {
          console.log("Cuenta creada con éxito:", response);
          this.router.navigate(['/confirmarCuenta', this.clienteId]);
        },
        (error: any) => {
          console.error("Error al crear cuenta:", error);
        }
      );
    }
  }

