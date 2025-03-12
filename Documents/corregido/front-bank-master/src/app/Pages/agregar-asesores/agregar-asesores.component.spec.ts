import { ComponentFixture, TestBed } from '@angular/core/testing';

import { AgregarAsesoresComponent } from './agregar-asesores.component';

describe('AgregarAsesoresComponent', () => {
  let component: AgregarAsesoresComponent;
  let fixture: ComponentFixture<AgregarAsesoresComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [AgregarAsesoresComponent]
    })
    .compileComponents();

    fixture = TestBed.createComponent(AgregarAsesoresComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
