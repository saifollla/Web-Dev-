import { User } from './user/user';
import { Comments } from './comments/comments';
import {RouterOutlet, RouterLink} from '@angular/router';
import {FormGroup, FormControl} from '@angular/forms';
import {ReactiveFormsModule, Validators} from '@angular/forms';
import {CarService} from './car';
import {Component, inject } from '@angular/core';
import {DecimalPipe, DatePipe, CurrencyPipe} from '@angular/common';



@Component({
  selector: 'app-root',
  standalone: true,
  imports: [User, Comments,RouterOutlet, RouterLink, ReactiveFormsModule, DecimalPipe, DatePipe, CurrencyPipe],
  template: `

    <nav>
      <a routerLink="/">Home</a>
      |
      <a routerLink="/user">User</a>
    </nav>
    <router-outlet />

    <form [formGroup]="profileForm">
      <input type="text" formControlName="name" name="name" />
      <input type="email" formControlName="email" name="email" />
      <button type="submit" [disabled]="!profileForm.valid">Submit</button>
    </form>

    <h2>Profile Form</h2>
    <p>Name: {{ profileForm.value.name }}</p>
    <p>Email: {{ profileForm.value.email }}</p>


    <p>Корзина: {{ items.join(', ') }}</p>
    <app-user name="Simran" (addItemEvent)="addItem($event)" />



    <div [contentEditable]="isEditable">
      some editable text
    </div>

    @for (user of users; track user.id) {
      <p>{{ user.name }}</p>
    }

    <section (mouseover)="showSecretMessage()">
      <p>hover to see the secret phrase</p>
      <p>{{ message }}</p>
    </section>

    <h1>How I feel about Angular..</h1>
    <article>
      <p>
        Angular is my favorite framework, and this is why. Angular has the coolest deferrable view
        feature that makes defer loading content the easiest and most ergonomic it could possibly be.
        The Angular community is also filled with amazing contributors and experts that create excellent
        content. The community is welcoming and friendly, and it really is the best community out there.
      </p>
      <p>
        I can't express enough how much I enjoy working with Angular. It offers the best developer
        experience I've ever had. I love that the Angular team puts their developers first and takes
        care to make us very happy. They genuinely want Angular to be the best framework it can be, and
        they're doing such an amazing job at it, too. This statement comes from my heart and is not at
        all copied and pasted. In fact, I think I'll say these exact same things again a few times.
      </p>
      <p>
        Angular is my favorite framework, and this is why. Angular has the coolest deferrable view
        feature that makes defer loading content the easiest and most ergonomic it could possibly be.
        The Angular community is also filled with amazing contributors and experts that create excellent
        content. The community is welcoming and friendly, and it really is the best community out there.
      </p>
      <p>
        I can't express enough how much I enjoy working with Angular. It offers the best developer
        experience I've ever had. I love that the Angular team puts their developers first and takes
        care to make us very happy. They genuinely want Angular to be the best framework it can be, and
        they're doing such an amazing job at it, too. This statement comes from my heart and is not at
        all copied and pasted. In fact, I think I'll say these exact same things again a few times.
      </p>
      <p>
        Angular is my favorite framework, and this is why. Angular has the coolest deferrable view
        feature that makes defer loading content the easiest and most ergonomic it could possibly be.
        The Angular community is also filled with amazing contributors and experts that create excellent
        content. The community is welcoming and friendly, and it really is the best community out there.
      </p>
      <p>
        I can't express enough how much I enjoy working with Angular. It offers the best developer
        experience I've ever had. I love that the Angular team puts their developers first and takes
        care to make us very happy. They genuinely want Angular to be the best framework it can be, and
        they're doing such an amazing job at it, too. This statement comes from my heart and is not at
        all copied and pasted.
      </p>
    </article>

    <p>Car Listing: {{ display }}</p>

    <ul>
      <li>Number with "decimal" {{ num | number: '3.2-2' }}</li>
      <li>Date with "date" {{ birthday | date: 'medium' }}</li>
      <li>Currency with "currency" {{ cost | currency }}</li>
    </ul>

    @defer (on viewport) {
      <comments />
    } @placeholder {
      <p>Future comments</p>
    } @loading (minimum 2s) {
      <p>Loading comments...</p>
    }



  `,
})


export class App {

  profileForm = new FormGroup({
    name: new FormControl('', Validators.required),
    email: new FormControl('', [Validators.required, Validators.email]),
  });

  handleSubmit() {
    alert(this.profileForm.value.name + ' | ' + this.profileForm.value.email);
  }

  isEditable = true;

  users = [
    {id: 0, name: 'Sarah'},
    {id: 1, name: 'Amy'},
    {id: 2, name: 'Rachel'},
    {id: 3, name: 'Jessica'},
    {id: 4, name: 'Poornima'},
  ];

  message = '';

  showSecretMessage() {
    this.message = 'Way to go 🚀';
  }

  items = ['🍎', '🍌'];

  addItem(newItem: string) {
    this.items.push(newItem);


  }

  carService = inject(CarService);
  display = this.carService.getCars().join(' ⭐️ ');
  num = 103.1234;
  birthday = new Date(2023, 3, 2);
  cost = 4560.34;
}
