import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Cuenta } from '../Interfaces/Cuenta';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class CuentaService {
  private ApiUrl='http://localhost:8080/api/Cuentas';

  constructor(private http:HttpClient) { }

//Guardar Clientes
createCuenta(cuentas: Cuenta): Observable<Cuenta> {
  return this.http.post<Cuenta>(this.ApiUrl, cuentas);
}
}
