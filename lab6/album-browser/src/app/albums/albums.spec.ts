import { ComponentFixture, TestBed } from '@angular/core/testing';
import { AlbumsComponent } from './albums';
import { AlbumService } from '../album';
import { provideHttpClient } from '@angular/common/http';
import { provideRouter } from '@angular/router';

describe('AlbumsComponent', () => {
  let component: AlbumsComponent;
  let fixture: ComponentFixture<AlbumsComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [AlbumsComponent],
      providers: [
        AlbumService,
        provideHttpClient(),
        provideRouter([])
      ]
    })
      .compileComponents();

    fixture = TestBed.createComponent(AlbumsComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
