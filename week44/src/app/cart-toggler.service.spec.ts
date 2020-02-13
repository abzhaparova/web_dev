import { TestBed } from '@angular/core/testing';

import { CartTogglerService } from './cart-toggler.service';

describe('CartTogglerService', () => {
  let service: CartTogglerService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(CartTogglerService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
