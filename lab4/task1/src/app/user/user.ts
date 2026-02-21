import { Component, input, output } from '@angular/core';
import {NgOptimizedImage} from '@angular/common';
import {FormsModule} from '@angular/forms';


@Component({
  selector: 'app-user',
  standalone: true,
  imports: [NgOptimizedImage, FormsModule],
  styleUrl: './user.css',
  template: `
    <p>{{ username }}'s favorite framework: {{ favoriteFramework }}</p>
    <label for="framework">
      Favorite Framework:
      <input id="framework" type="text" [(ngModel)]="favoriteFramework" />
    </label>
    <button (click)="showFramework()">Show Framework</button>
    <p>User: {{ name() }}</p>
    <button (click)="addItem()">Add Item</button>
    <p>Some cats:</p>
    <ul>
      <li>
        Static Image:
        <img ngSrc="/cat1.jpg"  width="32" height="32" />
      </li>
      <li>
        Dynamic Image:
        <img [ngSrc]="catUrl" [alt]="logoAlt" width="32" height="32" />
      </li>
    </ul>
  `,
})
export class User {
  catUrl = '/cat2.webp';
  favoriteFramework = '';
  name = input<string>();
  addItemEvent = output<string>();

  addItem() {
    this.addItemEvent.emit('🐢');
  }

  logoUrl = '/logo.svg';
  logoAlt = 'Angular logo';
  username = 'youngTech';

  showFramework() {
    alert(this.favoriteFramework);
  }
}
