import { ComponentFixture, TestBed } from '@angular/core/testing';

import { GestorRolesComponent } from './gestor-roles.component';

describe('GestorRolesComponent', () => {
  let component: GestorRolesComponent;
  let fixture: ComponentFixture<GestorRolesComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [GestorRolesComponent]
    })
    .compileComponents();

    fixture = TestBed.createComponent(GestorRolesComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
