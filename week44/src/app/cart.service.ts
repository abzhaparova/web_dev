import { Injectable } from '@angular/core';

@Injectable({
  providedIn: 'root'
})
export class CartService {

  isVisible = false;
  items = []

  addItem(item) {

    let exists = false;

    this.items.forEach(cartItem => {
      if(cartItem.product.name === item.name){
        cartItem.quantity++;
        exists = true;
      }
    });

    if(!exists) {
      this.items.push({
        product: item,
        quantity: 1,
      });
    }
  }
  
  removeItem(product) {
    let i = 0;
    
    this.items.forEach(item => {
      if(item.product.name === product.name){
        if(item.quantity === 1){ 
          this.items.splice(i, 1);
        }
        else {
          this.items[i].quantity--;
        }
      }
      i++;
    });
  }

  getItems() {
    return this.items;
  }

  constructor() { }
}
