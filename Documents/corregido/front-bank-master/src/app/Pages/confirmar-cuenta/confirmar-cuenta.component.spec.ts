import { ComponentFixture, TestBed } from '@angular/core/testing';

import { ConfirmarCuentaComponent } from './confirmar-cuenta.component';

describe('ConfirmarCuentaComponent', () => {
  let component: ConfirmarCuentaComponent;
  let fixture: ComponentFixture<ConfirmarCuentaComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [ConfirmarCuentaComponent]
    })
    .compileComponents();

    fixture = TestBed.createComponent(ConfirmarCuentaComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
