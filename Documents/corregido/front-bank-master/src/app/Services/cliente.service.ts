import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Cliente } from '../Interfaces/Cliente';
import { Observable } from 'rxjs';


@Injectable({
  providedIn: 'root'
})
export class ClienteService {
  private ApiUrl='http://localhost:8080/api/clientes';

  constructor(private http:HttpClient) { }

//Guardar Clientes
createCliente(cliente: Cliente): Observable<Cliente> {
  return this.http.post<Cliente>(this.ApiUrl, cliente);
}



}
