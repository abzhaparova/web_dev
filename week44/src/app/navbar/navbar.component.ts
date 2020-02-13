import { Component, OnInit } from '@angular/core';
import { CartService } from "../cart.service"
@Component({
  selector: 'app-navbar',
  templateUrl: './navbar.component.html',
  styleUrls: ['./navbar.component.css']
})
export class NavbarComponent implements OnInit {



  constructor(private cartService: CartService) { }

  toggleCart() {
    this.cartService.isVisible = !this.cartService.isVisible;
  }

  ngOnInit(): void {
  }

}
