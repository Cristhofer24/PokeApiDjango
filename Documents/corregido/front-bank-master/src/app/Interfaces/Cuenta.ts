export interface Cuenta {
  cuentaId?: number;
  tipoCuenta?: string;
  numeroCuenta?: string;
  fechaApertura?: string;
  fechaCaducidad?: string;
  estado?: string;
  fkCliente?: number;
}
