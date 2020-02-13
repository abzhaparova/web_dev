import { Component, OnInit } from '@angular/core';

import { products } from "../products"

import { CartService } from "../cart.service"

@Component({
  selector: 'app-products-list',
  templateUrl: './products-list.component.html',
  styleUrls: ['./products-list.component.css']
})
export class ProductsListComponent implements OnInit {

  products = products;

  constructor(
    public cartService: CartService,
  ) { }

  onClick(product) {
    this.cartService.addItem(product);
  }
  removeItem(item) {
    this.cartService.removeItem(item.product);
  }

  ngOnInit(): void {
  }

}
